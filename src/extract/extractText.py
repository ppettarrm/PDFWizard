from pathlib import Path
from pdfminer.high_level import extract_text #pdfminer.six


def export_text() -> None:
    print("Insert absolute path to pdf:\n")
    try:
        path_to_pdf = Path(input())
    except:
        print("Invalid path!")
        return

    print("Insert absolute path to folder where you want to save your extracted text:\n")
    try:
        output_path = Path(input())
    except:
        print("Invalid path!")
        return
    text = extract_text(path_to_pdf)

    with open(f"{output_path}/text.txt", "w") as f:
        print(text, file=f)
