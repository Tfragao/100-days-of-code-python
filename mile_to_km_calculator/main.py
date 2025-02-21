import tkinter
from tkinter import Entry

MILES_TO_KM = 1.60934

def miles_to_km():
    result.config(text=f"{float(entry.get()) * MILES_TO_KM}")

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=800, height=400)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.grid(column=1, row=0)

mile_label = tkinter.Label(text="Miles", font=("Arial", 14, "bold"))
mile_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)

result = tkinter.Label(height=1, width=10)
result.grid(column=1, row=1)

kilometer_label = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
kilometer_label.grid(column=2, row=1)

calculate_btn = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2)

window.mainloop()