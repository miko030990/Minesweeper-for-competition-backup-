import tkinter as tk
import sys
import os
def confirm():
    f = open('config.txt', 'w+')
    lines = f.readlines()
    for i in range(len(lines)):
        del lines[i-1]
    f.write(E1.get()+'\n'+E2.get()+'\n'+E3.get()+'\n'+E4.get())
    top.withdraw()
    os.startfile('main.bat')
    sys.exit(0)
if __name__ == "__main__":
    top = tk.Tk()
    top.title('config')
    top.geometry('250x150+200+100')
    L1 = tk.Label(master=top, text='x size:')
    L1.grid(row=0, column=0)
    L2 = tk.Label(master=top, text='y size:')
    L2.grid(row=1, column=0)
    L3 = tk.Label(master=top, text='seed:')
    L3.grid(row=2, column=0)
    L4 = tk.Label(master=top, text='mines:')
    L4.grid(row=3, column=0)
    E1 = tk.Entry(master=top, width=20, bg='white', bd=1)
    E1.grid(row=0, column=1)
    E2 = tk.Entry(master=top, width=20, bg='white', bd=1)
    E2.grid(row=1, column=1)
    E3 = tk.Entry(master=top, width=20, bg='white', bd=1)
    E3.grid(row=2, column=1)
    E4 = tk.Entry(master=top, width=20, bg='white', bd=1)
    E4.grid(row=3, column=1)
    B1 = tk.Button(master=top, bg='white', text='confirm', bd=1, command=confirm)
    B1.grid(row=4, column=1)
    top.mainloop()
