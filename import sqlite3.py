import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Connect to SQLite database
conn = sqlite3.connect('educode.db')
cursor = conn.cursor()

# Create tables (if not exist)
cursor.executescript('''
CREATE TABLE IF NOT EXISTS Subscription (
    SubscriptionID INTEGER PRIMARY KEY,
    Plans VARCHAR(100),
    ExpiryDate DATE
);

CREATE TABLE IF NOT EXISTS Payment (
    PaymentID INTEGER PRIMARY KEY,
    PaymentMethod VARCHAR(50),
    Amount DECIMAL(10, 2),
    Verification VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Member (
    MemberID INTEGER PRIMARY KEY,
    Name VARCHAR(100),
    MembershipDate DATE,
    SubscriptionID INTEGER,
    FOREIGN KEY (SubscriptionID) REFERENCES Subscription(SubscriptionID)
);

CREATE TABLE IF NOT EXISTS Courses (
    CourseID INTEGER PRIMARY KEY,
    CourseName VARCHAR(100),
    CourseVideo VARCHAR(100),
    CourseLesson VARCHAR(100),
    MemberID INTEGER,
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
);

CREATE TABLE IF NOT EXISTS Tutors (
    TutorID INTEGER PRIMARY KEY,
    Name VARCHAR(100),
    Occupation VARCHAR(100),
    ClassType VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Classes (
    ClassID INTEGER PRIMARY KEY,
    ClassType VARCHAR(100),
    TutorsName VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Classes_Tutors (
    ClassID INTEGER,
    TutorID INTEGER,
    PRIMARY KEY (ClassID, TutorID),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    FOREIGN KEY (TutorID) REFERENCES Tutors(TutorID)
);
''')
conn.commit()

# Function to create a subscription
def create_subscription():
    try:
        cursor.execute("INSERT INTO Subscription (SubscriptionID, Plans, ExpiryDate) VALUES (?, ?, ?)", 
                       (entry_subscription_id.get(), entry_plans.get(), entry_expiry_date.get()))
        conn.commit()
        messagebox.showinfo("Success", "Subscription created successfully")
        read_subscriptions()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read subscriptions
def read_subscriptions():
    for row in tree_subscriptions.get_children():
        tree_subscriptions.delete(row)
    cursor.execute("SELECT * FROM Subscription")
    records = cursor.fetchall()
    for record in records:
        tree_subscriptions.insert("", "end", values=record)

# Function to update a subscription
def update_subscription():
    try:
        cursor.execute("UPDATE Subscription SET Plans = ?, ExpiryDate = ? WHERE SubscriptionID = ?", 
                       (entry_plans.get(), entry_expiry_date.get(), entry_subscription_id.get()))
        conn.commit()
        messagebox.showinfo("Success", "Subscription updated successfully")
        read_subscriptions()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a subscription
def delete_subscription():
    try:
        cursor.execute("DELETE FROM Subscription WHERE SubscriptionID = ?", (entry_subscription_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Subscription deleted successfully")
        read_subscriptions()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to create a payment
def create_payment():
    try:
        cursor.execute("INSERT INTO Payment (PaymentID, PaymentMethod, Amount, Verification) VALUES (?, ?, ?, ?)", 
                       (entry_payment_id.get(), entry_payment_method.get(), entry_amount.get(), entry_verification.get()))
        conn.commit()
        messagebox.showinfo("Success", "Payment created successfully")
        read_payments()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read payments
def read_payments():
    for row in tree_payments.get_children():
        tree_payments.delete(row)
    cursor.execute("SELECT * FROM Payment")
    records = cursor.fetchall()
    for record in records:
        tree_payments.insert("", "end", values=record)

# Function to update a payment
def update_payment():
    try:
        cursor.execute("UPDATE Payment SET PaymentMethod = ?, Amount = ?, Verification = ? WHERE PaymentID = ?", 
                       (entry_payment_method.get(), entry_amount.get(), entry_verification.get(), entry_payment_id.get()))
        conn.commit()
        messagebox.showinfo("Success", "Payment updated successfully")
        read_payments()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a payment
def delete_payment():
    try:
        cursor.execute("DELETE FROM Payment WHERE PaymentID = ?", (entry_payment_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Payment deleted successfully")
        read_payments()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to create a member
def create_member():
    try:
        cursor.execute("INSERT INTO Member (MemberID, Name, MembershipDate, SubscriptionID) VALUES (?, ?, ?, ?)", 
                       (entry_member_id.get(), entry_member_name.get(), entry_membership_date.get(), entry_subscription_id_member.get()))
        conn.commit()
        messagebox.showinfo("Success", "Member created successfully")
        read_members()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read members
def read_members():
    for row in tree_members.get_children():
        tree_members.delete(row)
    cursor.execute("SELECT * FROM Member")
    records = cursor.fetchall()
    for record in records:
        tree_members.insert("", "end", values=record)

# Function to update a member
def update_member():
    try:
        cursor.execute("UPDATE Member SET Name = ?, MembershipDate = ?, SubscriptionID = ? WHERE MemberID = ?", 
                       (entry_member_name.get(), entry_membership_date.get(), entry_subscription_id_member.get(), entry_member_id.get()))
        conn.commit()
        messagebox.showinfo("Success", "Member updated successfully")
        read_members()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a member
def delete_member():
    try:
        cursor.execute("DELETE FROM Member WHERE MemberID = ?", (entry_member_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Member deleted successfully")
        read_members()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to create a course
def create_course():
    try:
        cursor.execute("INSERT INTO Courses (CourseID, CourseName, CourseVideo, CourseLesson, MemberID) VALUES (?, ?, ?, ?, ?)", 
                       (entry_course_id.get(), entry_course_name.get(), entry_course_video.get(), entry_course_lesson.get(), entry_member_id_course.get()))
        conn.commit()
        messagebox.showinfo("Success", "Course created successfully")
        read_courses()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read courses
def read_courses():
    for row in tree_courses.get_children():
        tree_courses.delete(row)
    cursor.execute("SELECT * FROM Courses")
    records = cursor.fetchall()
    for record in records:
        tree_courses.insert("", "end", values=record)

# Function to update a course
def update_course():
    try:
        cursor.execute("UPDATE Courses SET CourseName = ?, CourseVideo = ?, CourseLesson = ?, MemberID = ? WHERE CourseID = ?", 
                       (entry_course_name.get(), entry_course_video.get(), entry_course_lesson.get(), entry_member_id_course.get(), entry_course_id.get()))
        conn.commit()
        messagebox.showinfo("Success", "Course updated successfully")
        read_courses()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a course
def delete_course():
    try:
        cursor.execute("DELETE FROM Courses WHERE CourseID = ?", (entry_course_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Course deleted successfully")
        read_courses()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to create a tutor
def create_tutor():
    try:
        cursor.execute("INSERT INTO Tutors (TutorID, Name, Occupation, ClassType) VALUES (?, ?, ?, ?)", 
                       (entry_tutor_id.get(), entry_tutor_name.get(), entry_occupation.get(), entry_class_type.get()))
        conn.commit()
        messagebox.showinfo("Success", "Tutor created successfully")
        read_tutors()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read tutors
def read_tutors():
    for row in tree_tutors.get_children():
        tree_tutors.delete(row)
    cursor.execute("SELECT * FROM Tutors")
    records = cursor.fetchall()
    for record in records:
        tree_tutors.insert("", "end", values=record)

# Function to update a tutor
def update_tutor():
    try:
        cursor.execute("UPDATE Tutors SET Name = ?, Occupation = ?, ClassType = ? WHERE TutorID = ?", 
                       (entry_tutor_name.get(), entry_occupation.get(), entry_class_type.get(), entry_tutor_id.get()))
        conn.commit()
        messagebox.showinfo("Success", "Tutor updated successfully")
        read_tutors()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a tutor
def delete_tutor():
    try:
        cursor.execute("DELETE FROM Tutors WHERE TutorID = ?", (entry_tutor_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Tutor deleted successfully")
        read_tutors()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to create a class
def create_class():
    try:
        cursor.execute("INSERT INTO Classes (ClassID, ClassType, TutorsName) VALUES (?, ?, ?)", 
                       (entry_class_id.get(), entry_class_type_class.get(), entry_tutors_name.get()))
        conn.commit()
        messagebox.showinfo("Success", "Class created successfully")
        read_classes()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read classes
def read_classes():
    for row in tree_classes.get_children():
        tree_classes.delete(row)
    cursor.execute("SELECT * FROM Classes")
    records = cursor.fetchall()
    for record in records:
        tree_classes.insert("", "end", values=record)

# Function to update a class
def update_class():
    try:
        cursor.execute("UPDATE Classes SET ClassType = ?, TutorsName = ? WHERE ClassID = ?", 
                       (entry_class_type_class.get(), entry_tutors_name.get(), entry_class_id.get()))
        conn.commit()
        messagebox.showinfo("Success", "Class updated successfully")
        read_classes()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a class
def delete_class():
    try:
        cursor.execute("DELETE FROM Classes WHERE ClassID = ?", (entry_class_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Class deleted successfully")
        read_classes()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to create a class-tutor relationship
def create_class_tutor():
    try:
        cursor.execute("INSERT INTO Classes_Tutors (ClassID, TutorID) VALUES (?, ?)", 
                       (entry_class_id_ct.get(), entry_tutor_id_ct.get()))
        conn.commit()
        messagebox.showinfo("Success", "Class-Tutor relationship created successfully")
        read_classes_tutors()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read class-tutor relationships
def read_classes_tutors():
    for row in tree_classes_tutors.get_children():
        tree_classes_tutors.delete(row)
    cursor.execute("SELECT * FROM Classes_Tutors")
    records = cursor.fetchall()
    for record in records:
        tree_classes_tutors.insert("", "end", values=record)

# Function to update a class-tutor relationship
def update_class_tutor():
    try:
        cursor.execute("UPDATE Classes_Tutors SET TutorID = ? WHERE ClassID = ?", 
                       (entry_tutor_id_ct.get(), entry_class_id_ct.get()))
        conn.commit()
        messagebox.showinfo("Success", "Class-Tutor relationship updated successfully")
        read_classes_tutors()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a class-tutor relationship
def delete_class_tutor():
    try:
        cursor.execute("DELETE FROM Classes_Tutors WHERE ClassID = ? AND TutorID = ?", 
                       (entry_class_id_ct.get(), entry_tutor_id_ct.get()))
        conn.commit()
        messagebox.showinfo("Success", "Class-Tutor relationship deleted successfully")
        read_classes_tutors()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tkinter GUI setup
root = tk.Tk()
root.title("Educode App")
root.geometry("1000x800")

# Tab Control
tabControl = ttk.Notebook(root)
tab_subscription = ttk.Frame(tabControl)
tab_payment = ttk.Frame(tabControl)
tab_member = ttk.Frame(tabControl)
tab_course = ttk.Frame(tabControl)
tab_tutor = ttk.Frame(tabControl)
tab_class = ttk.Frame(tabControl)
tab_class_tutor = ttk.Frame(tabControl)

tabControl.add(tab_subscription, text="Subscriptions")
tabControl.add(tab_payment, text="Payments")
tabControl.add(tab_member, text="Members")
tabControl.add(tab_course, text="Courses")
tabControl.add(tab_tutor, text="Tutors")
tabControl.add(tab_class, text="Classes")
tabControl.add(tab_class_tutor, text="Class-Tutor Relationships")
tabControl.pack(expand=1, fill="both")

# Subscription Tab
tk.Label(tab_subscription, text="Subscription ID").grid(row=0, column=0)
tk.Label(tab_subscription, text="Plans").grid(row=1, column=0)
tk.Label(tab_subscription, text="Expiry Date").grid(row=2, column=0)

entry_subscription_id = tk.Entry(tab_subscription)
entry_plans = tk.Entry(tab_subscription)
entry_expiry_date = tk.Entry(tab_subscription)

entry_subscription_id.grid(row=0, column=1)
entry_plans.grid(row=1, column=1)
entry_expiry_date.grid(row=2, column=1)

tk.Button(tab_subscription, text="Create", command=create_subscription).grid(row=3, column=0)
tk.Button(tab_subscription, text="Read", command=read_subscriptions).grid(row=3, column=1)
tk.Button(tab_subscription, text="Update", command=update_subscription).grid(row=4, column=0)
tk.Button(tab_subscription, text="Delete", command=delete_subscription).grid(row=4, column=1)

tree_subscriptions = ttk.Treeview(tab_subscription, columns=("SubscriptionID", "Plans", "ExpiryDate"), show="headings")
for col in tree_subscriptions["columns"]:
    tree_subscriptions.heading(col, text=col)
tree_subscriptions.grid(row=5, column=0, columnspan=2)

# Payment Tab
tk.Label(tab_payment, text="Payment ID").grid(row=0, column=0)
tk.Label(tab_payment, text="Payment Method").grid(row=1, column=0)
tk.Label(tab_payment, text="Amount").grid(row=2, column=0)
tk.Label(tab_payment, text="Verification").grid(row=3, column=0)

entry_payment_id = tk.Entry(tab_payment)
entry_payment_method = tk.Entry(tab_payment)
entry_amount = tk.Entry(tab_payment)
entry_verification = tk.Entry(tab_payment)

entry_payment_id.grid(row=0, column=1)
entry_payment_method.grid(row=1, column=1)
entry_amount.grid(row=2, column=1)
entry_verification.grid(row=3, column=1)

tk.Button(tab_payment, text="Create", command=create_payment).grid(row=4, column=0)
tk.Button(tab_payment, text="Read", command=read_payments).grid(row=4, column=1)
tk.Button(tab_payment, text="Update", command=update_payment).grid(row=5, column=0)
tk.Button(tab_payment, text="Delete", command=delete_payment).grid(row=5, column=1)

tree_payments = ttk.Treeview(tab_payment, columns=("PaymentID", "PaymentMethod", "Amount", "Verification"), show="headings")
for col in tree_payments["columns"]:
    tree_payments.heading(col, text=col)
tree_payments.grid(row=6, column=0, columnspan=2)

# Member Tab
tk.Label(tab_member, text="Member ID").grid(row=0, column=0)
tk.Label(tab_member, text="Name").grid(row=1, column=0)
tk.Label(tab_member, text="Membership Date").grid(row=2, column=0)
tk.Label(tab_member, text="Subscription ID").grid(row=3, column=0)

entry_member_id = tk.Entry(tab_member)
entry_member_name = tk.Entry(tab_member)
entry_membership_date = tk.Entry(tab_member)
entry_subscription_id_member = tk.Entry(tab_member)

entry_member_id.grid(row=0, column=1)
entry_member_name.grid(row=1, column=1)
entry_membership_date.grid(row=2, column=1)
entry_subscription_id_member.grid(row=3, column=1)

tk.Button(tab_member, text="Create", command=create_member).grid(row=4, column=0)
tk.Button(tab_member, text="Read", command=read_members).grid(row=4, column=1)
tk.Button(tab_member, text="Update", command=update_member).grid(row=5, column=0)
tk.Button(tab_member, text="Delete", command=delete_member).grid(row=5, column=1)

tree_members = ttk.Treeview(tab_member, columns=("MemberID", "Name", "MembershipDate", "SubscriptionID"), show="headings")
for col in tree_members["columns"]:
    tree_members.heading(col, text=col)
tree_members.grid(row=6, column=0, columnspan=2)

# Course Tab
tk.Label(tab_course, text="Course ID").grid(row=0, column=0)
tk.Label(tab_course, text="Course Name").grid(row=1, column=0)
tk.Label(tab_course, text="Course Video").grid(row=2, column=0)
tk.Label(tab_course, text="Course Lesson").grid(row=3, column=0)
tk.Label(tab_course, text="Member ID").grid(row=4, column=0)

entry_course_id = tk.Entry(tab_course)
entry_course_name = tk.Entry(tab_course)
entry_course_video = tk.Entry(tab_course)
entry_course_lesson = tk.Entry(tab_course)
entry_member_id_course = tk.Entry(tab_course)

entry_course_id.grid(row=0, column=1)
entry_course_name.grid(row=1, column=1)
entry_course_video.grid(row=2, column=1)
entry_course_lesson.grid(row=3, column=1)
entry_member_id_course.grid(row=4, column=1)

tk.Button(tab_course, text="Create", command=create_course).grid(row=5, column=0)
tk.Button(tab_course, text="Read", command=read_courses).grid(row=5, column=1)
tk.Button(tab_course, text="Update", command=update_course).grid(row=6, column=0)
tk.Button(tab_course, text="Delete", command=delete_course).grid(row=6, column=1)

tree_courses = ttk.Treeview(tab_course, columns=("CourseID", "CourseName", "CourseVideo", "CourseLesson", "MemberID"), show="headings")
for col in tree_courses["columns"]:
    tree_courses.heading(col, text=col)
tree_courses.grid(row=7, column=0, columnspan=2)

# Tutor Tab
tk.Label(tab_tutor, text="Tutor ID").grid(row=0, column=0)
tk.Label(tab_tutor, text="Name").grid(row=1, column=0)
tk.Label(tab_tutor, text="Occupation").grid(row=2, column=0)
tk.Label(tab_tutor, text="Class Type").grid(row=3, column=0)

entry_tutor_id = tk.Entry(tab_tutor)
entry_tutor_name = tk.Entry(tab_tutor)
entry_occupation = tk.Entry(tab_tutor)
entry_class_type = tk.Entry(tab_tutor)

entry_tutor_id.grid(row=0, column=1)
entry_tutor_name.grid(row=1, column=1)
entry_occupation.grid(row=2, column=1)
entry_class_type.grid(row=3, column=1)

tk.Button(tab_tutor, text="Create", command=create_tutor).grid(row=4, column=0)
tk.Button(tab_tutor, text="Read", command=read_tutors).grid(row=4, column=1)
tk.Button(tab_tutor, text="Update", command=update_tutor).grid(row=5, column=0)
tk.Button(tab_tutor, text="Delete", command=delete_tutor).grid(row=5, column=1)

tree_tutors = ttk.Treeview(tab_tutor, columns=("TutorID", "Name", "Occupation", "ClassType"), show="headings")
for col in tree_tutors["columns"]:
    tree_tutors.heading(col, text=col)
tree_tutors.grid(row=6, column=0, columnspan=2)

# Class Tab
tk.Label(tab_class, text="Class ID").grid(row=0, column=0)
tk.Label(tab_class, text="Class Type").grid(row=1, column=0)
tk.Label(tab_class, text="Tutors Name").grid(row=2, column=0)

entry_class_id = tk.Entry(tab_class)
entry_class_type_class = tk.Entry(tab_class)
entry_tutors_name = tk.Entry(tab_class)

entry_class_id.grid(row=0, column=1)
entry_class_type_class.grid(row=1, column=1)
entry_tutors_name.grid(row=2, column=1)

tk.Button(tab_class, text="Create", command=create_class).grid(row=3, column=0)
tk.Button(tab_class, text="Read", command=read_classes).grid(row=3, column=1)
tk.Button(tab_class, text="Update", command=update_class).grid(row=4, column=0)
tk.Button(tab_class, text="Delete", command=delete_class).grid(row=4, column=1)

tree_classes = ttk.Treeview(tab_class, columns=("ClassID", "ClassType", "TutorsName"), show="headings")
for col in tree_classes["columns"]:
    tree_classes.heading(col, text=col)
tree_classes.grid(row=5, column=0, columnspan=2)

# Class-Tutor Tab
tk.Label(tab_class_tutor, text="Class ID").grid(row=0, column=0)
tk.Label(tab_class_tutor, text="Tutor ID").grid(row=1, column=0)

entry_class_id_ct = tk.Entry(tab_class_tutor)
entry_tutor_id_ct = tk.Entry(tab_class_tutor)

entry_class_id_ct.grid(row=0, column=1)
entry_tutor_id_ct.grid(row=1, column=1)

tk.Button(tab_class_tutor, text="Create", command=create_class_tutor).grid(row=2, column=0)
tk.Button(tab_class_tutor, text="Read", command=read_classes_tutors).grid(row=2, column=1)
tk.Button(tab_class_tutor, text="Update", command=update_class_tutor).grid(row=3, column=0)
tk.Button(tab_class_tutor, text="Delete", command=delete_class_tutor).grid(row=3, column=1)

tree_classes_tutors = ttk.Treeview(tab_class_tutor, columns=("ClassID", "TutorID"), show="headings")
for col in tree_classes_tutors["columns"]:
    tree_classes_tutors.heading(col, text=col)
tree_classes_tutors.grid(row=4, column=0, columnspan=2)

root.mainloop()