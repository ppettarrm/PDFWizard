import tabula


def export_tables() -> None:
    from_pdf = ""
    output_path = ""

    tables = tabula.read_pdf(from_pdf, pages="all")

    df = tables[0]

    with open(f"{output_path}/table.txt", "w") as f:
        print(df, file=f)
