from tkinter import *
from shutil import copyfile
import os
from tkinter import ttk
from tkinter import messagebox

count=0
root=Tk()
root.title("Phone Database")

f1=Frame(root,bg="white")

a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()
a5=StringVar()
a6=StringVar()

def add() :
    f=open("db.txt",'a')
    a1 = e1.get()
    a2 = e2.get()
    a3 = e3.get()
    a4 = e4.get()
    a5 = e5.get()
    f.writelines(a1.ljust(10)+a2.ljust(10)+a3.ljust(10)+a4.ljust(10)+a5.ljust(10)+"\n")
    f.close()

def srch():
    fname = "db.txt"

    aid=input("Enter the Name of the Model of the phone you want to search:")
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            if words[0]==aid:
                print(line)

def updt():
    fname = "db.txt"

    aid=input("Enter the Name of the Model of the phone you want to search: ")
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            if words[0]==aid:
                print(line)
                asd=int(input("Enter the attribute you want to update 0: Name of the model     1: Internal Storage    2: Camera Quality   3: RAM  4: Price "))
                twitch = (input("Enter the new value : "))
                words[asd]=twitch
                line1 = ""
                for k in words:
                    line1 += k
                    line1 += "          "

                fname = "db.txt"
                f2=open("db1.txt",'w')

                with open(fname, 'r') as f:
                    for line in f:
                        words = line.split()
                        if words[0]!=aid:
                             f2.writelines(line)

                f2.close()

                f2=open("db1.txt",'a')
                f2.writelines(line1)
                f2.close()


def Del() :
    str = input("Enter the Model Name for which you want to delete the record.")
    with open("db.txt",'r+') as f :
        f1=f.readlines()
        f.seek(0)
        for line in f1:
            if str not in line :
                f.write(line)
        f.truncate()


def Exit() :
        Exit = messagebox.askyesno("Quit System", "Do you want to quit?")
        if Exit > 0:
            root.destroy()
            return


def first():
    f = open("db.txt")
    line = f.readline()
    print(line)
    f.close()



def last():
    f4=open("db.txt","r")
    lp=f4.readlines()
    try:
        leng=lp[len(lp)-1]
        print(leng)
        l12=leng.split()
        a1.set(l12[0])
        a2.set(l12[1])
        a3.set(l12[2])
        a4.set(l12[3])
        a5.set(l12[4])
    except IndexError:
        a6.set("No records")
    f4.close()


def next():
    global count
    f=open('open.txt','r')
    i=0
    while(i<=count):
        l=f.readline()
        i=i+1
    list1=l.split()
    if list1.__len__() != 0:
        a1.set(list1[0])
        a2.set(list1[1])
        a3.set(list1[2])
        a4.set(list1[3])
        a5.set(list1[4])
        count = count + 1
    f.close()

def prev():
    global count
    if count!=1:
        f=open('open.txt','r')
        i=0
        count = count - 1
        while(i<count):
            l=f.readline()
            i=i+1
        list1=l.split()
        a1.set(list1[0])
        a2.set(list1[1])
        a3.set(list1[2])
        a4.set(list1[3])
        a5.set(list1[4])
        f.close()


l0=Label(root,text=" ")
l0.grid(row=1,column=1)

l1=Label(root,text="Model Name",bg="white",fg="blue")
l1.grid(row=2,column=1)

l2=Label(root,text="Internal Storage",bg="white",fg="blue")
l2.grid(row=3,column=1)

l3=Label(root,text="Camera Quality",bg="white",fg="blue")
l3.grid(row=4,column=1)

l4=Label(root,text="RAM",bg="white",fg="blue")
l4.grid(row=5,column=1)

l5=Label(root,text="Price",bg="white",fg="blue")
l5.grid(row=6,column=1)

l6=Label(root,text=" ")
l6.grid(row=7, column=1)

e1=Entry(root)
e1.grid(row=2,column=3)

e2=Entry(root)
e2.grid(row=3,column=3)

e3=Entry(root)
e3.grid(row=4,column=3)

e4=Entry(root)
e4.grid(row=5,column=3)

e5=Entry(root)
e5.grid(row=6,column=3)



first=Button(root,text="First Record",bg="white",fg="blue", width=20,relief=RAISED,command=first)
first.grid(row=8,column=1)

next= Button(root, text="Previous", bg="white", fg="blue", width=20, relief=RAISED,command=next)
next.grid(row=8, column=2)

previous = Button(root, text="Next", bg="white", fg="blue", width=20, relief=RAISED,command=prev)
previous.grid(row=8, column=3)

last=Button(root,text="Last Record",bg="white",fg="blue", width=20,relief=RAISED,command=last)
last.grid(row=8,column=4)

save=Button(root,text="Add",bg="white",fg="blue", width=20,relief=RAISED,command=add)
save.grid(row=9,column=1)

exit=Button(root,text="Exit",bg="white",fg="blue",relief=RAISED,width=20,command=Exit)
exit.grid(row=9,column=2)

Search=Button(root,text="Search",bg="white",fg="blue",relief=RAISED, width=20,command=srch)
Search.grid(row=9,column=3)

Update=Button(root,text="Update",bg="white",fg="blue",relief=RAISED, width=20,command=updt)
Update.grid(row=9,column=4)

Del=Button(root,text="Delete",bg="white",fg="blue",relief=RAISED, width=20,command=Del)
Del.grid(row=10,column=2)


root.mainloop()
