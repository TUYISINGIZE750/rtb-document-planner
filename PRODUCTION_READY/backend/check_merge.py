"""Check if cells are merged"""
from docx import Document

doc = Document('RTB Templates/Scheme of work.docx')
t1 = doc.tables[1]

print('Checking cell merging in Term 1 table:')
for i in range(2, 6):
    cell1 = t1.rows[i].cells[1]
    print(f'Row {i}, Cell 1:')
    print(f'  Text: "{cell1.text}"')
    print(f'  ID: {id(cell1._element)}')
    
    # Check if this cell is the same object as cells in other rows
    if i > 2:
        prev_cell = t1.rows[i-1].cells[1]
        print(f'  Same as previous row? {id(cell1._element) == id(prev_cell._element)}')
