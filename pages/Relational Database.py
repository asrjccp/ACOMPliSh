import streamlit as st
from langchain.prompts import PromptTemplate
from PIL import Image
st.set_page_config(
    page_title = "Relational Database",
    page_icon = "💻",
)
from cb_relationaldatabase import answer_relational_database
st.title(':rainbow[Relational Database]')
st.caption("Ask me anything! :)")
# Template
question_template = PromptTemplate(
    input_variables=['topic'],
    template=''' You are a H2 Computing Tutor in Singapore and you are teaching {topic}.
    Your role is to give a summary on {topic} and make sure its only relevant to {topic}'''
)

# Put Buttons together in Columns
col1, col2, col3 = st.columns(3)
# In Column 1
with col1:
    rd_definitions = st.button("Definitions")
with col2:
    rd_syntax = st.button("SQL Syntax CRUD")
with col3:
    rd_python = st.button("SQLite 3")
if rd_definitions:
    st.write("### Definitions")
    st.markdown("**Primary key:** **:red[unique identifier]** for each record in a database table")
    st.markdown("**Foreign key**: column(s) in a database table that provides a **:red[link/relationship]** between data in two tables by referencing the primary key of the source table")
    st.markdown("**1NF (First Normal Form)**: **no** **:red[repeating fields/groups]**")
    st.markdown("**2NF (Second Normal Form)**: **no **:red[partial key]** dependency**.")
    st.markdown("**3NF (Third Normal Form)**: **no **:red[non-key]** dependency**.")
    st.markdown("""
    ### Attributes of a Database

    **Table:** A collection of related data entries and it consists of columns and rows. 

    **Record:** A single, implicitly structured data item in a table.

    **Field:** Also known as a column, a field represents a data type for a single piece of data in a record.

    ### Key Types in Relational Databases

    **Primary Key:** A field (or combination of fields) that uniquely identifies a record in a table.

    **Secondary Key:** A field that is not a primary key but can be used for searching, sorting, and indexing.

    **Composite Key:** A combination of two or more columns used to uniquely identify a record where a single column is not enough.

    **Foreign Key:** A field in a table that links to the primary key of another table to maintain the relational aspect of the database.

    ### Data Redundancy and Data Dependency

    **Data Redundancy:** Occurs when the same piece of data exists in multiple places. This can lead to inconsistencies.

    **Data Dependency:** When data structure changes affect the data retrieval, this shows a dependency that can complicate updates and maintenance.

    **Example:** Suppose we have two tables, 'Orders' and 'Customers'. If customer address data is duplicated across both tables, any change in the address must be updated in multiple places, leading to potential inconsistencies.
    """)

    

    st.markdown("""
    ### Understanding Normal Forms: 1NF and 2NF

    #### First Normal Form (1NF)
    A table is in First Normal Form (1NF) if it contains no repeating groups or arrays. This means:
    - Each column must hold only atomic (indivisible) values.
    - Each column in a table must be unique.
    - The order in which data is stored does not affect the database's integrity.

    **Example:** Suppose we have a student table where the 'Courses' field contains multiple courses separated by commas, this would violate 1NF. To conform to 1NF, each course should have its own record.

    Here’s the non-1NF and 1NF version of a 'Student' table:
    """)

    st.code("""
    Non-1NF Student Table
    -------------------------------------
    ID    | StudentName | Courses
    -------------------------------------
    1     | John Doe    | Math, Science
    2     | Jane Smith  | Literature, Art
    -------------------------------------

    1NF Student Table
    -------------------------------------
    ID    | StudentName | Course
    -------------------------------------
    1     | John Doe    | Math
    1     | John Doe    | Science
    2     | Jane Smith  | Literature
    2     | Jane Smith  | Art
    -------------------------------------
    """)

    st.markdown("""
        #### Second Normal Form (2NF)
        A table is in Second Normal Form (2NF) if:
        - It is in 1NF.
        - All non-key attributes are fully functional dependent on the primary key.

        This means that there should be no partial dependency of any column on the primary key.

        **Example:** If a composite key exists, such as (ID, DepartmentID), then each attribute that is not part of the key must depend on the whole key for its existence, not just part of the key.

        Continuing with our student table, here's how we can ensure it's in 2NF:
        """)

    st.code("""
        Table: Student
        -------------------------------------
        ID    | DepartmentID | StudentName | Course
        -------------------------------------
        1     | 5            | John Doe    | Math
        1     | 5            | John Doe    | Science
        2     | 9            | Jane Smith  | Literature
        2     | 9            | Jane Smith  | Art
        -------------------------------------

        Table: Department
        ----------------------
        DepartmentID | Name
        ----------------------
        5            | Science
        9            | Humanities
        ----------------------
        """)
    st.write('''
    ### Reducing Data Redundancy to 3NF

    **Third Normal Form (3NF):** A table design is in 3NF if it is in Second Normal Form (2NF) and no non-prime attribute is transitively dependent on the primary key.

    **Example:** In a 'Student' table, to be in 3NF, there must not be attributes that are indirectly related to the primary key through another attribute.

    Here’s how to structure 'Student' table:''')
    st.code("""
    Table: Student
    -------------------------------------
    ID    | StudentName | DepartmentID
    -------------------------------------
    1     | John Doe    | 5
    2     | Jane Smith  | 5
    -------------------------------------

    Table: Department
    ----------------------
    DepartmentID | Name
    ----------------------
    5            | Science
    ----------------------
    """)
if rd_syntax:
    st.markdown("""
    ### Introduction to Basic SQL Syntax with SQLite 3

    SQL (Structured Query Language) is a standardized programming language used for managing relational databases and performing various operations on the data within them. SQLite 3 is a lightweight, disk-based database that doesn’t require a separate server process and allows access to the database using a nonstandard variant of the SQL query language. Here are some basic SQL commands:

    #### Creatin    g a Database and Tables
    To start using SQL in SQLite 3, you first need to create a database and then create tables within that database to hold the data.

    **Create Table Syntax:**
    """)
    st.code("""
    CREATE TABLE tablename (
        column1 datatype PRIMARY KEY,
        column2 datatype NOT NULL,
        column3 datatype DEFAULT 'value',
        ...
    );
    """)

    st.markdown("""
    **Example:**
    """)
    st.code("""
    CREATE TABLE Students (
        StudentID int PRIMARY KEY,
        StudentName text NOT NULL,
        Age int,
        Major text
    );
    """)

    st.markdown("""
    #### Inserting Data
    Once your table is created, you can start inserting data into the table.

    **Insert Syntax:**
    """)
    st.code("""
    INSERT INTO tablename (column1, column2, column3, ...)
    VALUES (value1, value2, value3, ...);
    """)

    st.markdown("""
    **Example:**
    """)
    st.code("""
    INSERT INTO Students (StudentID, StudentName, Age, Major)
    VALUES (1, 'John Doe', 20, 'Computer Science');
    """)

    st.markdown("""
    #### Querying Data
    To retrieve data from a database, you use the SELECT statement.

    **Select Syntax:**
    """)
    st.code("""
    SELECT column1, column2, ...
    FROM tablename
    WHERE condition
    ORDER BY column
    LIMIT number;
    """)

    st.markdown("""
    **Example:**
    """)
    st.code("""
    SELECT StudentName, Major FROM Students
    WHERE Age >= 20
    ORDER BY StudentName;
    """)

    st.markdown("""
    #### Updating Data
    To modify data in the database, you use the UPDATE statement.

    **Update Syntax:**
    """)
    st.code("""
    UPDATE tablename
    SET column1 = value1, column2 = value2, ...
    WHERE condition;
    """)

    st.markdown("""
    **Example:**
    """)
    st.code("""
    UPDATE Students
    SET Major = 'Information Technology'
    WHERE StudentID = 1;
    """)

    st.markdown("""
    #### Deleting Data
    To delete data from a table, you use the DELETE statement.

    **Delete Syntax:**
    """)
    st.code("""
    DELETE FROM tablename
    WHERE condition;
    """)

    st.markdown("""
    **Example:**
    """)
    st.code("""
    DELETE FROM Students
    WHERE StudentID = 1;
    """)
if rd_python:
    st.markdown("""
    #### Importing the Module
    First, you need to import the sqlite3 module into your Python script.

    **Example:**
    """)
    st.code("""
    import sqlite3
    """)

    st.markdown("""
    #### Creating a Connection
    To perform tasks on the database, you first need to create a connection to it. This is done using the `connect()` method, which returns a connection object.

    **Example:**
    """)
    st.code("""
    conn = sqlite3.connect('example.db')
    """)

    st.markdown("""
    #### Creating a Cursor Object
    Once a connection is established, you can create a cursor object using the cursor method of the connection object. The cursor is used to execute SQL commands.

    **Example:**
    """)
    st.code("""
    cursor = conn.cursor()
    """)

    st.markdown("""
    #### Executing SQL Commands
    You can execute SQL commands through the cursor object using the `execute()` method.

    **Create a Table Example:**
    """)
    st.code("""
    cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)")
    """)

    st.markdown("""
    **Insert Data Example:**
    """)
    st.code("""
    cursor.execute("INSERT INTO students (name, grade) VALUES ('John Doe', 90)")
    """)

    st.markdown("""
    **Select Data Example:**
    """)
    st.code("""
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    """)

    st.markdown("""
    #### Committing Transactions
    To save changes to the database, you need to commit the transactions. This is done using the `commit()` method of the connection object.

    **Example:**
    """)
    st.code("""
    conn.commit()
    """)

    st.markdown("""
    #### Closing the Connection
    Finally, it’s important to close the connection when you are done with it to free up system resources.

    **Example:**
    """)
    st.code("""
    conn.close()
    """)
    st.markdown("""
    #### Using Parameterized Queries to Insert Data

    To securely insert data into a SQLite database using Python's `sqlite3` module, you can use parameterized queries with placeholders (`?`). This method allows you to pass data values in a tuple or list at the time of executing the command, which helps prevent SQL injection attacks.

    **Example:**
    """)
    st.code("""
    # Example of inserting data using parameterized queries
    cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('Jane Doe', 85))
    """)
    st.markdown("""
    In this example, the `?` placeholders in the SQL command are replaced by the values in the tuple `('Jane Doe', 85)` at the time of execution. This approach ensures that data is handled safely and efficiently.
    """)




    
st.divider()

# Initialise a state to keep track of person response"
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

chat_box = st.chat_input("Enter your question")
if chat_box:
    with st.chat_message("user"):
        st.markdown(chat_box)
    st.session_state.messages.append({"role": "user", "content": chat_box})
    response = answer_relational_database(chat_box)
    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
