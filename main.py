from tkinter import *
from tkinter import simpledialog

window = Tk()
window.title("Text Disappearing Gui")
window.geometry("700x700")
window.minsize(height=600, width=600)

prompt_text = 'Turn on\ndisappearing button'

text_title = Label(text="Chat box", font=('Courier', 25, 'bold'), bg="light blue")
text_title.pack()
canvas = Frame(window, width=580, height=400, bg="#D9EEF3")
canvas.pack()

frame1 = Frame(window, width=30, height=15)
frame1.pack(side=LEFT)

frame2 = Frame(window, width=30, height=15)
frame2.pack(side=RIGHT)

text1label = Label(frame1, text="first user", font=('Courier', 9, 'bold'))
text2label = Label(frame2, text="second user", font=('Courier', 9, 'bold'))
text_input1 = Text(frame1, width=25, height=2)
text_input2 = Text(frame2, width=25, height=2)

text1label.grid(row=0, column=0)
text2label.grid(row=0, column=0)
text_input1.grid(row=0, column=1)
text_input2.grid(row=0, column=1)

disappear = False

answer = 0


def true_disappearing():
    global disappear
    global answer
    global prompt_text
    if prompt_text == 'Turn on\ndisappearing button':
        prompt_text = 'Turn off\ndisappearing button'
        disappearing_button.config(text=prompt_text)
        disappear = True
        answer = simpledialog.askfloat("Input", "Disappear after how many hours? input just numbers in hours",
                                       parent=window, minvalue=0, maxvalue=100)
        answer = int(answer * 60000)
    elif prompt_text == 'Turn off\ndisappearing button':
        prompt_text = 'Turn on\ndisappearing button'
        disappearing_button.config(text=prompt_text)
        disappear = False


def disappearing_text():
    class Label_text:

        def __init__(self, text, time):
            self.text = text
            self.canvass = Frame(master=canvas, bg="#D9EEF3")
            self.canvass.pack(side=TOP, fill=X, pady=5, padx=5)
            self.time = time

        def create_left_canvas_text(self, side):
            label = Message(master=self.canvass, text=self.text, bg="#A3E4D7",
                            font=('Courier', 9, 'bold'))
            label.pack(side=side)
            canvas.pack_propagate(0)

        def create_right_canvas_text(self, side):
            label = Message(master=self.canvass, text=self.text, bg="#A3E4D7",
                            font=('Courier', 9, 'bold'))
            label.pack(side=side)
            canvas.pack_propagate(0)

        def delete_text(self):
            self.canvass.destroy()

        def trigger_left_disappear(self):
            label = Message(master=self.canvass, text=self.text,
                            bg="#A3E4D7", font=('Courier', 9, 'bold'))
            label.pack(side=LEFT)
            canvas.pack_propagate(0)
            window.after(self.time, self.delete_text)

        def trigger_right_disappear(self):
            label = Message(master=self.canvass, text=self.text,
                            bg="#A3E4D7", font=('Courier', 9, 'bold'))
            label.pack(side=RIGHT)
            canvas.pack_propagate(0)
            window.after(self.time, self.delete_text)

    def send_button_response1():
        if len(text_input1.get(1.0, END)) > 1:
            label1 = Label_text(text_input1.get(1.0, END), answer)
            text_input1.delete(1.0, END)
            if disappear:
                label1.trigger_left_disappear()
            else:
                label1.create_left_canvas_text(LEFT)

    def send_button_response2():
        if len(text_input2.get(1.0, END)) > 1:
            label2 = Label_text(text_input2.get(1.0, END), answer)
            text_input2.delete(1.0, END)
            if disappear:
                label2.trigger_right_disappear()
            else:
                label2.create_right_canvas_text(RIGHT)

    send_button1 = Button(frame1, text="Send", width=5, height=1, font=('Arial', 10, 'bold'),
                          bg="light blue", command=send_button_response1)
    send_button1.grid(row=1, column=1, pady=3)

    send_button2 = Button(frame2, text="Send", width=5, height=1, font=('Arial', 10, 'bold'),
                          bg="light blue", command=send_button_response2)
    send_button2.grid(row=1, column=1, pady=3)


disappearing_text()

disappearing_button = Button(window, text=prompt_text, width=100, height=3,
                             font=('Arial', 8, 'bold'), bg="light blue", command=true_disappearing)
disappearing_button.pack(pady=2)

window.mainloop()
