import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import mysql.connector as msql

db = msql.connect(host='localhost', user='root', password='Benchmark@25678', database='study')
curs = db.cursor()


class Property_Form(tk.Toplevel):
    def __init__(self, master):
        self.p_no = None
        self.type = None
        self.rooms = None
        self.rent = None
        self.address = None
        self.owner_no = None
        self.b_name = None
        self.b_address = None
        self.tele_no = None
        self.b_type = None
        self.b_cont_name = None
        self.staff_manage = None
        self.branch_address = None

        super().__init__()
        self.geometry('640x480+448+192')
        self.config(bg='pink')
        self.title('Staff Registration')
        self.resizable(False, False)

        self.iconbitmap('DreamHome Logo.ico')

        self.I = Image.open("C:/Users/Welcome/Desktop/MiniProject/DreamHome Logo Final.png")
        self.res_img = self.I.resize((70, 70))
        self.l = ImageTk.PhotoImage(self.res_img)
        l_label = tk.Label(self, image=self.l, bg='pink')
        l_label.place(relx=0.0, rely=0.0)

        text = tk.Label(self, text='DreamHome', font=('Times New Roman', 20), bg='pink')
        text.place(relx=0.45, rely=0.010)
        sub_text = tk.Label(self, text='Property Registration Form', font=('Times New Roman', 19), bg='pink')
        sub_text.place(relx=0.35, rely=0.075)

        self.insert_labels()
        self.insert_Entry()
        self.styling()

        ttk.Button(self, text='Cancel', command=self.destroy).place(relx=0.70, rely=0.92)
        ttk.Button(self, text='Next', command=self.InsertIntoPropertyInfo).place(relx=0.85, rely=0.92)
        ttk.Button(self, text='Clear', command=self.clearForm).place(relx=0.035, rely=0.919)
        # ttk.Button(self, text='New User', command=self.createUser).place(relx=0.84, rely=0.225)

        query = "select case when mname is not null then concat(fname, ' ', mname, ' ', lname) else concat (fname, " \
                "' ', lname) end as full_name from staff natural join branches;"
        curs.execute(query)
        staff_names = [row[0] for row in curs.fetchall()]
        self.staff_manage['values'] = staff_names
        self.staff_manage.bind("<<ComboboxSelected>>", self.get_StaffDetails)

        query = "select o_no from owners;"
        curs.execute(query)
        owners_id = [row[0] for row in curs.fetchall()]
        self.owner_no['values'] = owners_id
        self.owner_no.bind("<<ComboboxSelected>>", self.get_OwnerDetails)

    def styling(self):
        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.17)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=320, height=0.5, bg='black')
        cv.place(relx=0.5, rely=0.55)
        cv.create_line(320, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.74)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.87)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=0.5, height=332, bg='black')
        cv.place(relx=0.5, rely=0.17)
        cv.create_line(320, 81.6, 320, 413, fill='pink', width=2)

    def insert_labels(self):
        tk.Label(self, text='Property Number', bg='pink').place(relx=0.035, rely=0.23)
        tk.Label(self, text='Type', bg='pink').place(relx=0.035, rely=0.29)
        tk.Label(self, text='Rooms', bg='pink').place(relx=0.20, rely=0.29)
        tk.Label(self, text='Rent', bg='pink').place(relx=0.035, rely=0.35)
        tk.Label(self, text='Address', bg='pink').place(relx=0.035, rely=0.41)
        tk.Label(self, text='Owner Number', bg='pink').place(relx=0.535, rely=0.23)
        tk.Label(self, text='Person/Business Name', bg='pink').place(relx=0.535, rely=0.29)
        tk.Label(self, text='Address', bg='pink').place(relx=0.535, rely=0.42)
        tk.Label(self, text='Tele No', bg='pink').place(relx=0.535, rely=0.48)

        tk.Label(self, text='Enter Details where applicable', bg='pink').place(relx=0.535, rely=0.58)
        tk.Label(self, text='Type of Business', bg='pink').place(relx=0.535, rely=0.62)
        tk.Label(self, text='Contact Name', bg='pink').place(relx=0.535, rely=0.67)

        tk.Label(self, text='Managed by Staff', bg='pink').place(relx=0.035, rely=0.76)
        tk.Label(self, text='Registered at branch', bg='pink').place(relx=0.535, rely=0.76)

    def p_no_generator(self):
        query = "select p_no from properties order by p_no desc limit 1"
        curs.execute(query)
        base = curs.fetchall()[0][0]
        num_str = int(base[1:])
        term = base[:-len(str(num_str + 1))] + str(num_str + 1)
        self.p_no.insert(0, term)

    def insert_Entry(self):
        self.p_no = ttk.Entry(self, width=7)
        self.p_no.place(relx=0.20, rely=0.23)
        self.p_no_generator()

        self.type = ttk.Entry(self, width=9)
        self.type.place(relx=0.10, rely=0.29)

        self.rooms = ttk.Entry(self, width=10)
        self.rooms.place(relx=0.28, rely=0.29)

        self.rent = ttk.Entry(self, width=10)
        self.rent.place(relx=0.10, rely=0.35)

        self.address = ttk.Entry(self, width=30)
        self.address.place(relx=0.035, rely=0.46)

        self.owner_no = ttk.Combobox(self, width=12, state='')
        self.owner_no.place(relx=0.68, rely=0.23)

        self.b_name = ttk.Entry(self, width=30)
        self.b_name.place(relx=0.533, rely=0.35)

        self.b_address = ttk.Entry(self, width=35)
        self.b_address.place(relx=0.62, rely=0.42)

        self.tele_no = ttk.Entry(self, width=20)
        self.tele_no.place(relx=0.62, rely=0.48)

        self.b_type = ttk.Entry(self, width=20)
        self.b_type.place(relx=0.70, rely=0.62)

        self.b_cont_name = ttk.Entry(self, width=20)
        self.b_cont_name.place(relx=0.70, rely=0.67)

        self.staff_manage = ttk.Combobox(self, width=30)
        self.staff_manage.place(relx=0.035, rely=0.81)

        self.branch_address = ttk.Entry(self, width=35)
        self.branch_address.place(relx=0.535, rely=0.81)

    def get_StaffDetails(self, event=None):
        self.branch_address.delete(0, 'end')
        get_name = self.staff_manage.get()
        query = f"select b_address from staff natural join branches where case when mname is not null then concat(" \
                f"fname, ' ', mname, ' ', lname) else concat (fname, ' ', lname) end like '{get_name}';"
        curs.execute(query)
        get_branch = curs.fetchall()[0][0]
        self.branch_address.insert(0, get_branch)

    def get_OwnerDetails(self, event=None):
        self.b_name.delete(0, 'end')
        self.b_address.delete(0, 'end')
        self.tele_no.delete(0, 'end')
        self.b_type.delete(0, 'end')
        self.b_cont_name.delete(0, 'end')
        get_o_id = self.owner_no.get()
        query = f"select o_no, case when mname is not null then concat(fname, ' ', mname, ' ', lname) else concat (" \
                f"fname, ' ', lname) end as full_name, o_address, o_phone_no, business_type, contact_name from owners " \
                f"where o_no = '{get_o_id}';"
        curs.execute(query)
        row = curs.fetchall()[0]
        self.b_name.insert(0, row[1])
        self.b_address.insert(0, row[2])
        self.tele_no.insert(0, row[3])
        self.b_type.insert(0, row[4] if row[4] is not None else '-')
        self.b_cont_name.insert(0, row[5] if row[5] is not None else '-')

    def insertIntoForms(self):
        query = "select s_no, b_no from staff natural join branches where case when mname is not null then concat(" \
                "fname, ' ', mname, ' ', lname) else concat (fname, ' ', lname) end like '{0}';".format(self.staff_manage.get())
        curs.execute(query)

        values = [i for i in curs.fetchall()[0]]
        print(values)
        query = "insert into forms (p_no, o_no, managed_by, registered_at) VALUES (%s, %s, %s, %s);"
        values = (self.p_no.get(), self.owner_no.get(), values[0], values[1])
        curs.execute(query, values)
        db.commit()

    def InsertIntoPropertyInfo(self):
        p_no = self.p_no.get()
        type = self.type.get()
        rooms = self.rooms.get()
        rent = self.rent.get()
        address = self.address.get()
        owner_no = self.owner_no.get()
        b_name = self.b_name.get()
        b_address = self.b_address.get()
        tele_no = self.tele_no.get()
        b_type = self.b_type.get()
        b_cont_name = self.b_cont_name.get()
        staff_manage = self.staff_manage.get()
        branch_address = self.branch_address.get()

        result = messagebox.askyesno("Confirm details", "Are the details correct ?")
        if result is True:
            query = "insert into properties (p_no, type, rooms, rent, p_address) VALUES (%s, %s, %s, %s, %s);"
            values = (p_no, type, rooms, rent, address)
            curs.execute(query, values)
            db.commit()
            self.insertIntoForms()
            messagebox.showinfo("Registration", "Successfully Registered")
            self.clearForm()

    def clearForm(self):
        self.p_no.delete(0, 'end')
        self.p_no_generator()
        self.type.delete(0, 'end')
        self.rooms.delete(0, 'end')
        self.rent.delete(0, 'end')
        self.address.delete(0, 'end')
        self.owner_no.delete(0, 'end')
        self.b_name.delete(0, 'end')
        self.b_address.delete(0, 'end')
        self.tele_no.delete(0, 'end')
        self.b_type.delete(0, 'end')
        self.b_cont_name.delete(0, 'end')
        self.staff_manage.delete(0, 'end')
        self.branch_address.delete(0, 'end')


# if __name__ == '__main__':
#     S = Property_Form()
#     S.mainloop()
