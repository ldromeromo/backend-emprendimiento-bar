from dotenv import load_dotenv
import pyodbc

load_dotenv()

def get_db_connection():
    """Establece y devuelve una conexión a la base de datos."""
    try:
        
        connection_string = (
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=DESKTOP-6RS0ODM\\MSSQLSERVER01;"
            "Database=bar;"
            "Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.InterfaceError as e:
        print(f"Database connection failed: {str(e)}")
        return None
    except pyodbc.Error as e:
        print(f"An error occurred while connecting to the database: {str(e)}")
        return None