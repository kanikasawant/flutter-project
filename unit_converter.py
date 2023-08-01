import tkinter as tk
from tkinter import ttk
import subprocess 

def convert_distance():
    input_value = float(input_entry.get())
    input_unit = unit_combobox.get()
    output_unit = result_combobox.get()

    # rates of convertion
    conversion_rates = {
        "Meters": 1.0,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Inches": 39.3701
    }

    # converts input
    meters = input_value / conversion_rates[input_unit]

    # converts meter into output unit
    result = meters * conversion_rates[output_unit]

    result_label.config(text=f"{input_value} {input_unit} is equal to {result} {output_unit}")

def open_currency_converter():
    subprocess.run(["python", "currency_converter.py"])

def exit_program():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Unit Converter")
window.configure(bg="darkseagreen3")

# Create input widgets
input_label = ttk.Label(window, text="Enter value:",font=("Helvetica", 15))
input_label.pack(pady=15)

input_entry = ttk.Entry(window)
input_entry.pack()

unit_label = ttk.Label(window, text="From:",font=("Helvetica", 15))
unit_label.pack(pady=15)

unit_combobox = ttk.Combobox(window, values=["Meters", "Kilometers", "Miles", "Feet", "Inches"])
unit_combobox.pack()

result_label = ttk.Label(window, text="To:",font=("Helvetica", 15))
result_label.pack(pady=15)

result_combobox = ttk.Combobox(window, values=["Meters", "Kilometers", "Miles", "Feet", "Inches"])
result_combobox.pack()

convert_button = ttk.Button(window, text="Convert", command=convert_distance)
convert_button.pack(pady=10)

result_label = ttk.Label(window)
result_label.pack()

unit_converter_button = ttk.Button(window, text="Currency Converter", command=open_currency_converter)
unit_converter_button.pack(pady=10)

exit_button = ttk.Button(window, text="Exit", command=exit_program)
exit_button.pack()

# end
window.mainloop()