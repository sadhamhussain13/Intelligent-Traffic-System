from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Lane Traffic Prediction')
root.geometry('800x680')
root.config(bg='white')
root.resizable(False, False)

red_sign = PhotoImage(file='Images/red.png')
yellow_sign = PhotoImage(file='Images/yellow.png')
green_sign = PhotoImage(file='Images/green.png')

def traffic_analysis():
    messagebox.showinfo("Notification", "Traffic Analysis has been initiated ..")
    time_1.config(text='On Time = 20')
    time_2.config(text='On Time = 35')
    time_3.config(text='On Time = 25')
    time_4.config(text='On Time = 15')

def Lane_one():
    time_1.config(text='On Time = 50')
    flow_1.config(text='Traffic Flow = 54')
    signal_1.config(image=green_sign)
    time_2.config(text='On Time = 10')
    flow_1.config(text='Traffic Flow = 23')
    signal_2.config(image=yellow_sign)
    time_3.config(text='On Time = 0')
    signal_3.config(image=red_sign)
    flow_3.config(text='Traffic Flow = 5')
    time_4.config(text='On Time = 10')
    signal_4.config(image=red_sign)
    flow_4.config(text='Traffic Flow = 2')

def Lane_two():
    time_1.config(text='On Time = 20')
    signal_1.config(image=yellow_sign)
    flow_1.config(text='Traffic Flow = 32')
    time_2.config(text='On Time = 0')
    signal_2.config(image=red_sign)
    flow_2.config(text='Traffic Flow = 21')
    time_3.config(text='On Time = 65')
    signal_3.config(image=green_sign)
    flow_3.config(text='Traffic Flow = 0')
    time_4.config(text='On Time = 21')
    signal_4.config(image=red_sign)
    flow_4.config(text='Traffic Flow = 13')

def Lane_three():
    time_1.config(text='On Time = 70')
    signal_1.config(image=green_sign)
    flow_1.config(text='Traffic Flow = 50')
    time_2.config(text='On Time = 10')
    signal_2.config(image=red_sign)
    flow_2.config(text='Traffic Flow = 5')
    time_3.config(text='On Time = 3')
    signal_3.config(image=yellow_sign)
    flow_3.config(text='Traffic Flow = 23')
    time_4.config(text='On Time = 2')
    signal_4.config(image=red_sign)
    flow_4.config(text='Traffic Flow = 11')

def Lane_four():
    time_1.config(text='On Time = 0')
    signal_1.config(image=red_sign)
    flow_1.config(text='Traffic Flow = 37')
    time_2.config(text='On Time = 2')
    signal_2.config(image=red_sign)
    flow_2.config(text='Traffic Flow = 29')
    time_3.config(text='On Time = 32')
    signal_3.config(image=yellow_sign)
    flow_3.config(text='Traffic Flow = 54')
    time_4.config(text='On Time = 100')
    signal_4.config(image=green_sign)
    flow_1.config(text='Traffic Flow = 12')

project_lbl = Label(root, text='Intelligent Traffic Prediction System', font=('Microsoft UI', 24, 'bold'))
project_lbl.config(fg='orange', bg='white')
project_lbl.place(x=121, y=35)

main_frame = Frame(root, width=650, height=500, bg='white')
main_frame.place(x=80, y=90)

button_1 = Button(main_frame, text='Lane 1', font=('Microsoft UI', 10), width=30, height=1)
button_1.config(command=Lane_one)
button_1.place(x=30, y=40)

signal_1 = Label(main_frame, image=red_sign, bg='white')
signal_1.place(x=30, y=70)

width_1 = Label(main_frame, text='Width of Lane 1 = 10.0', font=('Microsoft UI', 12), bg='white')
width_1.place(x=115, y=90)

vehicle_1 = Label(main_frame, text='Number of Vehicles = 20', font=('Microsoft UI', 12), bg='white')
vehicle_1.place(x=113, y=120)

flow_1 = Label(main_frame, text='Traffic Flow = 0', font=('Microsoft UI', 12), bg='white')
flow_1.place(x=113, y=150)

saturation_1 = Label(main_frame, text='Saturation Flow = 100', font=('Microsoft UI', 12), bg='white')
saturation_1.place(x=113, y=180)

time_1 = Label(main_frame, text='On Time = 30', font=('Microsoft UI', 12), bg='white')
time_1.place(x=113, y=210)

button_2 = Button(main_frame, text='Lane 2', font=('Microsoft UI', 10), width=30, height=1)
button_2.config(command=Lane_two)
button_2.place(x=360, y=40)

signal_2 = Label(main_frame, image=green_sign, bg='white', font=('Microsoft UI', 12))
signal_2.place(x=360, y=70)

width_2 = Label(main_frame, text='Width of Lane 2 = 10.0', font=('Microsoft UI', 12), bg='white')
width_2.place(x=445, y=90)

vehicle_2 = Label(main_frame, text='Number of Vehicles = 40', font=('Microsoft UI', 12), bg='white')
vehicle_2.place(x=443, y=120)

flow_2 = Label(main_frame, text='Traffic Flow = 0', font=('Microsoft UI', 12), bg='white')
flow_2.place(x=443, y=150)

saturation_2 = Label(main_frame, text='Saturation Flow = 100', font=('Microsoft UI', 12), bg='white')
saturation_2.place(x=443, y=180)

time_2 = Label(main_frame, text='On Time = 30', font=('Microsoft UI', 12), bg='white')
time_2.place(x=443, y=210)

button_3 = Button(main_frame, text='Lane 3', font=('Microsoft UI', 10), width=30, height=1)
button_3.config(command=Lane_three)
button_3.place(x=30, y=280)

signal_3 = Label(main_frame, image=yellow_sign, bg='white')
signal_3.place(x=30, y=310)

width_3 = Label(main_frame, text='Width of Lane 3 = 10.0', font=('Microsoft UI', 12), bg='white')
width_3.place(x=115, y=330)

vehicle_3 = Label(main_frame, text='Number of Vehicles = 30', font=('Microsoft UI', 12), bg='white')
vehicle_3.place(x=113, y=360)

flow_3 = Label(main_frame, text='Traffic Flow = 0', font=('Microsoft UI', 12), bg='white')
flow_3.place(x=113, y=390)

saturation_3 = Label(main_frame, text='Saturation Flow = 100', font=('Microsoft UI', 12), bg='white')
saturation_3.place(x=113, y=420)

time_3 = Label(main_frame, text='On Time = 30', font=('Microsoft UI', 12), bg='white')
time_3.place(x=113, y=450)

button_4 = Button(main_frame, text='Lane 4', font=('Microsoft UI', 10), width=30, height=1)
button_4.config(command=Lane_four)
button_4.place(x=360, y=280)

signal_4 = Label(main_frame, image=red_sign, bg='white')
signal_4.place(x=360, y=310)

width_4 = Label(main_frame, text='Width of Lane 4 = 10.0', font=('Microsoft UI', 12), bg='white')
width_4.place(x=445, y=330)

vehicle_4 = Label(main_frame, text='Number of Vehicles = 10', font=('Microsoft UI', 12), bg='white')
vehicle_4.place(x=443, y=360)

flow_4 = Label(main_frame, text='Traffic Flow = 0', font=('Microsoft UI', 12), bg='white')
flow_4.place(x=443, y=390)

saturation_4 = Label(main_frame, text='Saturation Flow = 100', font=('Microsoft UI', 12), bg='white')
saturation_4.place(x=443, y=420)

time_4 = Label(main_frame, text='On Time = 30', font=('Microsoft UI', 12), bg='white')
time_4.place(x=443, y=450)

start_btn = Button(root, text='Start', font=('Microsoft UI', 12), width=25)
start_btn.config(command=traffic_analysis)
start_btn.place(x=120, y=600)

back_btn = Button(root, text='Stop', font=('Microsoft UI', 12), width=25)
back_btn.place(x=450, y=600)

root.mainloop()
