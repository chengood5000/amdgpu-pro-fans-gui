import subprocess
import check
from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("AMD GPU Fan Control")
window.geometry('350x200')

btnTemp = Button(window, text='Check state', command=lambda *args: check.temp())
btnTemp.grid(column=3, row=5)


def changevalue(value):
    global speed
    speed = str(value)
    subprocess.run(["sudo", "./amdgpu-pro-fans.sh", "-s" + speed])
    messagebox.showinfo('Speed', 'Fan speed successfully set to ' + speed + '%')
    # sudo ./amdgpu-pro-fans.sh -s 100


def testfnc():
    return subprocess.run(["watch", "-n", "2", "sensors"])


btn1 = Button(window, text='Set 25% ', command=lambda *args: changevalue(25))
btn1.grid(column=1, row=0)

btn2 = Button(window, text='Set 50% ', command=lambda *args: changevalue(50))
btn2.grid(column=2, row=0)

btn3 = Button(window, text='Set 75% ', command=lambda *args: changevalue(75))
btn3.grid(column=1, row=1)

btn4 = Button(window, text='Set 100%', command=lambda *args: changevalue(100))
btn4.grid(column=2, row=1)

slider = Scale (window, orient=HORIZONTAL)
slider.grid(column=3, row=0)

btnSlide = Button(window, text='Set', command=lambda *args: changevalue(slider.get()))
btnSlide.grid(column=3, row=1)


window.mainloop()
