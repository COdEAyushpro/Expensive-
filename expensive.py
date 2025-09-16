import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"


if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    description = desc_entry.get()

    if not category or not amount:
        messagebox.showwarning("Input Error", "Category and Amount are required!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    messagebox.showinfo("Success", "Expense added successfully!")
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)


def view_expenses():
    for row in tree.get_children():
        tree.delete(row)

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            tree.insert("", tk.END, values=row)


def summary_report():
    total = 0
    category_totals = {}

    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["Amount"])
            total += amount
            category = row["Category"]
            category_totals[category] = category_totals.get(category, 0) + amount

    report = f"Total Spent: ₹{total:.2f}\n\nCategory-wise breakdown:\n"
    for category, amt in category_totals.items():
        report += f"- {category}: ₹{amt:.2f}\n"

    messagebox.showinfo("Expense Summary", report)



root = tk.Tk()
root.title("Expense Tracker")
root.geometry("700x500")


frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Category:").grid(row=0, column=0, padx=5, pady=5)
category_entry = tk.Entry(frame)
category_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Description:").grid(row=2, column=0, padx=5, pady=5)
desc_entry = tk.Entry(frame)
desc_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(frame, text="Add Expense", command=add_expense).grid(row=3, column=0, columnspan=2, pady=10)


tree = ttk.Treeview(root, columns=("Date", "Category", "Amount", "Description"), show="headings", height=10)
tree.pack(pady=10)

for col in ("Date", "Category", "Amount", "Description"):
    tree.heading(col, text=col)
    tree.column(col, width=150)


btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="View Expenses", command=view_expenses, width=20).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Summary Report", command=summary_report, width=20).grid(row=0, column=1, padx=10)

root.mainloop()
