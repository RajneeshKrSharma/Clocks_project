from tkinter import *
from tkinter.ttk import *
from time import *
import clock_home

class clock(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)

        self.title("clock")
        self.state("zoomed")
        self.resizable(FALSE,FALSE)
        self.style=Style()

        self.style.configure("Header.TFrame",background='navy')
        self.header_frame = Frame(self,style='Header.TFrame')
        self.header_frame.pack(side=TOP,fill=BOTH,expand=TRUE)

        self.style.configure('Header.TLabel',foreground='cyan',background='navy',
        font=('Book antiqua',80))

        self.style.configure('Header1.TLabel', foreground='light blue', background='navy',
                             font=('Book antiqua', 85))

        self.style.configure('Header2.TLabel', foreground='white', background='navy',
                             font=('Book antiqua', 80))

        self.clocks=Label(self.header_frame,style='Header1.TLabel',text='CLOCK')
        self.clocks.grid(pady=10)

        self.clock_label1 = Label(self.header_frame, style='Header2.TLabel',text=          '0')
        self.clock_label1.grid(row=1,column=0, pady=10)

        self.clock_label_intermidiate1 = Label(self.header_frame,text=':Hr  ', style='Header.TLabel')
        self.clock_label_intermidiate1.grid(row=1, column=1, pady=10)


        self.clock_label2=Label(self.header_frame,style='Header2.TLabel',text=' 0 ')
        self.clock_label2.grid(row=1,column=2,pady=10)

        self.clock_label_intermidiate1 = Label(self.header_frame, text=': Min  ', style='Header.TLabel')
        self.clock_label_intermidiate1.grid(row=1, column=3, pady=10)


        self.clock_label3=Label(self.header_frame,style='Header2.TLabel',text='0')
        self.clock_label3.grid(row=1,column=4,pady=10)

        self.clock_label_intermidiate2 = Label(self.header_frame,text=': Sec  ',style='Header.TLabel')
        self.clock_label_intermidiate2.grid(row=1, column=5, pady=10)

        self.style.configure('HeaderN.TLabel',background='navy',foreground='gold',font=('gigi',20))

        self.creater_label=Label(self.header_frame,text='Created By . . .',style='HeaderN.TLabel')
        self.creater_label.place(relx=.8,rely=.8)

        self.creater_label=Label(self.header_frame,text=' Rajneesh ',style='HeaderN.TLabel')
        self.creater_label.place(relx=.85,rely=.9)

        self.style.configure("Header.TButton",font=("gigi",20),foreground="red",background="black")
        self.button=Button(self.header_frame,text="Home",style="Header.TButton",
                           command=self.home)
        self.button.place(relx=.5,rely=.85)

        j=1
        x=0
        y=0
        self.clock3=[]
        self.clock2=[]
        self.clock1=[]

        while j!=0:
         for i in range(0,60):
            self.clock3.append(i)
         for i in range(len(self.clock3)):
            self.clock_label3['text']=self.clock3[i]
            self.update()
            sleep(1)

         if (x != -1):
              if(x!=60):
                x = x + 1
                self.clock2.append(x)
                for i in range(len(self.clock2)):
                    self.clock_label2['text']=self.clock2[i]
                self.clock2.remove(x)
              else:
                  x = 0
                  self.clock2.append(x)
                  for i in range(len(self.clock2)):
                      self.clock_label2['text']=self.clock2[i]
                  self.clock2.remove(x)


                  if(y!=60):
                       y=y+1
                       self.clock1.append(y)
                       for i in range(len(self.clock1)):
                           self.clock_label1['text']= self.clock1[i]
                       self.clock1.remove(y)

                  else:
                      y=0
                      self.clock1.append(y)
                      for i in range(len(self.clock1)):
                          self.clock_label1['text']= self.clock1[i]
                      self.clock1.remove(y)

         for i in range(0,60):
             self.clock3.remove(i)


    def home(self):
        self.destroy()
        clock_home.clock_home()