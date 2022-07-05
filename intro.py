from tkinter import *
from tkinter import messagebox
import math,random,os
class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title("Billing Software")
        bg_color='#074463'
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg='white',font=('times new roman',30,'bold'),pady=2).pack(fill=X)
#######################################################################
########variables################

        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.gel=IntVar()
        self.uptan=IntVar()
        self.lotion=IntVar()

        self.dal = IntVar()
        self.rice = IntVar()
        self.chana = IntVar()
        self.sugar = IntVar()
        self.oil= IntVar()
        self.tea = IntVar()

        self.bat = IntVar()
        self.ball = IntVar()
        self.footbal = IntVar()
        self.hockey = IntVar()
        self.tt= IntVar()
        self.racket = IntVar()

####################total_product_price######################


        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.sports_price=StringVar()

        self.cosmetic_tax=StringVar()

        self.grocery_tax=StringVar()

        self.sports_tax=StringVar()

        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
















        #frame 1
        F1=LabelFrame(self.root,text='Customer Details',bd=10,relief=GROOVE,font=('times new roman',15,'bold'),fg='gold',bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text='Customer name',bg=bg_color,fg='white',font=('times new roman',15,'bold')).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font='ariel 15',bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cname_lbl = Label(F1, text='Contact Number', bg=bg_color, fg='white', font=('times new roman', 15, 'bold')).grid(
            row=0, column=2, padx=20, pady=5)
        cname_txt = Entry(F1, width=20,textvariable=self.c_phone ,font='ariel 15', bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        cname_lbl = Label(F1, text='Bill Number', bg=bg_color, fg='white', font=('times new roman', 15, 'bold')).grid(
            row=0, column=4, padx=20, pady=5)
        cname_txt = Entry(F1, width=20,textvariable=self.bill_no, font='arial 15', bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text='Search',command=self.find_bill,width=10,bd=7,font="arial 12 bold",relief=SUNKEN).grid(row=0,column=6,padx=10,pady=10)

        #frame2

        F2 = LabelFrame(self.root, text='Cosmetics', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'),
                        fg='gold', bg=bg_color)
        F2.place(x=5, y=180,width=325,height=380)

        bath_lbl=Label(F2,text='Bath Soap',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky='w')

        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl = Label(F2, text='Face Cream', font=('times new roman', 16, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=1, column=0, padx=10, pady=10, sticky='w')

        face_cream__txt = Entry(F2, width=10,textvariable=self.face_cream, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)
        face_wash_lbl = Label(F2, text="Face Wash", font=('times new roman', 16, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=2, column=0, padx=10, pady=10, sticky='w')

        face_wash_txt = Entry(F2, width=10, textvariable=self.face_wash,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                       padx=10, pady=10)
        body_lotion_lbl = Label(F2, text='Body Lotion', font=('times new roman', 16, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=3, column=0, padx=10, pady=10, sticky='w')

        body_lotion_txt = Entry(F2, width=10,textvariable=self.lotion, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                       padx=10, pady=10)
        hair_gel_lbl = Label(F2, text='Hair Gel', font=('times new roman', 16, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=4, column=0, padx=10, pady=10, sticky='w')

        hair_gel_txt = Entry(F2, width=10, textvariable=self.gel,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                       padx=10, pady=10)
        uptan_lbl = Label(F2, text='Body Uptan', font=('times new roman', 16, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=5, column=0, padx=10, pady=10, sticky='w')

        uptan_txt = Entry(F2, width=10,textvariable=self.uptan, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)
#################################################
        F3 = LabelFrame(self.root, text='Rashan Item', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'),
                        fg='gold', bg=bg_color)
        F3.place(x=335, y=180, width=325, height=380)

        dal_lbl = Label(F3, text='Dal', font=('times new roman', 16, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=0, column=0, padx=10, pady=10, sticky='w')

        dal_txt = Entry(F3, width=10,textvariable=self.dal, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        rice_lbl = Label(F3, text='Rice', font=('times new roman', 16, 'bold'), bg=bg_color,
                               fg='lightgreen').grid(
            row=1, column=0, padx=10, pady=10, sticky='w')

        rice_txt = Entry(F3, width=10, textvariable=self.rice,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=10)
        chana_lbl = Label(F3, text="Chana Matar", font=('times new roman', 16, 'bold'), bg=bg_color,
                              fg='lightgreen').grid(
            row=2, column=0, padx=10, pady=10, sticky='w')

        chana_txt = Entry(F3, width=10,textvariable=self.chana, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=10)
        oil_lbl = Label(F3, text='Mustard Oil', font=('times new roman', 16, 'bold'), bg=bg_color,
                                fg='lightgreen').grid(
            row=3, column=0, padx=10, pady=10, sticky='w')

        oil_txt = Entry(F3, width=10, textvariable=self.oil,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=10)
        sugar_lbl = Label(F3, text='Sugar', font=('times new roman', 16, 'bold'), bg=bg_color,
                             fg='lightgreen').grid(
            row=4, column=0, padx=10, pady=10, sticky='w')

        sugar_txt = Entry(F3, width=10, textvariable=self.sugar,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=10)
        tea_lbl = Label(F3, text='Red Label Tea', font=('times new roman', 16, 'bold'), bg=bg_color,
                          fg='lightgreen').grid(
            row=5, column=0, padx=10, pady=10, sticky='w')

        tea_txt = Entry(F3, width=10, textvariable=self.tea,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)



###############################################################################################################################

        F4 = LabelFrame(self.root, text='Sports Item', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'),
                        fg='gold', bg=bg_color)
        F4.place(x=665, y=180, width=325, height=380)

        bat_lbl = Label(F4, text='Cricket Bat', font=('times new roman', 16, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=0, column=0, padx=10, pady=10, sticky='w')

        bat_txt = Entry(F4, width=10,textvariable=self.bat, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                      padx=10, pady=10)

        ball_lbl = Label(F4, text='Cricket Ball', font=('times new roman', 16, 'bold'), bg=bg_color,
                         fg='lightgreen').grid(
            row=1, column=0, padx=10, pady=10, sticky='w')

        ball_txt = Entry(F4, width=10,textvariable=self.ball, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                       column=1,
                                                                                                       padx=10,
                                                                                                       pady=10)
        football_lbl = Label(F4, text="Football", font=('times new roman', 16, 'bold'), bg=bg_color,
                          fg='lightgreen').grid(
            row=2, column=0, padx=10, pady=10, sticky='w')

        football_txt = Entry(F4, width=10, textvariable=self.footbal,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                        column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)
        badminton_lbl = Label(F4, text='Badminton Racket', font=('times new roman', 16, 'bold'), bg=bg_color,
                        fg='lightgreen').grid(
            row=3, column=0, padx=10, pady=10, sticky='w')

        badminton_txt = Entry(F4, width=10,textvariable=self.racket, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                      column=1,
                                                                                                      padx=10,
                                                                                                      pady=10)
        tt_lbl = Label(F4, text='Table Tenis', font=('times new roman', 16, 'bold'), bg=bg_color,
                          fg='lightgreen').grid(
            row=4, column=0, padx=10, pady=10, sticky='w')

        tt_txt = Entry(F4, width=10,textvariable=self.tt, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                        column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)
        hockey_lbl = Label(F4, text='Hockey Stick', font=('times new roman', 16, 'bold'), bg=bg_color,
                        fg='lightgreen').grid(
            row=5, column=0, padx=10, pady=10, sticky='w')

        hockey_txt = Entry(F4, width=10,textvariable=self.hockey, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                      padx=10,
                                                                                                      pady=10)
############################################################################################################################

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)


        bill_title=Label(F5,text='Bill Area',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)

        scroll_bar_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_bar_y.set)
        scroll_bar_y.pack(side=RIGHT,fill=Y)
        scroll_bar_y.config(command=self.txtarea.yview)
        self.txtarea.pack()

        F6 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'),
                        fg='gold', bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)


        m1_lbl=Label(F6,text='Total Cosmetics Price',bg=bg_color,fg='white',font=('times new roman',14,'bold')).grid(row=0,column=0,padx=20,pady=1,sticky='w')

        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font=('arial 10 bold'),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text='Total Rashan Price', bg=bg_color, fg='white',
                       font=('times new roman', 14, 'bold')).grid(row=1, column=0, padx=20, pady=1, sticky='w')

        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price,font=('arial 10 bold'), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text='Total Sports Price', bg=bg_color, fg='white',
                       font=('times new roman', 14, 'bold')).grid(row=2, column=0, padx=20, pady=1, sticky='w')

        m3_txt = Entry(F6, width=18, textvariable=self.sports_price,font=('arial 10 bold'), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)







####################################################################################################
        c1_lbl = Label(F6, text='Total Cosmetics Tax', bg=bg_color, fg='white',
                       font=('times new roman', 14, 'bold')).grid(row=0, column=2, padx=20, pady=1, sticky='w')

        c1_txt = Entry(F6, width=18,textvariable=self.cosmetic_tax, font=('arial 10 bold'), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text='Total Rashan Tax', bg=bg_color, fg='white',
                       font=('times new roman', 14, 'bold')).grid(row=1, column=2, padx=20, pady=1, sticky='w')

        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax,font=('arial 10 bold'), bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text='Total Sports Tax', bg=bg_color, fg='white',
                       font=('times new roman', 14, 'bold')).grid(row=2, column=2, padx=20, pady=1, sticky='w')

        c3_txt = Entry(F6, width=18,textvariable=self.sports_tax, font=('arial 10 bold'), bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=740,width=580,height=105)

        total_btn=Button(btn_f,command=self.total,text='Total',bg='cadetblue',fg='white',pady=15, width=10, font='arial 15 bold',bd=2).grid(row=0,column=0,padx=5,pady=5)
        gbill_btn = Button(btn_f, text='bill', bg='cadetblue',command=self.bill_area, fg='white', pady=15, width=10, font='arial 15 bold',
                           bd=2).grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_f,command=self.clear_bill, text='Clear', bg='cadetblue', fg='white', pady=15, width=10, font='arial 15 bold',
                           bd=2).grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_f,command=self.exit_bill, text='Exit', bg='cadetblue', fg='white', pady=15, width=10, font='arial 15 bold',
                           bd=2).grid(row=0, column=3, padx=4, pady=5)



    def total(self):

        self.csp=(self.soap.get()*40)
        self.cfw=(self.face_wash.get()*120)
        self.cfc=(self.face_cream.get()*80)
        self.cgg=(self.gel.get()*100)
        self.cl=(self.lotion.get()*140)
        self.cu=(self.uptan.get()*240)
        self.total_cosmetic_price=float(


             self.csp+self.cfw+self.cfc+self.cgg+self.cl+self.cu

        )
        self.cosmetic_price.set(str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set(str(self.c_tax))


        self.r=(self.rice.get() * 40)
        self.d=(self.dal.get() * 60)
        self.t=(self.tea.get() * 80)
        self.s=(self.sugar.get() * 30)
        self.o=(self.oil.get() * 200)
        self.c=(self.chana.get() * 10)


        self.total_grocery_price = float(

             self.r+self.d+self.t+self.s+self.o+self.c

        )
        self.grocery_price.set(str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set(str(self.g_tax))



        self.sbat=(self.bat.get() * 4000)
        self.sball=(self.ball.get() * 300)
        self.sfb=(self.footbal.get() * 3000)
        self.stt=(self.tt.get() * 600)
        self.sh=(self.hockey.get() * 2000)
        self.srac=(self.racket.get() * 1000)



        self.total_sports_price = float(

             self.sbat+self.sball+self.stt+self.sh+self.srac+self.sfb

        )
        self.sports_price.set(str(self.total_sports_price))
        self.s_tax=round((self.total_sports_price * 0.05), 2)
        self.sports_tax.set(str(self.s_tax))

        self.total_bill=(
            self.total_cosmetic_price+
            self.total_sports_price+
            self.total_grocery_price+
            self.g_tax+
            self.s_tax+self.c_tax
        )


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Paras Retail")
        self.txtarea.insert(END,f"\n Bill Number   : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name  : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number   : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n===========================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n===========================================")

    def bill_area(self):


        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror('Error','Customer Details Not found !')
        else:
            self.welcome_bill()
            if self.soap.get()!=0:

                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.csp}")

            if self.uptan.get()!=0:

                self.txtarea.insert(END,f"\n Uptan\t\t{self.uptan.get()}\t\t{self.cu}")


            if self.face_wash.get()!=0:

                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.cfw}")

            if self.face_cream.get()!=0:

                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.cfc}")

            if self.gel.get()!=0:

                self.txtarea.insert(END,f"\n Gel\t\t{self.gel.get()}\t\t{self.cgg}")


            if self.lotion.get()!=0:

                self.txtarea.insert(END,f"\n Lotion\t\t{self.lotion.get()}\t\t{self.cl}")





            if self.rice.get()!=0:

                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.r}")

            if self.dal.get()!=0:

                self.txtarea.insert(END,f"\n Dal\t\t{self.dal.get()}\t\t{self.d}")


            if self.chana.get()!=0:

                self.txtarea.insert(END,f"\n Chana\t\t{self.chana.get()}\t\t{self.c}")

            if self.oil.get()!=0:

                self.txtarea.insert(END,f"\n Oil\t\t{self.oil.get()}\t\t{self.o}")

            if self.sugar.get()!=0:

                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.s}")


            if self.tea.get()!=0:

                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.t}")









            if self.bat.get()!=0:

                self.txtarea.insert(END,f"\n Cricket Bat\t\t{self.bat.get()}\t\t{self.sbat}")

            if self.ball.get()!=0:

                self.txtarea.insert(END,f"\n Cricket Ball\t\t{self.ball.get()}\t\t{self.sball}")


            if self.hockey.get()!=0:

                self.txtarea.insert(END,f"\n Hockey\t\t{self.hockey.get()}\t\t{self.sh}")

            if self.tt.get()!=0:

                self.txtarea.insert(END,f"\n Table Tenis\t\t{self.tt.get()}\t\t{self.stt}")

            if self.footbal.get()!=0:

                self.txtarea.insert(END,f"\n Football\t\t{self.footbal.get()}\t\t{self.sfb}")


            if self.racket.get()!=0:

                self.txtarea.insert(END,f"\n Racket\t\t{self.racket.get()}\t\t{self.srac}")

            self.txtarea.insert(END, f"\n===========================================")

            self.txtarea.insert(END,f"Total Price :\t\t\t\t{self.total_grocery_price+self.total_sports_price+self.total_cosmetic_price}")

            self.txtarea.insert(END, f"\n--------------------------------------------")
            self.txtarea.insert(END,f"Total Tax   :\t\t\t\t{self.c_tax+self.g_tax+self.s_tax}")

            self.txtarea.insert(END, f"\n*******************************************")


            self.txtarea.insert(END,f"Total Payable Amount:\t\t\t\t{self.total_bill}")
            self.txtarea.insert(END, f"\n*******************************************")


            self.txtarea.insert(END,"\t\t THANKS FOR VISITING ! ")
    
            self.txtarea.insert(END, f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            self.save_bill()



    def save_bill(self):
        op=messagebox.askyesno("Save bill","Do you want to save the Bill?")

        if op>0:

            self.bill_data=self.txtarea.get('1.0',END)

            f1=open("/Users/test/Documents/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",'Saved Successfully')
        else:
            return

    def find_bill(self):
        present=0
        for i in os.listdir('/Users/test/Documents/'):
            if i.split('.')[0]==self.search_bill.get():

                f1=open(f"/Users/test/Documents/",'r')

                self.txtarea.delete('1.0',END)

                for d in f1:
                    self.txtarea.insert(END,d)

                f1.close()
                present=1

        if present ==0:
            messagebox.showerror("Error","Invalid Bill Number !")


    def clear_bill(self):

        op=messagebox.askyesno("Clear","Do you want to clear data?")

        if op>0:

            self.soap.set(0.0)
            self.face_cream.set(0.0)
            self.face_wash.set(0.0)
            self.gel.set(0.0)
            self.uptan.set(0.0)
            self.lotion.set(0.0)

            self.dal.set(0.0)
            self.rice.set(0.0)
            self.chana.set(0.0)
            self.sugar.set(0.0)
            self.oil.set(0.0)
            self.tea.set(0.0)

            self.bat.set(0.0)
            self.ball.set(0.0)
            self.footbal.set(0.0)
            self.hockey.set(0.0)
            self.tt.set(0.0)
            self.racket.set(0.0)

            ####################total_product_price######################

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.sports_price.set("")

            self.cosmetic_tax.set("")

            self.grocery_tax.set("")

            self.sports_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()






    def exit_bill(self):

        op=messagebox.askyesno("Exit","Do you want to Exit?")

        if op>0:
            self.root.destroy()





































root=Tk()
obj=bill_app(root)
root.mainloop()