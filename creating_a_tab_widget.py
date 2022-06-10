import tkinter as tk					
from tkinter import ttk

root = tk.Tk()
root.title("My First Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Tab Nº1')
tabControl.add(tab2, text ='Tab Nº2')
tabControl.add(tab3, text ='Tab Nº3')
tabControl.add(tab4, text ='Tab Nº4')
tabControl.pack(expand = 1, fill ="both")

ttk.Label(tab1, text ="Welcome to the world\
		\nof Python & Tkinter.").grid(column = 0,
                                                                               row = 0,
                                                                               padx = 30,
                                                                               pady = 30)

ttk.Label(tab2, text ="Now you learned\
		\nhow to create a tab.").grid(column = 0,
                                                                              row = 0,
                                                                              padx = 30,
                                                                              pady = 30)

ttk.Label(tab3, text ="You can look for\
		\nthis code for help.").grid(column = 0,
                                                                           row = 0,
                                                                           padx = 30,
                                                                           pady = 30)

ttk.Label(tab4, text ="Remember to keep improving\
		\nand happy coding!").grid(column = 0,
                                                                            row = 0,
                                                                            padx = 30,
                                                                            pady = 30)

root.mainloop()

#THIS CODE SHALL BE IMPROVED WHEN APPLIED TO PROGRAMMING
#IT SHOULD BE TAKEN AS AN EXAMPLE
