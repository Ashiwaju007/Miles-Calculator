from tkinter import *

# Button for computation


def button_clicked():
    answer = int(data.get()) * 1.61
    answer_label.config(text=int(answer))


# windows initialization
window = Tk()
window.title("Miles to Kilometer App")
window.config(padx=20, pady=20)


# Accepts Input and Label for miles
data = Entry(width=5)
data.grid(column=1, row=0)
miles = Label(text="Miles")
miles.grid(column=2, row=0)

# Kilometers
is_equals_to = Label(text="Is equals to ")
is_equals_to.grid(column=0, row=1)
answer_label = Label(text="0")
answer_label.grid(column=1, row=1)
kilometers = Label(text="KM")
kilometers.grid(column=2, row=1)

# Calculate Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
