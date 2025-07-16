import tkinter as tk

from tkinter import filedialog, messagebox

from tkinter import ttk

import os

import mysql.connector

from datetime import datetime

import subprocess



# Function to upload file and display filename

def upload_file(file_label):

    file_path = filedialog.askopenfilename(title="Select File", filetypes=[("PDF Files", "*.pdf"), ("Image Files", "*.jpg;*.png")])

    if file_path:

        file_label.config(text=os.path.basename(file_path))

    else:

        file_label.config(text="No file selected")



# Function to store records in the database

def store_in_db(user_id, mutual_fund_id, pan_file, address_file, photo_file, investment, frequency, duration, start_date, bank_account, bank_ifsc):

    try:

        # Ensure all parameters are in correct format

        user_id = int(user_id)

        mutual_fund_id = int(mutual_fund_id)

        investment = float(investment)

        frequency = str(frequency)

        duration = int(duration)

        start_date = str(start_date)

        bank_account = str(bank_account)

        bank_ifsc = str(bank_ifsc)



        # Establish database connection

        conn = mysql.connector.connect(

            host="localhost",        # Replace with your MySQL host

            user="root",             # Replace with your MySQL username

            password="",             # Replace with your MySQL password

            database="sip_tracker"   # Replace with your database name

        )

        cursor = conn.cursor()



        # Insert data into the registrations table

        cursor.execute("""

            INSERT INTO registrations (user_id, pan_card, address_proof, photo, investment_amount, frequency, duration, start_date, bank_account, bank_ifsc)

            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)

        """, (user_id, pan_file, address_file, photo_file, investment, frequency, duration, start_date, bank_account, bank_ifsc))



        # Insert data into the investments table

        cursor.execute("""

            INSERT INTO investments (user_id, mutual_fund_id, investment_amount, start_date)

            VALUES (%s, %s, %s, %s)

        """, (user_id, mutual_fund_id, investment, start_date))



        conn.commit()  # Commit changes to the database

        messagebox.showinfo("Success", "document verified successfully!")

        conn.close()

    except mysql.connector.Error as err:

        # Print detailed error information for debugging

        messagebox.showerror("Error", f"Failed to store data: {err}")

        print(f"Error: {err}")  # Print the MySQL error to the console

        if conn.is_connected():

            conn.rollback()  # Rollback any changes in case of an error



# Function to submit the KYC and SIP registration

def submit_kyc(user_id, mutual_fund_id):

    # Check if files are uploaded

    if (pan_label.cget("text") == "No file selected" or 

        address_label.cget("text") == "No file selected" or 

        photo_label.cget("text") == "No file selected"):

        messagebox.showerror("Error", "Please upload all required documents.")

    elif (not investment_amount.get() or not frequency_var.get() or not duration_var.get() or

          not start_date.get() or not bank_account.get() or not bank_ifsc.get()):

        messagebox.showerror("Error", "Please fill in all investment and bank details.")

    else:

        # Retrieve file paths

        pan_file = pan_label.cget("text")

        address_file = address_label.cget("text")

        photo_file = photo_label.cget("text")

        

        # Retrieve other form data

        investment = float(investment_amount.get())

        frequency = frequency_var.get()

        duration = int(duration_var.get())

        

        try:

            start_date_value = datetime.strptime(start_date.get(), "%d/%m/%Y").date()

        except ValueError:

            messagebox.showerror("Error", "Please enter a valid start date (DD/MM/YYYY).")

            return

        

        bank_account_value = bank_account.get()

        bank_ifsc_value = bank_ifsc.get()



        # Store the data in the database

        store_in_db(user_id, mutual_fund_id, pan_file, address_file, photo_file, investment, frequency, duration, start_date_value, bank_account_value, bank_ifsc_value)



        # Close the current window and open the main page

        root.destroy()

        subprocess.run(["python", "add.py"])



# Function to show investment performance

def show_investment_performance(user_id):

    # Establish database connection

    conn = mysql.connector.connect(

        host="localhost",        # Replace with your MySQL host

        user="root",             # Replace with your MySQL username

        password="",             # Replace with your MySQL password

        database="sip_tracker"   # Replace with your database name

    )

    cursor = conn.cursor()



    # Get user's investments

    cursor.execute("""

        SELECT investments.investment_amount, investments.investment_date, mutual_funds.name, mutual_funds.price

        FROM investments

        JOIN mutual_funds ON investments.mutual_fund_id = mutual_funds.id

        WHERE investments.user_id = %s

    """, (user_id,))

    investments = cursor.fetchall()



    if investments:

        for inv in investments:

            investment_amount, investment_date, mutual_fund_name, mutual_fund_price = inv

            current_value = mutual_fund_price * investment_amount  # Assuming the price is per unit

            profit_loss = current_value - investment_amount



            # Show investment performance in a new window

            performance_window = tk.Toplevel(root)

            performance_window.title("Investment Performance")

            performance_window.geometry("600x400")

            performance_label = tk.Label(performance_window, text=f"Mutual Fund: {mutual_fund_name}\n"

                                                                f"Investment Amount: ₹{investment_amount}\n"

                                                                f"Current Value: ₹{current_value}\n"

                                                                f"Profit/Loss: ₹{profit_loss}",

                                        font=("Arial", 14))

            performance_label.pack(pady=20)

    else:

        messagebox.showinfo("No Investment", "No investments found for this user.")



    conn.close()



# Main window

root = tk.Tk()

root.title("KYC and SIP Registration Form")



# Maximize the window on start

root.state("zoomed")

root.configure(bg="#f0f8ff")



# --- Menubar ---

menubar = tk.Menu(root)

root.config(menu=menubar)

menubar.add_command(label="Home")

menubar.add_command(label="Funds")

menubar.add_command(label="FAQS")



# --- Header ---

header_frame = tk.Frame(root, bg="#0073e6", height=60)

header_frame.pack(fill=tk.X)



header_label = tk.Label(header_frame, text="KYC and SIP Registration Form", font=("Arial", 24, "bold"), bg="#0073e6", fg="white")

header_label.pack(pady=10)



# --- Main Content Frame (Container) ---

content_frame = tk.Frame(root, bg="white", padx=30, pady=30, relief="solid", bd=2)

content_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the container in the middle of the window



# Instructions

instructions = tk.Label(content_frame, text="Please upload the required documents and provide investment details.", font=("Arial", 12), bg="white")

instructions.grid(row=0, column=0, columnspan=3, pady=15)



# Upload PAN Card

pan_label_text = tk.Label(content_frame, text="Upload PAN Card:", font=("Arial", 12), bg="white")

pan_label_text.grid(row=1, column=0, sticky="w", pady=10)



pan_label = tk.Label(content_frame, text="No file selected", bg="white", fg="grey")

pan_label.grid(row=1, column=1, sticky="w", pady=10)



pan_button = tk.Button(content_frame, text="Choose File", command=lambda: upload_file(pan_label), bg="#0073e6", fg="white")

pan_button.grid(row=1, column=2, padx=10)



# Upload Address Proof

address_label_text = tk.Label(content_frame, text="Upload Address Proof:", font=("Arial", 12), bg="white")

address_label_text.grid(row=2, column=0, sticky="w", pady=10)



address_label = tk.Label(content_frame, text="No file selected", bg="white", fg="grey")

address_label.grid(row=2, column=1, sticky="w", pady=10)



address_button = tk.Button(content_frame, text="Choose File", command=lambda: upload_file(address_label), bg="#0073e6", fg="white")

address_button.grid(row=2, column=2, padx=10)



# Upload Photo

photo_label_text = tk.Label(content_frame, text="Upload Recent Photograph:", font=("Arial", 12), bg="white")

photo_label_text.grid(row=3, column=0, sticky="w", pady=10)



photo_label = tk.Label(content_frame, text="No file selected", bg="white", fg="grey")

photo_label.grid(row=3, column=1, sticky="w", pady=10)



photo_button = tk.Button(content_frame, text="Choose File", command=lambda: upload_file(photo_label), bg="#0073e6", fg="white")

photo_button.grid(row=3, column=2, padx=10)



# Investment Details

investment_label = tk.Label(content_frame, text="Investment Amount (INR):", font=("Arial", 12), bg="white")

investment_label.grid(row=4, column=0, sticky="w", pady=10)



investment_amount = tk.Entry(content_frame)

investment_amount.grid(row=4, column=1, sticky="w", pady=10)



frequency_label = tk.Label(content_frame, text="Frequency:", font=("Arial", 12), bg="white")

frequency_label.grid(row=5, column=0, sticky="w", pady=10)



frequency_var = tk.StringVar()

frequency_dropdown = ttk.Combobox(content_frame, textvariable=frequency_var, values=["Monthly", "Weekly", "Quarterly", "Bi-annual"])

frequency_dropdown.grid(row=5, column=1, sticky="w", pady=10)



duration_label = tk.Label(content_frame, text="Investment Duration (Years):", font=("Arial", 12), bg="white")

duration_label.grid(row=6, column=0, sticky="w", pady=10)



duration_var = tk.StringVar()

duration_dropdown = ttk.Combobox(content_frame, textvariable=duration_var, values=["1", "2", "3", "5", "10"])

duration_dropdown.grid(row=6, column=1, sticky="w", pady=10)



start_date_label = tk.Label(content_frame, text="Start Date (DD/MM/YYYY):", font=("Arial", 12), bg="white")

start_date_label.grid(row=7, column=0, sticky="w", pady=10)



start_date = tk.Entry(content_frame)

start_date.grid(row=7, column=1, sticky="w", pady=10)



# Bank Details

bank_account_label = tk.Label(content_frame, text="Bank Account Number:", font=("Arial", 12), bg="white")

bank_account_label.grid(row=8, column=0, sticky="w", pady=10)



bank_account = tk.Entry(content_frame)

bank_account.grid(row=8, column=1, sticky="w", pady=10)



bank_ifsc_label = tk.Label(content_frame, text="Bank IFSC Code:", font=("Arial", 12), bg="white")

bank_ifsc_label.grid(row=9, column=0, sticky="w", pady=10)



bank_ifsc = tk.Entry(content_frame)

bank_ifsc.grid(row=9, column=1, sticky="w", pady=10)



# Submit Button

submit_button = tk.Button(content_frame, text="Submit KYC", command=lambda: submit_kyc(user_id=1, mutual_fund_id=1), bg="#28a745", fg="white")

submit_button.grid(row=10, column=0, columnspan=3, pady=20)



root.mainloop() 
