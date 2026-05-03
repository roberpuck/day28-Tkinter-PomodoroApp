from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✔️'
countdown_running = False
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_pomodoro():
    global reps
    window.after_cancel(timer)
    timer_label.config(text='Timer')
    bg_canvas.itemconfig(timer_text,text='00:00')
    tick_label.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps +=1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8 == 0:
        timer_label.config(text='Break', fg=RED)
        start_countdown(long_break_sec)

    elif reps%2==0:
        timer_label.config(text='Break', fg=PINK)
        start_countdown(short_break_sec)
    else:
        timer_label.config(text='Work', fg=GREEN)
        start_countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def start_countdown(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    bg_canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count >0:
        timer = window.after(1000,start_countdown,count -1)
    else:
        start_timer()
        marks=''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        tick_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

#Main window
window = Tk()
window.title('Pomodoro')
window.config(background=YELLOW,padx=100,pady=50)


#Background
bg_image = PhotoImage(file='./tomato.png')
bg_canvas = Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
bg_canvas.create_image(100,112,image=bg_image)
timer_text = bg_canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,25,'bold'))
bg_canvas.grid(column=1,row=1)

#Countdown

timer_label = Label(text='Timer',fg=GREEN,font=(FONT_NAME,30,'bold'),bg=YELLOW)
timer_label.grid(column=1,row=0)

#Buttoms
start_button = Button(text='Start', command=start_timer, highlightthickness=0)
stop_button = Button(text='Reset', command=reset_pomodoro, highlightthickness=0)
start_button.grid(column=0, row=2)
stop_button.grid(column=2, row=2)

#Ticks
rounds_counter = 0
tick_label = Label(fg=GREEN,background=YELLOW)
tick_label.grid(column=1,row=3)



window.mainloop()