import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Function to calculate retirement savings
def calculate_retirement():
    try:
        # Get user input values
        monthly_savings = float(savings_entry.get())
        annual_return = float(return_entry.get()) / 100
        current_age = int(age_entry.get())
        retirement_age = int(retirement_age_entry.get())

        if current_age >= retirement_age:
            messagebox.showerror("Error", "Current age should be less than retirement age.")
            return

        # Calculate the number of years until retirement
        years_until_retirement = retirement_age - current_age

        # Initialize variables for the calculation
        months = years_until_retirement * 12
        savings = 0
        monthly_rate_of_return = annual_return / 12

        # Create lists to store monthly data for plotting
        months_list = []
        savings_list = []

        # Calculate the savings for each month
        for month in range(1, months + 1):
            savings += monthly_savings
            savings *= (1 + monthly_rate_of_return)  # Apply the monthly return
            months_list.append(month)
            savings_list.append(savings)

        # Display the projected savings at retirement
        projected_savings = round(savings, 2)
        messagebox.showinfo("Retirement Savings", f"Your projected savings at retirement: ₹{projected_savings}")

        # Plot the savings growth
        plot_graph(months_list, savings_list)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Function to plot the graph
def plot_graph(months_list, savings_list):
    for widget in graph_frame.winfo_children():
        widget.destroy()  # Clear previous graph

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(months_list, savings_list, color='blue', label='Projected Savings')

    ax.set_title("Projected Retirement Savings Over Time")
    ax.set_xlabel("Months")
    ax.set_ylabel("Savings (₹)")
    ax.grid(True)

    # Create the canvas to display the plot
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Main window setup
root = tk.Tk()
root.title("Retirement Savings Calculator")
root.state("zoomed")
root.configure(bg="navy")

# Menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Retirement Savings Calculator v1.0"))
menubar.add_cascade(label="Help", menu=help_menu)

# Header
header = tk.Label(root, text="Retirement Savings Calculator", font=("Arial", 20, "bold"), bg="navy", fg="white")
header.pack(fill="x", pady=10)

# Main content container
container = tk.Frame(root, bg="white")
container.pack(fill="both", expand=True, padx=20, pady=10)

# Left section: Input form
form_frame = tk.Frame(container, bg="white")
form_frame.pack(side="left", fill="y", padx=20, pady=20)

tk.Label(form_frame, text="Monthly Savings (₹):", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=5)
savings_entry = tk.Entry(form_frame, font=("Arial", 12))
savings_entry.pack(fill="x", pady=5)

tk.Label(form_frame, text="Expected Annual Return (%):", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=5)
return_entry = tk.Entry(form_frame, font=("Arial", 12))
return_entry.pack(fill="x", pady=5)

tk.Label(form_frame, text="Current Age:", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=5)
age_entry = tk.Entry(form_frame, font=("Arial", 12))
age_entry.pack(fill="x", pady=5)

tk.Label(form_frame, text="Retirement Age:", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=5)
retirement_age_entry = tk.Entry(form_frame, font=("Arial", 12))
retirement_age_entry.pack(fill="x", pady=5)

calculate_button = tk.Button(form_frame, text="Calculate Retirement Savings", font=("Arial", 12), bg="green", fg="white", command=calculate_retirement)
calculate_button.pack(pady=20)

# Right section: Graph
graph_frame = tk.Frame(container, bg="white")
graph_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Footer
footer = tk.Label(root, text="@2024 SIP Investment Tracker.All Rights Reserved", font=("Arial", 10), bg="navy", fg="white")
footer.pack(fill="x", pady=10)

# Run the application
root.mainloop()
