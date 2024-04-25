import streamlit as st
import pyodbc


connection_string = """
Driver={ODBC Driver 17 for SQL Server};
Server=""" + st.secrets["db_server"] + """;
Database=RiAO.recap;
Uid=""" + st.secrets["db_uid"] + """;
Pwd=""" + st.secrets["db_pwd"] + """;
Encrypt=yes;
TrustServerCertificate=no;
Connection Timeout=30;
"""

# Initialize connection.
# Uses st.cache_resource to only run once.


@st.cache_resource
def init_connection():
    return pyodbc.connect(connection_string)


conn = init_connection()


# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


rows = run_query("SELECT * from riaoQuestionsList;")


# Print results.
for row in rows:
    st.write(row)
