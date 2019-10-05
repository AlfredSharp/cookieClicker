#Cookie Clicker in python by Alfred
from tkinter import *
from tkinter import ttk
import time

cookieCount = 0
cookiePerSec = 1
grandmaCount = 0
cookieTreeCount = 0

#add cookies per second
def add_cookie():
    global cookieCount
    global cookiePerSec
    cookieCount = cookieCount + cookiePerSec
    cookieNumber.set(cookieCount)
    root.after(1000, add_cookie)

def BtnPressed(*args):
    global cookieCount
    cookieCount = cookieCount + 1
    cookieNumber.set(cookieCount)
    print('+1')

def buyGrandma(*args):
    global cookieCount
    global cookiePerSec
    global grandmaCount
    if cookieCount >= 50:
        if grandmaCount < 20:
            print('You groomed a Grandma!')
            grandmaCount = grandmaCount + 1
            cookiePerSec = cookiePerSec + 2
            cookieCount = cookieCount - 50
            print("You now have " + str(grandmaCount) + " grandmas.")
        else:
            print("You have the maximum amount of grandmas!")
    else:
        print('You dont have enough cookies!')

def buyCookieTree(*args):
    global cookieCount
    global cookiePerSec
    global cookieTreeCount
    if cookieCount >= 200:
        if cookieTreeCount < 15:
            print('You planted a Cookie Tree!')
            cookieTreeCount = cookieTreeCount + 1
            cookiePerSec = cookiePerSec + 5
            cookieCount = cookieCount - 200
            print("You now have " + str(cookieTreeCount) + " cookie trees.")
        else:
            print("You have the maximum amount of cookie trees!")
    else:
        print('You dont have enough cookies!')

def shop(*args):
    print('You opened the shop')
    shop = Tk()
    shop.title("Shop")
    shop = ttk.Frame(shop, padding="1 12 12")
    shop.grid(column=0, row=0, sticky=(N, W, E, S))
    shop.columnconfigure(0, weight=1)
    shop.rowconfigure(0, weight=1)
    ttk.Label(shop, text='Grandma: 50 cookies').grid(column=1, row=1, sticky=(W, E))
    ttk.Button(shop, text="Buy a Grandma", command=buyGrandma).grid(column=2, row=1, sticky=(W, E))
    ttk.Label(shop, text='Cookie Tree: 200 cookies').grid(column=1, row=2, sticky=(W, E))
    ttk.Button(shop, text="Buy a Cookie Tree", command=buyCookieTree).grid(column=2, row=2, sticky=(W, E))

def grandmaInfo():
    grandmaInfo = Tk()
    grandmaProduction = grandmaCount * 2
    ttk.Label(grandmaInfo, text='You have ' + str(grandmaCount) + ' grandmas, \nproducing ' + str(grandmaProduction) + ' cps').grid(column=1, row=1, sticky=(W, E))
    ttk.Label(grandmaInfo, text='Grandmas cost 50 cookies. \nThey will produce 2 cookies per second. \nHowever, you can only get 20 grandmas.').grid(column=1, row=3, sticky=(W, E))
    
def cookieTreeInfo():
    cookieTreeInfo = Tk()
    cookieTreeProduction = cookieTreeCount * 2
    ttk.Label(cookieTreeInfo, text='You have ' + str(cookieTreeCount) + ' cookie trees, \nproducing ' + str(cookieTreeProduction) + ' cps').grid(column=1, row=1, sticky=(W, E))
    ttk.Label(cookieTreeInfo, text='Cookie Trees cost 200 cookies. \nThey will produce 5 cookies per second. \nHowever, you can only get 15 cookie trees.').grid(column=1, row=3, sticky=(W, E))

def info(*args):
    info = Tk()
    info.title("Info")
    info = ttk.Frame(info, padding="1 12 12")
    info.grid(column=0, row=0, sticky=(N, W, E, S))
    info.columnconfigure(0, weight=1)
    info.rowconfigure(0, weight=1)
    ttk.Label(info, text='Click on each upgrade to find out more information about them.').grid(column=1, row=1, sticky=(W, E))
    ttk.Button(info, text="Grandmas", command=grandmaInfo).grid(column=1, row=2)
    ttk.Button(info, text="Cookie Trees", command=cookieTreeInfo).grid(column=2, row=2)
    
    

#start tkinter frame
root = Tk()
root.title("Python Cookie Clicker")

mainframe = ttk.Frame(root, padding="1 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

cookieLbl = StringVar()
cookieNumber = StringVar()

#cookie clicker counter
ttk.Label(mainframe, textvariable=cookieLbl).grid(column=2, row=1, sticky=(W, E))
cookieLbl.set('Cookie count: ')
ttk.Label(mainframe, textvariable=cookieNumber).grid(column=3, row=1, sticky=(W, E))
cookieNumber.set('')

#indentations for asthetics
ttk.Label(mainframe).grid(column=1, row=2, sticky=(W, E))
ttk.Label(mainframe).grid(column=1, row=3, sticky=(W, E))
#buttons
ttk.Button(mainframe, text="Bake cookie", command=BtnPressed).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Shop", command=shop).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="Info", command=info).grid(column=3, row=4, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', BtnPressed)

root.after(0, add_cookie)
root.mainloop()
