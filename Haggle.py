import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Haggle user!", foreground="blue", 
	width = 25, height = 10)  
greeting.pack()
usernameframe = tk.Frame()
usernamelabel = tk.Label(master = usernameframe, text="Enter your username!")
usernamelabel.pack()
usernameentry = tk.Entry(master = usernameframe)
usernameentry.pack()
usernameframe.pack()
startacall = tk.Button(text="Start a call!", bg="#3DE100", width = 25, height = 2) 
startacall.pack()
window.mainloop()