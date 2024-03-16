from tkinter import*
first=Tk()
first.title("My First Frame")
frame1=Frame(first,height=100,width=200,bg="Blue")
frame1.pack()

label1=Label(first,text="Enter your name")
label1.pack()

entry1=Entry(first)
entry1.pack()
label2=Label(first,text="Enter Your City")
label2.pack()
entry2=Entry(first)
entry2.pack()

first.mainloop()
print(label2)