--[[
lehrbuch.lua – Pandoc-Lua-Filter des Lehrbuch-Satzsystems (übernommen aus dem BESS-Projekt, unverändert)

Aufgaben
  1. Kästen: GitHub-Alert-Syntax im Markdown wird zu gestalteten Kästen.
       > [!IMPORTANT]
       > **Hier Fachleute einbinden:** Fachanwalt Energierecht für …
     Typ ergibt sich aus dem Titel (fett, erste Zeile) oder aus dem Alert-Tag:
       NOTE→Merke, TIP→Praxis-Check, IMPORTANT→Hier Fachleute einbinden,
       WARNING/CAUTION→Achtung/Typische Fehler; eigene Tags: BEISPIEL,
       LERNZIELE, DEFINITION, STAND.
     Im DOCX werden Start-/Endmarken gesetzt; postprocess_docx.py baut daraus
     einzellige Tabellen mit Farbbalken und Hintergrund (robust in Word und
     LibreOffice, auch mit Listen und Tabellen im Kasten).
  2. Beschriftungen von Tabellen und Abbildungen werden nummeriert
     („Tabelle 3.2:“ kapitelweise oder „Tabelle 7:“ fortlaufend).
  3. Deckblattergänzung, Inhaltsverzeichnis-Feld und Seitenumbrüche.

Metadaten (YAML-Kopf):
  nummerierung: kapitelweise | fortlaufend   (Standard: fortlaufend)
  kapitel-start: 5            erste Kapitelnummer (Einzelkapitel-Build)
  deckblatt-info: [ "Stand: 27.09.2026", … ]   Zeilen unter dem Titel
  deckblatt-hinweis: "…"      Hinweiszeile unten auf dem Deckblatt
  inhaltsverzeichnis: true    TOC-Feld nach dem Deckblatt
  toc-tiefe: 2                Gliederungstiefe im Inhaltsverzeichnis
  h1-neue-seite: true         jede Hauptüberschrift auf neuer Seite
--]]

local stringify = pandoc.utils.stringify
local is_docx = FORMAT:match('docx') ~= nil
local is_typst = FORMAT:match('typst') ~= nil

local NBSP = '\u{00A0}'

local TAG_TYP = {
  NOTE = 'merke', TIP = 'praxis', IMPORTANT = 'fachleute', WARNING = 'achtung',
  CAUTION = 'achtung', BEISPIEL = 'beispiel', EXAMPLE = 'beispiel',
  LERNZIELE = 'lernziele', DEFINITION = 'definition', STAND = 'stand',
  MERKE = 'merke', PRAXIS = 'praxis', FACHLEUTE = 'fachleute', ACHTUNG = 'achtung',
}

local TITEL_TYP = {
  ['hier fachleute einbinden'] = 'fachleute', ['fachleute einbinden'] = 'fachleute',
  ['rechenbeispiel'] = 'beispiel', ['beispiel'] = 'beispiel', ['fallbeispiel'] = 'beispiel',
  ['lernziele'] = 'lernziele',
  ['merke'] = 'merke', ['kernaussage'] = 'merke', ['kernaussagen'] = 'merke',
  ['definition'] = 'definition',
  ['praxis-check'] = 'praxis', ['prüffragen'] = 'praxis', ['checkliste'] = 'praxis',
  ['typische fehler'] = 'achtung', ['achtung'] = 'achtung', ['fallstrick'] = 'achtung',
  ['fallstricke'] = 'achtung',
  ['stand'] = 'stand', ['regulatorisch beweglich'] = 'stand',
}

local STANDARD_TITEL = {
  merke = 'Merke', praxis = 'Praxis-Check', fachleute = 'Hier Fachleute einbinden',
  achtung = 'Achtung', beispiel = 'Beispiel', lernziele = 'Lernziele',
  definition = 'Definition', stand = 'Stand und Beweglichkeit',
}

local function xml_escape(s)
  return (s:gsub('&', '&amp;'):gsub('<', '&lt;'):gsub('>', '&gt;'):gsub('"', '&quot;'))
end

local function marker(text)
  return pandoc.RawBlock('openxml',
    '<w:p><w:pPr><w:pStyle w:val="KastenMarker"/></w:pPr><w:r><w:t>'
    .. xml_escape(text) .. '</w:t></w:r></w:p>')
end

local function seitenumbruch()
  if is_docx then
    return marker('§§SEITENUMBRUCH§§')
  end
  if is_typst then
    return pandoc.RawBlock('typst', '#pagebreak(weak: true)')
  end
  return pandoc.RawBlock('html', '<div style="page-break-after: always"></div>')
end

local function strip_leading_space(inl)
  while #inl > 0 and (inl[1].t == 'SoftBreak' or inl[1].t == 'Space'
                      or inl[1].t == 'LineBreak') do
    inl:remove(1)
  end
end

-- 0. Vermerke [LÜCKE: …] und [MODELL: …] -------------------------------------
-- Im Typst-Satz werden die Vermerke als hinterlegter Text gesetzt (#vermerk in der Vorlage);
-- verschachtelte Klammern wie [K05M-06] innerhalb eines Vermerks bleiben erhalten. Das Semikolon
-- beendet den Typst-Aufruf, damit eine direkt folgende Klammer nicht als Argument gelesen wird.
local VERMERKE = { {'[LÜCKE:', 'luecke'}, {'[MODELL:', 'modell'} }

local function klammer_ende(text, tiefe)
  for pos = 1, #text do
    local c = text:sub(pos, pos)
    if c == '[' then
      tiefe = tiefe + 1
    elseif c == ']' then
      tiefe = tiefe - 1
      if tiefe == 0 then return pos, 0 end
    end
  end
  return nil, tiefe
end

local function vermerke(inlines)
  if not is_typst then return nil end
  local out, i, geaendert = pandoc.Inlines({}), 1, false
  while i <= #inlines do
    local el = inlines[i]
    local treffer = nil
    if el.t == 'Str' then
      for _, v in ipairs(VERMERKE) do
        local s = el.text:find(v[1], 1, true)
        if s and (not treffer or s < treffer.s) then treffer = {s = s, muster = v[1], typ = v[2]} end
      end
    end
    if not treffer then
      out:insert(el)
      i = i + 1
    else
      local vor = el.text:sub(1, treffer.s - 1)
      local rest = el.text:sub(treffer.s + #treffer.muster)
      local inhalt = pandoc.Inlines({})
      local nach, ende = nil, nil
      local pos, tiefe = klammer_ende(rest, 1)
      if pos then
        if pos > 1 then inhalt:insert(pandoc.Str(rest:sub(1, pos - 1))) end
        nach, ende = rest:sub(pos + 1), i
      else
        if rest ~= '' then inhalt:insert(pandoc.Str(rest)) end
        for j = i + 1, #inlines do
          local x = inlines[j]
          if x.t == 'Str' then
            local p
            p, tiefe = klammer_ende(x.text, tiefe)
            if p then
              if p > 1 then inhalt:insert(pandoc.Str(x.text:sub(1, p - 1))) end
              nach, ende = x.text:sub(p + 1), j
              break
            end
          end
          inhalt:insert(x)
        end
      end
      if not ende then
        out:insert(el)            -- keine schließende Klammer: unverändert lassen
        i = i + 1
      else
        strip_leading_space(inhalt)
        while #inhalt > 0 and (inhalt[#inhalt].t == 'Space' or inhalt[#inhalt].t == 'SoftBreak') do
          inhalt:remove(#inhalt)
        end
        if vor ~= '' then out:insert(pandoc.Str(vor)) end
        out:insert(pandoc.RawInline('typst', '#vermerk(typ: "' .. treffer.typ .. '")['))
        out:extend(inhalt)
        out:insert(pandoc.RawInline('typst', '];'))
        geaendert = true
        if nach ~= '' then
          inlines[ende] = pandoc.Str(nach)   -- Rest weiter prüfen (weiterer Vermerk möglich)
          i = ende
        else
          i = ende + 1
        end
      end
    end
  end
  if geaendert then return out end
  return nil
end

-- 1. Kästen ----------------------------------------------------------------
function BlockQuote(el)
  local first = el.content[1]
  if not first or (first.t ~= 'Para' and first.t ~= 'Plain') then return nil end
  local inl = first.content
  if #inl == 0 or inl[1].t ~= 'Str' then return nil end
  local tag = inl[1].text:match('^%[!([%w%-]+)%]$')
  if not tag then return nil end

  local typ = TAG_TYP[tag:upper()] or 'merke'
  inl:remove(1)
  strip_leading_space(inl)

  local titel_inlines = nil
  if #inl > 0 and inl[1].t == 'Strong' then
    titel_inlines = inl[1].content
    local key = pandoc.text.lower(stringify(inl[1])):gsub('%s*:%s*$', '')
    if TITEL_TYP[key] then typ = TITEL_TYP[key] end
    inl:remove(1)
    strip_leading_space(inl)
    -- abschließenden Doppelpunkt im Titel entfernen
    local last = titel_inlines[#titel_inlines]
    if last and last.t == 'Str' then
      last.text = last.text:gsub(':$', '')
      if last.text == '' then titel_inlines:remove(#titel_inlines) end
    end
  end
  local blocks = el.content
  if #inl == 0 then blocks:remove(1) end
  if not titel_inlines then
    titel_inlines = pandoc.Inlines({pandoc.Str(STANDARD_TITEL[typ])})
  end

  if is_docx then
    local out = pandoc.List()
    out:insert(marker('§§KASTEN-START:' .. typ .. '§§'))
    out:insert(pandoc.Div({pandoc.Para(titel_inlines)}, {['custom-style'] = 'Kasten Titel'}))
    out:insert(pandoc.Div(blocks, {['custom-style'] = 'Kasten Text'}))
    out:insert(marker('§§KASTEN-ENDE§§'))
    return out
  end
  if is_typst then
    local titel = pandoc.write(pandoc.Pandoc({pandoc.Plain(titel_inlines)}), 'typst')
    titel = titel:gsub('%s+$', '')
    local out = pandoc.List()
    out:insert(pandoc.RawBlock('typst', '#kasten(typ: "' .. typ .. '", titel: [' .. titel .. '])['))
    out:extend(blocks)
    out:insert(pandoc.RawBlock('typst', ']'))
    return out
  end
  local div = pandoc.Div(blocks, {class = 'kasten kasten-' .. typ})
  div.content:insert(1, pandoc.Para({pandoc.Strong(titel_inlines)}))
  return div
end

-- 3a. Seitenumbruch-Kommentare -------------------------------------------------
function RawBlock(el)
  if el.format == 'html' and el.text:match('^%s*<!%-%-%s*neue%-seite%s*%-%->%s*$') then
    return seitenumbruch()
  end
  if (el.format == 'tex' or el.format == 'latex') and el.text:match('^%s*\\newpage%s*$') then
    return seitenumbruch()
  end
  return nil
end

-- 2./3b. Nummerierung, Deckblatt, Inhaltsverzeichnis ------------------------------
local function prefix_caption(blocks, label)
  if not blocks or #blocks == 0 then return end
  local b = blocks[1]
  if b.t == 'Plain' or b.t == 'Para' then
    b.content:insert(1, pandoc.Space())
    b.content:insert(1, pandoc.Strong({pandoc.Str(label .. ':')}))
  end
end

local function meta_bool(meta, key, default)
  local v = meta[key]
  if v == nil then return default end
  if type(v) == 'boolean' then return v end
  local s = pandoc.text.lower(stringify(v))
  return s == 'true' or s == 'ja' or s == 'yes'
end

local function toc_block(tiefe)
  local xml = table.concat({
    '<w:sdt><w:sdtPr><w:docPartObj><w:docPartGallery w:val="Table of Contents"/>',
    '<w:docPartUnique/></w:docPartObj></w:sdtPr><w:sdtContent>',
    '<w:p><w:pPr><w:pStyle w:val="TOCHeading"/></w:pPr><w:r><w:t>Inhaltsverzeichnis</w:t></w:r></w:p>',
    '<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>',
    '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-', tostring(tiefe), '" \\h \\z \\u </w:instrText></w:r>',
    '<w:r><w:fldChar w:fldCharType="separate"/></w:r>',
    '<w:r><w:t>Inhaltsverzeichnis: in Word mit F9 aktualisieren.</w:t></w:r>',
    '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>',
    '</w:sdtContent></w:sdt>'})
  return pandoc.RawBlock('openxml', xml)
end


-- Typst (Build v2): Spaltenbreiten, Metadaten für Deckblatt/Nummerierung --------
local TOTAL_ZEICHEN = 104   -- Textbreite 16,2 cm in Durchschnittszeichen (Carlito 9 pt)
local ZELL_RAND = 2.5       -- Zellinnenabstand in Zeichen
local MAX_WORT = 26         -- lange Einzelwörter (URLs) begrenzen
local SCHMAL = 11           -- Spalten bis zu dieser Mindestbreite gelten als schmal (IDs, Nummern)
local MONO = 1.2            -- Festbreitenschrift (raw, 8,8 pt) je Zeichen in Durchschnittszeichen Carlito 9 pt

local function text_units(s)
  local u = 0
  for _, c in utf8.codes(s) do
    local ch = utf8.char(c)
    if ch:match('^%u$') or ch == 'Ä' or ch == 'Ö' or ch == 'Ü' or ch == '%' or ch == '&' or ch == '@' then
      u = u + 1.3
    elseif ch:match('^%d$') then
      u = u + 1.1
    elseif ch:match("^[il%.,;:!|']$") then
      u = u + 0.6
    else
      u = u + 1.0
    end
  end
  return u
end

local function zeilen_von(tbl)
  local rows = pandoc.List()
  for _, r in ipairs(tbl.head.rows) do rows:insert(r) end
  for _, b in ipairs(tbl.bodies) do
    for _, r in ipairs(b.head) do rows:insert(r) end
    for _, r in ipairs(b.body) do rows:insert(r) end
  end
  for _, r in ipairs(tbl.foot.rows) do rows:insert(r) end
  return rows
end

-- Wörter in Code-Spannen (Festbreitenschrift) sind breiter als Fließtext; sie brechen nicht um.
local function code_woerter(contents)
  local woerter = {}
  pandoc.Blocks(contents):walk({
    Code = function(el)
      for w in el.text:gmatch('%S+') do table.insert(woerter, w) end
    end
  })
  return woerter
end

local function spaltenbreiten(tbl)
  local n = #tbl.colspecs
  if n == 0 then return tbl end
  local mins, maxs = {}, {}
  for j = 1, n do mins[j], maxs[j] = 0, 0 end
  for _, row in ipairs(zeilen_von(tbl)) do
    local j = 1
    for _, cell in ipairs(row.cells) do
      if cell.col_span ~= 1 then return tbl end
      local txt = stringify(cell.contents)
      local laengstes = 1
      for wort in txt:gmatch('%S+') do
        laengstes = math.max(laengstes, text_units(wort))
      end
      local zuschlag = 0
      for _, w in ipairs(code_woerter(cell.contents)) do
        local breite = utf8.len(w) * MONO
        laengstes = math.max(laengstes, breite + 0.6)
        zuschlag = zuschlag + math.max(0, breite - text_units(w))
      end
      mins[j] = math.max(mins[j], math.min(laengstes + 1, MAX_WORT) + ZELL_RAND)
      maxs[j] = math.max(maxs[j], text_units(txt) + zuschlag + ZELL_RAND)
      j = j + 1
    end
  end
  local smin, smax = 0, 0
  for j = 1, n do
    maxs[j] = math.max(maxs[j], mins[j])
    smin, smax = smin + mins[j], smax + maxs[j]
  end
  local breiten = {}
  if smax <= TOTAL_ZEICHEN then
    for j = 1, n do breiten[j] = maxs[j] / smax end
  elseif smin >= TOTAL_ZEICHEN then
    -- zu breit: schmale Spalten (IDs, Nummern, kurze Werte) behalten ihre Mindestbreite,
    -- die übrigen teilen sich den Rest im Verhältnis ihrer Mindestbreiten
    local fest, rest = 0, 0
    for j = 1, n do
      if mins[j] <= SCHMAL then fest = fest + mins[j] else rest = rest + mins[j] end
    end
    for j = 1, n do
      if rest == 0 or fest >= 0.5 * TOTAL_ZEICHEN then
        breiten[j] = mins[j] / smin
      elseif mins[j] <= SCHMAL then
        breiten[j] = mins[j] / TOTAL_ZEICHEN
      else
        breiten[j] = (mins[j] / rest) * (TOTAL_ZEICHEN - fest) / TOTAL_ZEICHEN
      end
    end
  else
    local extra, spanne = TOTAL_ZEICHEN - smin, smax - smin
    for j = 1, n do
      breiten[j] = (mins[j] + extra * (maxs[j] - mins[j]) / spanne) / TOTAL_ZEICHEN
    end
  end
  local specs = pandoc.List()
  for j = 1, n do
    local ausrichtung = tbl.colspecs[j][1]
    if ausrichtung == 'AlignDefault' then ausrichtung = 'AlignLeft' end
    specs:insert({ausrichtung, breiten[j]})
  end
  tbl.colspecs = specs
  return tbl
end

-- Tabellenzellen: Pandoc maskiert am Zellanfang keine Typst-Markupzeichen; „= EBITDA“ würde zur
-- Überschrift, „+ …“ zur Aufzählung, „- …“ zur Liste, „/ …“ zur Begriffsliste. Erstes Zeichen maskieren.
local MARKUP_ANFANG = { ['='] = true, ['+'] = true, ['-'] = true, ['/'] = true }

local function zelle_maskieren(cell)
  local b = cell.contents[1]
  if b and (b.t == 'Plain' or b.t == 'Para') and b.content[1] and b.content[1].t == 'Str' then
    local s = b.content[1].text
    local c = s:sub(1, 1)
    if MARKUP_ANFANG[c] and (#s == 1 or s:sub(1, 2) == c .. c or #s > 1) then
      b.content[1] = pandoc.Str(s:sub(2))
      b.content:insert(1, pandoc.RawInline('typst', '\\' .. c))
      if b.content[2].text == '' then b.content:remove(2) end
    end
  end
  return cell
end

local function tabellen_maskieren(tbl)
  for _, row in ipairs(tbl.head.rows) do for i, c in ipairs(row.cells) do row.cells[i] = zelle_maskieren(c) end end
  for _, body in ipairs(tbl.bodies) do
    for _, row in ipairs(body.head) do for i, c in ipairs(row.cells) do row.cells[i] = zelle_maskieren(c) end end
    for _, row in ipairs(body.body) do for i, c in ipairs(row.cells) do row.cells[i] = zelle_maskieren(c) end end
  end
  return tbl
end

-- Formeln: deutsches Dezimalkomma. LaTeX-Konvention 0{,}87 (auch 0,87 ohne Leerzeichen) wird
-- in Typst als Komma ohne Nachabstand gesetzt; „1, 2“ mit Leerzeichen bleibt Aufzählung.
local function typst_math(el)
  local tex, n1, n2 = el.text, 0, 0
  tex, n1 = tex:gsub('(%d){,}(%d)', '%1\\text{DEZKOMMA}%2')
  tex, n2 = tex:gsub('(%d),(%d)', '%1\\text{DEZKOMMA}%2')
  if n1 + n2 == 0 then return nil end
  el.text = tex
  local typ = pandoc.write(pandoc.Pandoc({pandoc.Plain({el})}), 'typst',
                           {wrap_text = 'wrap-none'})
  typ = typ:gsub('upright%("DEZKOMMA"%)', 'class("normal", \\,)'):gsub('%s+$', '')
  return pandoc.RawInline('typst', typ)
end

-- Quellenzeile direkt unter einer Tabelle oder Abbildung („Quelle: …“) als Tabellennotiz setzen
local function ist_quellenzeile(blk)
  return blk and (blk.t == 'Para' or blk.t == 'Plain') and blk.content[1]
    and blk.content[1].t == 'Str' and (blk.content[1].text == 'Quelle:' or blk.content[1].text == 'Quellen:')
end

local function quellenzeilen(blocks)
  local neu = pandoc.Blocks({})
  for i, blk in ipairs(blocks) do
    local vorher = blocks[i - 1]
    local nach_objekt = vorher and (vorher.t == 'Table' or vorher.t == 'Figure'
      or (vorher.t == 'Para' and #vorher.content == 1 and vorher.content[1].t == 'Image'))
    if ist_quellenzeile(blk) and nach_objekt then
      neu:insert(pandoc.RawBlock('typst', '#quellenzeile['))
      neu:insert(pandoc.Plain(blk.content))
      neu:insert(pandoc.RawBlock('typst', ']'))
    else
      neu:insert(blk)
    end
  end
  return neu
end

-- Gesamtbuch: Stichwortverzeichnis ------------------------------------------------
-- Die Stichwortdatei (JSON, von 07_build/stichwoerter.py aus dem Glossar erzeugt) enthält je Eintrag
-- das Stichwort und seine Suchmuster. Markiert wird die erste Fundstelle je Kapitel (H1) im
-- Fließtext, in Listen, Tabellen und Kästen der Kapitel; Überschriften, Abbildungsbeschriftungen,
-- die Abschnitte „Quellen und Stand“ und die Anhänge bleiben unmarkiert.
local RAND_VORN = '^[„"%(%[‚\'«»“]+'
local RAND_HINTEN = '[%.,;:!%?%)%]“”"\'»…’]+$'

local function normiert(s)
  return (s:gsub(RAND_VORN, ''):gsub(RAND_HINTEN, ''))
end

local function ist_kuerzel(s)
  local gross = 0
  for _, c in utf8.codes(s) do
    local ch = utf8.char(c)
    if ch:match('^%u$') or ch:match('^%d$') or ch == 'Ä' or ch == 'Ö' or ch == 'Ü' then gross = gross + 1 end
  end
  return gross >= 2
end

local function passt(tok, muster, letztes)
  if ist_kuerzel(muster) then
    return tok == muster or tok == muster .. 's' or tok:sub(1, #muster + 1) == muster .. '-'
  end
  local tl, ml = pandoc.text.lower(tok), pandoc.text.lower(muster)
  if tl == ml or tl:sub(1, #ml + 1) == ml .. '-' then return true end
  local lt, lm = utf8.len(tl) or #tl, utf8.len(ml) or #ml
  if lm >= 4 and tl:sub(1, #ml) == ml and lt - lm <= 3 then return true end
  -- Beugung vor dem letzten Wort (netzbildende/netzbildender)
  if not letztes and lm >= 6 and ml:sub(1, #tl) == tl and lm - lt <= 2 then return true end
  return false
end

local function stichwort_marker(wort)
  local s = wort:gsub('\\', '\\\\'):gsub('"', '\\"')
  return pandoc.RawInline('typst', '#metadata("' .. s .. '")<stichwort>')
end

local function lade_stichwoerter(pfad)
  local f = io.open(pfad, 'r')
  if not f then return nil end
  local daten = pandoc.json.decode(f:read('a'), false)
  f:close()
  local index = {}
  for _, e in ipairs(daten) do
    for _, m in ipairs(e.muster) do
      local woerter = {}
      for w in m:gmatch('%S+') do woerter[#woerter + 1] = w end
      if #woerter > 0 then
        local k = ist_kuerzel(woerter[1]) and woerter[1] or pandoc.text.lower(woerter[1])
        k = pandoc.text.sub(k, 1, 4)
        index[k] = index[k] or {}
        table.insert(index[k], {wort = e.wort, teile = woerter})
      end
    end
  end
  return index
end

local function markiere_inlines(inlines, index, gesehen)
  local out, geaendert = pandoc.Inlines({}), false
  for i, el in ipairs(inlines) do
    if el.t == 'Str' then
      local tok1 = normiert(el.text)
      if tok1 ~= '' then
        local kandidaten = {}
        for _, k in ipairs({pandoc.text.sub(tok1, 1, 4), pandoc.text.sub(pandoc.text.lower(tok1), 1, 4)}) do
          for _, c in ipairs(index[k] or {}) do kandidaten[#kandidaten + 1] = c end
        end
        for _, c in ipairs(kandidaten) do
          if not gesehen[c.wort] then
            local ok, j = true, i
            for n, teil in ipairs(c.teile) do
              if n > 1 then
                if not (inlines[j + 1] and (inlines[j + 1].t == 'Space' or inlines[j + 1].t == 'SoftBreak')
                        and inlines[j + 2] and inlines[j + 2].t == 'Str') then ok = false; break end
                j = j + 2
              end
              local tok = (n == 1) and tok1 or normiert(inlines[j].text)
              if not passt(tok, teil, n == #c.teile) then ok = false; break end
            end
            if ok then
              out:insert(stichwort_marker(c.wort))
              gesehen[c.wort] = true
              geaendert = true
            end
          end
        end
      end
    end
    out:insert(el)
  end
  if geaendert then return out end
  return nil
end

local function stichwoerter_setzen(blocks, index)
  local gesehen, anhang, quellen = {}, false, false
  local neu = pandoc.Blocks({})
  for _, blk in ipairs(blocks) do
    if blk.t == 'Header' then
      if blk.level == 1 then gesehen = {} end
      if blk.level <= 2 then quellen = false end
      if blk.level == 1 then anhang = blk.classes:includes('anhang') end
      if blk.level == 2 and stringify(blk.content):match('^Quellen und Stand') then quellen = true end
      neu:insert(blk)
    elseif anhang or quellen or blk.t == 'Figure' or blk.t == 'RawBlock' then
      neu:insert(blk)
    else
      neu:insert(blk:walk({ Inlines = function(il) return markiere_inlines(il, index, gesehen) end }))
    end
  end
  return neu
end

-- Gesamtbuch: nicht nummerierte Abschnitte (Warum, Rechenbeispiele, Zusammenfassung, Übungen, Quellen)
-- nicht ins Inhaltsverzeichnis; Klasse .toc behält sie (z. B. Kapitel im Lösungsanhang).
local function buch_ueberschriften(blocks)
  return blocks:walk({ Header = function(h)
    if h.level == 1 and h.classes:includes('teil') then
      local inhalt = pandoc.write(pandoc.Pandoc({pandoc.Plain(h.content)}), 'typst'):gsub('%s+$', '')
      return pandoc.RawBlock('typst', '#heading(level: 1, numbering: none)[' .. inhalt .. '] <teil>')
    end
    if h.level == 2 and h.classes:includes('unnumbered') and not h.classes:includes('toc') then
      local inhalt = pandoc.write(pandoc.Pandoc({pandoc.Plain(h.content)}), 'typst'):gsub('%s+$', '')
      return pandoc.RawBlock('typst', '#heading(level: 2, numbering: none, outlined: false)[' .. inhalt .. ']')
    end
  end })
end

local function pandoc_typst(doc)
  local meta = doc.meta
  if meta['nummerierung'] and pandoc.text.lower(stringify(meta['nummerierung'])) == 'kapitelweise' then
    meta['nummerierung-kapitelweise'] = true
    -- Kapiteldateien: lebender Kolumnentitel mit Kapitelnummer, sofern nicht anders angegeben
    if not meta['kolumnentitel'] then meta['kolumnentitel-kapitel'] = true end
  end
  local start = tonumber(meta['kapitel-start'] and stringify(meta['kapitel-start']) or '1') or 1
  if start > 1 then meta['kapitel-offset'] = pandoc.MetaString(tostring(start - 1)) end
  if meta['kolumnentitel'] and pandoc.text.lower(stringify(meta['kolumnentitel'])) == 'kapitel' then
    meta['kolumnentitel-kapitel'] = true
  end
  local info = meta['deckblatt-info']
  if info and type(info) == 'table' and info[1] then
    local zeilen = pandoc.List()
    for _, zeile in ipairs(info) do
      local s = stringify(zeile)
      local k, v = s:match('^([^:]+):%s*(.*)$')
      if not k then k, v = '', s end
      if k ~= '' then k = k .. ':' end
      zeilen:insert(pandoc.MetaMap({k = pandoc.MetaInlines(pandoc.Inlines(k)),
                                    v = pandoc.MetaInlines(pandoc.Inlines(v))}))
    end
    meta['deckblatt-zeilen'] = pandoc.MetaList(zeilen)
  end
  doc.meta = meta
  local datei = meta['stichwort-datei'] and stringify(meta['stichwort-datei'])
  if datei and datei ~= '' then
    local index = lade_stichwoerter(datei)
    if index then doc.blocks = stichwoerter_setzen(doc.blocks, index) end
  end
  if meta_bool(meta, 'buch', false) then doc.blocks = buch_ueberschriften(doc.blocks) end
  doc.blocks = doc.blocks:walk({ Div = function(d) if d.classes:includes('nur-docx') then return {} end end })
  doc.blocks = doc.blocks:walk({ Table = function(tb) return spaltenbreiten(tabellen_maskieren(tb)) end, Math = typst_math })
  doc.blocks = doc.blocks:walk({ Blocks = quellenzeilen })
  return doc
end

function Pandoc(doc)
  if is_typst then return pandoc_typst(doc) end
  local meta = doc.meta
  local kapitelweise = meta['nummerierung'] and
    pandoc.text.lower(stringify(meta['nummerierung'])) == 'kapitelweise'
  local kap = (tonumber(meta['kapitel-start'] and stringify(meta['kapitel-start']) or '1') or 1) - 1
  local ntab, nfig = 0, 0
  local h1_neue_seite = meta_bool(meta, 'h1-neue-seite', false)
  local nummern = meta_bool(meta, 'ueberschriften-nummern', true)
  local nummern_tiefe = tonumber(meta['nummern-tiefe'] and stringify(meta['nummern-tiefe'])
                                 or '3') or 3
  local zaehler = {kap, 0, 0, 0, 0, 0}
  local kap_label = tostring(kap)
  local erste_h1 = true

  local blocks = pandoc.List()
  for _, blk in ipairs(doc.blocks) do
    if blk.t == 'Header' then
      local lvl = blk.level
      if not blk.classes:includes('unnumbered') then
        if lvl == 1 then
          kap = kap + 1
          kap_label = tostring(kap)
          zaehler = {kap, 0, 0, 0, 0, 0}
          if kapitelweise then ntab, nfig = 0, 0 end
        else
          zaehler[lvl] = zaehler[lvl] + 1
          for j = lvl + 1, 6 do zaehler[j] = 0 end
        end
        if nummern and lvl <= nummern_tiefe then
          local teile = {}
          for j = 1, lvl do teile[#teile + 1] = tostring(zaehler[j]) end
          blk.content:insert(1, pandoc.Str(table.concat(teile, '.') .. '\u{2002}'))
        end
      end
      if lvl == 1 then
        if h1_neue_seite and not erste_h1 then blocks:insert(seitenumbruch()) end
        erste_h1 = false
        local buchstabe = blk.classes:includes('anhang') and stringify(blk.content):match('^Anhang (%u)')
        if buchstabe then kap_label = buchstabe; ntab, nfig = 0, 0 end
      end
    end
    local ergebnis = pandoc.Blocks({blk}):walk({
      Table = function(t)
        local cap = t.caption
        if cap and cap.long and #cap.long > 0 then
          ntab = ntab + 1
          local nr = kapitelweise and (kap_label .. '.' .. ntab) or tostring(ntab)
          local lang = cap.long
          prefix_caption(lang, 'Tabelle' .. NBSP .. nr)
          cap.long = lang
          t.caption = cap
        end
        return t
      end,
      Figure = function(f)
        local cap = f.caption
        if cap and cap.long and #cap.long > 0 then
          nfig = nfig + 1
          local nr = kapitelweise and (kap_label .. '.' .. nfig) or tostring(nfig)
          local lang = cap.long
          prefix_caption(lang, 'Abbildung' .. NBSP .. nr)
          cap.long = lang
          f.caption = cap
        end
        return f
      end,
    })
    blocks:extend(ergebnis)
  end

  local vorspann = pandoc.List()
  local info = meta['deckblatt-info']
  if info then
    if info.t == 'MetaList' or type(info) == 'table' and info[1] then
      for _, zeile in ipairs(info) do
        local s = stringify(zeile)
        local k, v = s:match('^([^:]+):%s*(.*)$')
        local inl
        if k then
          inl = {pandoc.Strong({pandoc.Str(k .. ':')}), pandoc.Str('\t' .. v)}
        else
          inl = {pandoc.Str(s)}
        end
        vorspann:insert(pandoc.Div({pandoc.Para(inl)}, {['custom-style'] = 'Deckblatt Meta'}))
      end
    end
  end
  if meta['deckblatt-hinweis'] then
    vorspann:insert(pandoc.Div({pandoc.Para({pandoc.Str(stringify(meta['deckblatt-hinweis']))})},
      {['custom-style'] = 'Deckblatt Hinweis'}))
  end
  if is_docx and meta_bool(meta, 'inhaltsverzeichnis', false) then
    local tiefe = tonumber(meta['toc-tiefe'] and stringify(meta['toc-tiefe']) or '2') or 2
    vorspann:insert(seitenumbruch())
    vorspann:insert(toc_block(tiefe))
    vorspann:insert(seitenumbruch())
  elseif #vorspann > 0 then
    vorspann:insert(seitenumbruch())
  end
  vorspann:extend(blocks)
  doc.blocks = vorspann
  return doc
end

return {
  { Inlines = vermerke },
  { BlockQuote = BlockQuote, RawBlock = RawBlock },
  { Pandoc = Pandoc },
}
