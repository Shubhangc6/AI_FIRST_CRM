import streamlit as st
import pandas as pd

from database import (
    create_tables,
    add_customer,
    get_customers,
    update_customer,
    delete_customer,
    add_interaction,
    get_interactions
)


# -----------------------------
# Initialize Database
# -----------------------------

create_tables()


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI First CRM",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Header
# -----------------------------

st.title("🤖 AI First CRM")
st.write("AI-powered Customer Relationship Management System")


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("CRM Modules")


menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Dashboard",
        "Add Customer",
        "View Customers",
        "Search Customer",
        "Add Interaction",
        "View Interactions",
        "Update Customer",
        "Delete Customer",
        "Analytics"
    ]
)


# Get customers from database

customers = get_customers()



# ==================================================
# Dashboard
# ==================================================

if menu == "Dashboard":

    st.subheader("📊 Dashboard")


    total_customers = len(customers)

    total_interactions = len(
        get_interactions()
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Total Customers",
            total_customers
        )


    with col2:

        st.metric(
            "Total Interactions",
            total_interactions
        )


    st.success(
        "CRM system is running successfully"
    )



# ==================================================
# Add Customer
# ==================================================

elif menu == "Add Customer":

    st.subheader("➕ Add New Customer")


    name = st.text_input(
        "Customer Name"
    )


    email = st.text_input(
        "Email"
    )


    phone = st.text_input(
        "Phone"
    )


    company = st.text_input(
        "Company"
    )


    if st.button("Add Customer"):


        add_customer(
            name,
            email,
            phone,
            company
        )


        st.success(
            "Customer added successfully"
        )



# ==================================================
# View Customers
# ==================================================

elif menu == "View Customers":

    st.subheader("👥 Customer Details")


    customers = get_customers()


    if customers:


        df = pd.DataFrame(
            customers,
            columns=[
                "ID",
                "Name",
                "Email",
                "Phone",
                "Company"
            ]
        )


        st.dataframe(
            df,
            use_container_width=True
        )


    else:

        st.info(
            "No customers found"
        )



# ==================================================
# Search Customer
# ==================================================

elif menu == "Search Customer":

    st.subheader("🔍 Search Customer")


    search = st.text_input(
        "Enter customer name"
    )


    if st.button("Search"):


        customers = get_customers()


        result = []


        for customer in customers:


            if search.lower() in customer[1].lower():

                result.append(customer)



        if result:


            df = pd.DataFrame(
                result,
                columns=[
                    "ID",
                    "Name",
                    "Email",
                    "Phone",
                    "Company"
                ]
            )


            st.dataframe(df)


        else:

            st.warning(
                "Customer not found"
            )



# ==================================================
# Add Interaction
# ==================================================

elif menu == "Add Interaction":

    st.subheader("📞 Add Customer Interaction")


    customers = get_customers()


    if not customers:


        st.warning(
            "Please add customer first"
        )


    else:


        customer_id = st.selectbox(

            "Select Customer",

            [c[0] for c in customers],

            format_func=lambda x:
            next(
                c[1]
                for c in customers
                if c[0] == x
            )

        )


        interaction_type = st.selectbox(

            "Interaction Type",

            [
                "Call",
                "Email",
                "Meeting",
                "Follow Up"
            ]

        )


        notes = st.text_area(
            "Notes"
        )



        if st.button("Save Interaction"):


            add_interaction(

                customer_id,

                interaction_type,

                notes

            )


            st.success(
                "Interaction saved successfully"
            )



# ==================================================
# View Interaction
# ==================================================

elif menu == "View Interactions":

    st.subheader(
        "📋 Customer Interactions"
    )


    interactions = get_interactions()


    if interactions:


        df = pd.DataFrame(

            interactions,

            columns=[

                "Customer",

                "Type",

                "Notes"

            ]

        )


        st.dataframe(
            df,
            use_container_width=True
        )


    else:


        st.info(
            "No interactions available"
        )



# ==================================================
# Update Customer
# ==================================================

elif menu == "Update Customer":


    st.subheader(
        "✏️ Update Customer"
    )


    customers = get_customers()



    if customers:


        customer_id = st.selectbox(

            "Select Customer",

            [c[0] for c in customers],

            format_func=lambda x:
            next(
                c[1]
                for c in customers
                if c[0] == x
            )

        )


        new_name = st.text_input(
            "New Name"
        )


        new_phone = st.text_input(
            "New Phone"
        )



        if st.button("Update Customer"):


            update_customer(

                customer_id,

                new_name,

                new_phone

            )


            st.success(
                "Customer updated successfully"
            )



    else:


        st.info(
            "No customers found"
        )



# ==================================================
# Delete Customer
# ==================================================

elif menu == "Delete Customer":


    st.subheader(
        "🗑️ Delete Customer"
    )


    customers=get_customers()



    if customers:


        customer_id = st.selectbox(

            "Select Customer",

            [c[0] for c in customers],

            format_func=lambda x:
            next(
                c[1]
                for c in customers
                if c[0] == x
            )

        )



        if st.button("Delete Customer"):


            delete_customer(
                customer_id
            )


            st.success(
                "Customer deleted successfully"
            )



    else:


        st.info(
            "No customers available"
        )



# ==================================================
# Analytics
# ==================================================

elif menu == "Analytics":


    st.subheader(
        "📈 CRM Analytics"
    )


    customers = get_customers()


    if customers:


        df = pd.DataFrame(

            customers,

            columns=[

                "ID",
                "Name",
                "Email",
                "Phone",
                "Company"

            ]

        )


        st.bar_chart(
            df["Company"].value_counts()
        )


    else:


        st.info(
            "No data available"
        )