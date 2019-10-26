import random
from tkinter import *
from tkinter import ttk
c=""

time=['7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00']
station=['mysore road','depanjali nagar','attiguppe','vijaynagar','hosahalli','magadi road','railway station','majestic','central college','vidhan soudha','cubbon park','mg road','trinity','halasuru','indrinagar','vivekanada road','baiyapanahalli']
station1=['mysore road','depanjali nagar','attiguppe','vijaynagar','hosahalli','magadi road','railway station','majestic','central college','vidhan soudha','cubbon park','mg road','trinity','halasuru','indrinagar','vivekanada road','baiyapanahalli']
def train_det():
     #newwin=Toplevel(window)
     Label(window, text="enter the departure station", bg="white", fg="black", font="none 12 bold").grid(row=2,
                                                                                                            column=1,
                                                                                                            sticky=W)
     Label(window, text="enter the destination station", bg="white", fg="black", font="none 12 bold").grid(row=3,
                                                                                                              column=1,
                                                                                                              sticky=W)
     textentry1=Entry(window,width=20,bg="white")
     textentry=Entry(window,width=20,bg="white")
     textentry1.grid(row=2,column=3,sticky=W)
     textentry.grid(row=3,column=3,sticky=W)
     button = Button(window, text="submit", width=6, command=train_det).grid(row=5, column=2, sticky=W)
     output = Text(window, width=75, height=6, wrap=WORD, background="white")
     Label(window, text="choose your time ", bg="white", fg="black", font="none 12 bold").grid(row=4, column=1,
                                                                                                  sticky=W)
     cb = ttk.Combobox(values=time, width=5).grid(column=2, row=4)#time drop down

    total =
    entry = random.randrange(30)
     #cb1 = ttk.Combobox(values=station, width=20).grid(column=3, row=2)#departure drop down
     #cb2 = ttk.Combobox(values=station1, width=20).grid(column=3, row=3)#destination drop

     #print("wrong entry")
     #else:
        #print("seats available for ",cb,"is",)
        #print("recoomended to take",)
def retieve():
    c=train_det.textentry.get()
    print(c)
'''def seats():
    seat=180
    ins=int(input("enter the no of getting in"))#this will actually done by sensors set up
    out=int(input("Enter the no of people getting out"))#this will actually done by sensors
    seat=seat+out-ins
    return seat
'''

def seats(total,entry):
    tmax = 120
    global total
    global entry
    out = int(input("Enter the no of people getting out"))  # this will actually done by sensors
    if(tmax<total-out+entry): #Fill the metro, Queue the remaining passengers
        temp = tmax - (total - out)
        entry = entry - temp
        total = tmax
    else:   #Train not full
        total = total + entry - out
        entry = 0

window=Tk()
window.title("metro train management system")#tittle
window.configure(background="white")
display=Label(text="signin page")
Label(window, text="user name ", bg="white", fg="black", font="none 12 bold").grid(row=2, column=1,sticky=W)
Label(window, text="password", bg="white", fg="black", font="none 12 bold").grid(row=3,column=1, sticky=W)
textentry=Entry(window,width=20,bg="white")
textentry.grid(row=2, column=3, sticky=W)
textentry1=Entry(window,width=20,bg="white",show="*")
textentry1.grid(row=3, column=3, sticky=W)
#textentry1.pack()
button = Button(window, text="submit", width=6,command=train_det).grid(row=5, column=2, sticky=W)
if(textentry.get()=="abcde" and textentry1.get()=="123"):
        command=train_det()
window.mainloop()