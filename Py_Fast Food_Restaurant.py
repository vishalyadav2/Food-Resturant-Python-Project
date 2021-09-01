
##        varTotal.set(iTotalq)
##        cChange = (iChange - (iCost + iTax))
##        cChangeq = "$", str('%.2f'%(cChange))
##        varChange.set(cChangeq)
##    elif(var22.get() == "Master Card" or "Visa Card" or "Debit Card"):
##        varPayment.set("")
##        iCost = (iTotal1 + iTotal2 +iTotal3 + iTotal4 + iTotal5)
##        iTax = (icost * 3.4)/100
##        iTaxq="$", str('%.2f'%(iTax))
##        varTax.set(iTaxq)
##        iCostq="$", str('%.2f'%(iCost))
##        varSubTotal.set(iCostq)
##        iTotalq="$", str('%.2f'%((iCost + iTax)))
##        varTotal.set(iTotalq)
##        varChange.set("")
##        
        
        
        
        


from tkinter import*
import messagebox
import random
import time;
import datetime;
from tkinter import Tk, StringVar, ttk

root=Tk()
root.geometry("1350x750+0+0")
root.title("Fast Food Restaurant")

Tops = Frame (root, width = 350 , height=100, bd= 6, relief="raise")
Tops.pack(side=TOP) 
lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="\tFast Food Restaurant\t\t\t")
lblTitle.grid(row =0, column=0)

BottomMainFrame = Frame (root, width = 1350 , height=650, bd= 6, relief="raise")
BottomMainFrame.pack(side=BOTTOM) 

f1 = Frame (BottomMainFrame, width = 450 , height=650, bd= 2, relief="raise")
f1.pack(side=LEFT)
f2 = Frame (BottomMainFrame, width = 450 , height=650, bd= 2, relief="raise")
f2.pack(side=LEFT)
f2TOP = Frame (f2, width = 450 , height=350, bd= 2, relief="raise")
f2TOP.pack(side=TOP)
f2BOTTOM = Frame (f2, width = 450 , height=300, bd= 1, relief="raise")
f2BOTTOM.pack(side=BOTTOM) 

f3 = Frame (BottomMainFrame, width = 450 , height=650, bd= 2, relief="raise")
f3.pack(side=RIGHT) 


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)

varSamosa =StringVar()
varSandwich =StringVar()
varHamburger =StringVar()
varVadapav =StringVar()
varNoodle =StringVar()
varFrankie =StringVar()
varNoodleFrankie =StringVar()
varCheeseFrankie =StringVar()
varVegFrankie =StringVar()

varHashBrown =StringVar()
varToastedBagel =StringVar()
varPancake =StringVar()
varPineappleStick =StringVar()
varChocolateIcecream =StringVar()

varTea= StringVar()
varCola= StringVar()
varCoffee= StringVar()
varOrange= StringVar()
varColdCoffee= StringVar()
varVanillaShake= StringVar()
varVanillaCone= StringVar()
varStrawberryShake= StringVar()


varVAT= StringVar()
varTax= StringVar()
varTotal= StringVar()
varChange= StringVar()
varSubTotal= StringVar()


varSamosa.set("0")
varSandwich.set("0")
varHamburger.set("0")
varVadapav.set("0")
varNoodle.set("0")
varFrankie.set("0")
varNoodleFrankie.set("0")
varCheeseFrankie.set("0")
varVegFrankie.set("0")

varHashBrown.set("0")
varToastedBagel.set("0")
varPancake.set("0")
varPineappleStick.set("0")
varChocolateIcecream.set("0")

varTea.set("0")
varCola.set("0")
varCoffee.set("0")
varOrange.set("0")
varColdCoffee.set("0")
varVanillaShake.set("0")
varVanillaCone.set("0")
varStrawberryShake.set("0")

varVAT.set("0")
varTax.set("0")
varTotal.set("0")
varChange.set("0")
varSubTotal.set("0")












def iExit():
    qExit= messagebox.askyesno("Fast Food","Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return


def Reset():
    varSamosa.set("0")
    varSandwich.set("0")
    varHamburger.set("0")
    varVadapav.set("0")
    varNoodle.set("0")
    varFrankie.set("0")
    varNoodleFrankie.set("0")
    varCheeseFrankie.set("0")
    varVegFrankie.set("0")

    varHashBrown.set("0")
    varToastedBagel.set("0")
    varPancake.set("0")
    varPineappleStick.set("0")
    varChocolateIcecream.set("0")

    varTea.set("0")
    varCola.set("0")
    varCoffee.set("0")
    varOrange.set("0")
    varColdCoffee.set("0")
    varVanillaShake.set("0")
    varVanillaCone.set("0")
    varStrawberryShake.set("0")

    varVAT.set("0")
    varTax.set("0")
    varTotal.set("0")
    varChange.set("0")
    varSubTotal.set("0")



    txtSamosa.configure(state =DISABLED)
    txtSandwich.configure(state =DISABLED)
    txtHamburger.configure(state =DISABLED)
    txtVadapav.configure(state =DISABLED)
    txtNoodle.configure(state =DISABLED)
    
    txtNoodleFrankie.configure(state =DISABLED)
    txtCheeseFrankie.configure(state =DISABLED)
    txtVegFrankie.configure(state =DISABLED)

    txtHashBrown.configure(state =DISABLED)
    txtToastedBagel.configure(state =DISABLED)
    txtPancake.configure(state =DISABLED)
    txtPineappleStick.configure(state =DISABLED)
    txtChocolateIcecream.configure(state =DISABLED)

    txtTea.configure(state =DISABLED)
    txtCola.configure(state =DISABLED)
    txtCoffee.configure(state =DISABLED)
    txtOrange.configure(state =DISABLED)
    txtColdCoffee.configure(state =DISABLED)
    txtVanillaShake.configure(state =DISABLED)
    txtVanillaCone.configure(state =DISABLED)
    txtStrawberryShake.configure(state =DISABLED)

    txtPayment.configure(state =DISABLED)
    txtTax.configure(state =DISABLED)
    txtTotal.configure(state =DISABLED)
    txtChange.configure(state =DISABLED)
    txtSubTotal.configure(state =DISABLED)
    var8.get()==0

    
def chkSamosa():
    if (var1.get() ==1):
        txtSamosa.configure(state = NORMAL)
        varSamosa.set("")
    elif(var1.get() ==0):
        txtSamosa.configure(state = DISABLED)
        varSamosa.set("0")


def chkSandwich():
    if (var2.get() ==1):
        txtSandwich.configure(state = NORMAL)
        varSandwich.set("")
    elif(var2.get() ==0):
        txtSandwich.configure(state = DISABLED)
        varSandwich.set("0")

def chkHamburger():
    if (var3.get() ==1):
        txtHamburger.configure(state = NORMAL)
        varHamburger.set("")
    elif(var3.get() ==0):
        txtHamburger.configure(state = DISABLED)
        varHamburger.set("0")

def chkVadapav():
    if (var4.get() ==1):
        txtVadapav.configure(state = NORMAL)
        varVadapav.set("")
    elif(var4.get() ==0):
        txtVadapav.configure(state = DISABLED)
        varVadapav.set("0")

def chkNoodle():
    if (var5.get() ==1):
        txtNoodle.configure(state = NORMAL)
        varVadapav.set("")
    elif(var5.get() ==0):
        txtNoodle.configure(state = DISABLED)
        varNoodle.set("0")

def chkNoodleFrankie():
    if (var6.get() ==1):
        txtNoodleFrankie.configure(state = NORMAL)
        varNoodleFrankie.set("")
    elif(var6.get() ==0):
        txtNoodleFrankie.configure(state = DISABLED)
        varNoodleFrankie.set("0")

def chkCheeseFrankie():
    if (var7.get() ==1):
        txtCheeseFrankie.configure(state = NORMAL)
        varCheeseFrankie.set("")
    elif(var7.get() ==0):
        txtCheeseFrankie.configure(state = DISABLED)
        varCheeseFrankie.set("0")

def chkVegFrankie():
    if (var8.get() ==1):
        txtVegFrankie.configure(state = NORMAL)
        varVegFrankie.set("")
    elif(var8.get() ==0):
        txtVegFrankie.configure(state = DISABLED)
        varVegFrankie.set("0")

def chkHashBrown():
    if (var9.get() ==1):
        txtHashBrown.configure(state = NORMAL)
        varHashBrown.set("")
    elif(var9.get() ==0):
        txtHashBrown.configure(state = DISABLED)
        varHashBrown.set("0")

def chkToastedBagel():
    if (var10.get() ==1):
        txtToastedBagel.configure(state = NORMAL)
        varToastedBagel.set("")
    elif(var10.get() ==0):
        txtToastedBagel.configure(state = DISABLED)
        varToastedBagel.set("0")

def chkPancake():
    if (var11.get() ==1):
        txtPancake.configure(state = NORMAL)
        varPancake.set("")
    elif(vr11.get() ==0):
        txtPancake.configure(state = DISABLED)
        varPancake.set("0")

def chkPineappleStick():
    if (var12.get() ==1):
        txtPineappleStick.configure(state = NORMAL)
        varPineappleStick.set("")
    elif(var12.get() ==0):
        txtPineappleStick.configure(state = DISABLED)
        varPineappleStick.set("0")

def chkChocolateIcecream():
    if (var13.get() ==1):
        txtChocolateIcecream.configure(state = NORMAL)
        varChocolateIcecream.set("")
    elif(var13.get() ==0):
        txtChocolateIcecream.configure(state = DISABLED)
        varChocolateIcecream.set("0")

def chkTea():
    if (var14.get() ==1):
        txtTea.configure(state = NORMAL)
        varTea.set("")
    elif(var14.get() ==0):
        txtTea.configure(state = DISABLED)
        varTea.set("0")

def chkCola():
    if (var15.get() ==1):
        txtCola.configure(state = NORMAL)
        varCola.set("")
    elif(var15.get() ==0):
        txtCola.configure(state = DISABLED)
        varCola.set("0")

def chkCoffee():
    if (var16.get() ==1):
        txtCoffee.configure(state = NORMAL)
        varCoffee.set("")
    elif(var16.get() ==0):
        txtCoffee.configure(state = DISABLED)
        varCoffee.set("0")

def chkOrange():
    if (var17.get() ==1):
        txtOrange.configure(state = NORMAL)
        varOrange.set("")
    elif(var17.get() ==0):
        txtOrange.configure(state = DISABLED)
        varOrange.set("0")

def chkColdCoffee():
    if (var18.get() ==1):
        txtColdCoffee.configure(state = NORMAL)
        varColdCoffee.set("")
    elif(var18.get() ==0):
        txtColdCoffee.configure(state = DISABLED)
        varColdCoffee.set("0")

def chkVanillaShake():
    if (var19.get() ==1):
        txtVanillaShake.configure(state = NORMAL)
        varVanillaShake.set("")
    elif(var19.get() ==0):
        txtVanillaShake.configure(state = DISABLED)
        varVanillaShake.set("0")

def chkVanillaCone():
    if (var20.get() ==1):
        txtVanillaCone.configure(state = NORMAL)
        varVanillaCone.set("")
    elif(var20.get() ==0):
        txtVanillaCone.configure(state = DISABLED)
        varVanillaCone.set("0")

def chkStrawberryShake():
    if (var21.get() ==1):
        txtStrawberryShake.configure(state = NORMAL)
        varStrawberryShake.set("")
    elif(var21.get() ==0):
        txtStrawberryShake.configure(state = DISABLED)
        varStrawberryShake.set("0")

def costofmeal():
    meal1 = float(varSamosa.get())
    meal2 = float(varSandwich.get())
    meal3 = float(varHamburger.get())
    meal4 = float(varVadapav.get())
    meal5 = float(varNoodle.get())
    meal6 = float(varNoodleFrankie.get())
    meal7 = float(varCheeseFrankie.get())
    meal8 = float(varVegFrankie.get())
    meal9 = float(varHashBrown.get())
    meal10 = float(varToastedBagel.get())
    meal11 = float(varPancake.get())
    meal12 = float(varPineappleStick.get())
    meal13 = float(varChocolateIcecream.get())
    meal14 = float(varTea.get())
    meal15 = float(varCola.get())
    meal16 = float(varCoffee.get())
    meal17 = float(varOrange.get())
    meal18 = float(varColdCoffee.get())
    meal19 = float(varVanillaShake.get())
    meal20 = float(varVanillaCone.get())
    meal21 = float(varStrawberryShake.get())

    iTotal1=((meal1 * 25) + (meal2 * 45) + (meal3 * 85) + (meal4 * 25) + (meal5 * 25))
    iTotal2=((meal6 * 45) + (meal7 * 55) + (meal8 * 25) + (meal9 * 75) + (meal10 * 85))
    iTotal3=((meal11 * 15) + (meal12 * 15) + (meal13 * 95) + (meal14 * 15) + (meal15 * 25))
    iTotal4=((meal16 * 25) + (meal17 * 55) + (meal18 * 75) + (meal19 * 65) + (meal20 * 85) + (meal21 * 85))

    iCost = (iTotal1 + iTotal2 +iTotal3 + iTotal4)
    iTax = (iCost * 3.4)/100
    varTax.set(iTax)
    varSubTotal.set(iCost )
    varTotal.set(iCost + iTax)

##    if (var22.get() == "Cash"):
##        iChange = float(varPayment.get())
##        iCost = (iTotal1 + iTotal2 +iTotal3 + iTotal4 + iTotal5)
##        iTax = (icost * 3.4)/100
##        iTaxq="$", str('%.2f'%(iTax))
##        varTax.set(iTaxq)
##
##        iCostq = "$", str('%.2f'%(iCost))
##        varSubTotal.set(iCostq)
##        iTotalq="$", str('%.2f'%((iCost + iTax)))


















































###=============================================Frame 1==================================================================================================================

lblMeal = Label(f1, font=('arial', 20, 'bold'), text="Fast Food Meal & Vegitarian\n")
lblMeal.grid(row =0, column=0)

Samosa =Checkbutton(f1, text="Samosa\t\t\t25", variable=var1, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkSamosa).grid(row=1, column=0, sticky=W)
txtSamosa = Entry(f1,font=('arial',18,'bold'), textvariable =varSamosa, width =6, justify ='right', state =DISABLED)
txtSamosa.grid(row =1 , column =1)

Sandwich =Checkbutton(f1, text="Sandwich\t\t45", variable=var2, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkSandwich).grid(row=2, column=0, sticky=W)
txtSandwich = Entry(f1,font=('arial',18,'bold'), textvariable =varSandwich, width =6, justify ='right', state =DISABLED)
txtSandwich.grid(row =2 , column =1)

Hamburger =Checkbutton(f1, text="Hamburger\t\t85", variable=var3, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkHamburger).grid(row=3, column=0, sticky=W)
txtHamburger = Entry(f1,font=('arial',18,'bold'), textvariable =varHamburger, width =6, justify ='right', state =DISABLED)
txtHamburger.grid(row =3 , column =1)

Vadapav =Checkbutton(f1, text="Vadapav\t\t\t25", variable=var4, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkVadapav).grid(row=4, column=0, sticky=W)
txtVadapav = Entry(f1,font=('arial',18,'bold'), textvariable =varVadapav, width =6, justify ='right', state =DISABLED)
txtVadapav.grid(row =4 , column =1)

Noodle =Checkbutton(f1, text="Noodle\t\t\t15", variable=var5, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkNoodle).grid(row=5, column=0, sticky=W)
txtNoodle = Entry(f1,font=('arial',18,'bold'), textvariable =varNoodle, width =6, justify ='right', state =DISABLED)
txtNoodle.grid(row =5 , column =1)

lblFrankie = Label(f1, font=('arial', 20, 'bold'), text="\nFrankie\n")
lblFrankie.grid(row =6, column=0)

NoodleFrankie =Checkbutton(f1, text="NoodleFrankie\t\t45", variable=var6, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkNoodleFrankie).grid(row=7, column=0, sticky=W)
txtNoodleFrankie = Entry(f1,font=('arial',18,'bold'), textvariable =varNoodleFrankie, width =6, justify ='right', state =DISABLED)
txtNoodleFrankie.grid(row =7 , column =1)

CheeseFrankie =Checkbutton(f1, text="CheeseFrankie\t\t55", variable=var7, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkCheeseFrankie).grid(row=8, column=0, sticky=W)
txtCheeseFrankie = Entry(f1,font=('arial',18,'bold'), textvariable =varCheeseFrankie, width =6, justify ='right', state =DISABLED)
txtCheeseFrankie.grid(row =8 , column =1)

VegFrankie =Checkbutton(f1, text="VegFrankie\t\t25", variable=var8, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkVegFrankie).grid(row=9, column=0, sticky=W)
txtVegFrankie = Entry(f1,font=('arial',18,'bold'), textvariable =varVegFrankie, width =6, justify ='right', state =DISABLED)
txtVegFrankie.grid(row =9 , column =1)

lblspace=Label( f1, text="\n\n\n\n\n\n\n\n\n")
lblspace.grid(row =10, column=0)

#============================================Frame 2===================================================================================================================
lblMeal = Label(f2TOP, font=('arial', 18, 'bold'), text="Desserts\n")
lblMeal.grid(row =0, column=0)

HashBrown =Checkbutton(f2TOP, text="HashBrown\t\t75", variable=var9, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkHashBrown).grid(row=1, column=0, sticky=W)
txtHashBrown = Entry(f2TOP,font=('arial',18,'bold'), textvariable =varHashBrown, width =6, justify ='right', state =DISABLED)
txtHashBrown.grid(row =1 , column =1)

ToastedBagel =Checkbutton(f2TOP, text="ToastedBagel\t\t85", variable=var10, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkToastedBagel).grid(row=2, column=0, sticky=W)
txtToastedBagel = Entry(f2TOP,font=('arial',18,'bold'), textvariable =varToastedBagel, width =6, justify ='right', state =DISABLED)
txtToastedBagel.grid(row =2 , column =1)

Pancake =Checkbutton(f2TOP, text="Pancake\t\t\t15", variable=var11, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkPancake).grid(row=3, column=0, sticky=W)
txtPancake = Entry(f2TOP,font=('arial',18,'bold'), textvariable =varPancake, width =6, justify ='right', state =DISABLED)
txtPancake.grid(row =3 , column =1)

PineappleStick =Checkbutton(f2TOP, text="PineappleStick\t\t15", variable=var12, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkPineappleStick).grid(row=4, column=0, sticky=W)
txtPineappleStick = Entry(f2TOP,font=('arial',18,'bold'), textvariable =varPineappleStick, width =6, justify ='right', state =DISABLED)
txtPineappleStick.grid(row =4 , column =1)

ChocolateIcecream =Checkbutton(f2TOP, text="ChocolateIcecream\t95", variable=var13, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkChocolateIcecream).grid(row=5, column=0, sticky=W)
txtChocolateIcecream = Entry(f2TOP,font=('arial',18,'bold'), textvariable =varChocolateIcecream,width =6, justify ='right', state =DISABLED)
txtChocolateIcecream.grid(row =5 , column =1)
##
#==================================================Frame 3=============================================================================================================
lblMeal = Label(f3,font=('arial', 18, 'bold'), text="Drinks\n")
lblMeal.grid(row =0, column=0)

Tea =Checkbutton(f3, text="Tea\t\t15", variable=var14, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'), command=chkTea).grid(row=1, column=0, sticky=W)
txtTea = Entry(f3,font=('arial',18,'bold'), textvariable =varTea, width =6, justify ='left', state =DISABLED)
txtTea.grid(row =1 , column =1)

Cola =Checkbutton(f3, text="Cola\t\t25", variable=var15, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkCola).grid(row=2, column=0, sticky=W)
txtCola = Entry(f3,font=('arial',18,'bold'), textvariable =varCola, width =6, justify ='left', state =DISABLED)
txtCola.grid(row =2 , column =1)

Coffee =Checkbutton(f3, text="Coffee\t\t25", variable=var16, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkCoffee).grid(row=3, column=0, sticky=W)
txtCoffee = Entry(f3,font=('arial',18,'bold'), textvariable =varCoffee, width =6, justify ='left', state =DISABLED)
txtCoffee.grid(row =3 , column =1)

Orange =Checkbutton(f3, text="Orange\t\t55", variable=var17, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkOrange).grid(row=4, column=0, sticky=W)
txtOrange = Entry(f3,font=('arial',18,'bold'), textvariable =varOrange, width =6, justify ='left', state =DISABLED)
txtOrange.grid(row =4 , column =1)

ColdCoffee =Checkbutton(f3, text="ColdCoffee\t75", variable=var18, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkColdCoffee).grid(row=5, column=0, sticky=W)
txtColdCoffee = Entry(f3,font=('arial',18,'bold'), textvariable =varColdCoffee, width =6, justify ='left', state =DISABLED)
txtColdCoffee.grid(row =5 , column =1)

lblShakes = Label(f3,font=('arial', 20, 'bold'), text="\nShakes\n")
lblShakes.grid(row =6, column=0)

VanillaShake =Checkbutton(f3, text="VanillaShake\t65", variable=var19, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkVanillaShake).grid(row=7, column=0, sticky=W)
txtVanillaShake = Entry(f3,font=('arial',18,'bold'), textvariable =varVanillaShake, width =6, justify ='left', state =DISABLED)
txtVanillaShake.grid(row =7 , column =1)

VanillaCone =Checkbutton(f3, text="VanillaCone\t85", variable=var20, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkVanillaCone).grid(row=8, column=0, sticky=W)
txtVanillaCone = Entry(f3,font=('arial',18,'bold'), textvariable =varVanillaCone, width =6, justify ='left', state =DISABLED)
txtVanillaCone.grid(row =8 , column =1)

StrawberryShake =Checkbutton(f3, text="StrawberryShake\t85", variable=var21, onvalue =1, offvalue=0,
                    font=('arial',18,'bold'), command=chkStrawberryShake).grid(row=9, column=0, sticky=W)
txtStrawberryShake = Entry(f3,font=('arial',18,'bold'), textvariable =varStrawberryShake, width =6, justify ='left', state =DISABLED)
txtStrawberryShake.grid(row =9 , column =1)

lblspace=Label( f3, text="\n\n\n\n\n\n\n\n\n")
lblspace.grid(row =10, column=0)

#===================================================frame 2 BOTTOM=====================================================================================================
lblPaymentMethod = Label(f2BOTTOM , font=('arial',14, 'bold'), text="Payment Method", bd=10, width= 16, anchor='w')
lblPaymentMethod.grid(row=0,column=0)

##lblChange = Label(f2BOTTOM , font=('arial',14, 'bold'), text="Change", bd=10, anchor='w')
##lblChange.grid(row=0,column=1)
##txtChange = Entry(f2BOTTOM,font=('arial',18,'bold'), textvariable =varChange, width =6, state =DISABLED)
##txtChange.grid(row =0 , column =2)

##cmbPaymentMethod = ttk.Combobox(f2BOTTOM , textvariable = var22, state='readonly', font=('arial',10, 'bold'), width= 20)
##cmbPaymentMethod['value']=('Cash','Master Card','Visa Card','Debit Card')
##cmbPaymentMethod.current(0)
##cmbPaymentMethod.grid(row=1,column=0)

lblTax = Label(f2BOTTOM , font=('arial',14,'bold'), text="Tax  ",bd=10, anchor='w')
lblTax.grid(row=1,column=1)
txtTax = Entry(f2BOTTOM,font=('arial',18, 'bold'), textvariable =varTax, width=6, justify='left', state =DISABLED)
txtTax.grid(row =1 , column =2)

txtPayment = Entry(f2BOTTOM,font=('arial',18,'bold'), textvariable =varChange, width =6, justify='left', state =DISABLED)
txtPayment.grid(row =2 , column =0)
lblSubTotal = Label(f2BOTTOM , font=('arial',14, 'bold'), text="SubTotal", bd=10, width =8,anchor='w')
lblSubTotal.grid(row=2,column=1)
txtSubTotal = Entry(f2BOTTOM,font=('arial',18,'bold'), textvariable =varSubTotal, width =6, justify='left', state =DISABLED)
txtSubTotal.grid(row =2 , column =2)

lblTotal = Label(f2BOTTOM , font=('arial',14, 'bold'), text="Total", bd=10, width =6,anchor='w')
lblTotal.grid(row=3,column=1)
txtTotal = Entry(f2BOTTOM,font=('arial',18,'bold'), textvariable =varTotal, width =6, justify='left', state =DISABLED)
txtTotal.grid(row =3 , column =2)

#=========================================================frame  2 Button============================================================================================
btnTotal=Button(f2BOTTOM,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'), width=5,text="Total ", command = costofmeal).grid(row=4, column=0)

btnReset=Button(f2BOTTOM,padx=16,pady=1, bd=4, fg="blue",font=('arial', 16,'bold'), width=5,text="Reset", command =Reset).grid(row=4, column=1)

btnExit=Button(f2BOTTOM,padx=16,pady=1, bd=4, fg="red",font=('arial', 16,'bold'), width=5,text="Exit",command=lambda: iExit()).grid(row=4, column=2)

lblspace=Label( f2BOTTOM, text="\n\n\n\n\n\n\n")
lblspace.grid(row= 5, column=0)










root.mainloop()
