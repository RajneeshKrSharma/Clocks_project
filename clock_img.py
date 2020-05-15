from tkinter import *
from tkinter.ttk import *
import clock_home
from time import *
import winsound
from tkinter import filedialog
from sqlite3 import connect

class timer(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)

        self.geometry("320x200+1010+200")
        self.title("Timer_clock_with_notifying_alarm")
        self.style=Style()
        self.resizable(FALSE,FALSE)

        self.style.configure('Header1.TFrame',background="black")

        self.style.configure("Header1.TButton",font=("calibri",10),foreground="magenta")


        self.style.configure("Header.TLabel", background="black", foreground="white", font=("calibri", 10))


        self.header1_frame=Frame(self,style='Header1.TFrame')
        self.header1_frame.pack(side=TOP,fill=BOTH,expand=TRUE)

        self.img = PhotoImage(file="oldpiano.png")
        self.img_label = Label(self.header1_frame, image=self.img)
        self.img_label.place(relx=.5,rely=.5,anchor=CENTER )


        self.style.configure("Header1.TLabel", background="grey", foreground="white", font=("calibri",20))
        self.style.configure("Header2.TLabel", background="grey", foreground="black", font=("calibri", 20))
        self.style.configure("Header3.TLabel", background="black", foreground="white", font=("calibri",20))
        self.style.configure("Header4.TLabel", background="grey", foreground="aqua", font=("calibri",20))
        self.style.configure("Header5.TLabel", foreground="black" ,background="white", font=("calibri",20))
        self.style.configure("Header6.TLabel",foreground="black",font=("time new roman",12))
        self.style.configure("Header1.TButton",foreground="crimson",font=("time new roman ",10))
        self.style.configure("Header.TButton", foreground="navy", font=("calibri",10))

        self.label1=Label(self.header1_frame,style="Header2.TLabel",text="0")
        self.label1.place(relx=.35,rely=.0)

        self.label2=Label(self.header1_frame,style="Header2.TLabel",text=":")
        self.label2.place(relx=.434,rely=.0)


        self.label3=Label(self.header1_frame,style="Header2.TLabel",text="0")
        self.label3.place(relx=.48,rely=.0)

        self.label4=Label(self.header1_frame,style="Header2.TLabel",text=":")
        self.label4.place(relx=.57,rely=.0)

        self.label5=Label(self.header1_frame,style="Header2.TLabel",text="0")
        self.label5.place(relx=.62,rely=.0)

        self.label7=Label(self.header1_frame,style="Header3.TLabel",text="Timer ->")
        self.label7.place(relx=.027,rely=.0)

        self.label8 = Label(self.header1_frame, style="Header5.TLabel", text="SET ->")
        self.label8.place(relx=.027, rely=.73)

        self.entry1=Entry(self.header1_frame,width=2,font=("arial",15))
        self.entry1.place(relx=.289,rely=.73)
        self.label9 = Label(self.header1_frame, style="Header6.TLabel", text="Hr")
        self.label9.place(relx=.3,rely=.885)

        self.entry2 = Entry(self.header1_frame, width=2, font=("arial",15))
        self.entry2.place(relx=.39, rely=.73)

        self.label10 = Label(self.header1_frame, style="Header6.TLabel", text="Min")
        self.label10.place(relx=.39, rely=.885)


        self.entry3 = Entry(self.header1_frame, width=2, font=("arial",15))
        self.entry3.place(relx=.51, rely=.73)

        self.label11 = Label(self.header1_frame, style="Header6.TLabel", text="Sec")
        self.label11.place(relx=.51, rely=.885)

        self.button1=Button(self.header1_frame,text="Ok",style="Header1.TButton",
                           width=5 ,command=self.click_ok)
        self.button1.place(relx=.72,rely=.75)

        self.button_stop_music=Button(self.header1_frame,text="Stop Music",style="Header.TButton",width=10,command=self.stop_music)
        self.button_stop_music.place(relx=.72,rely=0.2)

        self.button_to_home=Button(self.header1_frame,text="Home",style="Header1.TButton",command=self.home)
        self.button_to_home.place(relx=0.027,rely=0.2)


        self.song=Button(self.header1_frame,text="Change Song",style="Header1.TButton",command=self.another_song)
        self.song.place(relx=0.4,rely=0.2)

    def another_song(self):
        con = connect("clock.db")
        cur = con.cursor()
        cur.execute("select * from clock")
        accounts = cur.fetchall()
        x = accounts[len(accounts) - 1]
        print("x[0] : ",x[0])
        songs =filedialog.askopenfilename(filetypes=(("Audio Files",".wav"),("All Files","*.*")))
        y=songs.split("/")
        print("y[3] :",y[3])
        cur.execute(" update clock set song ='{0}'".format(y[3]))
        con.commit()


    def home(self):
        self.destroy()
        clock_home.clock_home()

    def stop_music(self):
        winsound.PlaySound(None,winsound.SND_PURGE)

    def click_ok(self):

        j=1
        x=int(self.entry2.get())
        y=int(self.entry1.get())
        z=int(self.entry3.get())
        self.label1["text"]=y
        self.label3["text"]=x
        self.label5["text"]=z
        self.clock3=[]
        self.clock2=[]
        self.clock1=[]



        while j!=0:
         for i in range(z,0,-1):
            self.clock3.append(i)
         for i in range(len(self.clock3)):
            self.label5['text'] = self.clock3[i]
            self.update()
            sleep(1)

         if self.label3['text']!=0:

                    self.clock2.append(x)
                    for i in range(len(self.clock2)):
                         self.label3['text']=self.clock2[i]
                         self.label3['text']= self.label3['text']-1
                         self.clock2.remove(x)
                         x=x-1


         else:
            if self.label1["text"]==0 and self.label3["text"]==0:
                con = connect("clock.db")
                cur = con.cursor()
                cur.execute("select * from clock")
                accounts = cur.fetchall()
                x = accounts[len(accounts) - 1]
                print(x[0])
                print(type(x[0]))
                winsound.PlaySound(x[0],winsound.SND_FILENAME|winsound.SND_ASYNC)

            else:
              self.label3['text'] = 59
              x=59
              if self.label1["text"] != 0:
               self.label1["text"]=self.label1["text"]-1
              else:

                  con = connect("clock.db")
                  cur = con.cursor()
                  cur.execute("select * from clock")
                  accounts = cur.fetchall()
                  x = accounts[len(accounts) - 1]
                  print(x[0])
                  songs = filedialog.askopenfilename(filetypes=(("Audio Files",".wav"), ("All Files", "*.*")))
                  print(y)
                  y = songs.split("/")
                  print("y[3] :", y[3])
                  cur.execute(" update clock set song ='{0}'".format(y[3]))
                  con.commit()

         for i in range(z,0,-1):
                self.clock3.remove(i)
         z=59

