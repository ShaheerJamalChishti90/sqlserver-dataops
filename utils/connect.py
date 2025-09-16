# # import os, logging
# # import pyodbc
# # from dotenv import load_dotenv


# # def create_connection():
# #     """Create a connection to SQL Server using ODBC Driver 17"""
# #     load_dotenv()
    
# #     # Create connection string with ODBC Driver 17
# #     conn_str = (
# #         f"DRIVER={{ODBC Driver 17 for SQL Server}};"
# #         f"SERVER={os.getenv('DB_SERVER')};"
# #         f"DATABASE={os.getenv('DB_NAME')};"
# #         f"UID={os.getenv('DB_USER')};"
# #         f"PWD={os.getenv('DB_PASSWORD')};"
# #         f"Trusted_Connection=no;"
# #     )
    
# #     try:
# #         connection = pyodbc.connect(conn_str)
# #         print(f"Connection has been successfuly established!")
# #         return connection

        
# #     except Exception as e:
# #         print(logging.error(f"Connection error: {e}"))
# #         return None


# import os, logging
# import pyodbc
# from dotenv import load_dotenv

# def create_connection():
#     """Create a connection to SQL Server using ODBC Driver 17"""
#     load_dotenv()
    
#     # Create connection string with ODBC Driver 17
#     conn_str = (
#         "DRIVER={ODBC Driver 17 for SQL Server};"
#         f"SERVER={os.getenv('DB_SERVER')};"
#         f"DATABASE={os.getenv('DB_NAME')};"
#         f"UID={os.getenv('DB_USER')};"
#         f"PWD={os.getenv('DB_PASSWORD')};"
#         # "Trusted_Connection=yes;"
#         )
    
#     try:
#         connection = pyodbc.connect(conn_str)
#         print("✅ Connection has been successfully established!")
#         return connection
#     except Exception as e:
#         print(f"❌ Connection error: {e}")
#         return None


# # 👇 actually call the function
# if __name__ == "__main__":
#     conn = create_connection()

import os
import pyodbc
from dotenv import load_dotenv

def create_connection():
    """Create a connection to SQL Server using ODBC Driver 17"""
    load_dotenv()

    # Create connection string with ODBC Driver 17
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
    )

    try:
        connection = pyodbc.connect(conn_str)
        print("✅ Connection has been successfully established!")

        # 👉 Create a cursor and run a test query
        cursor = connection.cursor()
        
        # Check SQL Server version
        cursor.execute("SELECT @@VERSION;")
        version = cursor.fetchone()[0]
        print("🖥️ SQL Server Version:", version)

        # Check which database you’re connected to
        cursor.execute("SELECT DB_NAME();")
        dbname = cursor.fetchone()[0]
        print("📂 Connected to Database:", dbname)

        return connection

    except Exception as e:
        print(f"❌ Connection error: {e}")
        return None


# 👇 actually call the function
if __name__ == "__main__":
    conn = create_connection()



