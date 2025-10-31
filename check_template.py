from docx import Document

doc = Document('PRODUCTION_READY/OFFICIALRTBTEMPLATES/SESSION PLAN TEMPLATES.docx')
table = doc.tables[0]

print(f"Total rows: {len(table.rows)}")
print("\nChecking activity rows:")
for i in range(10, 20):
    print(f"\nRow {i} ({len(table.rows[i].cells)} cells):")
    for j, cell in enumerate(table.rows[i].cells[:6]):
        text = cell.text.strip()[:40]
        print(f"  Cell {j}: '{text}'")
