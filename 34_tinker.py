import tkinter as tk
root = tk.Tk()
lebel = tk.Label (root, text="label 1")
lebel.pack()

button = tk.Button(root, text="tombol 1")
button.pack()

checkbox = tk.Checkbutton(root, text= "centang 1")
checkbox.pack()
root.mainloop()