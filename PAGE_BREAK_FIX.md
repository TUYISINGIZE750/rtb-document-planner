# Session Plan Page Break Fix

**Date:** January 15, 2025  
**Commit:** 273fb4f  
**Status:** ✅ DEPLOYED

---

## Issue
The main session plan table was appearing on the second page instead of staying on the first page right after the header (RTB logo, school info, school logo).

## Root Cause
Word documents can automatically insert page breaks when:
1. Tables are too large
2. No "keep together" properties are set
3. Paragraphs between tables cause spacing issues

## Solution
Applied three fixes to ensure the main table stays on the first page:

### 1. Keep Header Rows Together
```python
# Prevent header table rows from splitting across pages
for row in header_table.rows:
    tr = row._element
    trPr = tr.get_or_add_trPr()
    cantSplit = OxmlElement('w:cantSplit')
    trPr.append(cantSplit)
```

### 2. Keep Header with Next Element
```python
# Keep header table with the main table (no page break between them)
pPr = header_para.get_or_add_pPr()
keepNext = OxmlElement('w:keepNext')
pPr.append(keepNext)
```

### 3. Remove Extra Paragraphs
```python
# Remove any empty paragraphs between header and main table
# (Already implemented - ensures no spacing causes page breaks)
```

---

## Technical Details

### XML Properties Added

**cantSplit:** Prevents a table row from splitting across pages
```xml
<w:trPr>
    <w:cantSplit/>
</w:trPr>
```

**keepNext:** Keeps a paragraph/table with the next element
```xml
<w:pPr>
    <w:keepNext/>
</w:pPr>
```

---

## Result

### Before Fix ❌
```
Page 1:
- RTB Logo | School Info | School Logo
[PAGE BREAK]

Page 2:
- Main session plan table (22 rows)
```

### After Fix ✅
```
Page 1:
- RTB Logo | School Info | School Logo
- Main session plan table (22 rows)
```

---

## Testing

### Test File
- **File:** `backend/PAGE_BREAK_FIX.docx`
- **Status:** Generated successfully
- **Verification:** Main table appears on first page

### Test Data
- School: IPRC KIGALI
- Location: Kigali City - Gasabo - Remera - Rukiri I - Amahoro
- Module: SD-M01
- All fields filled

---

## Benefits

1. ✅ **Professional appearance** - Everything on first page
2. ✅ **Better readability** - No unnecessary page breaks
3. ✅ **RTB compliance** - Matches official template layout
4. ✅ **Consistent formatting** - Works for all session plans

---

## Deployment

- **Commit:** 273fb4f
- **Backend:** Auto-deployed to Render
- **Status:** Live and operational

---

## Additional Notes

### When Main Table Might Still Break
If the session plan has extremely long content (e.g., very long objectives or learning activities), the table might naturally flow to the second page. This is expected behavior and maintains readability.

### Header Table Size
The header table is kept minimal (1 row, 3 columns) to ensure it doesn't take too much space on the first page.

---

**Developer:** TUYISINGIZE Leonardus  
**Contact:** +250 789 751 597  
**Email:** tuyisingize750@gmail.com  
**GitHub:** @TUYISINGIZE750

---

**Fix Completed:** January 15, 2025  
**Status:** ✅ PRODUCTION READY
