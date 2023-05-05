from pdfminer.high_level import extract_text


def export_text() -> None:
    from_pdf = ""
    output_path = ""
    text = extract_text(from_pdf)

    with open(f"{output_path}/text.txt", "w") as f:
        print(text, file=f)
