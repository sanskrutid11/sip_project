import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Database connection configuration
DB_CONFIG = {
    "host": "localhost",  # Replace with your database host
    "user": "root",       # Replace with your database username
    "password": "",       # Replace with your database password
    "database": "sip_tracker"  # Replace with your database name
}

# Function to fetch data from the database
def fetch_data(table_name):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

# Global variables for admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# Function to handle logout
def logout(current_window):
    current_window.destroy()
    create_login_screen()

# Function to open the admin dashboard
def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Admin Dashboard")
    dashboard.state("zoomed")
    dashboard.config(bg="white")

    # Colors
    NAVY_BLUE = "#00274D"
    WHITE = "#FFFFFF"
    BUTTON_BG = "#00509E"
    BUTTON_FG = WHITE

    # Header
    header = tk.Frame(dashboard, bg=NAVY_BLUE, height=60)
    header.pack(side="top", fill="x")
    tk.Label(header, text="Admin Dashboard", fg=WHITE, bg=NAVY_BLUE, font=("Arial", 20, "bold")).pack(side="left", padx=20)
    tk.Button(header, text="Logout", command=lambda: logout(dashboard), bg="red", fg=WHITE, font=("Arial", 12, "bold"), width=10).pack(side="right", padx=20)

    # Footer
    footer = tk.Frame(dashboard, bg=NAVY_BLUE, height=30)
    footer.pack(side="bottom", fill="x")
    tk.Label(footer, text="© 2025 Admin Dashboard", fg=WHITE, bg=NAVY_BLUE, font=("Arial", 12)).pack()

    # Sidebar
    sidebar = tk.Frame(dashboard, bg=NAVY_BLUE, width=250)
    sidebar.pack(side="left", fill="y")

    # Sidebar Buttons
    sidebar_buttons = [
        ("View Users", "users"),
        ("View Withdrawals", "withdrawals"),
        ("View Mutual Funds", "mutual_funds"),
        ("Add Mutual Fund", "add_mutual_fund"),
        ("View Registrations", "registrations")
    ]

    for text, table in sidebar_buttons:
        tk.Button(sidebar, text=text, fg=BUTTON_FG, bg=BUTTON_BG, font=("Arial", 14), command=lambda t=table: handle_sidebar_action(t)).pack(fill="x", pady=10, padx=20)

    # Main Content Area
    main_content = tk.Frame(dashboard, bg=WHITE)
    main_content.pack(side="right", expand=True, fill="both", padx=20, pady=20)

    def handle_sidebar_action(action):
        if action == "add_mutual_fund":
            add_mutual_fund(main_content)
        else:
            display_data(main_content, action)

    dashboard.mainloop()

# Function to display data in Treeview with Edit and Delete functionality
def display_data(frame, table_name):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text=f"{table_name.capitalize()} Data", font=("Arial", 18, "bold"), bg="white").pack(pady=20)

    # Columns based on table_name
    columns = {
        "users": ["ID", "PAN Number", "Password"],
        "withdrawals": ["ID", "User ID", "Mutual Fund ID", "Withdrawal Amount", "Withdrawal Date"],
        "mutual_funds": ["ID", "Name", "Price", "Risk", "Expected Return", "Description", "Actions"],
        "registrations": ["ID", "User ID", "PAN Card", "Address Proof", "Photo", "Investment Amount", "Frequency", "Duration", "Start Date", "Bank Account", "Bank IFSC"]
    }

    # Treeview widget
    tree = ttk.Treeview(frame, columns=columns[table_name], show="headings", height=15)
    for col in columns[table_name]:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    # Fetch data from the database
    data = fetch_data(table_name)

    # Insert data into the treeview
    for row in data:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill="both", pady=10)

    # Buttons for editing and deleting mutual funds
    if table_name == "mutual_funds":
        def edit_mutual_fund():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "Please select a mutual fund to edit.")
                return

            item_values = tree.item(selected_item, "values")
            mutual_fund_id = item_values[0]
            edit_window = tk.Toplevel(frame)
            edit_window.title("Edit Mutual Fund")
            edit_window.geometry("400x400")

            fields = ["Name", "Price", "Risk", "Expected Return", "Description"]
            entries = {}

            for field in fields:
                tk.Label(edit_window, text=field, font=("Arial", 14)).pack(pady=5)
                entry = tk.Entry(edit_window, width=30, font=("Arial", 14))
                entry.pack(pady=5)
                entries[field] = entry

            # Pre-fill the data
            for i, field in enumerate(fields):
                entries[field].insert(0, item_values[i + 1])

            def save_changes():
                data = {field.lower(): entries[field].get() for field in fields}
                try:
                    conn = mysql.connector.connect(**DB_CONFIG)
                    cursor = conn.cursor()
                    query = ("UPDATE mutual_funds SET name=%s, price=%s, risk=%s, expected_return=%s, description=%s WHERE id=%s")
                    cursor.execute(query, (*data.values(), mutual_fund_id))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Success", "Mutual Fund updated successfully!")
                    edit_window.destroy()
                    display_data(frame, table_name)
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Failed to update mutual fund: {err}")

            tk.Button(edit_window, text="Save", command=save_changes, bg="#00509E", fg="white", font=("Arial", 14), width=15).pack(pady=20)

        def delete_mutual_fund():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "Please select a mutual fund to delete.")
                return

            item_values = tree.item(selected_item, "values")
            mutual_fund_id = item_values[0]
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this mutual fund?")
            if confirm:
                try:
                    conn = mysql.connector.connect(**DB_CONFIG)
                    cursor = conn.cursor()
                    query = "DELETE FROM mutual_funds WHERE id=%s"
                    cursor.execute(query, (mutual_fund_id,))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Success", "Mutual Fund deleted successfully!")
                    display_data(frame, table_name)
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Failed to delete mutual fund: {err}")

        action_frame = tk.Frame(frame, bg="white")
        action_frame.pack(fill="x", pady=10)

        tk.Button(action_frame, text="Edit", command=edit_mutual_fund, bg="#00509E", fg="white", font=("Arial", 14), width=15).pack(side="left", padx=10)
        tk.Button(action_frame, text="Delete", command=delete_mutual_fund, bg="red", fg="white", font=("Arial", 14), width=15).pack(side="right", padx=10)

# Function to add a new mutual fund
def add_mutual_fund(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Add New Mutual Fund", font=("Arial", 18, "bold"), bg="white").pack(pady=20)

    fields = ["Name", "Price", "Risk", "Expected Return", "Description"]
    entries = {}

    for field in fields:
        tk.Label(frame, text=field, font=("Arial", 14), bg="white").pack(pady=5)
        entry = tk.Entry(frame, width=30, font=("Arial", 14))
        entry.pack(pady=5)
        entries[field] = entry

    def submit_fund():
        data = {field.lower(): entries[field].get() for field in fields}
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            query = "INSERT INTO mutual_funds (name, price, risk, expected_return, description) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, tuple(data.values()))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Success", "Mutual Fund added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to add mutual fund: {err}")

    tk.Button(frame, text="Submit", command=submit_fund, bg="#00509E", fg="white", font=("Arial", 14), width=15).pack(pady=20)

# Login screen inside a container
def create_login_screen():
    login_window = tk.Tk()
    login_window.title("Admin Login")
    login_window.state("zoomed")
    login_window.config(bg="white")

    login_container = tk.Frame(login_window, bg="white", padx=20, pady=20)
    login_container.pack(expand=True)

    tk.Label(login_container, text="Admin Login", font=("Arial", 24, "bold"), bg="white").pack(pady=30)

    tk.Label(login_container, text="Username", font=("Arial", 14), bg="white").pack(pady=10)
    username_entry = tk.Entry(login_container, width=30, font=("Arial", 14))
    username_entry.pack(pady=10)

    tk.Label(login_container, text="Password", font=("Arial", 14), bg="white").pack(pady=10)
    password_entry = tk.Entry(login_container, show="*", width=30, font=("Arial", 14))
    password_entry.pack(pady=10)

    tk.Button(login_container, text="Login", command=lambda: admin_login(username_entry.get(), password_entry.get(), login_window),
              bg="#00509E", fg="white", font=("Arial", 14), width=15).pack(pady=30)

    login_window.mainloop()

# Admin login function
def admin_login(username, password, login_window):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        login_window.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")

# Run the application
create_login_screen()
