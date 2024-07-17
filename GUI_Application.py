   #create a simple GUI application
from tkinter import*
def button_click():
    print("Button clicked!")
root=Tk()
root.title("My GUI Application")
label=Label(root,text="HELLO WORLD.my name is Kewir Jewel and I have a twin brother called Kewir Jason.My nick name is called Linx.I am a software programmmer")
label.pack()
button=Button(root,text="Click me",command=button_click)
button.pack()
root.mainloop()