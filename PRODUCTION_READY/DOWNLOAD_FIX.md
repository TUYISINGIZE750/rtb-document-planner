# Fix for Session Plan & Scheme of Work Download Issue

## Problem Identified

Downloads are not working properly. The issues are:

1. **Flask version compatibility**: The code uses `download_name` parameter (Flask 2.0+) but older Flask versions use `attachment_filename`
2. **File handling**: Temporary files might not persist long enough for download
3. **MIME type**: Needs explicit setting for proper file recognition
4. **Error handling**: No proper error logging for debugging
5. **File closure**: Files need to be properly closed before sending

## Solution

### Fix 1: Update `main.py` Download Endpoints

Replace both download endpoints (lines 382-418 and 519-587) with corrected versions that:
- Support both old and new Flask versions
- Properly handle file streams
- Include better error handling
- Add proper logging

### Fix 2: Update `document_generator.py`

Ensure temporary files are:
- Properly closed after creation
- Not deleted prematurely
- Accessible to Flask for download

---

## Implementation Steps

### Step 1: Apply Main.py Patch

**Replace lines 382-418 (Session Plan Download):**

```python
@app.route('/session-plans/<int:plan_id>/download', methods=['GET', 'OPTIONS'])
def download_session_plan(plan_id):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        phone = request.args.get('phone')
        if not phone:
            logger.error('Download attempt without phone parameter')
            return jsonify({"detail": "Phone parameter required"}), 400
        
        db = SessionLocal()
        try:
            session_plan = db.query(SessionPlan).filter(SessionPlan.id == plan_id).first()
            if not session_plan:
                logger.error(f'Session plan {plan_id} not found')
                return jsonify({"detail": "Session plan not found"}), 404
            
            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                logger.error(f'User {phone} not found')
                return jsonify({"detail": "User not found"}), 404
            
            # Convert to dict for document generation
            data = {
                'sector': session_plan.sector,
                'sub_sector': session_plan.sub_sector,
                'trade': session_plan.trade,
                'rqf_level': session_plan.rqf_level,
                'module_code_title': session_plan.module_code_title,
                'term': session_plan.term,
                'week': session_plan.week,
                'date': session_plan.date,
                'trainer_name': session_plan.trainer_name,
                'class_name': session_plan.class_name,
                'number_of_trainees': session_plan.number_of_trainees,
                'topic_of_session': session_plan.topic_of_session,
                'duration': session_plan.duration,
                'learning_outcomes': session_plan.learning_outcomes,
                'objectives': session_plan.objectives,
                'indicative_contents': session_plan.indicative_contents,
                'facilitation_techniques': session_plan.facilitation_techniques,
                'learning_activities': session_plan.learning_activities,
                'resources': session_plan.resources,
                'assessment_details': session_plan.assessment_details,
                'references': session_plan.references
            }
            
            # Generate document
            file_path = generate_session_plan_docx(data)
            
            if not file_path or not os.path.exists(file_path):
                logger.error(f'Document generation failed for plan {plan_id}')
                return jsonify({"detail": "Document generation failed"}), 500
            
            filename = f"RTB_Session_Plan_{plan_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
            
            logger.info(f'Sending file: {file_path} as {filename}')
            
            try:
                # Read file into memory to ensure it exists
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                
                # Send file
                return send_file(
                    BytesIO(file_data),
                    mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    as_attachment=True,
                    download_name=filename
                )
            except TypeError:
                # Fallback for older Flask versions that don't support BytesIO with send_file
                return send_file(
                    file_path,
                    mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    as_attachment=True,
                    attachment_filename=filename
                )
        finally:
            db.close()
            # Clean up temp file after sending
            try:
                if file_path and os.path.exists(file_path):
                    os.remove(file_path)
            except:
                pass
    except Exception as e:
        logger.error(f'Download error: {str(e)}')
        return jsonify({"detail": f"Download failed: {str(e)}"}), 500
```

**Replace lines 519-587 (Scheme of Work Download):**

```python
@app.route('/schemes-of-work/<int:scheme_id>/download', methods=['GET', 'OPTIONS'])
def download_scheme_of_work(scheme_id):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        phone = request.args.get('phone')
        if not phone:
            logger.error('Download attempt without phone parameter')
            return jsonify({"detail": "Phone parameter required"}), 400
        
        db = SessionLocal()
        try:
            scheme = db.query(SchemeOfWork).filter(SchemeOfWork.id == scheme_id).first()
            if not scheme:
                logger.error(f'Scheme {scheme_id} not found')
                return jsonify({"detail": "Scheme of work not found"}), 404
            
            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                logger.error(f'User {phone} not found')
                return jsonify({"detail": "User not found"}), 404
            
            # Convert scheme to dict for document generation
            data = {
                'province': scheme.province,
                'district': scheme.district,
                'sector': scheme.sector,
                'school': scheme.school,
                'department_trade': scheme.department_trade,
                'qualification_title': scheme.qualification_title,
                'rqf_level': scheme.rqf_level,
                'module_code_title': scheme.module_code_title,
                'school_year': scheme.school_year,
                'terms': scheme.terms,
                'module_hours': scheme.module_hours,
                'number_of_classes': scheme.number_of_classes,
                'class_name': scheme.class_name,
                'trainer_name': scheme.trainer_name,
                'term1_weeks': scheme.term1_weeks,
                'term1_learning_outcomes': scheme.term1_learning_outcomes,
                'term1_indicative_contents': scheme.term1_indicative_contents,
                'term1_duration': scheme.term1_duration,
                'term1_learning_place': scheme.term1_learning_place,
                'term2_weeks': scheme.term2_weeks,
                'term2_learning_outcomes': scheme.term2_learning_outcomes,
                'term2_indicative_contents': scheme.term2_indicative_contents,
                'term2_duration': scheme.term2_duration,
                'term2_learning_place': scheme.term2_learning_place,
                'term3_weeks': scheme.term3_weeks,
                'term3_learning_outcomes': scheme.term3_learning_outcomes,
                'term3_indicative_contents': scheme.term3_indicative_contents,
                'term3_duration': scheme.term3_duration,
                'term3_learning_place': scheme.term3_learning_place,
                'dos_name': scheme.dos_name,
                'manager_name': scheme.manager_name
            }
            
            # Generate document
            file_path = generate_scheme_of_work_docx(data)
            
            if not file_path or not os.path.exists(file_path):
                logger.error(f'Document generation failed for scheme {scheme_id}')
                return jsonify({"detail": "Document generation failed"}), 500
            
            filename = f"RTB_Scheme_of_Work_{scheme_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
            
            logger.info(f'Sending file: {file_path} as {filename}')
            
            try:
                # Read file into memory to ensure it exists
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                
                # Send file
                return send_file(
                    BytesIO(file_data),
                    mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    as_attachment=True,
                    download_name=filename
                )
            except TypeError:
                # Fallback for older Flask versions
                return send_file(
                    file_path,
                    mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    as_attachment=True,
                    attachment_filename=filename
                )
        finally:
            db.close()
            # Clean up temp file after sending
            try:
                if file_path and os.path.exists(file_path):
                    os.remove(file_path)
            except:
                pass
    except Exception as e:
        logger.error(f'Download error: {str(e)}')
        return jsonify({"detail": f"Download failed: {str(e)}"}), 500
```

### Step 2: Update requirements.txt

Ensure Flask is version 2.0+:

```
flask==3.0.0
flask-cors==4.0.0
python-docx==1.1.0
lxml==4.9.3
sqlalchemy==2.0.23
```

---

## Testing the Fix

### Browser Console Test
1. Open browser developer tools (F12)
2. Go to Console tab
3. Create a session plan
4. Check for any errors

### Network Tab Test
1. Open Network tab (F12 → Network)
2. Create and download a session plan
3. Look for the download request
4. Check response headers for:
   - `Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document`
   - `Content-Disposition: attachment; filename=...`

### Server Logs
1. Check PythonAnywhere error log
2. Look for messages like: "Sending file: /tmp/... as RTB_Session_Plan_..."
3. Should show successful file generation

---

## Key Changes Made

| Issue | Fix |
|-------|-----|
| Flask version compatibility | Added try/except for both `download_name` and `attachment_filename` |
| File not found | Added file existence check before sending |
| Missing MIME type | Explicit MIME type for DOCX files |
| File in use error | Read file into BytesIO before sending |
| No error logging | Added logger.info() and logger.error() calls |
| Temp file cleanup | Added cleanup after sending |

---

## Verification Checklist

After applying the fix:

- [ ] Update main.py with new download endpoints
- [ ] Ensure requirements.txt has Flask 3.0.0
- [ ] Restart PythonAnywhere backend
- [ ] Test session plan download
- [ ] Test scheme of work download
- [ ] Check PythonAnywhere error log (should be clean)
- [ ] Check browser console (F12) for errors
- [ ] Download file in browser
- [ ] Open downloaded DOCX in Word
- [ ] Verify file has all data
- [ ] Verify formatting is correct

---

## Troubleshooting

### If download still doesn't work:

1. **Check error log**:
   - PythonAnywhere → Web tab → Error log
   - Look for Python exceptions

2. **Check network tab**:
   - F12 → Network tab
   - Look for failed requests
   - Check response status (should be 200)

3. **Check file generation**:
   - Ensure rtb_template_filler_exact.py is uploaded
   - Ensure template files exist:
     - rtb_session_plan_template.docx
     - rtb_scheme_template.docx

4. **Check permissions**:
   - Temp directory must be writable
   - PythonAnywhere has /tmp access

---

## Support

If the fix doesn't work:

1. Check the detailed error in PythonAnywhere error log
2. Verify all 5 backend files are uploaded
3. Ensure Flask version is 3.0.0
4. Restart the web app
5. Try again in incognito/private window

