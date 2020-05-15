from tkinter import *
from tkinter.ttk import *
import clock_img
import clock
from time import *

class clock_home(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Clocks")
        self.state("zoomed")
        self.style=Style()

        self.style.configure("Header.TLabel",background="black")
        self.style.configure("Header2.TLabel", background="black",foreground="gold",font=("curlz mt",40))
        self.style.configure("Header.TFrame",background="Black")

        self.header_frame=Frame(self,style="Header.TFrame")
        self.header_frame.pack(side=TOP,fill=BOTH,expand=True)

        self.img=PhotoImage(file="a.png")
        self.label_img=Label(self.header_frame,image=self.img,style="Header.TLabel")
        self.label_img.place(relx=.2,rely=.2)


        self.timer_img=PhotoImage(file="timer.png")
        self.button_timer=Button(self.header_frame, style="Header.TLabel",image=self.timer_img,command=self.timer)
        self.button_timer.place(relx=.45,rely=.45)

        self.stopwatch_img = PhotoImage(file="stopwatch.png")
        self.button_stopwatch = Button(self.header_frame, style="Header.TLabel",image=self.stopwatch_img,command=self.stopwatch)
        self.button_stopwatch.place(relx=.45, rely=.6)



        canvas = Canvas(self.header_frame, width=1366, height=200, bg="black",
                        highlightthickness=0)
        canvas.place(relx=.0,rely=.0)

        self.label1 = Label(canvas,style="Header2.TLabel",text="- - : Choose Any : - -")
        self.label1.place(relx=0.2, rely=.05)
        l = canvas.create_window(100, 100, window=self.label1)

        xspeed =5
        yspeed = 0

        while True:
            canvas.move(l, xspeed, yspeed)
            pos = canvas.coords(l)
            print(pos)
            print(pos[0])
            if pos[0] >= 865:
                xspeed = -xspeed
            if pos[0] == 485:
                xspeed =5

            self.update()
            sleep(.1)

        
    def timer(self):
        self.destroy()
        clock_img.timer()
    def stopwatch(self):
        self.destroy()
        clock.clock()

if __name__=="__main__":

    x=clock_home()
    x.mainloop()

