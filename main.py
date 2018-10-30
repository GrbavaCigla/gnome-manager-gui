import tkinter as tk
import time
from tkinter import ttk
LARGE_FONT = ("Verdana", 14)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
Capital = ("Verdana",12)
packages=[]
truefalse=[]
commandsi=[]
commandsd=[]
commandse=[]
try:
    f=open('txt.txt')
    f=f.readlines()
    for i in f:
        l=i.split(',')
        i=l[0]
        packages.append(i.strip())
        i=l[1]
        truefalse.append(i.strip())
        i=l[2]
        commandsi.append(i.strip())
        i=l[3]
        commandsd.append(i.strip())
        i=l[4]
        commandse.append(i.strip())        
except:
    print('No file found.')

    
class FirstClass(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        ##tk.Tk.iconbitmap(self, default="imgtk.ico")
        tk.Tk.wm_title(self,"Manage gnome styles")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        tk.Tk.config(self)
        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

height=0
def clickmanager(option,j):
    print(commandsi[j])
    print(commandsd[j])
    print(commandse[j])
    print(option)
 
class StartPage(tk.Frame):
    def __init__(self,parent, controller):
        
        

        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Manage styles", font=LARGE_FONT)
        label.grid(columnspan=10,pady=30)
        label = ttk.Label(self, text="Name:", font=Capital)
        label.grid(row=1)
        
        frame=tk.Frame(self,height=100,width=100,borderwidth=2,relief='solid')
        frame.grid(column=1,row=1)
        
        canvas = tk.Canvas(frame, width=500, height=700-2, scrollregion=(0,0,3000,3000))
        
        scrollbar=ttk.Scrollbar(frame,orient='vertical',command=canvas.yview)
        scrollbar.grid(rowspan=100,column=5,row=0,sticky='ns')
        
        canvas.config(xscrollcommand=scrollbar.set)
        canvas.grid(row=0,column=0,pady=30,padx=30)
        canvas.create_window(20, 25, window=label, anchor='w')
        buttons1=[]
        buttons2=[]
        buttons3=[]
        for j,i in enumerate(packages):
            #UNFINISHED CODE
##            button1=ttk.Button(self,text="Enable",command=lambda:clickmanager('e',j))
##            button2=ttk.Button(self,text="Disable",command=lambda:clickmanager('d',j))
##            button3=ttk.Button(self,text="Install",command=lambda:clickmanager('i',j))
            buttons1.append(ttk.Button(self,text="Enable",command=lambda:clickmanager('e',len(buttons1)-1)))
            buttons2.append(ttk.Button(self,text="Disable",command=lambda:clickmanager('d',len(buttons2)-1)))
            buttons3.append(ttk.Button(self,text="Install",command=lambda:clickmanager('i',len(buttons3)-1)))
            
            label= ttk.Label(self, text=i, font=NORMAL_FONT)
            label.grid(row=j+2,column=0,padx=20)
            canvas.create_window(20, j*25, window=label, anchor='w')
            
            label= ttk.Label(self, text=truefalse[j], font=NORMAL_FONT)
            label.grid(row=j+2,column=1,padx=20)
            
            buttons1[j].grid(row=j+2,column=2)
            buttons2[j].grid(row=j+2,column=3)
            buttons3[j].grid(row=j+2,column=3)
            
            canvas.create_window(20+400, j*25, window=buttons1[j], anchor='w')
            canvas.create_window(20+325, j*25, window=buttons2[j], anchor='w')
            canvas.create_window(20+250, j*25, window=buttons3[j], anchor='w')
            canvas.create_window(20+125, j*25, window=label, anchor='w')
       
        global height
        
        
        
            
        




    
print(commandse,commandsd,commandsi)

app = FirstClass()
app.resizable(False, False)
##app.geometry("")
app.mainloop()
