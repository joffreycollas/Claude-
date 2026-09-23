---
name: ALTHO Expertise, révision des honoraires
description: A daylight office desk where a real-scale A4 letter sits at the centre and every control around it changes what goes on the paper.
colors:
  bordeaux: "#9d202e"
  bordeaux-hover: "#7c1823"
  bordeaux-tint: "oklch(95.5% 0.018 18)"
  bordeaux-tint-2: "oklch(90.5% 0.042 18)"
  letter-highlight: "oklch(92% 0.04 18)"
  letter-hover: "oklch(96.5% 0.016 18)"
  desk: "oklch(93.5% 0.006 75)"
  desk-deep: "oklch(90% 0.008 75)"
  panel: "oklch(98.6% 0.003 75)"
  paper: "#ffffff"
  ink: "oklch(21% 0.006 30)"
  ink-2: "oklch(38% 0.008 30)"
  ink-3: "oklch(48% 0.008 30)"
  rule: "oklch(87.5% 0.007 75)"
  rule-soft: "oklch(92% 0.005 75)"
  up: "oklch(45% 0.11 150)"
  warn-tint: "oklch(95% 0.045 80)"
  warn-ink: "oklch(38% 0.1 60)"
  danger: "oklch(50% 0.17 27)"
  danger-tint: "oklch(95.5% 0.03 27)"
  letter-ink: "#1a1a1a"
  letter-ink-2: "#3d3d3d"
  letter-rule: "#e3dcdc"
  letter-total: "#f6ebec"
  letter-foot: "#6b7280"
  letter-placeholder: "#9aa3b2"
typography:
  brand:
    fontFamily: "Hanken Grotesk, Segoe UI, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.02em"
  headline:
    fontFamily: "Hanken Grotesk, Segoe UI, system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 700
    lineHeight: 1.25
  title:
    fontFamily: "Hanken Grotesk, Segoe UI, system-ui, sans-serif"
    fontSize: "14.5px"
    fontWeight: 600
    lineHeight: 1.45
  body:
    fontFamily: "Hanken Grotesk, Segoe UI, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.45
    fontFeature: "tnum"
  label:
    fontFamily: "Hanken Grotesk, Segoe UI, system-ui, sans-serif"
    fontSize: "12.5px"
    fontWeight: 600
    lineHeight: 1.45
  section-head:
    fontFamily: "Hanken Grotesk, Segoe UI, system-ui, sans-serif"
    fontSize: "12.5px"
    fontWeight: 700
    letterSpacing: "0.06em"
  letter-letterhead:
    fontFamily: "Hanken Grotesk, Arial, sans-serif"
    fontSize: "16.5pt"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.02em"
  letter-body:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "9.5pt"
    fontWeight: 400
    lineHeight: 1.33
    fontFeature: "tnum"
  letter-address:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "10.2pt"
    fontWeight: 400
    lineHeight: 1.38
  letter-table:
    fontFamily: "Hanken Grotesk, Arial, sans-serif"
    fontSize: "8.8pt"
    fontWeight: 400
    fontFeature: "tnum"
  letter-footer:
    fontFamily: "Hanken Grotesk, Arial, sans-serif"
    fontSize: "7pt"
    fontWeight: 400
    lineHeight: 1.35
rounded:
  xs: "4px"
  s: "6px"
  m: "8px"
  dialog: "10px"
  pill: "13px"
spacing:
  xs: "4px"
  s: "8px"
  m: "14px"
  l: "20px"
  xl: "24px"
components:
  button-primary:
    backgroundColor: "{colors.bordeaux}"
    textColor: "{colors.paper}"
    rounded: "{rounded.s}"
    padding: "0 14px"
    height: "36px"
  button-primary-hover:
    backgroundColor: "{colors.bordeaux-hover}"
  button-secondary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.s}"
    padding: "0 14px"
    height: "36px"
  button-secondary-hover:
    backgroundColor: "{colors.rule-soft}"
  button-quiet:
    textColor: "{colors.ink-2}"
    rounded: "{rounded.s}"
    padding: "0 14px"
    height: "36px"
  button-quiet-hover:
    backgroundColor: "{colors.desk-deep}"
    textColor: "{colors.ink}"
  button-danger:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.danger}"
    rounded: "{rounded.s}"
  button-danger-hover:
    backgroundColor: "{colors.danger-tint}"
  input:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.s}"
    padding: "0 9px"
    height: "34px"
  tab:
    textColor: "{colors.ink-2}"
    typography: "{typography.title}"
    padding: "0 14px"
  tab-selected:
    textColor: "{colors.bordeaux}"
  chip:
    backgroundColor: "{colors.desk-deep}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "0 10px"
    height: "26px"
  chip-go:
    backgroundColor: "{colors.bordeaux-tint}"
    textColor: "{colors.bordeaux}"
  chip-warn:
    backgroundColor: "{colors.warn-tint}"
    textColor: "{colors.warn-ink}"
  segmented:
    backgroundColor: "{colors.desk}"
    rounded: "{rounded.s}"
    padding: "3px"
  segmented-selected:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.bordeaux}"
  list-item:
    rounded: "{rounded.s}"
    padding: "9px 8px"
  list-item-current:
    backgroundColor: "{colors.bordeaux-tint}"
    textColor: "{colors.bordeaux}"
  letter-sheet:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.letter-ink}"
    typography: "{typography.letter-body}"
    width: "210mm"
    height: "297mm"
---

# Design System: ALTHO Expertise, révision des honoraires

## Overview

**Creative North Star: "The Letter on the Desk"**

The printed letter is the product. A white A4 sheet at true scale lies at the centre of a warm-grey daylight desk, with a real paper shadow under it, and every control around it (the client list on the left, the client record on the right, the settings form) exists to change what is on that paper. The interface is quiet so the sheet can be the loudest object on screen. There are no dashboard cards, no metric tiles and no spreadsheet chrome in the working view. The Clients view is a table because editing thirty rows of fees is table work, but it still sits on the same desk as a single bordered sheet.

The world is lit like an office in daylight. It has one ink: the bordeaux of the ALTHO letterhead. That bordeaux carries the primary action, the selection, the focus ring and the letter's own letterhead and table header. Everything else is warm-grey paper, hairline rules and near-black ink. Density is that of a working tool used once a year by a non-technical accountant. Labels are explicit French words, targets are 30 to 36px tall, and every amount uses tabular figures so columns of euros line up.

Type follows the Anthropic pairing the user asked for (a geometric grotesque over a text serif), set with free look-alikes embedded in the file: Hanken Grotesk for the interface and the letter's structure (letterhead, references, fee table, footer), Source Serif 4 for the letter's prose and address. The fonts print the same on every machine. The theme is light only. The office-daylight scene is the world, and a dark mode would turn the paper metaphor upside down.

**Key Characteristics:**
- A real-scale A4 sheet with a layered paper shadow is the centrepiece; panels frame it rather than compete with it.
- One accent ink (bordeaux #9d202e); all tints are bordeaux tints, never a second hue.
- Two families, one pairing: Hanken Grotesk (UI and letter structure) and Source Serif 4 (letter prose); tabular numerals everywhere.
- Hairline rules (1px) and 6–8px radii instead of cards and heavy borders.
- Flat panels; shadows are reserved for paper and for floating layers.
- Light theme only.

## Colors

A warm-grey desk, near-white panels, near-black ink and one bordeaux accent. Status colours appear only as text or pale tints, never as fills that compete with the bordeaux.

### Primary
- **ALTHO Bordeaux** (bordeaux): the only accent. It is used for the primary button, the selected tab underline, the current list item's name, segmented and radio selections, checkboxes and toggles (via `accent-color`), the caret, the focus outline, and the letter's fee-table header. It is sampled from the firm's logo and letterhead (#9D202E, RGB 157/32/46).
- **Deep Bordeaux** (bordeaux-hover): the hover state of the primary button only.
- **Bordeaux Tint** (bordeaux-tint): pale bordeaux wash behind the current client in the list, the "par courrier" chip, and hovered menu rows.
- **Bordeaux Tint Strong** (bordeaux-tint-2): the 3px focus halo around inputs and the text selection colour.
- **Letter Highlight** (letter-highlight): the wash that lights up a field's place on the letter when that field is hovered or edited in the client record. **Letter Hover** (letter-hover) is the fainter wash for hovering a live field directly on the sheet.

### Neutral
- **Daylight Desk** (desk): the app background, the surface the sheet rests on, and the track of segmented controls.
- **Desk Shadow** (desk-deep): the hover wash for quiet and icon buttons, and neutral chips.
- **Panel White** (panel): top bar, client rail, client record, toolbar, settings form, sticky table headers. It is barely warmer than paper, so panels read as part of the desk rather than as cards.
- **Paper** (paper): the letter sheet, inputs, secondary buttons, menus, dialogs and the Clients table body.
- **Ink** (ink): primary text and the toast background. **Ink 2** (ink-2): secondary text, labels and inactive tabs. **Ink 3** (ink-3): meta text, placeholders, counts and hints.
- **Rule** (rule): 1px panel borders and input strokes. **Rule Soft** (rule-soft): inner dividers between list sections, fee rows and table rows.

### Status (semantic, not accent)
- **Increase Green** (up): the "+3,5 %" and "+126 €" deltas beside new amounts. Text only.
- **Notice Amber** (warn-tint with warn-ink): the fictional-sample notice, the "exemple" tag and warning chips.
- **Error Red** (danger with danger-tint): destructive buttons, invalid fields (red border plus a red-tint halo) and error text.

### Letter inks
The letter uses fixed hex inks so it prints identically regardless of the UI tokens: **Letter Ink** (letter-ink) for body text, **Letter Ink 2** (letter-ink-2) for the letterhead address, references and the monthly-instalment line, **Letter Rule** (letter-rule) for table row rules, **Letter Total** (letter-total) for the bordeaux-tinted total row, **Letter Foot** (letter-foot) for the legal footer, and **Letter Placeholder** (letter-placeholder) for on-screen placeholder text.

### Named Rules
**The One Ink Rule.** Bordeaux is the only accent. Emphasis, selection, focus and the letter-to-field highlight are all bordeaux or bordeaux tints. There is no second highlight hue. Green, amber and red are status signals, not accents.

**The Desk Is Warm, the Ink Is Cool Rule.** Surfaces sit at hue 75 (warm grey) and inks sit at hue 30 (a near-black with the faintest warmth). Don't introduce neutrals outside these two hues.

## Typography

**Display Font:** none (no display face)
**UI and Structure Font:** Hanken Grotesk (embedded woff2, variable 400–700), fallbacks Segoe UI / system-ui, Arial on the letter
**Letter Text Font:** Source Serif 4 (embedded woff2, variable 400–700 with optical sizing, plus italic 400), fallback Georgia
**Label/Mono Font:** Hanken Grotesk; code-like tags such as `{civilite}` use it too

**Character:** The pairing echoes Anthropic's Styrene-over-Tiempos voice without its licensed faces: a clean geometric grotesque for everything the user operates and for the letter's frame, a warm text serif for what the client reads. In the UI, hierarchy comes from weight (400 / 600 / 700) and size only.

### Hierarchy
- **Brand**: the firm's own logo image (30px tall) in the top bar, followed by "Révision des honoraires" in Label style.
- **Headline** (700, 18px, 1.25): the client name at the top of the client record and dialog titles. The settings section titles use 16px/700 and the empty-state title uses 20px.
- **Title** (600, 14.5px): tabs and the stage bar's client name.
- **Body** (400, 15px, 1.45): base UI text. Buttons and inputs are 14px/600 and 14px/400.
- **Label** (600, 12.5px): field labels, list sub-lines, counts and the rail footer. Hints and deltas are 12px.
- **Section Head** (700, 12.5px, +0.06em, uppercase, ink-2): headings for field groups in the client record ("Destinataire", "Honoraires annuels HT", "Envoi"). It is a real heading for the group below it, not a kicker above another title.
- **Letter** (letterhead and footer are the firm's own letterhead images, not type; letter-address Source Serif 10.2pt; letter-body Source Serif 9.5pt/1.33; letter-table Hanken 8.8pt, headers nowrap; references Hanken 9pt): print sizes in points. The worst case (four missions, two-line address, signatory set) leaves about 6mm above the letterhead footer image.

### Named Rules
**The One Pairing Rule.** Hanken Grotesk and Source Serif 4, both embedded, are the only families. The serif is reserved for the letter's prose and address; the UI never uses it. Don't add a third face, and never ship Anthropic's licensed fonts (Styrene, Tiempos) in the file. Don't rely on a web font request; the file works offline.

**The Tabular Rule.** `font-variant-numeric: tabular-nums` is set on the root and on the sheet. Every amount, percentage and count uses tabular figures, and amounts are right-aligned in every table and number input.

**The Ragged-Right Letter Rule.** Letter paragraphs are left-aligned, never justified. Justifying a 170mm measure produced loose word spacing.

**The Superscript Ordinal Rule.** On the letter, "1er" is always set as `1<sup>er</sup>` (0.66em, raised 0.5em, zero line-height so line spacing is not disturbed).

## Layout

The app is a fixed-height grid: a 56px top bar over one working view. The Courriers view is a three-column desk: a 300px client rail, the flexible stage holding the sheet, and a 340px client record. The sheet is set at 210 × 297mm and scaled to fit the stage height (with a "Taille réelle" toggle for true scale), centred with `justify-content: safe center`. On the letter, the recipient block sits at 110mm from the left and 52mm from the top, inside a DL window (100 × 45mm at 100mm, 47mm) that an "Enveloppe" toggle draws on the sheet. Fold marks are drawn in the left margin.

The Clients view is a toolbar, a totals line and one bordered table with the first three columns (send, ref, company) sticky. The Réglages view pairs a 620px form column with the live sheet.

Spacing follows a loose 4px-based rhythm: 4 / 8 / 10 within controls, 14 / 18 / 20 for panel padding, 22–24 between sections and around dialogs.

**Responsive:** at 1180px and below, the desk becomes rail + stage, and the client record drops under them at full width; settings stack. At 760px and below, the top bar wraps with the tabs on their own scrolling row, the print button shows a short label, the rail becomes a 46vh block above the sheet, and paired fields go full width except the rows marked to stay together (civility / first name / surname, and postcode / city). The page gutter is 16px at phone width.

## Elevation & Depth

The system is flat by default. Panels are separated from the desk by 1px rules and a slight tone step (panel against desk), not by shadows. Shadows exist for exactly two physical things: paper lying on the desk, and layers that float above everything (menus, dialogs, toasts). A tiny 1px shadow lifts the selected thumb in segmented controls and the toggle knob.

### Shadow Vocabulary
- **Paper** (`box-shadow: 0 1px 2px oklch(28% 0.01 30 / 0.10), 0 8px 24px oklch(28% 0.01 30 / 0.10), 0 24px 60px oklch(28% 0.01 30 / 0.08)`): the on-screen letter only. It is removed in print.
- **Pop** (`box-shadow: 0 4px 12px oklch(28% 0.01 30 / 0.14), 0 16px 40px oklch(28% 0.01 30 / 0.12)`): print menu, dialogs, toast.
- **Thumb** (`box-shadow: 0 1px 2px oklch(28% 0.01 30 / 0.14)`): selected segment or radio option, toggle knob.
- **Sticky edge** (`box-shadow: 6px 0 8px -6px oklch(28% 0.01 30 / 0.22)`): the right edge of the sticky columns in the Clients table while scrolling horizontally.

### Named Rules
**The Only Paper Casts a Shadow Rule.** On the working surface, only the letter has a real shadow. Panels, lists and tables stay flat. If something needs separating, use a rule or a tone step.

## Shapes

Gently rounded, never pill-heavy. Controls, inputs, list rows and segmented tracks use 6px corners. Menus, the Clients table and the toast use 8px, and dialogs use 10px. Chips are fully rounded (13px on a 26px height), and small inline tags use 4px. The letter itself is square-cornered. Only the field highlight on the sheet has a 1mm radius, and the envelope window a 2mm dashed outline. Lines are hairlines: 1px in the UI, 0.25–0.6mm on the letter.

## Components

### Buttons
Restrained and solid: flat fills with no gradient or lift.
- **Shape:** gently rounded (6px), 36px tall, 14px/600 label with an optional 18px stroke icon and an 8px gap. The small variant is 30px tall.
- **Primary:** bordeaux fill, white label, deepening to bordeaux-hover on hover. Used once per view for the main action, such as "Imprimer les courriers postaux (N)" (a split button with a caret for other print options) or "Importer un fichier Excel ou CSV".
- **Secondary:** paper fill with a rule-coloured 1px stroke, turning rule-soft on hover.
- **Quiet:** no fill or stroke, ink-2 text; desk-deep wash and ink text on hover. Used for less frequent actions ("Supprimer les exemples", "Exporter pour Excel").
- **Danger:** secondary shape with red text and a red-tint wash on hover.
- **Focus / Disabled:** 2px bordeaux outline, 2px offset, on every focusable element. Disabled buttons drop to 45% opacity.

### Chips
- **Style:** 26px pill, 12.5px/600. The neutral chip is desk-deep with ink-2 text.
- **State:** "go" (bordeaux tint with bordeaux text) marks the send mode on the stage bar; "warn" (amber tint with amber ink) flags problems. The Clients table uses a smaller 4px-radius amber "exemple" tag for fictional rows.

### Inputs / Fields
- **Style:** paper fill, 1px rule stroke, 6px radius, 34px tall (32px in the fee table, 30px in the Clients grid, where the stroke stays transparent until hover). Labels sit above in 12.5px/600 ink-2. Numeric inputs are right-aligned. Percentage and euro inputs carry a "%" or "€" suffix inside the field.
- **Focus:** the border turns bordeaux with a 3px bordeaux-tint-2 halo. There is no browser outline on text fields.
- **Error:** red border, 3px red-tint halo, 12px red message below.

### Navigation
Text tabs in the top bar (14.5px/600, ink-2). The selected tab turns bordeaux with a 2px bordeaux underline inset 10px from each side. Counts sit beside the label in 12.5px ink-3. Segmented filters (Tous / Poste / E-mail / Non envoyés) use a desk-coloured track with a paper thumb and bordeaux text for the selected option. The same pattern is used for radio groups in the client record.

### Client List Item
A three-column row: checkbox, company plus "ref · city", and the new total with its green delta beneath. The current item gets a bordeaux-tint background and a bordeaux name, and hover gives a desk wash. Unselected ("not sending") clients drop to ink-3.

### The Letter (signature component)
A 210 × 297mm sheet with 20mm side margins, printed on the firm's own letterhead: the header image from `Papier_en_t_te_definitif.docx` (181mm wide, 8mm from the top, 14.8mm from the left) and its footer image (180mm wide, 7mm from the bottom, carrying the legal mentions, address and contacts), both embedded from `app/assets/` (provenance in `app/assets/PROVENANCE.md`). Between them: a reference block on the left and a recipient block in the DL window on the right, the subject, paragraphs, a two-column fee table (Mission, Honoraires annuels HT: the new amounts only, typed by hand; no former amount, rate or difference is ever printed) with a bordeaux header row and a bordeaux-tinted total row, an italic monthly-instalment line and the signature at 90mm. Only missions with an amount appear in the table.
- **Live link:** hovering or editing a field in the client record washes its place on the letter with letter-highlight (plus a 1.2mm spread of the same tint). Hovering a field on the sheet gives a fainter letter-hover wash and clicking it goes to that field. The transition is 180ms on the shared ease-out curve (`cubic-bezier(0.16, 1, 0.3, 1)`).
- **Envelope window:** a toggle draws the DL window as a dashed bordeaux outline with a 5% bordeaux wash and a small caption, to show the address fits.
- **Placeholders:** empty fields show italic letter-placeholder text on the on-screen letter only. The print render emits nothing in their place.
- **Print:** A4 portrait with zero page margin, one letter per page. Shadow, envelope window and highlights are stripped.

## Do's and Don'ts

### Do:
- **Do** keep the A4 sheet at the centre of any view that edits letter content, and let the controls around it change it live.
- **Do** use bordeaux (#9d202e) as the single accent for the primary action, selection and focus, and bordeaux tints for every highlight, including the letter-to-field link.
- **Do** set every amount in tabular figures and right-align it.
- **Do** keep letter paragraphs left-aligned and set "1er" as a superscript ordinal.
- **Do** show placeholder text only on the on-screen letter and make sure the print render never contains it.
- **Do** separate panels with 1px rules and the panel/desk tone step; keep radii at 6px for controls and 8px for floating layers and tables.
- **Do** embed Hanken Grotesk and Source Serif 4 in the file so the app and the letter render identically offline.

### Don't:
- **Don't** introduce a second accent hue. Amber, green and red are status signals only, and the field highlight is bordeaux, not yellow.
- **Don't** justify letter text.
- **Don't** add a second type family or a system display face.
- **Don't** add a dark theme; the world is an office in daylight.
- **Don't** wrap content in shadowed cards or build admin-dashboard metric tiles; only the paper and floating layers cast shadows.
- **Don't** let the envelope window, highlights, placeholders or the paper shadow reach the printed page.
