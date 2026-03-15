from langchain_core.messages import HumanMessage


def generate_ddr(model, inspection_context, thermal_context):

    prompt = f"""
You are a structural inspection expert.

Using the following inspection and thermal data,
generate a professional Detailed Diagnostic Report.

Inspection Data:
{inspection_context}

Thermal Data:
{thermal_context}

Generate the report in the following structure:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

Rules:
- Do NOT invent facts not present in the documents
- If information conflicts → mention the conflict
- If information is missing → write "Not Available"
- Avoid duplicate points
- Use simple client-friendly language
"""

    # Convert prompt to LangChain message format
    message = HumanMessage(content=prompt)

    # Call Gemini model
    response = model.invoke([message])

    # Return generated DDR report
    return response.content