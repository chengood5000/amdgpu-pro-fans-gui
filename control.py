import subprocess
from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("AMD Fan Control")
window.geometry('350x200')


def changevalue(value):
    global speed
    speed = str(value)
    print(speed)
    subprocess.run(["sudo", "./amdgpu-pro-fans.sh", "-s" + speed])
    messagebox.showinfo('Speed', 'Fan speed successfully set to' + speed + '%')
    # sudo ./amdgpu-pro-fans.sh -s 100


btn1 = Button(window, text='Set 25% ', command=lambda *args: changevalue(25))
btn1.grid(column=1, row=0)

btn2 = Button(window, text='Set 50% ', command=lambda *args: changevalue(50))
btn2.grid(column=2, row=0)

btn3 = Button(window, text='Set 75% ', command=lambda *args: changevalue(75))
btn3.grid(column=1, row=1)

btn4 = Button(window, text='Set 100%', command=lambda *args: changevalue(100))
btn4.grid(column=2, row=1)

spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=3, row=1)

slider = Scale (window, orient=HORIZONTAL)
slider.grid(column=3, row=0)
s_val = slider.get()
#Spinbox.setvar(s_val)

window.mainloop()
