import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import subprocess

def open_detailed_page(fund):
    """Display detailed page for the selected fund."""
    detailed_window = tk.Toplevel()
    detailed_window.title(f"Details of {fund['name']}")
    detailed_window.state("zoomed")

    # --- Menubar ---
    menubar = tk.Menu(detailed_window)
    detailed_window.config(menu=menubar)
    menubar.add_command(label="Home", command=detailed_window.quit)
    menubar.add_command(label="SIP Benefits", command=detailed_window.quit)
    menubar.add_command(label="FAQS", command=detailed_window.quit)
    menubar.add_command(label="Plan", command=detailed_window.quit)
    menubar.add_command(label="Funds", command=detailed_window.quit)
    

    # --- Header ---
    tk.Label(detailed_window, text="Fund Performance", font=("Arial", 24, "bold"), bg="#0077cc", fg="white").pack(fill="x", pady=5)

    # --- Fund Name and Details ---
    tk.Label(detailed_window, text=f"{fund['name']}", font=("Arial", 20, "bold")).pack(anchor="w", padx=20, pady=10)

    fund_details_frame = tk.Frame(detailed_window)
    fund_details_frame.pack(anchor="w", padx=20)

    fund_details = [
        f"Price: {fund['price']}",
        f"Risk: {fund['risk']}",
        f"Expected Return: {fund['return']}",
        f"Description: {fund['desc']}"
    ]

    for detail in fund_details:
        tk.Label(fund_details_frame, text=detail, font=("Arial", 14)).pack(anchor="w", pady=2)

    # --- Rectangles Section ---
    rectangles_frame = tk.Frame(detailed_window)
    rectangles_frame.pack(fill="both", padx=20, pady=10)

    # First Rectangle: Performance Calculator and Histogram
    left_rect = tk.Frame(rectangles_frame, width=600, height=350, bg="#F0F0F0", padx=10, pady=10, relief="solid", bd=1)
    left_rect.pack(side="left", padx=10, pady=10, expand=True, fill="both")

    # Performance Title
    title_frame = tk.Frame(left_rect, bg="#F0F0F0")
    title_frame.pack(anchor="w", padx=5, pady=5)
    tk.Label(title_frame, text="Performance", font=("Arial", 16, "bold"), bg="#F0F0F0").pack(side="left", padx=10)

    # Inputs for SIP Calculation
    input_frame = tk.Frame(left_rect, bg="#F0F0F0")
    input_frame.pack(anchor="w", padx=10, pady=10)

    tk.Label(input_frame, text="Monthly SIP (₹):", font=("Arial", 12), bg="#F0F0F0").grid(row=0, column=0, padx=5, pady=5)
    sip_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
    sip_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Years:", font=("Arial", 12), bg="#F0F0F0").grid(row=0, column=2, padx=5, pady=5)
    years_entry = tk.Entry(input_frame, font=("Arial", 12), width=5)
    years_entry.grid(row=0, column=3, padx=5, pady=5)

    calc_button = tk.Button(input_frame, text="Calculate", font=("Arial", 12), bg="#4CAF50", fg="white",
                            command=lambda: calculate_performance(sip_entry, years_entry, histogram_frame))
    calc_button.grid(row=0, column=4, padx=10, pady=5)

    # Histogram Frame
    histogram_frame = tk.Frame(left_rect, bg="#F0F0F0")
    histogram_frame.pack(expand=True, fill="both", pady=10)

    # Second Rectangle: SIP Details
    right_rect = tk.Frame(rectangles_frame, width=300, height=300, bg="#E0E0E0", padx=10, pady=10, relief="solid", bd=1)
    right_rect.pack(side="left", padx=10, pady=10, fill="both")

    tk.Label(right_rect, text="SIP Amount:", font=("Arial", 14, "bold"), bg="#E0E0E0").pack(anchor="w", pady=10)
    sip_amount_entry = tk.Entry(right_rect, font=("Arial", 12))
    sip_amount_entry.pack(anchor="w", padx=5, pady=5)

    tk.Label(right_rect, text="SIP Start Date:", font=("Arial", 14), bg="#E0E0E0").pack(anchor="w", pady=10)

    date_label = tk.Label(right_rect, text="Select Date", font=("Arial", 12), bg="#E0E0E0")
    date_label.pack(anchor="w", padx=5)

    tk.Button(right_rect, text="📅", font=("Arial", 14), command=lambda: open_calendar(date_label)).pack(anchor="w", padx=5, pady=5)

    tk.Button(right_rect, text="Invest Now", font=("Arial", 14), bg="green", fg="white", command=lambda: subprocess.run(["python", "kyc_form.py"])).pack(pady=20)

# Function to calculate and display histogram
def calculate_performance(sip_entry, years_entry, histogram_frame):
    try:
        sip_amount = int(sip_entry.get())
        years = int(years_entry.get())
        months = years * 12
        rate_of_return = 0.12 / 12

        values = [sip_amount * ((1 + rate_of_return) ** i - 1) / rate_of_return for i in range(1, months + 1)]
        months_list = np.arange(1, months + 1)

        for widget in histogram_frame.winfo_children():
            widget.destroy()

        # Plot the histogram
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(months_list, values, color='blue')
        ax.set_title("SIP Performance")
        ax.set_xlabel("Months")
        ax.set_ylabel("Total Value (₹)")

        canvas = FigureCanvasTkAgg(fig, master=histogram_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for SIP amount and years.")

# Function to open calendar
def open_calendar(date_label):
    calendar_window = tk.Toplevel()
    calendar_window.title("Select Date")

    cal = Calendar(calendar_window, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.pack(pady=20)

    def set_date():
        date_label.config(text=f"Start Date: {cal.get_date()}")
        calendar_window.destroy()

    tk.Button(calendar_window, text="Select", command=set_date).pack(pady=10)

# Main window
if __name__ == "__main__":
    fund = {
        "name": "XYZ Growth Fund",
        "price": "₹200",
        "risk": "Moderate",
        "return": "12%",
        "desc": "This fund focuses on high-growth companies with stable potential."
    }

    root = tk.Tk()
    root.title("Fund Details")
    root.state("zoomed")

    tk.Button(root, text="View Fund Details", font=("Arial", 14), command=lambda: open_detailed_page(fund)).pack(pady=50)

    root.mainloop()
