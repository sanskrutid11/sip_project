import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess

# --- Colors and Styling ---
HEADER_BG_COLOR = "#2C3E50"
HEADER_TEXT_COLOR = "white"
BTN_COLOR = "#3498DB"
BTN_TEXT_COLOR = "white"
CONTAINER_BG_COLOR = "#ECF0F1"
TEXT_COLOR = "#2C3E50"
SIDEBAR_BG_COLOR = "#34495E"
SIDEBAR_TEXT_COLOR = "white"
HIGHLIGHT_COLOR = "#1ABC9C"
FOOTER_BG_COLOR = "#2C3E50"

# --- Database Connection ---
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",       # Replace with your MySQL username
            password="",       # Replace with your MySQL password
            database="sip_tracker"  # Replace with your database name
        )
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return None

# --- Fetch User's Mutual Fund Data ---
def fetch_user_mutual_funds(user_id):
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT 
            r.id,
            r.investment_amount,
            r.start_date,
            r.duration,
            mf.name AS mutual_fund_name,
            mf.expected_return,
            r.user_id
        FROM 
            registrations r
        JOIN 
            mutual_funds mf ON mf.id = r.id
        WHERE 
            r.user_id = %s
    """
    try:
        cursor.execute(query, (user_id,))
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as e:
        messagebox.showerror("Query Error", f"Error fetching data: {e}")
        return []
    finally:
        conn.close()

# --- Helper Function to Clean Percentage Value ---
def clean_percentage(value):
    if isinstance(value, str):
        value = value.replace('%', '').strip()
    try:
        return float(value)
    except ValueError:
        return 0.0

# --- Display Mutual Funds List ---
def display_mutual_funds_list(data):
    for widget in left_frame.winfo_children():
        widget.destroy()

    ttk.Label(left_frame, text="Your Investments", font=("Arial", 18, "bold"), background=SIDEBAR_BG_COLOR, foreground=SIDEBAR_TEXT_COLOR).pack(pady=10)

    for record in data:
        btn = tk.Button(
            left_frame, 
            text=record['mutual_fund_name'], 
            font=("Arial", 12),
            bg=HIGHLIGHT_COLOR, 
            fg="white",
            width=25,
            command=lambda r=record: display_selected_fund(r)
        )
        btn.pack(pady=5)

# --- Display Selected Mutual Fund Performance ---
def display_selected_fund(record):
    for widget in middle_frame.winfo_children():
        widget.destroy()

    try:
        investment_amount = float(record['investment_amount'])
        expected_return = clean_percentage(record['expected_return'])
    except ValueError as e:
        messagebox.showerror("Data Error", f"Invalid data for investment or return: {e}")
        return

    profit_loss = calculate_profit_loss(investment_amount, expected_return, record['start_date'])

    # Display Line Graph
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    months = list(range(1, 13))
    values = [
        investment_amount * (1 + (expected_return / 100) * (month / 12))
        for month in months
    ]
    ax.plot(months, values, color="#1ABC9C", label="Projected Growth")
    ax.set_title(f"{record['mutual_fund_name']} Performance")
    ax.set_xlabel("Months")
    ax.set_ylabel("Amount (₹)")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, middle_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

    # Profit/Loss Details
    status = "Profit" if profit_loss >= 0 else "Loss"
    status_color = "green" if profit_loss >= 0 else "red"

    details = f"""
    Mutual Fund: {record['mutual_fund_name']}
    Investment Amount: ₹{investment_amount}
    Start Date: {record['start_date']}
    Profit/Loss: ₹{profit_loss} ({status})
    """
    tk.Label(middle_frame, text=details, font=("Arial", 14), fg=status_color, bg=CONTAINER_BG_COLOR, justify="left").pack(pady=10)

    # Withdrawal Button
    withdrawal_btn = tk.Button(
        middle_frame,
        text="Withdraw Investment",
        font=("Arial", 12),
        bg=BTN_COLOR,
        fg=BTN_TEXT_COLOR,
        command=lambda: initiate_withdrawal(record)
    )
    withdrawal_btn.pack(pady=10)

    # Next Investment Button
    next_investment_btn = tk.Button(
        middle_frame,
        text="Next Investment",
        font=("Arial", 12),
        bg=BTN_COLOR,
        fg=BTN_TEXT_COLOR,
        command=lambda: add_next_investment(record)
    )
    next_investment_btn.pack(pady=10)

# --- Handle Withdrawal Request ---
def initiate_withdrawal(record):
    def submit_withdrawal():
        try:
            withdrawal_amount = float(withdrawal_entry.get())
            if withdrawal_amount <= 0:
                raise ValueError("Amount should be greater than zero.")

            if withdrawal_amount > float(record['investment_amount']):
                raise ValueError("Withdrawal amount cannot be greater than your investment.")

            # Record withdrawal in the database
            conn = get_db_connection()
            if not conn:
                return

            cursor = conn.cursor()
            query = """
                INSERT INTO withdrawals (user_id, mutual_fund_id, withdrawal_amount)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (record['user_id'], record['id'], withdrawal_amount))
            conn.commit()

            # Update the investment amount
            update_query = """
                UPDATE registrations
                SET investment_amount = investment_amount - %s
                WHERE id = %s
            """
            cursor.execute(update_query, (withdrawal_amount, record['id']))
            conn.commit()

            conn.close()

            # Success message
            messagebox.showinfo("Success", f"₹{withdrawal_amount} successfully withdrawn.")
            withdrawal_window.destroy()

            # Move to add.py
            subprocess.run(["python", "add.py"])

        except ValueError as ve:
            messagebox.showerror("Input Error", f"Error: {ve}")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error while processing withdrawal: {e}")

    def set_withdrawal_amount(amount):
        withdrawal_entry.delete(0, tk.END)
        withdrawal_entry.insert(0, str(amount))

    withdrawal_window = tk.Toplevel(root)
    withdrawal_window.title("Withdraw Investment")
    withdrawal_window.state("zoomed")

    # Header
    header = tk.Frame(withdrawal_window, bg=HEADER_BG_COLOR, height=60)
    header.pack(fill="x", side="top")
    tk.Label(header, text="Withdrawal Options", font=("Arial", 18, "bold"), fg=HEADER_TEXT_COLOR, bg=HEADER_BG_COLOR).pack(pady=10)

    # Menubar
    menubar = tk.Menu(withdrawal_window)
    menubar.add_command(label="Exit", command=withdrawal_window.quit)
    withdrawal_window.config(menu=menubar)

    # Footer
    footer = tk.Label(withdrawal_window, text="© 2025 SIP Investment Tracker. All Rights Reserved.", font=("Arial", 12), bg=FOOTER_BG_COLOR, fg=HEADER_TEXT_COLOR)
    footer.pack(side="bottom", fill="x")

    # Container between header and footer
    container = tk.Frame(withdrawal_window, bg=CONTAINER_BG_COLOR)
    container.pack(fill="both", expand=True)

    # Title
    tk.Label(container, text="Withdrawals", font=("Arial", 20, "bold"), bg=CONTAINER_BG_COLOR, fg=TEXT_COLOR).pack(pady=20)

    # Current Balance
    current_balance = record['investment_amount']
    tk.Label(container, text=f"Current Balance: ₹{current_balance}", font=("Arial", 14, "bold"), bg=CONTAINER_BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

    # Withdrawal Amount
    tk.Label(container, text="Enter Withdrawal Amount:", font=("Arial", 12), bg=CONTAINER_BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    withdrawal_entry = tk.Entry(container, font=("Arial", 12))
    withdrawal_entry.pack(pady=10)

    # Radio Buttons for Transfer Option
    transfer_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
    transfer_frame.pack(pady=20)

    transfer_options = [("Bank Transfer", 1), ("UPI Transfer", 2), ("Cheque", 3)]
    transfer_type = tk.IntVar()

    for text, value in transfer_options:
        tk.Radiobutton(transfer_frame, text=text, variable=transfer_type, value=value, font=("Arial", 12), bg=CONTAINER_BG_COLOR, fg=TEXT_COLOR).pack(anchor="w")

    # Submit Button
    submit_btn = tk.Button(
        container,
        text="Submit",
        font=("Arial", 12),
        bg=BTN_COLOR,
        fg=BTN_TEXT_COLOR,
        command=submit_withdrawal,
    )
    submit_btn.pack(pady=20)

# --- Add Next Investment ---
def add_next_investment(record):
    def submit_investment():
        try:
            new_investment = float(investment_entry.get())
            if new_investment <= 0:
                raise ValueError("Investment amount should be greater than zero.")

            # Update the investment amount in the database
            conn = get_db_connection()
            if not conn:
                return

            cursor = conn.cursor()
            update_query = """
                UPDATE registrations
                SET investment_amount = investment_amount + %s
                WHERE id = %s
            """
            cursor.execute(update_query, (new_investment, record['id']))
            conn.commit()

            # Recalculate and display the updated performance
            updated_data = fetch_user_mutual_funds(record['user_id'])
            display_mutual_funds_list(updated_data)

            messagebox.showinfo("Success", f"₹{new_investment} successfully added to your investment.")

            next_investment_window.destroy()

        except ValueError as ve:
            messagebox.showerror("Input Error", f"Error: {ve}")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error while updating investment: {e}")

    next_investment_window = tk.Toplevel(root)
    next_investment_window.title("Add Next Investment")
    next_investment_window.state("zoomed")

    # Header
    header = tk.Frame(next_investment_window, bg=HEADER_BG_COLOR, height=60)
    header.pack(fill="x", side="top")
    tk.Label(header, text="Next Investment", font=("Arial", 18, "bold"), fg=HEADER_TEXT_COLOR, bg=HEADER_BG_COLOR).pack(pady=10)

    # Menubar
    menubar = tk.Menu(next_investment_window)
    menubar.add_command(label="Exit", command=next_investment_window.quit)
    next_investment_window.config(menu=menubar)

    # Footer
    footer = tk.Label(next_investment_window, text="© 2025 SIP Investment Tracker. All Rights Reserved.", font=("Arial", 12), bg=FOOTER_BG_COLOR, fg=HEADER_TEXT_COLOR)
    footer.pack(side="bottom", fill="x")

    # Container between header and footer
    container = tk.Frame(next_investment_window, bg=CONTAINER_BG_COLOR)
    container.pack(fill="both", expand=True)

    # Title
    tk.Label(container, text="Add Next Investment", font=("Arial", 20, "bold"), bg=CONTAINER_BG_COLOR, fg=TEXT_COLOR).pack(pady=20)

    # Investment Amount
    tk.Label(container, text="Enter Next Investment Amount:", font=("Arial", 12), bg=CONTAINER_BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    investment_entry = tk.Entry(container, font=("Arial", 12))
    investment_entry.pack(pady=10)

    # Submit Button
    submit_btn = tk.Button(
        container,
        text="Submit Investment",
        font=("Arial", 12),
        bg=BTN_COLOR,
        fg=BTN_TEXT_COLOR,
        command=submit_investment,
    )
    submit_btn.pack(pady=20)

# --- Calculate Profit or Loss ---
def calculate_profit_loss(investment_amount, expected_return, start_date):
    try:
        start = datetime.strptime(str(start_date), "%Y-%m-%d")
        today = datetime.now()
        months_invested = (today.year - start.year) * 12 + today.month - start.month

        if months_invested > 0:
            growth = investment_amount * (1 + (expected_return / 100) * (months_invested / 12))
            profit_loss = growth - investment_amount
        else:
            profit_loss = 0

        return round(profit_loss, 2)
    except Exception:
        return 0

# --- Add Header ---
def add_header():
    header = tk.Frame(root, bg=HEADER_BG_COLOR, height=60)
    header.pack(fill="x", side="top")
    tk.Label(header, text="Investment Performance", font=("Arial", 24, "bold"), fg=HEADER_TEXT_COLOR, bg=HEADER_BG_COLOR).pack(pady=10)

# --- Add Footer ---
def add_footer():
    footer = tk.Label(root, text="© 2025 SIP Investment Tracker. All Rights Reserved.", font=("Arial", 12), bg=FOOTER_BG_COLOR, fg=HEADER_TEXT_COLOR)
    footer.pack(side="bottom", fill="x")

# --- Add Menubar ---
def add_menubar():
    menubar = tk.Menu(root)
    menubar.add_command(label="Exit", command=root.quit)
    root.config(menu=menubar)

# --- Main UI ---
def create_investment_performance_ui(user_id):
    global root, left_frame, middle_frame

    root = tk.Tk()
    root.title("Investment Performance")
    root.state("zoomed")

    add_header()
    add_menubar()

    container = tk.Frame(root, bg=CONTAINER_BG_COLOR)
    container.pack(fill="both", expand=True)

    left_frame = tk.Frame(container, bg=SIDEBAR_BG_COLOR, width=250)
    left_frame.pack(side="left", fill="y")

    middle_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
    middle_frame.pack(side="left", fill="both", expand=True)

    add_footer()

    data = fetch_user_mutual_funds(user_id)
    if data:
        display_mutual_funds_list(data)
    else:
        messagebox.showinfo("No Data", "No investment records found.")

    root.mainloop()

# --- Run the UI ---
if __name__ == "__main__":
    create_investment_performance_ui(user_id=1)
