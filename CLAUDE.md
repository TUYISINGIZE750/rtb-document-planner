# RTB Document Planner - Development Notes

## Build & Run Commands

### Backend
```bash
# Install dependencies
cd backend
pip install -r requirements.txt

# Initialize database
python init_db.py

# Run development server
python startup.py
# OR
python PRODUCTION_READY/backend/main.py
```

### Frontend
```bash
cd frontend
python -m http.server 5173
```

### Full Stack (Windows)
```bash
start_all.bat
```

---

## Recent Changes & Features

### 1. Admin Panel Modernization (October 25, 2025)

**Files Modified**:
- `login.html` - Updated redirect from `admin.html` to `admin-final.html`
- `admin-final.html` - Enhanced with modern design and complete features
- `PRODUCTION_READY/backend/main.py` - Added notification endpoints

**Features Added**:
- ✅ Real-time admin dashboard with user statistics
- ✅ Broadcast notifications to user groups
- ✅ Personal messaging system for individual teachers
- ✅ User activation/deactivation controls
- ✅ Premium subscription grant/revoke functionality
- ✅ CSV export of user data
- ✅ Advanced filtering and search

### 2. Teacher Dashboard Notifications (October 25, 2025)

**Files Modified**:
- `teacher-dashboard.html` - Added notification panel with real-time updates

**Features Added**:
- ✅ Notification panel displaying admin messages
- ✅ Unread notification badge
- ✅ Color-coded notifications (info/success/warning/alert)
- ✅ Timestamp for each notification
- ✅ Dismiss individual notifications
- ✅ Auto-refresh every 30 seconds

### 3. Backend Notification System

**Files Modified**:
- `PRODUCTION_READY/backend/main.py` - New endpoints

**New API Endpoints**:
- `GET /users/{phone}/notifications` - Get teacher notifications
- `POST /notifications/broadcast` - Send broadcast notification
- `POST /notifications/send` - Send personal message
- `PUT /users/{phone}/status` - Toggle teacher activation
- `PUT /users/{phone}/premium` - Grant/revoke premium
- `PUT /users/{phone}` - Update teacher details

### 4. Document Formatting & References Enhancement (October 25, 2025)

**Files Modified**:
- `PRODUCTION_READY/backend/rtb_template_filler_exact.py` - Enhanced with professional formatting
- Created: `DOCUMENT_FORMATTING_IMPROVEMENTS.md` - Complete documentation

**Formatting Improvements**:
- ✅ **Font**: Book Antiqua applied consistently throughout documents
- ✅ **Size**: 12pt for all body text
- ✅ **Spacing**: 1.5 line spacing for optimal readability
- ✅ **Structure**: Introduction/Development sections properly separated with trainer/learner activities
- ✅ **Table Layout**: Proper centering, margins (1.27cm), no text overflow
- ✅ **Bibliography**: Smart APA-formatted reference generation based on content

**Smart Reference Generation**:
- Automatically detects subject matter (Programming, Database, Networking, Web, Business, TVET)
- Generates 4-5 relevant, APA-formatted references
- Includes author(s), year, title, publisher information
- Fallback to general TVET references if topic unrecognized

**Facilitation Technique Support**:
- Trainer-guided instruction
- Simulation/Role-play
- Group work/Collaborative learning
- Hands-on/Practical exercises
- Discussion/Brainstorming
- Project-based learning

**Each facilitation technique automatically generates**:
- Subject-appropriate Introduction activities (trainer/learner separated)
- Technique-specific Development activities
- Matching Assessment methods
- Relevant Resource lists

**APA Format References**:
- All references in proper APA 7 format
- Subject-specific curated reference lists
- Includes publication URLs where applicable

---

## Document Generation Verification

### Templates Verified
- ✅ `rtb_session_plan_template.docx` - 23 rows × 6 columns table
- ✅ `rtb_scheme_template.docx` - 3 tables with full data mapping

### Filler Code
- Location: `PRODUCTION_READY/backend/rtb_template_filler_exact.py`
- Status: ✅ Correctly maps user input to template cells
- Cell Mapping: Uses preserve_cell_format() to maintain RTB formatting

### Document Generation Pipeline
1. User creates session plan/scheme via wizard
2. Form data sent to `/upload-session-plan` or `/upload-scheme`
3. Backend calls `generate_session_plan_docx()` or `generate_scheme_of_work_docx()`
4. Template filler preserves exact RTB formatting
5. Document returned with original RTB structure intact
6. Teacher downloads DOCX file matching official RTB template 100%

---

## Database Schema

### Key Tables
```sql
-- Users
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    phone VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(255),
    email VARCHAR(255),
    institution VARCHAR(255),
    password VARCHAR(255),
    role VARCHAR(50) DEFAULT 'user',
    is_premium BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    session_plans_limit INTEGER DEFAULT 2,
    schemes_limit INTEGER DEFAULT 2,
    session_plans_downloaded INTEGER DEFAULT 0,
    schemes_downloaded INTEGER DEFAULT 0,
    created_at DATETIME
);

-- Notifications
CREATE TABLE notifications (
    id INTEGER PRIMARY KEY,
    user_id INTEGER FOREIGN KEY,
    title VARCHAR(255),
    message TEXT,
    type VARCHAR(50) DEFAULT 'info',
    is_read BOOLEAN DEFAULT FALSE,
    created_at DATETIME
);

-- Session Plans
CREATE TABLE session_plans (
    id INTEGER PRIMARY KEY,
    user_phone VARCHAR(50),
    sector VARCHAR(255),
    trade VARCHAR(255),
    trainer_name VARCHAR(255),
    module_code_title VARCHAR(500),
    topic_of_session VARCHAR(500),
    duration VARCHAR(100),
    learning_outcomes TEXT,
    objectives TEXT,
    facilitation_techniques TEXT,
    learning_activities TEXT,
    resources TEXT,
    assessment_details TEXT,
    created_at DATETIME
);

-- Schemes of Work
CREATE TABLE schemes_of_work (
    id INTEGER PRIMARY KEY,
    user_phone VARCHAR(50),
    sector VARCHAR(255),
    trade VARCHAR(255),
    trainer_name VARCHAR(255),
    module_code_title VARCHAR(500),
    term1_weeks TEXT,
    term1_learning_outcomes TEXT,
    term1_indicative_contents TEXT,
    term1_duration TEXT,
    term2_weeks TEXT,
    term2_learning_outcomes TEXT,
    term2_indicative_contents TEXT,
    term2_duration TEXT,
    term3_weeks TEXT,
    term3_learning_outcomes TEXT,
    term3_indicative_contents TEXT,
    term3_duration TEXT,
    created_at DATETIME
);
```

---

## Testing Notifications

### Send Broadcast Notification
```javascript
// Via admin panel:
POST /notifications/broadcast
{
    "target": "all|premium|free|inactive",
    "message": "Your message here",
    "title": "Notification Title",
    "type": "info|success|warning|alert"
}
```

### Send Personal Message
```javascript
// Via admin panel to specific teacher:
POST /notifications/send
{
    "recipient": "+250789123456",
    "message": "Your personal message",
    "title": "Personal Message",
    "type": "personal"
}
```

### Retrieve Notifications
```javascript
// Automatic on teacher dashboard:
GET /users/+250789123456/notifications
```

---

## Deployment Checklist

- [ ] Copy `PRODUCTION_READY/backend/main.py` to PythonAnywhere
- [ ] Copy RTB template files to PythonAnywhere:
  - `rtb_session_plan_template.docx`
  - `rtb_scheme_template.docx`
- [ ] Copy notification endpoint code
- [ ] Test document generation with real data
- [ ] Test admin-to-teacher notification flow
- [ ] Verify only targeted teachers see notifications
- [ ] Test premium grant/revoke functionality
- [ ] Monitor for any errors in logs

---

## Configuration Files

### Frontend Config
- `frontend/config.js` - API base URL (defaults to localhost:8000)
- `frontend/auth.js` - Authentication helper functions

### Backend Config
- `backend/main.py` - Flask app with CORS settings
- `database.py` - Database connection string
- `.env` - Environment variables (if using)

---

## Troubleshooting

### Notifications Not Showing
1. Check notification endpoint is running: `GET /users/{phone}/notifications`
2. Verify teacher phone is in URL correctly (URL encoded if needed)
3. Check browser console for JavaScript errors
4. Verify database has notification records

### Admin to Teacher Communication Not Working
1. Ensure backend endpoints return 200 status
2. Check notification records created in DB
3. Verify user_phone matches in session table
4. Check CORS settings if cross-origin errors

### Documents Not Matching Template
1. Verify template files in backend directory
2. Check rtb_template_filler_exact.py row indices match template
3. Test with verify_template_match.py script
4. Compare generated document with official RTB template

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `login.html` | Login form with admin redirect |
| `admin-final.html` | Admin control panel |
| `teacher-dashboard.html` | Teacher dashboard with notifications |
| `PRODUCTION_READY/backend/main.py` | FastAPI backend with all endpoints |
| `PRODUCTION_READY/backend/rtb_template_filler_exact.py` | Document template filler |
| `rtb_session_plan_template.docx` | Official RTB session plan template |
| `rtb_scheme_template.docx` | Official RTB scheme of work template |

---

**Last Updated**: October 25, 2025  
**Version**: 2.1  
**Status**: Production Ready
