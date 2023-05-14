from pathlib import Path
import tabula #tabula-py


def export_tables() -> None:
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

    tables = tabula.read_pdf(path_to_pdf, pages="all")

    df = tables[0]

    with open(f"{output_path}/table.txt", "w") as f:
        print(df, file=f)
