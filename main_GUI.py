import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from main import generate_password

"""
Author: G@b
Date: 13/04/2021
"""


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Random Password Generator")
        self.master.tk.call(
            'wm',
            'iconphoto',
            self.master._w,
            tk.PhotoImage(file='password.png')
        )
        self.master.resizable(False, False)

        self.widgets()

    def widgets(self):
        # First Frame
        self.numbers = tk.IntVar()
        self.sepcials = tk.IntVar()

        option_frame = tk.LabelFrame(self.master, text="Options")
        self.scale_length = tk.Scale(option_frame,
                                     orient="horizontal",
                                     length=150,
                                     from_=4,
                                     to=30,
                                     width=12,
                                     label="Length of the password")

        add_numbers = tk.Checkbutton(option_frame, text="Add numbers", variable=self.numbers)
        add_specials = tk.Checkbutton(option_frame, text="Add specials characters", variable=self.sepcials)

        self.scale_length.grid(column=0, row=0, pady=10, sticky=tk.W)
        add_numbers.grid(column=0, row=1, sticky=tk.W)
        add_specials.grid(column=0, row=2, sticky=tk.W)

        option_frame.grid(column=0, row=0, pady=20)

        # Second Frame
        password_history_frame = tk.LabelFrame(self.master, text="Password History")
        self.password_history = ScrolledText(password_history_frame, state="disabled", height=9, width=30, spacing3=10)

        self.password_history.grid(padx=5, sticky=tk.N)
        password_history_frame.grid(column=1, row=0, padx=10)

        # Generate button
        generate = tk.Button(self.master, text="Generate password", command=self.get_attributes)
        generate.grid(column=1, row=1)

    def get_attributes(self):
        password_len = self.scale_length.get()
        add_numbers = bool(self.numbers.get())
        add_specials = bool(self.sepcials.get())

        password = generate_password(password_len, add_numbers, add_specials) + "\n"

        self.password_history.config(state="normal")
        self.password_history.insert(tk.INSERT, password)
        self.password_history.config(state="disabled")


if "__main__" == __name__:
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
