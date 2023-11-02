from tkinter import *
import random

animate = False 

def animate_background_color():
    if animate:
        colors = ["#FF5733", "#33FF57", "#5733FF", "#33B5E5", "#FFBB33"]
        random_color = random.choice(colors)
        window.configure(bg=random_color)
        window.after(2000, animate_background_color)
        
def change_window_background_color(button):
    border_color = button.cget('highlightbackground')
    window.configure(bg=border_color)

def buttonee5(button):
    window.configure(bg="#282a36")

def start_animation():
    global animate
    animate = True
    animate_button.config(state=DISABLED) 
    stop_button.config(state=NORMAL) 
    animate_background_color()

def stop_animation():
    global animate
    animate = False
    animate_button.config(state=NORMAL) 
    stop_button.config(state=DISABLED) 

window = Tk()
window.title("My Window")
window.geometry("300x600")
window.config(highlightbackground="black", highlightthickness=5, bd=0, bg="#282a36")

frame = Frame(window, bg="#282a36") 
frame.pack(side=TOP)

button1 = Button(window, text='click on me 1', width=36, height=1, highlightbackground='blue', highlightthickness=2, bd=0)
button1.pack(pady=4)
button1.config(command=lambda btn=button1: change_window_background_color(btn))

button2 = Button(window, text='click on me 2', width=36, height=1, highlightbackground='red', highlightthickness=2, bd=0)
button2.pack(pady=4)
button2.config(command=lambda btn=button2: change_window_background_color(btn))

button3 = Button(window, text='click on me 3', width=36, height=1, highlightbackground='yellow', highlightthickness=2, bd=0)
button3.pack(pady=4)
button3.config(command=lambda btn=button3: change_window_background_color(btn))

button4 = Button(window, text='click on me 4', width=36, height=1, highlightbackground='green', highlightthickness=2, bd=0)
button4.pack(pady=4)
button4.config(command=lambda btn=button4: change_window_background_color(btn))

button5 = Button(window, text='Reset', width=36, height=5, highlightbackground='black', highlightthickness=2, bd=0)
button5.pack(pady=20)
button5.config(command=lambda btn=button5: buttonee5(btn))

animate_button = Button(frame, text='Start', width=15, height=5, highlightbackground='black', highlightthickness=2, bd=0, command=start_animation)
animate_button.pack(side=LEFT, padx=5, pady=4)

stop_button = Button(frame, text='Stop', width=15, height=5, highlightbackground='black', highlightthickness=2, bd=0, command=stop_animation, state=DISABLED)
stop_button.pack(side=LEFT, padx=5, pady=0)

window.mainloop()