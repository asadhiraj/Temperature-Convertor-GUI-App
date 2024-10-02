import tkinter
import tkinter.messagebox
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.resizable(False,False)
        self.main_window.title('Temp. Converter')
        self.top_frame = tkinter.Frame(self.main_window, background='Pink')
        self.label1 = tkinter.Label(self.top_frame, text='Enter Temperature')
        self.label1.pack(side='top')
        self.myentry = tkinter.Entry(self.top_frame, borderwidth=4, foreground='Yellow', background='Black')
        self.myentry.pack(side='top')
        self.my_button = tkinter.Button(self.top_frame, text="Convert into Fahrenhit", foreground='Black',
                                        background='Yellow', command=self.feh)
        self.my_button.pack()
        self.my_button1 = tkinter.Button(self.top_frame, text="Convert into Celcius", foreground='Black',
                                        background='Yellow', command=self.celc)
        self.my_button1.pack()
        self.my_button = tkinter.Button(self.top_frame, text="Quit", foreground='White', background='Red', width='15',
                                        command=self.main_window.destroy)
        self.my_button.pack()
        self.label2 = tkinter.Label(self.top_frame, text='Temperature Converter', foreground='Red', borderwidth=5)
        self.label2.pack()
        self.label3 = tkinter.Label(self.top_frame, text="Developed by SP20-BSI-003", background='Pink', borderwidth=50,
                                    relief='sunken')
        self.label3.pack(padx=(1, 5), pady=(2, 10))
        self.top_frame.pack()
        self.my_button = tkinter.Button(self.top_frame, text="Return", command=self.top_frame.destroy)
        # self.my_button.pack()
        tkinter.mainloop()

    def feh(self):
        cel = float(self.myentry.get())
        fer = (cel * 1.8) + 32
        tkinter.messagebox.showinfo("Temp. Convert Result",
                                    str(cel) + " Degree Celcius = {:.2f}".format(fer) + ' Degree Fahrenheit ')
    def celc(self):
        fer = float(self.myentry.get())
        cel = (fer - 32) * 5/9
        tkinter.messagebox.showinfo("Temp. Convert Result",
                                    str(fer) + " Degree Fahrenheit = {:.2f}".format(cel) + ' Degree Celcius ')

my_gui = MyGUI()
