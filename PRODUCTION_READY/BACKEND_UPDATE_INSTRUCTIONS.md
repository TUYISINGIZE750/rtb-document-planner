# BACKEND UPDATE INSTRUCTIONS

## Files to Upload to PythonAnywhere

Upload these 3 files to `/home/leonardus437/`:

1. **document_generator.py** (Updated with RTB template support)
2. **rtb_session_plan_template.docx** (Official RTB template)
3. **rtb_scheme_template.docx** (Official RTB template)

## Steps:

### 1. Upload Files
- Go to PythonAnywhere Files tab
- Navigate to `/home/leonardus437/`
- Upload the 3 files from `PRODUCTION_READY/backend/`

### 2. Reload Web App
- Go to Web tab
- Click green "Reload" button
- Wait 30 seconds

### 3. Test
- Visit: https://leonardus437.pythonanywhere.com/
- Should see API status online

## What Changed:

### ✅ Document Generator Improvements:
- Now uses official RTB templates as base
- Better table formatting with proper borders
- Correct cell background colors (RTB blue header)
- Proper column widths and spacing
- Falls back to creating from scratch if templates not found

### ✅ Frontend Dashboard Updates:
- Upgrade card now hidden for premium users
- When free downloads end, buttons show subscription modal
- Upgrade card highlighted when limits reached
- Better visual feedback for users

## Testing Checklist:

- [ ] Create session plan - document matches RTB format
- [ ] Create scheme of work - document matches RTB format
- [ ] Free user reaches limit - sees subscription modal
- [ ] Premium user - upgrade card hidden
- [ ] Documents have proper RTB headers and formatting

## Rollback:

If issues occur, keep backup of old `document_generator.py` and restore it.
