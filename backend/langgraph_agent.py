from langgraph.graph import StateGraph
from backend.tools import (
    search_customer,
    add_customer,
    update_customer,
    delete_customer,
    customer_analytics
)


tools = [
    search_customer,
    add_customer,
    update_customer,
    delete_customer,
    customer_analytics
]


def run_agent(query):

    query = query.lower()

    if "search" in query:
        return search_customer(query)

    elif "add" in query:
        return add_customer(query)

    elif "update" in query:
        return update_customer(query)

    elif "delete" in query:
        return delete_customer(query)

    elif "analytics" in query:
        return customer_analytics()

    else:
        return "I can help with customer search, add, update, delete and analytics."
