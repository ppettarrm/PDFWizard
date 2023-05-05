from PyPDF2 import PdfMerger
from pathlib import Path

def merge_pdf() -> None:

    print("Insert absolute path to folder with pdfs that you want to merge:\n")
    try:
        path_to_pdfs = Path(input())
    except:
        print("Invalid path!")
        return

    pdf_list = list(path_to_pdfs.glob('*.pdf'))

    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    print("Insert absolute path to folder where you want to save your merged pdf:\n")
    try:
        output_path = Path(input())
    except:
        print("Invalid path!")
        return

    try:
        merger.write(f"{output_path}/merged.pdf")
        merger.close()
    except:
        print("Fail!")
        return