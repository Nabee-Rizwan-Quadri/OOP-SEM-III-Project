from tkinter import *
import random


root = Tk()
root.geometry("900x500+0+0")
root.title("Restaurant Management System")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)



#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System" )
lblinfo.grid(row=0,column=0)


#---------------Calculator------------------
text_Input=StringVar()
operator =""



def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set(0)
    Fries.set(0)
    Largefries.set(0)
    Burger.set(0)
    Filet.set(0)
    Subtotal.set(0)
    Total.set(0)
    Service_Charge.set(0)
    Drinks.set(0)
    Tax.set(0)
    cost.set(0)
    Cheese_burger.set(0)




#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.")
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4 ,justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,justify='right')
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT",command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("250x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), fg="white")
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=CENTER)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()

