from tkinter import *
import math


# Button
def button_clicked():
    mile_entry = int(input.get())
    converted_value = mile_entry * 1.60934
    converted_number.config(text=round(converted_value))

# User screen
window = Tk()
window.title("Miles to Km Converter")

window.config(padx=20, pady=20)

# Entry
input = Entry(width=7)
input.grid(column=1, row=0)
print(input.get())

# Labels
# Miles
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=25)

# is Equal
equal_label = Label(text="is equal to", font=("Arial", 18, "normal"))
equal_label.grid(column=0, row=1)

# Converted number
converted_number = Label(text=0, font=("Arial", 24, "bold"))
converted_number.grid(column=1, row=1)
converted_number.config(padx=10, pady=25)

# KM Label
km_label = Label(text="KM", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)

# Button
calc_button = Button(text="Calculate", command=button_clicked, font=("Arial", 15, "bold"))
calc_button.grid(column=1, row=2)



window.mainloop()
