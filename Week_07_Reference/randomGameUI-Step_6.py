import random
import tkinter as tk

def process_number():
	user_entry = entry_field.get()
	if user_entry.isdigit():
		i = int(user_entry)
		if i == num:
			answer_text.set('Correct!')
		elif i < num:
			answer_text.set('Try Higher!')
		elif i > num:
			answer_text.set('Try Lower!')
	else:
		answer_text.set('That is not a number silly!')
			

num = random.randint(1, 100)
guess_count = 0

master = tk.Tk()
top_label = tk.Label(master, text="Enter a number between 1 and 100 below:")
top_label.pack()

entry_field = tk.Entry(master)
entry_field.pack()

entry_button = tk.Button(master, text="Enter", command = process_number)
entry_button.pack()

spacer_label = tk.Label(master, text=" ")
spacer_label.pack()

answer_text = tk.StringVar()
answer_text.set('Welcome to my game!')
answer_label = tk.Label(master, textvariable = answer_text)
answer_label.pack()




tk.mainloop()