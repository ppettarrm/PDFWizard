from extract import extractText, extractImages, extractTables
from merge import mergepdf
from split import split
from translate.translate import translate_pdf

def main() -> None:
    print("Choose option:\n#-----------------------#\n1. MergePDF\n2. ExtractPDF\n3. SplitPDF\n4. TranslatePDF")
    try:
        pdf_operation_type = int(input())
    except:
        print("Invalid input!")
        return

    if pdf_operation_type < 1 or pdf_operation_type > 4:
        print("Unknown operation!")
        return

    match pdf_operation_type:
        case 1:
            mergepdf.merge_pdf()
        case 2:
            print("Choose option:\n#-----------------------#\n1. Text\n2. Images\n3. Tables")
            try:
                extract_type = int(input())
            except:
                print("Invalid input!")
                return

            if extract_type < 1 or extract_type > 3:
                print("Unknown operation!")
                return

            match extract_type:
                case 1:
                    extractText.extract_text()
                case 2:
                    extractImages.extract_images()
                case 3:
                    extractTables.extract_tables()
        case 3:
            split.split_pdf()
        case 4:
            translate_pdf()

    return


if __name__ == "__main__":
    main()