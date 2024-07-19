import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Function to initialize the database
def init_db():
    try:
        conn = sqlite3.connect('educode.db')
        with open('Educode.sql', 'r') as f:
            sql = f.read()
        conn.executescript(sql)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to initialize database: {str(e)}")

# Function to add a record to a specified table
def add_record(table, values):
    try:
        conn = sqlite3.connect('educode.db')
        cursor = conn.cursor()
        placeholders = ', '.join(['?'] * len(values))
        cursor.execute(f"INSERT INTO {table} VALUES ({placeholders})", values)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Record added to {table} successfully")
        clear_entries()
        read_records(table)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add record to {table}: {str(e)}")

# Function to read records from a specified table
def read_records(table):
    try:
        conn = sqlite3.connect('educode.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        conn.close()

        # Clear existing rows in Treeview
        for row in tree.get_children():
            tree.delete(row)

        # Insert new rows into Treeview
        for row in rows:
            tree.insert("", tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read records from {table}: {str(e)}")

# Function to update a record in a specified table
def update_record(table, id_column, id_value, values):
    try:
        conn = sqlite3.connect('educode.db')
        cursor = conn.cursor()
        columns = ', '.join([f"{col}=?" for col in values.keys()])
        cursor.execute(f"UPDATE {table} SET {columns} WHERE {id_column}=?", (*values.values(), id_value))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Record in {table} updated successfully")
        clear_entries()
        read_records(table)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update record in {table}: {str(e)}")

# Function to delete a record from a specified table
def delete_record(table, id_column, id_value):
    try:
        conn = sqlite3.connect('educode.db')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE {id_column}=?", (id_value,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Record from {table} deleted successfully")
        clear_entries()
        read_records(table)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete record from {table}: {str(e)}")

# Function to clear entry fields
def clear_entries():
    for entry in entries.values():
        entry.delete(0, tk.END)

# Initialize the database
init_db()

# Create the main application window
root = tk.Tk()
root.title("Educational Database")

# Dictionary to hold entry widgets for dynamic form creation
entries = {}

# Function to create form dynamically based on selected table
def create_form(table):
    global entries
    entries = {}
    fields = {
        'Subscription': ['SubscriptionID', 'Plans', 'ExpiryDate'],
        'Payment': ['PaymentID', 'PaymentMethod', 'Amount', 'Verification'],
        'Member': ['MemberID', 'Name', 'MembershipDate', 'SubscriptionID'],
        'Courses': ['CourseID', 'CourseName', 'CourseVideo', 'CourseLesson', 'MemberID'],
        'Tutors': ['TutorID', 'Name', 'Occupation', 'ClassType'],
        'Classes': ['ClassID', 'ClassType', 'TutorsName'],
        'Classes_Tutors': ['ClassID', 'TutorID']
    }

    for widget in form_frame.winfo_children():
        widget.destroy()

    for idx, field in enumerate(fields[table]):
        tk.Label(form_frame, text=field).grid(row=idx, column=0)
        entry = tk.Entry(form_frame)
        entry.grid(row=idx, column=1)
        entries[field] = entry

    btn_add.config(command=lambda: add_record(table, [entry.get() for entry in entries.values()]))
    btn_read.config(command=lambda: read_records(table))
    btn_update.config(command=lambda: update_record(table, fields[table][0], entries[fields[table][0]].get(), {k: v.get() for k, v in entries.items() if k != fields[table][0]}))
    btn_delete.config(command=lambda: delete_record(table, fields[table][0], entries[fields[table][0]].get()))
    
    # Update Treeview columns
    tree["columns"] = fields[table]
    for field in fields[table]:
        tree.heading(field, text=field)
        tree.column(field, width=100)

    # Read and display the initial records
    read_records(table)

# Create and place the widgets
tk.Label(root, text="Select Table").grid(row=0, column=0)
table_var = tk.StringVar(value='Subscription')
tables = ['Subscription', 'Payment', 'Member', 'Courses', 'Tutors', 'Classes', 'Classes_Tutors']
table_menu = tk.OptionMenu(root, table_var, *tables, command=create_form)
table_menu.grid(row=0, column=1)

form_frame = tk.Frame(root)
form_frame.grid(row=1, column=0, columnspan=2)

btn_add = tk.Button(root, text="Add Record")
btn_add.grid(row=2, column=0)

btn_read = tk.Button(root, text="Read Records")
btn_read.grid(row=2, column=1)

btn_update = tk.Button(root, text="Update Record")
btn_update.grid(row=3, column=0)

btn_delete = tk.Button(root, text="Delete Record")
btn_delete.grid(row=3, column=1)

# Create a Treeview widget to display records
tree = ttk.Treeview(root, columns=(), show='headings')
tree.grid(row=4, column=0, columnspan=2)

# Initialize the form with the default table
create_form('Subscription')

# Start the main loop
root.mainloop()