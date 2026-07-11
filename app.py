import streamlit as st

# Temporary database (replace later with MySQL)
if "customers" not in st.session_state:
    st.session_state.customers = []


st.set_page_config(
    page_title="AI First CRM",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI First CRM")


menu = st.sidebar.selectbox(
    "CRM Menu",
    [
        "Dashboard",
        "Add Customer",
        "View Customers",
        "Update Customer",
        "Delete Customer"
    ]
)


# Dashboard
if menu == "Dashboard":

    st.subheader("📊 Dashboard")

    total = len(st.session_state.customers)

    st.metric(
        "Total Customers",
        total
    )


# Add Customer
elif menu == "Add Customer":

    st.subheader("➕ Add Customer")

    name = st.text_input("Customer Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")


    if st.button("Add Customer"):

        customer = {
            "name": name,
            "email": email,
            "phone": phone
        }

        st.session_state.customers.append(customer)

        st.success("Customer added successfully")


# View Customers
elif menu == "View Customers":

    st.subheader("👥 Customers")

    if len(st.session_state.customers) == 0:

        st.info("No customers available")

    else:

        st.table(
            st.session_state.customers
        )


# Update Customer
elif menu == "Update Customer":

    st.subheader("✏️ Update Customer")


    if len(st.session_state.customers) == 0:

        st.warning("No customers to update")

    else:

        index = st.number_input(
            "Customer Index",
            min_value=0,
            max_value=len(st.session_state.customers)-1
        )

        new_name = st.text_input(
            "New Name"
        )


        if st.button("Update"):

            st.session_state.customers[index]["name"] = new_name

            st.success(
                "Customer updated successfully"
            )


# Delete Customer
elif menu == "Delete Customer":

    st.subheader("🗑️ Delete Customer")


    if len(st.session_state.customers) == 0:

        st.warning("No customers available")

    else:

        index = st.number_input(
            "Customer Index",
            min_value=0,
            max_value=len(st.session_state.customers)-1
        )


        if st.button("Delete"):

            st.session_state.customers.pop(index)

            st.success(
                "Customer deleted successfully"
            )