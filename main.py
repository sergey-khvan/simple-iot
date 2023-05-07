import matlab.engine
import boto3
from aws import AWSclient
from tkinter import *
# from tkinter import ttk

SUB_TOPIC = "home/doctor"
PUB_TOPIC = "home/patient"
TOPIC_ARN = 'my-test-topic' # arn of the topic in AWS SNS


def calculate_t():    
    weight = int(weight_entry.get())
    hip_angle = float(hip_angle_entry.get())
    knee_angle = float(knee_angle_entry.get())
    ankle_angle = float(ankle_angle_entry.get())
    result = eng.calculateMS(weight, hip_angle, knee_angle, ankle_angle, nargout=1)
    print(result)
    hip_torque = round(result[0][0], 4)
    knee_torque = round(result[0][1], 4) 
    ankle_torque = round(result[0][2], 4)
    hip_torque_entry.delete(0, END)
    hip_torque_entry.insert(0, hip_torque)
    knee_torque_entry.delete(0, END)
    knee_torque_entry.insert(0, knee_torque)
    ankle_torque_entry.delete(0, END)
    ankle_torque_entry.insert(0, ankle_torque)
    muscles_st()
    pass


def muscles_st():
    keys = ["Hip Flexors","Hip Extensors", "Knee Flexors", "Knee Extensors","Ankle Dorsiflexors","Ankle Plantarflexors"]

    muscles_dict = {}
    muscles_list = []
    hip_angle = float(hip_angle_entry.get())
    knee_angle = float(knee_angle_entry.get())
    ankle_angle = float(ankle_angle_entry.get())
    patient_name = name_entry.get()
    muscles_dict.update({"Patient":patient_name})

    for value in keys:
        new_res = eng.muscleGroup(hip_angle, knee_angle, ankle_angle, value, nargout=1)
        muscles_list = new_res.split("\n")
        muscles_list.remove('')
        dict_v = {}
        for muscle in muscles_list:
            values = muscle.split(':')
            dict_v.update({values[0]:values[1]})
        muscles_dict.update({value: dict_v})    
    data_field.delete(1.0,END)
    format_output(muscles_dict)
    pass

def format_output(data_dict):
    for key, value in data_dict.items():
        if key == "Patient":
            data_field.insert(END,f"{key}: {value.title()}")
        else:
            data_field.insert(END,f"\n{key}")
            for keyin, valuein in value.items():
                data_field.insert(END,f"\n\t{keyin}: {valuein}")                
    pass
    

def send_email():
    #connection to aws
    aws_cl = AWSclient()
    email_data = data_field.get(1.0, END)
    aws_cl.aws_pub(topic=PUB_TOPIC, line=email_data)
    client.publish(TopicArn= TOPIC_ARN,
                          Message=email_data,
                          Subject=f'Rehabilitation of patient:{name_entry.get()}',)

def check_comments():
    aws_cl = AWSclient()
    aws_cl.aws_sub(topic=SUB_TOPIC)
    
# calculations
eng = matlab.engine.start_matlab()

# SNS client
client = boto3.client('sns')


# interface

window = Tk()
window.title("Rehabilitation app")
window.config(padx=50, pady=50)



bg_label = Label(text="Torque calculator", font=("Arial", 30, "bold"))
bg_label.grid(row=0, column=1, columnspan=3, pady=(0,30),padx=(30,100))

name_label = Label(text="Patient name")
name_label.grid(row=1, column=0)
hip_angle_label = Label(text="Hip Angle (deg)")
hip_angle_label.grid(row=2, column=0)
knee_angle_label = Label(text="Knee Angle (deg)")
knee_angle_label.grid(row=3, column=0)
ankle_angle_label = Label(text="Ankle Angle (deg)")
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


weight_label = Label(text="Weight (kg)")
weight_label.grid(row=1, column=2)
hip_torque_label = Label(text="Hip Torque (Nm)")
hip_torque_label.grid(row=2, column=2)
knee_torque_label = Label(text="Knee Torque (Nm)")
knee_torque_label.grid(row=3, column=2)
ankle_torque_label = Label(text="Ankle Torque (Nm)")
ankle_torque_label.grid(row=4, column=2)

# # Using combobox
# weight = IntVar()
# weight_entry = ttk.Combobox(window, width = 18, textvariable = weight)
# weight_entry['values'] = (80,72,64,56,48,40)
# weight_entry.current(1)

weight_entry = Entry(width=20)
weight_entry.insert(0,"80")
weight_entry.grid(row=1, column=3)
hip_torque_entry = Entry(width=20)
hip_torque_entry.insert(0, "10")
hip_torque_entry.grid(row=2, column=3)
knee_torque_entry = Entry(width=20)
knee_torque_entry.insert(0, "10")
knee_torque_entry.grid(row=3,column=3)
ankle_torque_entry = Entry(width=20)
ankle_torque_entry.insert(0, "10")
ankle_torque_entry.grid(row=4, column=3)


data_field = Text(height=10, width= 100)
data_field.grid(row=5, column=0, columnspan=4, pady=(30,10))  


calc_button = Button(text="Calculate Torque", height=3, width= 20, command=calculate_t)
calc_button.grid(row=6, column=0, columnspan=2, pady=(10))


email_button = Button(text="Send email to the doctor", height=3,width= 20,command=send_email)
email_button.grid(row=6, column=2, columnspan=2, pady=(10))

check_button = Button(text="Check doctor's intructions", height=3,width= 20,command=check_comments)
check_button.grid(row=7, column=1, columnspan=3,padx=(10,100))

window.mainloop()


