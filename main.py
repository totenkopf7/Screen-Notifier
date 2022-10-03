import datetime
from tkinter import *
# from plyer import notification
from tkinter import messagebox
# import winsound
# # import subprocess
import pyautogui
import time



# def stop():
#     pyautogui.FAILSAFE = False
#     while True:
#         pyautogui.moveTo(x=768, y=1360, duration=60)
#         pyautogui.click(x=768, y=1360, clicks=1000000000000)
#         pyautogui.dragTo(789, 1359)
#         time.sleep(1)



# def set_notifier():
#     notification.notify(
#         title=f"{value}",
#         message="Don't screw your health!",
#         timeout=3
#     )


# def play_sound():
#     winsound.PlaySound('Alert.wav', winsound.SND_FILENAME)


# def autolock():
#     cmd = 'rundll32.exe user32.dll, LockWorkStation'
#     subprocess.call(cmd)


def space():
    space = Label(text="", bg="black")
    space.grid()


def forget(widget):
    widget.grid_forget()


def countdown(count):
    count_label["text"] = count
    conversion = datetime.timedelta(seconds=count_label["text"])
    converted_time = str(conversion)
    count_label["text"] = converted_time

    if count > 0:
        root.after(1000, countdown, count - 1)
    if count == 0:
        notify.config(text=f"* {value} *", background="#FFC300",
                      width=33, height=11, relief=FLAT, state=DISABLED, disabledforeground="black", wraplength=200,
                      justify=CENTER)
        root.state("zoomed")
        # forget(dev_label)
        dev_label.config(text="\n\n\n\n\nTake a bloody break!", bg="black", fg="#FFC300", font=("jost", 23, "bold"))
        forget(task_box)
        forget(task_label)
        forget(time_box)
        forget(time_label)
        forget(set_btn)
        forget(count_label)
        root.update()
        root.attributes("-fullscreen", True, "-topmost", True, "-disabled", True)
        # root.after(1000, stop)
        root.after(300000, refresh)
        # 300000



def start_countdown():
    if task_box.get() != "" and time_box.get() != "" and time_box.get().isdigit():
        countdown(60 * int(time_box.get()))
        global value
        value = task_box.get()
        task_box.delete(0, END)
        task_box.config(state="disabled")
        time_box.delete(0, END)
        time_box.config(state="disabled")
        set_btn.config(state="disabled")
        root.update()

    else:
        messagebox.showwarning(title="Error", message="Please set task and / or time")


def start_gui():
    global task_box
    global time_box
    global set_btn
    global count_label
    global root
    global notify
    global task_label
    global time_label
    global refresh_btn
    global dev_label

    root = Tk()
    root.title("Notifier")
    root.geometry("300x350")
    root.columnconfigure(0, weight=1)
    root.resizable(0, 0)
    root.config(bg=f"black")

    space()
    space()

    task_label = Label(root, text="Enter task", bg="black", fg="#FFC300", font=("jost", 9, "bold"))
    task_label.grid()

    EntryVar = StringVar()
    task_box = Entry(root, width=27, textvariable=EntryVar)
    task_box.grid()

    space()

    time_label = Label(root, text="Set time (minutes)", bg="black", fg="#FFC300", font=("jost", 9, "bold"))
    time_label.grid()

    EntryVar = StringVar()
    time_box = Entry(root, width=27, textvariable=EntryVar)
    time_box.grid()

    space()

    notify = Label(text="", bg="black")
    notify.grid()

    set_btn = Button(width=23, height=1, bg="black", fg="#FFC300", text="Start", font=("jost", 11, "bold"),
                     command=start_countdown)
    set_btn.grid()

    space()

    count_label = Label(root, text="", bg="black", fg="#FFC300")
    count_label.grid()

    space()

    dev_label = Label(root, text="Notifier developed by Totenkopf 💀", bg="black", fg="#FFC300", font=("jost", 11))
    dev_label.grid()

    # root.bind('<Return>', start_countdown)
    root.mainloop()


if __name__ == '__main__':
    def refresh():
        root.destroy()
        start_gui()

start_gui()
