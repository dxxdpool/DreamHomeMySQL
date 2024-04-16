import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import mysql.connector as msql

db = msql.connect(host='localhost', user='root', password='Benchmark@25678', database='study')
curs = db.cursor()


class Client_Form(tk.Toplevel):
    def __init__(self, master):
        self.c_no = None
        self.f_name = None
        self.m_name = None
        self.l_name = None
        self.type = None
        self.max_rent = None
        self.b_no = None
        self.tele_no = None
        self.b_address = None
        self.reg_by = None
        self.date_reg = None

        super().__init__()
        self.geometry('640x480+448+192')
        self.config(bg='pink')
        self.title('Client Registration')
        self.resizable(False, False)

        self.iconbitmap('DreamHome Logo.ico')

        self.I = Image.open("C:/Users/Welcome/Desktop/MiniProject/DreamHome Logo Final.png")
        self.res_img = self.I.resize((70, 70))
        self.l = ImageTk.PhotoImage(self.res_img)
        l_label = tk.Label(self, image=self.l, bg='pink')
        l_label.place(relx=0.0, rely=0.0)

        text = tk.Label(self, text='DreamHome', font=('Times New Roman', 20), bg='pink')
        text.place(relx=0.45, rely=0.010)
        sub_text = tk.Label(self, text='Client Registration Form', font=('Times New Roman', 19), bg='pink')
        sub_text.place(relx=0.355, rely=0.075)

        self.insert_labels()
        self.insert_Entry()
        self.styling()

        ttk.Button(self, text='Cancel', command=self.destroy).place(relx=0.70, rely=0.92)
        ttk.Button(self, text='Next', command=self.InsertIntoPropertyInfo).place(relx=0.85, rely=0.92)
        ttk.Button(self, text='Clear', command=self.clearForm).place(relx=0.035, rely=0.919)

        self.c_no_generator()

        query = "select b_no from branches order by b_no;"
        curs.execute(query)
        branch_names = [row[0] for row in curs.fetchall()]
        self.b_no['values'] = branch_names
        self.b_no.bind("<<ComboboxSelected>>", self.get_BranchDetails)

    def styling(self):
        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.17)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=320, height=0.5, bg='black')
        cv.place(relx=0, rely=0.55)
        cv.create_line(0, 200, 320, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.87)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=0.5, height=332, bg='black')
        cv.place(relx=0.5, rely=0.17)
        cv.create_line(320, 81.6, 320, 413, fill='pink', width=2)

    def insert_labels(self):
        tk.Label(self, text='Client Number', bg='pink').place(relx=0.035, rely=0.23)
        tk.Label(self, text='Full Name', bg='pink').place(relx=0.035, rely=0.31)
        tk.Label(self, text='Tele No', bg='pink').place(relx=0.035, rely=0.43)
        tk.Label(self, text='Branch Number', bg='pink').place(relx=0.535, rely=0.23)
        tk.Label(self, text='Branch Address', bg='pink').place(relx=0.535, rely=0.35)
        tk.Label(self, text='Registered By', bg='pink').place(relx=0.535, rely=0.52)
        tk.Label(self, text='Date Registered', bg='pink').place(relx=0.535, rely=0.68)
        #
        tk.Label(self, text='Enter Property Requirements', bg='pink').place(relx=0.035, rely=0.58)
        tk.Label(self, text='Type', bg='pink').place(relx=0.035, rely=0.67)
        tk.Label(self, text='Max Rent', bg='pink').place(relx=0.035, rely=0.77)

    def c_no_generator(self):
        query = "select c_no from clients order by c_no desc limit 1;"
        curs.execute(query)
        base = curs.fetchall()[0][0]
        num_str = int(base[1:])
        term = base[:-len(str(num_str + 1))] + str(num_str + 1)
        self.c_no.insert(0, term)

    def insert_Entry(self):
        self.c_no = ttk.Entry(self, width=7)
        self.c_no.place(relx=0.20, rely=0.23)

        self.f_name = ttk.Entry(self, width=10)
        self.f_name.place(relx=0.035, rely=0.37)

        self.m_name = ttk.Entry(self, width=2)
        self.m_name.place(relx=0.155, rely=0.37)

        self.l_name = ttk.Entry(self, width=10)
        self.l_name.place(relx=0.20, rely=0.37)

        self.tele_no = ttk.Entry(self, width=30)
        self.tele_no.place(relx=0.035, rely=0.48)

        self.type = ttk.Entry(self, width=20)
        self.type.place(relx=0.10, rely=0.67)

        self.max_rent = ttk.Entry(self, width=20)
        self.max_rent.place(relx=0.14, rely=0.77)

        self.b_no = ttk.Combobox(self, width=12, state='')
        self.b_no.place(relx=0.68, rely=0.23)

        self.b_address = ttk.Entry(self, width=30)
        self.b_address.place(relx=0.535, rely=0.41)

        self.reg_by = ttk.Combobox(self, width=35)
        self.reg_by.place(relx=0.535, rely=0.58)

        self.date_reg = ttk.Entry(self, width=20)
        self.date_reg.place(relx=0.535, rely=0.74)

    def get_BranchDetails(self, event=None):
        self.b_address.delete(0, 'end')
        branch_name = self.b_no.get()
        query = f"select b_address from branches where b_no = '{branch_name}';"
        curs.execute(query)
        get_branch = curs.fetchall()[0][0]
        self.b_address.insert(0, get_branch)

        self.reg_by.delete(0, 'end')
        query = f"select case when mname is not null then concat(fname, ' ', mname, ' ', lname) else concat(fname, " \
                f"' ', lname) end as full_name from staff where b_no = '{branch_name}';"
        curs.execute(query)
        names = [row[0] for row in curs.fetchall()]
        self.reg_by['values'] = names

    def insertIntoForms(self):
        query = "select s_no, b_no from staff natural join branches where case when mname is not null then concat(" \
                "fname, ' ', mname, ' ', lname) else concat (fname, ' ', lname) end like '{0}';".format(self.reg_by.get())
        curs.execute(query)

        values = [i for i in curs.fetchall()[0]]
        print(values)
        query = "insert into client_registration (c_no, b_no, registered_by, date_registered) VALUES (%s, %s, %s, %s);"
        values = (self.c_no.get(), values[1], values[0], self.date_reg.get())
        curs.execute(query, values)
        db.commit()

    def InsertIntoPropertyInfo(self):
        c_no = self.c_no.get()
        f_name = self.f_name.get()
        m_name = self.m_name.get()
        l_name = self.l_name.get()
        type = self.type.get()
        max_rent = self.max_rent.get()
        tele_no = self.tele_no.get()

        result = messagebox.askyesno("Confirm details", "Are the details correct ?")
        if result is True:
            query = "insert into clients (c_no, fname, mname, lname, c_phone_no, req_type, req_rent) VALUES (%s, %s, " \
                    "%s, %s, %s, %s, %s);"
            values = (c_no, f_name, m_name, l_name, tele_no, type, max_rent)
            curs.execute(query, values)
            db.commit()
            self.insertIntoForms()
            messagebox.showinfo("Registration", "Successfully Registered")
            self.clearForm()

    def clearForm(self):
        self.c_no.delete(0, 'end')
        self.c_no_generator()
        self.f_name.delete(0, 'end')
        self.m_name.delete(0, 'end')
        self.l_name.delete(0, 'end')
        self.tele_no.delete(0, 'end')
        self.type.delete(0, 'end')
        self.max_rent.delete(0, 'end')
        self.b_no.delete(0, 'end')
        self.b_address.delete(0, 'end')
        self.reg_by.delete(0, 'end')
        self.date_reg.delete(0, 'end')


if __name__ == '__main__':
    S = Client_Form()
    S.mainloop()
