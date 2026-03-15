from langgraph.graph import StateGraph

class DDRState(dict):
    pass


def extract_state(state):

    state["inspection_context"] = state["vector_db"].similarity_search(
        "inspection issues"
    )

    state["thermal_context"] = state["vector_db"].similarity_search(
        "thermal temperature moisture"
    )

    return state


def generate_report(state):

    report = state["llm"].generate_content(
        state["inspection_context"] + state["thermal_context"]
    )

    state["ddr"] = report.text

    return state


def build_graph():

    workflow = StateGraph(DDRState)

    workflow.add_node("extract", extract_state)

    workflow.add_node("generate", generate_report)

    workflow.set_entry_point("extract")

    workflow.add_edge("extract", "generate")

    return workflow.compile()