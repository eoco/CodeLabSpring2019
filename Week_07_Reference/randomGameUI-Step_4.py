import random
import tkinter as tk




num = random.randint(1, 100)

master = tk.Tk()
top_label = tk.Label(master, text="Enter a number between 1 and 100 below:")
top_label.pack()

entry_field = tk.Entry(master)
entry_field.pack()

entry_button = tk.Button(master, text="Enter")
entry_button.pack()

spacer_label = tk.Label(master, text=" ")
spacer_label.pack()

answer_text = tk.StringVar()
answer_text.set('Welcome to my game!')
answer_label = tk.Label(master, textvariable = answer_text)
answer_label.pack()




tk.mainloop()