import ctypes
import random
import time
import tkinter as tk

#################################################
#  Program that prompts user every hour to answer a math question and locks the computer if incorrect 5 times or no answer
#  Good for kids to learn math.
#  Requires python3 and windows
#################################################

attempt=0

while 1:	
#if 1:
	#ask question before anything starts
	correct = False
	attempt=0

	a = random.randint(10,99)
	b = random.randint(10,99)
	c = random.randint(10,99)
	correct_answer = (a+b)-c
	
	window = tk.Tk()
	

	greeting = tk.Label(text="Answer this correctly or PC will be locked. You have 5 attempts and 5 minutes\n( "+str(a)+" + "+str(b)+" ) - "+str(c)+" = ?")
	window.after(300000,lambda:window.destroy())
	greeting.pack()
	entry = tk.Entry()

	def check_submit(event=None):
		global attempt
		global correct_answer
		global correct
		#these are for debugging
		#print(str(correct_answer))
		#print(str(attempt))
		answer = entry.get()
		if str(correct_answer) == answer:
			correct = True
		else:
			attempt+=1
		if attempt > 5 or correct:
			window.destroy()

	attempt=0
	
	entry.bind('<Return>', check_submit)
	entry.pack()

	submit = tk.Button(text="Submit",command=check_submit)

	submit.pack()
	window.mainloop()

	if not correct:
		answer_window = tk.Tk()
		label = tk.Label(text="Correct answer is "+str(correct_answer)+"\nThis will now lock in 5 seconds.")
		label.pack()
		answer_window.after(7000,lambda:answer_window.destroy())
		answer_window.mainloop()
		#lock windows
		ctypes.windll.user32.LockWorkStation()
	else:
		answer_window = tk.Tk()
		label = tk.Label(text="Thats corect! This window will close in 10 seconds.")
		label.pack()
		answer_window.after(10000,lambda:answer_window.destroy())
		answer_window.mainloop()


	#wait sleep for an hour
	time.sleep(3600)


