import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess
import bcrypt

# --- Colors ---
HEADER_BG_COLOR = "navy"
LOGO_TEXT_COLOR = "white"
BTN_COLOR = "#4682B4"
BTN_TEXT_COLOR = "white"
CONTAINER_BG_COLOR = "white"
TEXT_COLOR = "navy"
LINE_COLOR = "#4682B4"
ENTRY_BG_COLOR = "white"

# --- Database Setup ---
def create_database():
    """Create a MySQL database and users table if it doesn't exist."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sip_tracker"
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        pan_number VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )''')
    conn.commit()
    conn.close()

def store_user(pan_number, password):
    """Store the PAN number and hashed password in the database."""
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sip_tracker"
    )
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (pan_number, password) VALUES (%s, %s)', (pan_number, hashed_password))
        conn.commit()
        return True
    except mysql.connector.IntegrityError:
        return False
    finally:
        conn.close()

# --- Functions ---
def validate_pan():
    """Validate PAN and store it in the database with a password."""
    pan_number = pan_entry.get().strip()
    password = password_entry.get().strip()
    if pan_number and password:
        if store_user(pan_number, password):
            messagebox.showinfo("Registration Success", "PAN validated and account created successfully!")
            show_login_page()
        else:
            messagebox.showerror("Error", "This PAN number already exists.")
    else:
        messagebox.showerror("Error", "Please enter a valid PAN number and password.")

def validate_login():
    """Validate login using PAN number and password."""
    entered_pan = login_pan_entry.get().strip()
    entered_password = login_password_entry.get().strip()

    if entered_pan and entered_password:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="sip_tracker"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE pan_number = %s", (entered_pan,))
            result = cursor.fetchone()

            if result:
                hashed_password = result[0]
                try:
                    if bcrypt.checkpw(entered_password.encode(), hashed_password.encode('utf-8')):
                        messagebox.showinfo("Login Success", "Login successful!")
                        root.destroy()  # Close the current Tkinter window
                        subprocess.run(["python", "add.py"])  # Replace with the actual path to add.py
                    else:
                        messagebox.showerror("Error", "Invalid password.")
                except ValueError:
                    messagebox.showerror("Error", "Stored password format is invalid. Please contact support.")
            else:
                messagebox.showerror("Error", "PAN number not found.")
        finally:
            conn.close()
    else:
        messagebox.showerror("Error", "Please enter both PAN number and password.")

def show_login_page():
    """Hide PAN page and show login page."""
    pan_frame.pack_forget()
    login_frame.pack(pady=(50, 30))

# --- Initialize Main Window ---
root = tk.Tk()
root.title("SIP Investment Tracker - Enter PAN")
root.state("zoomed")  # Full screen on window start

# --- Create Database ---
create_database()

# --- Menubar Setup ---
menubar = tk.Menu(root, bg=HEADER_BG_COLOR, fg="white", font=("Arial", 14))
menubar.add_command(label="Back", command=root.quit)
menubar.add_command(label="SIP Benefits", command=lambda: messagebox.showinfo("SIP Benefits", "Learn about SIP."))
root.config(menu=menubar)

# --- Header with Logo ---
def add_logo_title():
    logo_frame = tk.Frame(root, bg=HEADER_BG_COLOR, height=50)
    logo_frame.pack(fill="x")
    logo_label = tk.Label(logo_frame, text="SIP Tracker", font=("Arial", 20, "bold"), fg=LOGO_TEXT_COLOR, bg=HEADER_BG_COLOR)
    logo_label.pack(side="left", padx=20)

add_logo_title()

# --- Main Title ---
def add_main_title():
    main_title = tk.Label(root, text="Enter PAN and Start Your Journey", font=("Arial", 24, "bold"), fg=TEXT_COLOR)
    main_title.pack(pady=(30, 20))

add_main_title()

# --- PAN Validation Section ---
pan_frame = tk.Frame(root, bg=CONTAINER_BG_COLOR, bd=2, relief="solid", padx=20, pady=20)
pan_frame.pack(pady=(20, 50), padx=100)

pan_label = tk.Label(pan_frame, text="Enter PAN:", font=("Arial", 16, "bold"), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
pan_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

pan_entry = tk.Entry(pan_frame, font=("Arial", 14), bg=ENTRY_BG_COLOR, fg=TEXT_COLOR, relief="flat", justify="center", width=40)
pan_entry.grid(row=0, column=1, pady=10)

password_label = tk.Label(pan_frame, text="Set Password:", font=("Arial", 16, "bold"), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

password_entry = tk.Entry(pan_frame, font=("Arial", 14), bg=ENTRY_BG_COLOR, fg=TEXT_COLOR, relief="flat", show="*", width=40)
password_entry.grid(row=1, column=1, pady=10)

validate_btn = tk.Button(pan_frame, text="Validate", font=("Arial", 14, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=validate_pan, relief="flat", padx=20, pady=5)
validate_btn.grid(row=2, column=0, columnspan=2, pady=20)

# --- Login Page Section ---
login_frame = tk.Frame(root, bg=CONTAINER_BG_COLOR, bd=2, relief="solid", padx=30, pady=30)

login_title = tk.Label(login_frame, text="Login with Password", font=("Arial", 24, "bold"), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
login_title.pack(pady=(20, 10))

login_pan_label = tk.Label(login_frame, text="PAN Number:", font=("Arial", 14, "bold"), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
login_pan_label.pack(pady=5, anchor="w")

login_pan_entry = tk.Entry(login_frame, font=("Arial", 14), bg=ENTRY_BG_COLOR, fg=TEXT_COLOR, relief="flat", justify="center", width=40)
login_pan_entry.pack(pady=10)

login_password_label = tk.Label(login_frame, text="Password:", font=("Arial", 14, "bold"), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
login_password_label.pack(pady=5, anchor="w")

login_password_entry = tk.Entry(login_frame, font=("Arial", 14), bg=ENTRY_BG_COLOR, fg=TEXT_COLOR, relief="flat", show="*", width=40)
login_password_entry.pack(pady=10)

login_button = tk.Button(login_frame, text="Login", font=("Arial", 14, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=validate_login, relief="flat", padx=20, pady=5)
login_button.pack(pady=20)

# --- Footer ---
def add_footer():
    footer_label = tk.Label(root, text="© 2024 SIP Investment Tracker. All Rights Reserved.", font=("Arial", 12), bg=HEADER_BG_COLOR, fg=LOGO_TEXT_COLOR)
    footer_label.pack(side="bottom", fill="x")

add_footer()

# --- Main Application Loop ---
root.mainloop()
