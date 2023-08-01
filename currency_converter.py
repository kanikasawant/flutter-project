import tkinter as tk
from tkinter import ttk

def open_currency_converter():
    # Read currency data from file
    with open('currencyData.txt') as f:
        lines = f.readlines()

    currencyDict = {}
    for line in lines:
        parsed = line.split("\t")
        currencyDict[parsed[0]] = parsed[1]

    # Create the currency converter window
    currency_window = tk.Tk()
    currency_window.title("Currency Converter")
    currency_window.configure(bg="darkseagreen3")

    # Create input widgets
    amount_label = ttk.Label(currency_window, text="Enter amount:",font=("Helvetica", 15))
    amount_label.pack(pady=10)

    amount_entry = ttk.Entry(currency_window)
    amount_entry.pack()

    currency_label = ttk.Label(currency_window, text="Enter the name of the currency you want to convert this amount to! ",font=("Helvetica", 10))
    currency_label.pack(pady=10)

    currency_listbox = tk.Listbox(currency_window)
    for item in currencyDict.keys():
        currency_listbox.insert(tk.END, item)
    currency_listbox.pack()

    result_label = ttk.Label(currency_window)
    result_label.pack()

    def convert_currency():
        selected_currency = currency_listbox.get(tk.ACTIVE)
        amount = float(amount_entry.get())
        converted_amount = amount * float(currencyDict[selected_currency])
        result_label.config(text=f"{amount} INR is equal to {converted_amount} {selected_currency}")

    convert_button = ttk.Button(currency_window, text="Convert", command=convert_currency)
    convert_button.pack()

    # Add an exit button
    exit_button = ttk.Button(currency_window, text="Exit", command=currency_window.destroy)
    exit_button.pack()

    currency_window.mainloop()

#conditinal block
if __name__== "__main__":
    open_currency_converter()