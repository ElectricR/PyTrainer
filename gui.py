from engine import Engine
import tkinter as tk

class GUI:

    def __init__(self):
        self.engine = Engine()
        self.window = tk.Tk()
        self.window.bind('<Escape>', self.close)
        self.window.geometry('900x500')
        self.window.title('Radicals')

        self.reset_button = tk.Button(self.window, text='Reset', command=self.reset)
        self.reset_button.pack(side='left', anchor='n')

        self.quit_button = tk.Button(self.window, text='Quit', command=self.close)
        self.quit_button.pack(side='right', anchor='n')

        self.character = tk.StringVar()
        self.character_label = tk.Label(self.window, textvariable=self.character, font=('Arial', '200'))
        self.character_label.pack(side='top')

        self.dialog_label = tk.Label(self.window, text='What\'s this?')
        self.dialog_label.pack(side='top')

        self.entry = tk.Entry(self.window)
        self.entry.pack(side='top')
        self.entry.focus()

        self.check_button = tk.Button(self.window, text='Check', command=self.check)
        self.check_button.pack(side='top', pady=32)

        self.wrong_answer_label = tk.Label(self.window, text='Wrong answer!')

        self.correct_answer_label = tk.Label(self.window, text='Correct!')

        self.update_character()
        self.window.mainloop()

    def close(self, event=None):
        self.window.destroy()

    def update_character(self):
        self.character.set(self.engine.get_lesson()[1])

    def check(self):
        self.wrong_answer_label.pack_forget()
        self.correct_answer_label.pack_forget()
        if self.engine.check(self.entry.get()):
            self.character.set(self.engine.get_lesson()[1])
            self.correct_answer_label.pack(side='top')
            self.entry.delete(0, 'end')
        else:
            self.wrong_answer_label.pack(side='top')

    def reset(self):
        self.entry.delete(0, 'end')
        self.wrong_answer_label.pack_forget()
        self.correct_answer_label.pack_forget()
        self.engine.reset()
        self.character.set(self.engine.get_lesson()[1])

