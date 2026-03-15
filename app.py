import streamlit as st

from modules.pdf_loader import load_pdf
from modules.text_processor import split_documents
from modules.rag_pipeline import build_vector_store
from modules.ddr_generator import generate_ddr
from config import configure_gemini


st.title("AI DDR Report Generator")

inspection_file = st.file_uploader("Upload Inspection Report")
thermal_file = st.file_uploader("Upload Thermal Report")


if inspection_file and thermal_file:

    with open("data/uploaded_reports/inspection.pdf", "wb") as f:
        f.write(inspection_file.read())

    with open("data/uploaded_reports/thermal.pdf", "wb") as f:
        f.write(thermal_file.read())

    st.success("Files uploaded successfully")

    if st.button("Generate DDR Report"):

        model = configure_gemini()

        inspection_text = load_pdf("data/uploaded_reports/inspection.pdf")
        thermal_text = load_pdf("data/uploaded_reports/thermal.pdf")

        inspection_chunks = split_documents(inspection_text)
        thermal_chunks = split_documents(thermal_text)

        all_chunks = inspection_chunks + thermal_chunks

        vector_store = build_vector_store(all_chunks)

        inspection_context = " ".join(
            [c["content"] for c in inspection_chunks[:10]]
        )

        thermal_context = " ".join(
            [c["content"] for c in thermal_chunks[:10]]
        )

        report = generate_ddr(
            model,
            inspection_context,
            thermal_context
        )

        st.subheader("Generated DDR Report")

        st.write(report)