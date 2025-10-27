import shutil
import os

src1 = r"c:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\RTB Templates\RTB Session plan template.docx"
dst1 = r"c:\Users\PC\Music\Scheme of work and session plan planner\backend\rtb_session_plan_template.docx"
src2 = r"c:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\RTB Templates\Scheme of work.docx"
dst2 = r"c:\Users\PC\Music\Scheme of work and session plan planner\backend\rtb_scheme_template.docx"

if os.path.exists(src1):
    shutil.copy(src1, dst1)
    print(f"Copied: {src1}")
else:
    print(f"Not found: {src1}")

if os.path.exists(src2):
    shutil.copy(src2, dst2)
    print(f"Copied: {src2}")
else:
    print(f"Not found: {src2}")

print("Done")
