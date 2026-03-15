from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def build_vector_store(chunks):

    texts = [c["content"] for c in chunks]

    # Use BGE embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    vector_store = FAISS.from_texts(
        texts,
        embedding=embeddings
    )

    return vector_store


def retrieve_context(vector_store, query):

    docs = vector_store.similarity_search(query, k=6)

    context = "\n".join([d.page_content for d in docs])

    return context