"""
This is my al in one llm orignizer for my family.  

It will have users

It will have an input box that will add items to a database. We'll feed those items to an LLM and figure out what to do with them

"""



import sqlite3
from datetime import datetime
import sys



LIFE_DB_FNAME = "life.db"

def get_db_connection():
	connection = sqlite3.connect(LIFE_DB_FNAME)
	return connection

def init_table(connection):
	connection.cursor().execute("""
		CREATE TABLE IF NOT EXISTS all_events(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			datetimestamp TEXT NOT NULL,
			original_details TEXT NOT NULL
			)
		""")
	connection.commit()

def add_to_table(item_to_add, connection):
	full_item = (datetime.now().isoformat(), item_to_add)
	connection.cursor().execute("INSERT INTO all_events (datetimestamp, original_details) VALUES (?,?)", full_item)
	connection.commit()

def print_table(connection):
    rows = connection.cursor().execute(
        "SELECT * FROM all_events"
    ).fetchall()

    for row in rows:
        print(row)	


if __name__ == '__main__':

	if len(sys.argv) == 1:
		print_table(connection)
	else:
		connection = get_db_connection()
		init_table(connection)
		new_data = " ".join(sys.argv[1:])
		add_to_table(new_data, connection)
		connection.close()


"""
# 1. Connect to a database file (or create it if it doesn't exist)
# Use ':memory:' instead of a filename to test entirely in RAM
with sqlite3.connect("company.db") as conn:
    # 2. Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # 3. CREATE: Define a table structure
    cursor.execute(" ""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            salary REAL
        )
    "" ")

    # 4. INSERT (Create): Add data safely using parameters to block SQL injection
    new_employees = [
        ("Alice", "Developer", 85000.0),
        ("Bob", "Designer", 70000.0),
        ("Charlie", "Manager", 95000.0)
    ]
    # executemany lets you insert a list of tuples efficiently
    cursor.executemany(
        "INSERT INTO employees (name, role, salary) VALUES (?, ?, ?)", 
        new_employees
    )
    
    # 5. UPDATE: Modify existing records
    cursor.execute(
        "UPDATE employees SET salary = ? WHERE name = ?", 
        (75000.0, "Bob")
    )

    # 6. DELETE: Remove records
    cursor.execute(
        "DELETE FROM employees WHERE name = ?", 
        ("Charlie",)
    )

    # Note: Changes are automatically saved (committed) when exiting the 'with' block

# 7. READ: Fetching data from the database
with sqlite3.connect("company.db") as conn:
    cursor = conn.cursor()
    
    # Query all remaining employees
    cursor.execute("SELECT id, name, role, salary FROM employees")
    
    # fetchall() grabs all matching rows as a list of tuples
    rows = cursor.fetchall()
    
    print("Employee Records:")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Role: {row[2]} | Salary: ${row[3]:,.2f}")
"""