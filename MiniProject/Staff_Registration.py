import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import mysql.connector as msql

db = msql.connect(host='localhost', user='root', password='Benchmark@25678', database='study')
curs = db.cursor()


class Staff_Form(tk.Toplevel):
    def __init__(self, master):
        self.s_no = None
        self.f_name = None
        self.m_name = None
        self.l_name = None
        self.gender = None
        self.DOB = None
        self.position = None
        self.salary = None
        self.BranchNo = None
        self.b_address = None
        self.tele_no = None
        self.supervisor = None
        self.DOB_start = None
        self.m_bonus = None

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
        sub_text = tk.Label(self, text='Staff Registration Form', font=('Times New Roman', 19), bg='pink')
        sub_text.place(relx=0.37, rely=0.075)

        self.insert_labels()
        self.insert_Entry()
        self.styling()

        ttk.Button(self, text='Cancel', command=self.destroy).place(relx=0.70, rely=0.92)
        ttk.Button(self, text='Next', command=self.InsertIntoStaffInfo).place(relx=0.85, rely=0.92)
        ttk.Button(self, text='Clear', command=self.clearForm).place(relx=0.035, rely=0.919)

        query = "select b_no from branches order by b_no;"
        curs.execute(query)
        self.BranchNo['values'] = [row[0] for row in curs.fetchall()]

        self.BranchNo.bind('<<ComboboxSelected>>', self.get_BranchDetails)

    def styling(self):
        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.17)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.61)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.86)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=0.5, height=331.2, bg='black')
        cv.place(relx=0.5, rely=0.17)
        cv.create_line(320, 81.6, 320, 412.8, fill='pink', width=2)

    def insert_labels(self):
        tk.Label(self, text='Staff No', bg='pink').place(relx=0.035, rely=0.23)
        tk.Label(self, text='Full Name', bg='pink').place(relx=0.035, rely=0.29)
        tk.Label(self, text='Gender', bg='pink').place(relx=0.035, rely=0.35)
        tk.Label(self, text='DOB', bg='pink').place(relx=0.20, rely=0.35)
        tk.Label(self, text='Position', bg='pink').place(relx=0.035, rely=0.41)
        tk.Label(self, text='Salary', bg='pink').place(relx=0.035, rely=0.47)
        tk.Label(self, text='Branch Number', bg='pink').place(relx=0.60, rely=0.23)
        tk.Label(self, text='Branch Address', bg='pink').place(relx=0.60, rely=0.31)
        tk.Label(self, text='Telephone number(s)', bg='pink').place(relx=0.60, rely=0.42)

        tk.Label(self, text='Enter Details where applicable', bg='pink').place(relx=0.035, rely=0.65)

        tk.Label(self, text='Supervisor Name', bg='pink').place(relx=0.035, rely=0.72)
        tk.Label(self, text='Manager Start Date', bg='pink').place(relx=0.60, rely=0.65)
        tk.Label(self, text='Manager Bonus', bg='pink').place(relx=0.60, rely=0.75)

    def insert_Entry(self):
        self.s_no = ttk.Entry(self, width=5)
        self.s_no.place(relx=0.15, rely=0.23)

        self.f_name = ttk.Entry(self, width=9)
        self.f_name.place(relx=0.15, rely=0.29)

        self.m_name = ttk.Entry(self, width=2)
        self.m_name.place(relx=0.25, rely=0.29)

        self.l_name = ttk.Entry(self, width=9)
        self.l_name.place(relx=0.285, rely=0.29)

        self.gender = ttk.Entry(self, width=2)
        self.gender.place(relx=0.15, rely=0.35)

        self.DOB = ttk.Entry(self, width=10)
        self.DOB.place(relx=0.26, rely=0.35)

        self.position = ttk.Entry(self, width=15)
        self.position.place(relx=0.15, rely=0.41)

        self.salary = ttk.Entry(self, width=12)
        self.salary.place(relx=0.15, rely=0.47)

        self.BranchNo = ttk.Combobox(self, width=5)
        self.BranchNo.place(relx=0.75, rely=0.23)

        self.b_address = ttk.Entry(self, width=35)
        self.b_address.place(relx=0.60, rely=0.36)

        self.tele_no = ttk.Entry(self, width=35)
        self.tele_no.place(relx=0.60, rely=0.47)

        self.supervisor = ttk.Entry(self, width=20)
        self.supervisor.place(relx=0.035, rely=0.78)

        self.DOB_start = ttk.Entry(self, width=10)
        self.DOB_start.place(relx=0.60, rely=0.70)

        self.m_bonus = ttk.Entry(self, width=12)
        self.m_bonus.place(relx=0.60, rely=0.80)

    def get_BranchDetails(self, event=None):
        self.tele_no.delete(0, 'end')
        self.b_address.delete(0, 'end')

        bget = self.BranchNo.get()
        query = f"select b_address, phone_no from branches natural join telephone_nos where b_no = '{bget}'"
        curs.execute(query)
        res = curs.fetchall()

        numbers = []
        adrs = ""

        for row in res:
            numbers.append(f"{row[1]}")
            adrs = row[0]
        num = " / ".join(numbers)

        self.b_address.insert(0, adrs)
        self.tele_no.insert(0, num)

    def InsertIntoStaffInfo(self):
        s_no = self.s_no.get()
        b_no = self.BranchNo.get()
        fname = self.f_name.get()
        mname = self.m_name.get() if self.m_name.get() != "" else None
        lname = self.l_name.get()
        dob = self.DOB.get()
        sex = self.gender.get()
        position = self.position.get()
        salary = self.salary.get()
        supervisor = self.supervisor.get() if self.supervisor.get() != "" else None
        sup_dob = self.DOB_start.get() if self.DOB_start.get() != "" else None
        super_bonus = self.m_bonus.get() if self.m_bonus.get() != "" else None

        result = messagebox.askyesno("Confirm details", "Are the details correct ?")
        if result is True:
            query = "INSERT INTO staff (s_no, b_no, fname, mname, lname, dob, sex, position, salary, supervisor, Manager_start_date, Manager_bonus) " \
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            values = (s_no, b_no, fname, mname, lname, dob, sex, position, salary, supervisor, sup_dob, super_bonus)
            curs.execute(query, values)
            db.commit()
            messagebox.showinfo("Registration", "Successfully Registered")
            self.clearForm()

    def clearForm(self):
        self.f_name.delete(0, 'end')
        self.m_name.delete(0, 'end')
        self.l_name.delete(0, 'end')
        self.gender.delete(0, 'end')
        self.DOB.delete(0, 'end')
        self.position.delete(0, 'end')
        self.salary.delete(0, 'end')
        self.BranchNo.delete(0, 'end')
        self.b_address.delete(0, 'end')
        self.tele_no.delete(0, 'end')
        self.supervisor.delete(0, 'end')
        self.DOB_start.delete(0, 'end')
        self.m_bonus.delete(0, 'end')
        self.s_no.delete(0, 'end')


if __name__ == '__main__':
    S = Staff_Form()
    S.mainloop()
