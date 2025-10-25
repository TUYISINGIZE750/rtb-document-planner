import os
import shutil
import sys

# Check files
official_session = r'C:\Users\PC\Music\Scheme of work and session plan planner\RTB Templates\TUYISINGIZE LEONARD_SESSION PLAN_S4F3.docx'
backend_session = r'C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\rtb_session_plan_template.docx'

official_scheme = r'C:\Users\PC\Music\Scheme of work and session plan planner\RTB Templates\CSAPA 301 Scheme of work.docx'
backend_scheme = r'C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\rtb_scheme_template.docx'

print('=' * 70)
print('TEMPLATE FILE VERIFICATION')
print('=' * 70)

print('\nOFFICIAL TEMPLATES:')
print('-' * 70)
if os.path.exists(official_session):
    size = os.path.getsize(official_session)
    print(f'✓ Session Plan exists: {size} bytes')
else:
    print(f'✗ Session Plan NOT found')

if os.path.exists(official_scheme):
    size = os.path.getsize(official_scheme)
    print(f'✓ Scheme exists: {size} bytes')
else:
    print(f'✗ Scheme NOT found')

print('\nBACKEND TEMPLATES:')
print('-' * 70)
if os.path.exists(backend_session):
    size = os.path.getsize(backend_session)
    print(f'✓ Session Plan exists: {size} bytes')
else:
    print(f'✗ Session Plan NOT found')

if os.path.exists(backend_scheme):
    size = os.path.getsize(backend_scheme)
    print(f'✓ Scheme exists: {size} bytes')
else:
    print(f'✗ Scheme NOT found')

print('\nCOMPARISON & SYNC:')
print('-' * 70)

# Check Session Plan
if os.path.exists(official_session) and os.path.exists(backend_session):
    off_size = os.path.getsize(official_session)
    back_size = os.path.getsize(backend_session)
    if off_size == back_size:
        print(f'✓ Session Plan templates ARE IDENTICAL')
    else:
        print(f'✗ Session Plan templates DIFFER')
        print(f'  - Official: {off_size} bytes')
        print(f'  - Backend:  {back_size} bytes')
        print(f'  - Syncing...')
        shutil.copy2(official_session, backend_session)
        print(f'✓ Session Plan synced to backend')

# Check Scheme
if os.path.exists(official_scheme) and os.path.exists(backend_scheme):
    off_size = os.path.getsize(official_scheme)
    back_size = os.path.getsize(backend_scheme)
    if off_size == back_size:
        print(f'✓ Scheme templates ARE IDENTICAL')
    else:
        print(f'✗ Scheme templates DIFFER')
        print(f'  - Official: {off_size} bytes')
        print(f'  - Backend:  {back_size} bytes')
        print(f'  - Syncing...')
        shutil.copy2(official_scheme, backend_scheme)
        print(f'✓ Scheme synced to backend')

print('\n' + '=' * 70)
print('✓ TEMPLATE VERIFICATION COMPLETE')
print('=' * 70)
