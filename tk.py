from tkinter import *
window= Tk()
window.title("Sample window")
window.geometry("300x300")
greeting= Label(text="hi!",fg= 'white',bg= 'black')
button= Button(text= "Click me!",fg= 'black',bg= 'black')
entry= Entry(fg= "red",bg= "blue",width= 50)
greeting.pack()
button.pack()
entry.pack()
frame= Frame(master= window,relief= RAISED, borderwidth= 5)
frame.pack()
label= Label(master= frame, text= "sample")
label.pack()
window.mainloop()