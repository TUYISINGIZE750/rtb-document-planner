import sys
from docx import Document

# Set UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

doc = Document(r'RTB Templates\TUYISINGIZE LEONARD_SESSION PLAN_S4F3.docx')

print("SESSION PLAN TEMPLATE ANALYSIS")
print("="*80)

for idx, table in enumerate(doc.tables):
    print(f"\nTable {idx+1}: {len(table.rows)} rows x {len(table.columns)} columns")
    
    for row_idx, row in enumerate(table.rows[:10]):  # First 10 rows
        print(f"\nRow {row_idx+1}:")
        for cell_idx, cell in enumerate(row.cells):
            text = cell.text.strip()[:40]
            print(f"  Cell {cell_idx+1}: {text}")
