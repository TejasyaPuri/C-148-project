from tkinter import *
import random

root=Tk()
root.title("Picnic Bag List")
root.geometry("400x400")

list_of_items = Label(root)
random_number_list = Label(root)

random_list = itemlist(root)

def randomitemlist():
    list_of_items["text"] = " List of items : " + str(randomlist)
    randomlist = random.sample(range(0, 7),1)
    random_number_list["text"] = " Put item into the bag : " + str(randomlist)
    
btn = Button(root, text="Which Item To Put inside the bag?", command = randomlist, bg = "yellow", fg="white")
btn.place(relx = 0.5, rely = 0.4, anchor=CENTER)

list_of_items.place(relx=0.5, rely=0.5, anchor=CENTER)
random_number_list(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
