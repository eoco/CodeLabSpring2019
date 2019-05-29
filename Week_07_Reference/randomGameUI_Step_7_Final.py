import random
import tkinter as tk

# Our function that is bound to the 'entry_button'; code gets called when clicked
def process_number():
	user_entry = entry_field.get()
	entry_field.delete(0, tk.END)
	global guess_count
	guess_count += 1
	if user_entry.isdigit():
		i = int(user_entry)
		if i == num:
			answer_text.set('Correct! You took %s guesses!' % guess_count)
		elif i < num:
			answer_text.set('Try Higher!')
		elif i > num:
			answer_text.set('Try Lower!')
	else:
		answer_text.set('That is not a number silly!')

# generate a random number when first run			
num = random.randint(1, 100)
guess_count#sets a counter to zero. We access this from our function by using the 'global' keyword
guess_count = 0

# Interface Elements
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

#Make sure you have this at the bottom!
tk.mainloop()