from pathlib import Path
import PIL.Image #pillow
import fitz #PyMuPDF
import io


def export_images() -> None:
    print("Insert absolute path to pdf:\n")
    try:
        path_to_pdf = Path(input())
    except:
        print("Invalid path!")
        return

    print("Insert absolute path to folder where you want to save your extracted images:\n")
    try:
        output_path = Path(input())
    except:
        print("Invalid path!")
        return

    pdf = fitz.open(path_to_pdf)
    count = 1
    for i in range(len(pdf)):
        page = pdf[i]
        images = page.get_images()
        for image in images:
            base_img = pdf.extract_image(image[0])
            image_data = base_img["image"]
            img = PIL.Image.open(io.BytesIO(image_data))
            extension = base_img["ext"]
            img.save(open(f"{output_path}/image{count}.{extension}", "wb"))
            count += 1
