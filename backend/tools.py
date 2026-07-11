customers = []


def search_customer(query):

    return {
        "customers": customers
    }


def add_customer(query):

    customers.append(query)

    return "Customer added successfully"


def update_customer(query):

    return "Customer updated successfully"


def delete_customer(query):

    return "Customer deleted successfully"


def customer_analytics():

    return {
        "Total Customers": len(customers)
    }
