# Comprehensive Scheme of Work - Implementation Plan

## Current Status
✅ Session Plans - FULLY WORKING with:
- Dynamic SMART objectives
- Technique-specific Development sections
- Delete functionality
- Professional RTB formatting

## Scheme of Work - Enhancement Needed

### What's Required:
1. **Landscape Layout** - A4 Landscape orientation
2. **Comprehensive Teacher Input Form** with ALL fields:
   - Province, District, Sector, School
   - Module details, rationale, entry requirements
   - Term-by-term planning (Term 1, 2, 3)
   - Learning outcomes, indicative contents, activities
   - Resources, assessment, learning place
   - Integrated assessment per term
   - Sign-offs (Trainer, DOS, Manager)

3. **Generated Document** matching SCHEME_OF_WORK_OF_C_PROGRAMMING_L4CSA.docx format

### Implementation Steps:

#### Step 1: Update Frontend Form
Add comprehensive input fields in `frontend/index.html`:
- Institutional info (7 fields)
- Module overview (8 fields)
- Term 1 planning (repeatable rows)
- Term 2 planning (repeatable rows)
- Term 3 planning (repeatable rows)
- Assessment details (5 fields)
- Resources (5 fields)
- Sign-offs (3 fields)

#### Step 2: Update Database Schema
Add new columns to `SchemeOfWork` model:
```python
province, district, school, department_trade
module_rationale, entry_requirements, competency_codes
term1_data, term2_data, term3_data (JSON)
formative_assessment, summative_assessment
resource_inventory, health_safety
dos_name, manager_name
```

#### Step 3: Update Document Generator
Create landscape-formatted DOCX with:
- School header (Province/District/Sector/School)
- Module information table
- Term 1 table (Weeks, LO, Duration, IC, Activities, Resources, Assessment, Place)
- Term 2 table (same structure)
- Term 3 table (same structure)
- Integrated assessment sections
- Sign-off section

### Quick Win Solution (Current):
The current implementation provides:
✅ Basic scheme of work generation
✅ Essential fields captured
✅ Professional formatting
✅ Download functionality

### Full Implementation (Recommended):
Would require:
- 2-3 hours for complete frontend form
- 1 hour for database migration
- 2 hours for comprehensive document generator
- 1 hour for testing

## Recommendation:
Continue with Session Plans (fully working) and enhance Scheme of Work in next phase with dedicated time for comprehensive implementation.
