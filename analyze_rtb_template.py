from docx import Document
from docx.oxml import parse_xml
from docx.oxml.ns import qn

def analyze_table_structure(doc_path):
    doc = Document(doc_path)
    
    print(f"\n{'='*80}")
    print(f"ANALYZING: {doc_path}")
    print(f"{'='*80}\n")
    
    # Analyze each table
    for table_idx, table in enumerate(doc.tables):
        print(f"\n--- TABLE {table_idx + 1} ---")
        print(f"Rows: {len(table.rows)}, Columns: {len(table.columns)}")
        
        # Analyze each row
        for row_idx, row in enumerate(table.rows):
            print(f"\n  Row {row_idx + 1}:")
            for cell_idx, cell in enumerate(row.cells):
                # Get cell properties
                tc = cell._element
                tcPr = tc.tcPr
                
                # Check for merged cells
                vMerge = None
                gridSpan = None
                
                if tcPr is not None:
                    vMerge_elem = tcPr.find(qn('w:vMerge'))
                    gridSpan_elem = tcPr.find(qn('w:gridSpan'))
                    
                    if vMerge_elem is not None:
                        vMerge = vMerge_elem.get(qn('w:val'), 'continue')
                    if gridSpan_elem is not None:
                        gridSpan = gridSpan_elem.get(qn('w:val'))
                
                cell_text = cell.text.strip()[:50]  # First 50 chars
                
                print(f"    Cell {cell_idx + 1}: '{cell_text}'")
                if gridSpan:
                    print(f"      colspan: {gridSpan}")
                if vMerge:
                    print(f"      rowspan: {vMerge}")
                
                # Check cell borders and shading
                if tcPr is not None:
                    shd = tcPr.find(qn('w:shd'))
                    if shd is not None:
                        fill = shd.get(qn('w:fill'))
                        print(f"      background: {fill}")

# Analyze both templates
analyze_table_structure(r'RTB Templates\TUYISINGIZE LEONARD_SESSION PLAN_S4F3.docx')
analyze_table_structure(r'RTB Templates\CSAPA 301 Scheme of work.docx')
