# import pyodbc
# print(pyodbc.drivers())


import pyodbc

try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=127.0.0.1,1433;"   # force TCP
        "DATABASE=BikeStore;"
        "UID=sa;"
        "PWD=shaheersql;"
    )
    print("✅ Connection successful")
    conn.close()
except Exception as e:
    print("❌ Connection error:", e)
