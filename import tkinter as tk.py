import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Connect to SQLite database
conn = sqlite3.connect('travel_app.db')
cursor = conn.cursor()

# Create tables (if not exist)
cursor.executescript('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS friendship (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_1_id INTEGER,
    user_2_id INTEGER,
    connected_date DATE,
    FOREIGN KEY (user_1_id) REFERENCES user(id),
    FOREIGN KEY (user_2_id) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS destination (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    address TEXT,
    about TEXT,
    longitude REAL,
    latitude REAL
);

CREATE TABLE IF NOT EXISTS schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    destination_id INTEGER,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (destination_id) REFERENCES destination(id)
);
''')
conn.commit()

# Function to create a user
def create_user():
    try:
        cursor.execute("INSERT INTO user (username, email, phone, address, password) VALUES (?, ?, ?, ?, ?)", 
                       (entry_username.get(), entry_email.get(), entry_phone.get(), entry_address.get(), entry_password.get()))
        conn.commit()
        messagebox.showinfo("Success", "User created successfully")
        read_users()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read users
def read_users():
    for row in tree_users.get_children():
        tree_users.delete(row)
    cursor.execute("SELECT * FROM user")
    records = cursor.fetchall()
    for record in records:
        tree_users.insert("", "end", values=record)

# Function to update a user
def update_user():
    try:
        cursor.execute("UPDATE user SET username = ?, email = ?, phone = ?, address = ?, password = ? WHERE id = ?", 
                       (entry_username.get(), entry_email.get(), entry_phone.get(), entry_address.get(), entry_password.get(), entry_id.get()))
        conn.commit()
        messagebox.showinfo("Success", "User updated successfully")
        read_users()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a user
def delete_user():
    try:
        cursor.execute("DELETE FROM user WHERE id = ?", (entry_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "User deleted successfully")
        read_users()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to create a friendship
def create_friendship():
    try:
        cursor.execute("INSERT INTO friendship (user_1_id, user_2_id, connected_date) VALUES (?, ?, ?)", 
                       (entry_user_1_id.get(), entry_user_2_id.get(), entry_connected_date.get()))
        conn.commit()
        messagebox.showinfo("Success", "Friendship created successfully")
        read_friendships()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read friendships
def read_friendships():
    for row in tree_friendships.get_children():
        tree_friendships.delete(row)
    cursor.execute("SELECT * FROM friendship")
    records = cursor.fetchall()
    for record in records:
        tree_friendships.insert("", "end", values=record)

# Function to update a friendship
def update_friendship():
    try:
        cursor.execute("UPDATE friendship SET user_1_id = ?, user_2_id = ?, connected_date = ? WHERE id = ?", 
                       (entry_user_1_id.get(), entry_user_2_id.get(), entry_connected_date.get(), entry_friendship_id.get()))
        conn.commit()
        messagebox.showinfo("Success", "Friendship updated successfully")
        read_friendships()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a friendship
def delete_friendship():
    try:
        cursor.execute("DELETE FROM friendship WHERE id = ?", (entry_friendship_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Friendship deleted successfully")
        read_friendships()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to create a destination
def create_destination():
    try:
        cursor.execute("INSERT INTO destination (name, type, address, about, longitude, latitude) VALUES (?, ?, ?, ?, ?, ?)", 
                       (entry_dest_name.get(), entry_dest_type.get(), entry_dest_address.get(), entry_dest_about.get(), entry_dest_longitude.get(), entry_dest_latitude.get()))
        conn.commit()
        messagebox.showinfo("Success", "Destination created successfully")
        read_destinations()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read destinations
def read_destinations():
    for row in tree_destinations.get_children():
        tree_destinations.delete(row)
    cursor.execute("SELECT * FROM destination")
    records = cursor.fetchall()
    for record in records:
        tree_destinations.insert("", "end", values=record)

# Function to update a destination
def update_destination():
    try:
        cursor.execute("UPDATE destination SET name = ?, type = ?, address = ?, about = ?, longitude = ?, latitude = ? WHERE id = ?", 
                       (entry_dest_name.get(), entry_dest_type.get(), entry_dest_address.get(), entry_dest_about.get(), entry_dest_longitude.get(), entry_dest_latitude.get(), entry_dest_id.get()))
        conn.commit()
        messagebox.showinfo("Success", "Destination updated successfully")
        read_destinations()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a destination
def delete_destination():
    try:
        cursor.execute("DELETE FROM destination WHERE id = ?", (entry_dest_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Destination deleted successfully")
        read_destinations()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to create a schedule
def create_schedule():
    try:
        cursor.execute("INSERT INTO schedule (user_id, destination_id, start_date, end_date) VALUES (?, ?, ?, ?)",
                       (entry_sched_user_id.get(), entry_sched_dest_id.get(), entry_sched_start_date.get(), entry_sched_end_date.get()))
        conn.commit()
        messagebox.showinfo("Success", "Schedule created successfully")
        read_schedules()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read schedules
def read_schedules():
    for row in tree_schedules.get_children():
        tree_schedules.delete(row)
    cursor.execute("SELECT * FROM schedule")
    records = cursor.fetchall()
    for record in records:
        tree_schedules.insert("", "end", values=record)

# Function to update a schedule
def update_schedule():
    try:
        cursor.execute("UPDATE schedule SET user_id = ?, destination_id = ?, start_date = ?, end_date = ? WHERE id = ?",
                       (entry_sched_user_id.get(), entry_sched_dest_id.get(), entry_sched_start_date.get(), entry_sched_end_date.get(), entry_sched_id.get()))
        conn.commit()
        messagebox.showinfo("Success", "Schedule updated successfully")
        read_schedules()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a schedule
def delete_schedule():
    try:
        cursor.execute("DELETE FROM schedule WHERE id = ?", (entry_sched_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Schedule deleted successfully")
        read_schedules()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tkinter GUI setup
root = tk.Tk()
root.title("CRUD App")
root.geometry("1000x800")

# Tab Control
tabControl = ttk.Notebook(root)
tab_user = ttk.Frame(tabControl)
tab_friendship = ttk.Frame(tabControl)
tab_destination = ttk.Frame(tabControl)
tab_schedule = ttk.Frame(tabControl)

tabControl.add(tab_user, text="Users")
tabControl.add(tab_friendship, text="Friendships")
tabControl.add(tab_destination, text="Destinations")
tabControl.add(tab_schedule, text="Schedules")
tabControl.pack(expand=1, fill="both")

# User Tab
user_frame = ttk.Frame(tab_user, padding="10 10 10 10")
user_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

tk.Label(user_frame, text="ID").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(user_frame, text="Username").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(user_frame, text="Email").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(user_frame, text="Phone").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(user_frame, text="Address").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(user_frame, text="Password").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

entry_id = tk.Entry(user_frame)
entry_username = tk.Entry(user_frame)
entry_email = tk.Entry(user_frame)
entry_phone = tk.Entry(user_frame)
entry_address = tk.Entry(user_frame)
entry_password = tk.Entry(user_frame)

entry_id.grid(row=0, column=1, padx=5, pady=5)
entry_username.grid(row=1, column=1, padx=5, pady=5)
entry_email.grid(row=2, column=1, padx=5, pady=5)
entry_phone.grid(row=3, column=1, padx=5, pady=5)
entry_address.grid(row=4, column=1, padx=5, pady=5)
entry_password.grid(row=5, column=1, padx=5, pady=5)

button_frame = ttk.Frame(user_frame, padding="10 10 10 10")
button_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))
tk.Button(button_frame, text="Create", command=create_user).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Read", command=read_users).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Update", command=update_user).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Delete", command=delete_user).grid(row=1, column=1, padx=5, pady=5)

tree_users = ttk.Treeview(user_frame, columns=("ID", "Username", "Email", "Phone", "Address", "Password"), show="headings")
for col in tree_users["columns"]:
    tree_users.heading(col, text=col)
tree_users.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

# Friendship Tab
friendship_frame = ttk.Frame(tab_friendship, padding="10 10 10 10")
friendship_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

tk.Label(friendship_frame, text="ID").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(friendship_frame, text="User 1 ID").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(friendship_frame, text="User 2 ID").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(friendship_frame, text="Connected Date").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

entry_friendship_id = tk.Entry(friendship_frame)
entry_user_1_id = tk.Entry(friendship_frame)
entry_user_2_id = tk.Entry(friendship_frame)
entry_connected_date = tk.Entry(friendship_frame)

entry_friendship_id.grid(row=0, column=1, padx=5, pady=5)
entry_user_1_id.grid(row=1, column=1, padx=5, pady=5)
entry_user_2_id.grid(row=2, column=1, padx=5, pady=5)
entry_connected_date.grid(row=3, column=1, padx=5, pady=5)

button_frame_friendship = ttk.Frame(friendship_frame, padding="10 10 10 10")
button_frame_friendship.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
tk.Button(button_frame_friendship, text="Create", command=create_friendship).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame_friendship, text="Read", command=read_friendships).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame_friendship, text="Update", command=update_friendship).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame_friendship, text="Delete", command=delete_friendship).grid(row=1, column=1, padx=5, pady=5)

tree_friendships = ttk.Treeview(friendship_frame, columns=("ID", "User 1 ID", "User 2 ID", "Connected Date"), show="headings")
for col in tree_friendships["columns"]:
    tree_friendships.heading(col, text=col)
tree_friendships.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

# Destination Tab
destination_frame = ttk.Frame(tab_destination, padding="10 10 10 10")
destination_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

tk.Label(destination_frame, text="ID").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(destination_frame, text="Name").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(destination_frame, text="Type").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(destination_frame, text="Address").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(destination_frame, text="About").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(destination_frame, text="Longitude").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(destination_frame, text="Latitude").grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

entry_dest_id = tk.Entry(destination_frame)
entry_dest_name = tk.Entry(destination_frame)
entry_dest_type = tk.Entry(destination_frame)
entry_dest_address = tk.Entry(destination_frame)
entry_dest_about = tk.Entry(destination_frame)
entry_dest_longitude = tk.Entry(destination_frame)
entry_dest_latitude = tk.Entry(destination_frame)

entry_dest_id.grid(row=0, column=1, padx=5, pady=5)
entry_dest_name.grid(row=1, column=1, padx=5, pady=5)
entry_dest_type.grid(row=2, column=1, padx=5, pady=5)
entry_dest_address.grid(row=3, column=1, padx=5, pady=5)
entry_dest_about.grid(row=4, column=1, padx=5, pady=5)
entry_dest_longitude.grid(row=5, column=1, padx=5, pady=5)
entry_dest_latitude.grid(row=6, column=1, padx=5, pady=5)

button_frame_destination = ttk.Frame(destination_frame, padding="10 10 10 10")
button_frame_destination.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E))
tk.Button(button_frame_destination, text="Create", command=create_destination).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame_destination, text="Read", command=read_destinations).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame_destination, text="Update", command=update_destination).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame_destination, text="Delete", command=delete_destination).grid(row=1, column=1, padx=5, pady=5)

tree_destinations = ttk.Treeview(destination_frame, columns=("ID", "Name", "Type", "Address", "About", "Longitude", "Latitude"), show="headings")
for col in tree_destinations["columns"]:
    tree_destinations.heading(col, text=col)
tree_destinations.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

# Schedule Tab
schedule_frame = ttk.Frame(tab_schedule, padding="10 10 10 10")
schedule_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

tk.Label(schedule_frame, text="ID").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(schedule_frame, text="User ID").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(schedule_frame, text="Destination ID").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(schedule_frame, text="Start Date").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(schedule_frame, text="End Date").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

entry_sched_id = tk.Entry(schedule_frame)
entry_sched_user_id = tk.Entry(schedule_frame)
entry_sched_dest_id = tk.Entry(schedule_frame)
entry_sched_start_date = tk.Entry(schedule_frame)
entry_sched_end_date = tk.Entry(schedule_frame)

entry_sched_id.grid(row=0, column=1, padx=5, pady=5)
entry_sched_user_id.grid(row=1, column=1, padx=5, pady=5)
entry_sched_dest_id.grid(row=2, column=1, padx=5, pady=5)
entry_sched_start_date.grid(row=3, column=1, padx=5, pady=5)
entry_sched_end_date.grid(row=4, column=1, padx=5, pady=5)

button_frame_schedule = ttk.Frame(schedule_frame, padding="10 10 10 10")
button_frame_schedule.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
tk.Button(button_frame_schedule, text="Create", command=create_schedule).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame_schedule, text="Read", command=read_schedules).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame_schedule, text="Update", command=update_schedule).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame_schedule, text="Delete", command=delete_schedule).grid(row=1, column=1, padx=5, pady=5)

tree_schedules = ttk.Treeview(schedule_frame, columns=("ID", "User ID", "Destination ID", "Start Date", "End Date"), show="headings")
for col in tree_schedules["columns"]:
    tree_schedules.heading(col, text=col)
tree_schedules.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

# Run the main loop
root.mainloop()
