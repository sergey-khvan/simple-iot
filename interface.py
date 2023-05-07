from tkinter import *
from tkinter import ttk

def gen_response():
    pass


window = Tk()
window.title("Rehabilitation app")
window.config(padx=50, pady=50)

bg_label = Label(text="Torque calculator", font=("Arial", 30, "bold"))
bg_label.grid(row=0, column=1, columnspan=3, pady=(0,30),padx=(30,100))

name_label = Label(text="Patient name")
name_label.grid(row=1, column=0)
hip_angle_label = Label(text="Hip Angle")
hip_angle_label.grid(row=2, column=0)
knee_angle_label = Label(text="Knee Angle")
knee_angle_label.grid(row=3, column=0)
ankle_angle_label = Label(text="Ankle Angle")
ankle_angle_label.grid(row=4, column=0)

name_entry = Entry(width=20)
name_entry.focus()
name_entry.grid(row=1, column=1)
hip_angle_entry = Entry(width=20)
hip_angle_entry.insert(0, "10")
hip_angle_entry.grid(row=2, column=1)
knee_angle_entry = Entry(width=20)
knee_angle_entry.insert(0, "10")
knee_angle_entry.grid(row=3,column=1)
ankle_angle_entry = Entry(width=20)
ankle_angle_entry.insert(0, "10")
ankle_angle_entry.grid(row=4, column=1)


weight_label = Label(text="Weight")
weight_label.grid(row=1, column=2)
hip_torque_label = Label(text="Hip Angle")
hip_torque_label.grid(row=2, column=2)
knee_torque_label = Label(text="Knee Angle")
knee_torque_label.grid(row=3, column=2)
ankle_torque_label = Label(text="Ankle Angle")
ankle_torque_label.grid(row=4, column=2)


weight = IntVar()
weight_entry = ttk.Combobox(window, width = 18, textvariable = weight)
weight_entry['values'] = (72,68,46,52)
weight_entry.grid(row=1, column=3)
weight_entry.current(1)
hip_torque_entry = Entry(width=20)
hip_torque_entry.insert(0, "10")
hip_torque_entry.grid(row=2, column=3)
knee_torque_entry = Entry(width=20)
knee_torque_entry.insert(0, "10")
knee_torque_entry.grid(row=3,column=3)
ankle_torque_entry = Entry(width=20)
ankle_torque_entry.insert(0, "10")
ankle_torque_entry.grid(row=4, column=3)


gen_button = Button(text="Calculate Torque", command=gen_response)
gen_button.grid(row=5, column=1, columnspan=3, pady=(30,10),padx=(30,100))



weight = weight_entry.get()
hip_angle = hip_angle_entry.get()
knee_angle = knee_angle_entry.get()
ankle_angle = ankle_angle_entry.get()



window.mainloop()