"""Analyze the template merge pattern"""
from docx import Document

doc = Document('RTB Templates/Scheme of work.docx')
t1 = doc.tables[1]

print("Analyzing Term 1 table cell merging:")
print(f"Total rows: {len(t1.rows)}\n")

# Track which cells are the same object
cell_map = {}
for row_idx in range(2, len(t1.rows)):
    row = t1.rows[row_idx]
    print(f"Row {row_idx}:")
    for col_idx in range(min(9, len(row.cells))):
        cell = row.cells[col_idx]
        cell_id = id(cell._element)
        
        # Check if we've seen this cell before
        if cell_id in cell_map:
            print(f"  Col {col_idx}: MERGED with {cell_map[cell_id]}")
        else:
            cell_map[cell_id] = f"R{row_idx}C{col_idx}"
            print(f"  Col {col_idx}: Independent (text: '{cell.text.strip()[:20]}')")
