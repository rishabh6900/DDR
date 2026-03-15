import fitz

def load_pdf(file_path):

    document = fitz.open(file_path)

    text_data = []

    for page_num in range(len(document)):

        page = document.load_page(page_num)

        text = page.get_text()

        text_data.append({
            "page": page_num,
            "text": text
        })

    return text_data