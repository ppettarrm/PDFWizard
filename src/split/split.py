from PyPDF2 import PdfReader, PdfWriter


def split_pdf() -> None:
    from_path = ""
    split_pages = []
    with open(from_path, "rb") as f:
        pdf_reader = PdfReader(f)
        pdf_writer = PdfWriter()
        rest_writer = PdfWriter()

        for page in range(len(pdf_reader.pages)):
            if page in split_pages:
                pdf_writer.add_page(pdf_reader.pages[page])
            else:
                rest_writer.add_page(pdf_reader.pages[page])

    # FIX THIS
        with open("./splitPDFs/selected.pdf", "wb") as f2:
            pdf_writer.write(f2)

        with open("./splitPDFs/rest.pdf", "wb") as f2:
            rest_writer.write(f2)
