import sqlite3


DB_NAME = "crm.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        company TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        interaction_type TEXT,
        notes TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(id)
    )
    """)


    conn.commit()
    conn.close()



# -------------------------
# Customer CRUD Operations
# -------------------------


def add_customer(name,email,phone,company):

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute(
        """
        INSERT INTO customers
        (name,email,phone,company)
        VALUES(?,?,?,?)
        """,
        (name,email,phone,company)
    )

    conn.commit()
    conn.close()



def get_customers():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute(
        "SELECT * FROM customers"
    )

    data=cursor.fetchall()

    conn.close()

    return data



def update_customer(id,name,phone):

    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute(
        """
        UPDATE customers
        SET name=?, phone=?
        WHERE id=?
        """,
        (name,phone,id)
    )


    conn.commit()
    conn.close()



def delete_customer(id):

    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute(
        """
        DELETE FROM customers
        WHERE id=?
        """,
        (id,)
    )


    conn.commit()
    conn.close()



# -------------------------
# Interaction
# -------------------------


def add_interaction(customer_id,interaction_type,notes):

    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute(
        """
        INSERT INTO interactions
        (customer_id,interaction_type,notes)
        VALUES(?,?,?)
        """,
        (
            customer_id,
            interaction_type,
            notes
        )
    )


    conn.commit()
    conn.close()



def get_interactions():

    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute(
        """
        SELECT 
        customers.name,
        interactions.interaction_type,
        interactions.notes

        FROM interactions

        JOIN customers
        ON customers.id=interactions.customer_id
        """
    )


    data=cursor.fetchall()

    conn.close()

    return data