# Final Fixes Needed

## Issue 1: Scheme of Work "Invalid Document ID" Error ✅

**Problem**: The error message appears to be a duplicate function definition in scheme-wizard.html

**Fix**: The scheme wizard has TWO `checkDownloadLimits()` functions defined. Remove the duplicate.

**Location**: Line ~450 in scheme-wizard.html

**Action**: Remove the second `checkDownloadLimits()` function (the one with the `id` parameter)

## Issue 2: RTB-Inspired Landing Page

**Current**: Modern gradient design
**Needed**: Professional RTB.gov.rw style

**Changes Required**:

### 1. Color Scheme
- Primary: #003366 (RTB Blue)
- Secondary: #FFD700 (Gold)
- Background: White/Light Gray
- Text: Dark Gray (#333)

### 2. Layout
- Clean header with RTB logo
- Professional navigation
- Hero section with RTB imagery
- Service cards (Session Plans, Schemes)
- Footer with contact info

### 3. Images
Use RTB-related images:
- TVET training photos
- Technical education
- Rwanda classroom settings
- Professional learning environments

### 4. Typography
- Professional fonts (Arial, Helvetica)
- Clear hierarchy
- Readable sizes

## Quick Fix Files

I'll create 2 files:
1. Fixed scheme-wizard.html (remove duplicate function)
2. New RTB-style index.html (professional design)

Upload to PythonAnywhere and Cloudflare.
