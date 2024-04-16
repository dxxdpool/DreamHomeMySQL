import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import mysql.connector as msql
import datetime as dt

db = msql.connect(host='localhost', user='root', password='Benchmark@25678', database='study')
curs = db.cursor()


class Lease_Form(tk.Toplevel):
    def __init__(self, master):
        self.c_no = None
        self.name = None
        self.p_no = None
        self.p_address = None
        self.mon_rent= None
        self.payment_method = None
        self.dep_status = None
        self.rent_start = None
        self.rent_finish = None
        self.duration = None

        super().__init__()
        self.geometry('640x480+448+192')
        self.config(bg='pink')
        self.title('Lease Form')
        self.resizable(False, False)

        self.iconbitmap('DreamHome Logo.ico')

        self.I = Image.open("C:/Users/Welcome/Desktop/MiniProject/DreamHome Logo Final.png")
        self.res_img = self.I.resize((70, 70))
        self.l = ImageTk.PhotoImage(self.res_img)
        l_label = tk.Label(self, image=self.l, bg='pink')
        l_label.place(relx=0.0, rely=0.0)

        text = tk.Label(self, text='DreamHome', font=('Times New Roman', 20), bg='pink')
        text.place(relx=0.45, rely=0.010)
        sub_text = tk.Label(self, text='Lease Form', font=('Times New Roman', 19), bg='pink')
        sub_text.place(relx=0.465, rely=0.075)

        self.insert_labels()
        self.insert_Entry()
        self.styling()

        ttk.Button(self, text='Cancel', command=self.destroy).place(relx=0.70, rely=0.92)
        ttk.Button(self, text='Next', command=self.InsertIntoLeaseInfo).place(relx=0.85, rely=0.92)
        ttk.Button(self, text='Clear', command=self.clearForm).place(relx=0.035, rely=0.919)

        query = "select c_no from clients order by c_no;"
        curs.execute(query)
        self.c_no['values'] = [row[0] for row in curs.fetchall()]

        self.c_no.bind('<<ComboboxSelected>>', self.get_ClientDetails)

        query = "select p_no from properties order by p_no;"
        curs.execute(query)
        self.p_no['values'] = [row[0] for row in curs.fetchall()]

        self.p_no.bind('<<ComboboxSelected>>', self.get_PropertyDetails)
        self.mon_rent.bind('<KeyRelease>', self.checkMoney)

    def styling(self):
        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.17)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.50)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.86)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=0.5, height=331.2, bg='black')
        cv.place(relx=0.5, rely=0.17)
        cv.create_line(320, 81.6, 320, 412.8, fill='pink', width=2)

    def insert_labels(self):
        tk.Label(self, text='Client No', bg='pink').place(relx=0.035, rely=0.23)
        tk.Label(self, text='Full Name', bg='pink').place(relx=0.035, rely=0.32)
        tk.Label(self, text='Rent Start', bg='pink').place(relx=0.535, rely=0.55)
        tk.Label(self, text='Rent_Finish', bg='pink').place(relx=0.535, rely=0.65)
        tk.Label(self, text='Duration', bg='pink').place(relx=0.535, rely=0.75)
        tk.Label(self, text='Property Number', bg='pink').place(relx=0.535, rely=0.23)
        tk.Label(self, text='Property Address', bg='pink').place(relx=0.535, rely=0.33)

        tk.Label(self, text='Enter payment details', bg='pink').place(relx=0.035, rely=0.55)

        tk.Label(self, text='Monthly Rent', bg='pink').place(relx=0.035, rely=0.63)
        tk.Label(self, text='Payment method', bg='pink').place(relx=0.035, rely=0.705)
        tk.Label(self, text='Deposit Paid(Y or N)', bg='pink').place(relx=0.035, rely=0.78)

    def insert_Entry(self):
        self.c_no = ttk.Combobox(self, width=8)
        self.c_no.place(relx=0.15, rely=0.23)

        self.name = ttk.Entry(self, width=25)
        self.name.place(relx=0.15, rely=0.32)

        self.rent_start = ttk.Entry(self, width=10)
        self.rent_start.place(relx=0.65, rely=0.55)

        self.rent_finish = ttk.Entry(self, width=15)
        self.rent_finish.place(relx=0.65, rely=0.65)

        self.duration = ttk.Entry(self, width=12)
        self.duration.place(relx=0.65, rely=0.75)

        self.p_no = ttk.Combobox(self, width=7)
        self.p_no.place(relx=0.70, rely=0.23)

        self.p_address = ttk.Entry(self, width=35)
        self.p_address.place(relx=0.535, rely=0.40)

        self.mon_rent = ttk.Entry(self, width=20)
        self.mon_rent.place(relx=0.18, rely=0.63)

        self.payment_method = ttk.Combobox(self, width=10)
        self.payment_method.place(relx=0.24, rely=0.705)
        self.payment_method['values'] = ['Cash', 'Cheque']

        self.dep_status = ttk.Combobox(self, width=12)
        self.dep_status.place(relx=0.24, rely=0.78)
        self.dep_status['values'] = ['Y', 'N']

    def get_ClientDetails(self, event=None):
        self.name.delete(0, 'end')

        cget = self.c_no.get()
        query = f"select case when mname is not null then concat(fname, ' ', mname, ' ', lname) else concat (fname, " \
                f"' ', lname) end as Full_Name from clients where c_no = '{cget}';"
        curs.execute(query)
        res = curs.fetchall()
        self.name.insert(0, res[0][0])

    def get_PropertyDetails(self, event=None):
        self.p_address.delete(0, 'end')

        p_get = self.p_no.get()
        query = f"select p_address from properties where p_no = '{p_get}';"
        curs.execute(query)
        res = curs.fetchall()
        self.p_address.insert(0, res[0][0])

    def InsertIntoLeaseInfo(self):
        c_no = self.c_no.get()
        p_no = self.p_no.get()
        rent = self.mon_rent.get()
        pay_method = self.payment_method.get()
        deposit_paid = self.dep_status.get()
        rent_start = self.rent_start.get()
        rent_finish = self.rent_finish.get()

        result = messagebox.askyesno("Confirm details", "Are the details correct ?")
        if result is True:
            query = f'insert into lease_form(c_no, p_no, rent, pay_method, deposit_paid, rent_start, rent_finish) ' \
                    f'values(%s, %s, %s, %s, %s, %s, %s);'
            values = (c_no, p_no, rent, pay_method, deposit_paid, rent_start, rent_finish)
            curs.execute(query, values)
            db.commit()

            if deposit_paid == 'Y':
                query = f"update properties set on_rent = 'Y' where p_no = '{p_no}';"
                curs.execute(query)
                db.commit()
            messagebox.showinfo("Registration", "Successfully Registered")
            self.clearForm()

    def clearForm(self):
        self.c_no.delete(0, 'end')
        self.p_no.delete(0, 'end')
        self.name.delete(0, 'end')
        self.p_address.delete(0, 'end')
        self.mon_rent.delete(0, 'end')
        self.dep_status.delete(0, 'end')
        self.payment_method.delete(0, 'end')
        self.rent_start.delete(0, 'end')
        self.rent_finish.delete(0, 'end')
        self.duration.delete(0, 'end')

    def checkMoney(self, event=None):
        query = f"select rent from properties where p_no = '{self.p_no.get()}';"
        curs.execute(query)
        max_rent = curs.fetchall()[0][0]
        mon_rent = self.mon_rent.get()
        if mon_rent and int(mon_rent) > int(max_rent):
            messagebox.showwarning('Notification', f'The max rent approved by the owner is {max_rent}')


if __name__ == '__main__':
    S = Lease_Form()
    S.mainloop()
