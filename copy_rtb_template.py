from docx import Document
import shutil

# Copy the RTB template to use as base
shutil.copy(
    r'RTB Templates\TUYISINGIZE LEONARD_SESSION PLAN_S4F3.docx',
    r'PRODUCTION_READY\backend\rtb_session_plan_template.docx'
)

shutil.copy(
    r'RTB Templates\CSAPA 301 Scheme of work.docx',
    r'PRODUCTION_READY\backend\rtb_scheme_template.docx'
)

print("Templates copied successfully!")
