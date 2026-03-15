from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(text_data):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = []

    for page in text_data:

        texts = splitter.split_text(page["text"])

        for t in texts:

            chunks.append({
                "page": page["page"],
                "content": t
            })

    return chunks