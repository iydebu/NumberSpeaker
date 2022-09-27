from multiprocessing.connection import wait
from time import sleep
import pyttsx3
import tkinter as tk
from PIL import ImageTk, Image
numsinW = ["one ", "two ", "three ", "four ",
           "five ", "six ", "seven ", "eight ", "nine "]
numteenW = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ",
            "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
numtyW = ["twenty ", "thirty ", "forty ", "fifty ",
          "sixty ", "seventy ", "eighty ", "ninety "]
numW = ["hundred ", "thousand ", "million ",
        "billion ", "trillion ", "quadrillion "]
numN = ["100", "1000", "1000000", "1000000000",
        "1000000000000", "1000000000000000"]


def number_word(num, word=""):
    if (num == 0):
        return word
    elif (num < 10):
        word += numsinW[num-1]
        return word
    elif (num < 20):
        word += numteenW[num-10]
        return word
    elif (num < 100):
        if(num % 10 == 0):
            word += numtyW[int(num/10)-2]
            return word
        else:
             word += numtyW[int(num/10)-2]+numsinW[num % 10-1]
        return word
    for i in reversed(range(0, len(numN))):
        if (num >= int(numN[i])):
            word += number_word(int(num/int(numN[i])))
            word += numW[i]
            word += number_word(num % int(numN[i]))
            return word


def speak():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    try:
        num = int(inputtxt.get())
    except:
        log_label.config(text="Please enter a number!")
        engine.say("Please enter a valid number")
        engine.runAndWait()
        return
    log_label.config(text="Speeking...")
    answer = "{money} rupees is debited in your account".format(
        money=number_word(num))
    engine.say(answer)
    engine.runAndWait()


root = tk.Tk()
ico = ImageTk.PhotoImage(Image.open(
    r"C:\\Users\\debut\\OneDrive\\Documents\\Mega\\Programming\\python\\NumberSpeak\\coding.png").resize((200, 200)))
root.wm_iconphoto(False, ico)
root.resizable(0, 0)

root.title("Number to Word")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight()*0.1)
root.geometry('400x400+'+str(x)+'+'+str(y))
frame = tk.Frame(root, width=400, height=400, bg="#3d6466")
frame.grid(row=0, column=0)
frame.pack_propagate(False)

img = ImageTk.PhotoImage(Image.open(
    r"C:\\Users\\debut\\OneDrive\\Documents\\Mega\\Programming\\python\\NumberSpeak\\logo.png").resize((200, 200)))
logo = tk.Label(frame, image=img, bg="#3d6466")
logo.pack()

number_label = tk.Label(frame, text="Enter a number", bg="#3d6466",
                        fg="white", font=('Nunito', 20, "bold")).pack()

inputtxt = tk.Entry(frame, width=30, font=('Nunito', 16), justify='center')
inputtxt.pack()

speak_but = tk.Button(frame, text="Speak", bg="#28393a", fg="white", font=(
    'Nunito', 20, "bold"), command=speak).pack(pady=20)

log_label = tk.Label(frame, text="logs", bg="#3d6466",
                     fg="white", font=('Nunito', 10, "bold"))
log_label.pack()
root.mainloop()
