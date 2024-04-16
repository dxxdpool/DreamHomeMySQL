import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import mysql.connector as msql

db = msql.connect(host='localhost', user='root', password='Benchmark@25678', database='study')
curs = db.cursor()


class Staff_List(tk.Toplevel):
    def __init__(self, master):
        super().__init__()

        self.b_city = None
        self.tele_no = None
        self.b_no = None
        self.b_address = None
        self.table = None

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
        sub_text = tk.Label(self, text='Staff Listing', font=('Times New Roman', 19), bg='pink')
        sub_text.place(relx=0.46, rely=0.075)

        ttk.Button(self, text='Cancel', command=self.destroy).place(relx=0.70, rely=0.92)
        ttk.Button(self, text='Get List', command=self.get_List).place(relx=0.85, rely=0.92)
        ttk.Button(self, text='Get Branches', command=self.getBranchDetails).place(relx=0.37, rely=0.222)

        self.insert_labels()
        self.insert_Entry()
        self.insert_table()
        self.styling()

    def insert_labels(self):
        tk.Label(self, text='Branch City', bg='pink').place(relx=0.035, rely=0.23)
        tk.Label(self, text='Telephone number(s)', bg='pink').place(relx=0.035, rely=0.29)
        tk.Label(self, text='Branch No', bg='pink').place(relx=0.65, rely=0.23)
        tk.Label(self, text='Branch Address', bg='pink').place(relx=0.65, rely=0.29)

    def insert_Entry(self):
        self.b_city = ttk.Entry(self, width=20)
        self.b_city.place(relx=0.15, rely=0.23)

        self.tele_no = ttk.Entry(self, width=38)
        self.tele_no.place(relx=0.035, rely=0.345)

        self.b_no = ttk.Combobox(self, width=5)
        self.b_no.place(relx=0.76, rely=0.23)

        self.b_address = ttk.Entry(self, width=30)
        self.b_address.place(relx=0.65, rely=0.345)

    def insert_table(self):
        self.table = ttk.Treeview(self, height=9, columns=('StaffNumber', 'Name', 'Position'))

        self.table.column('#0', width=0, stretch=False)
        self.table.heading('#0', text='')

        self.table.heading('StaffNumber', text='Staff Number')
        self.table.heading('Name', text='Name')
        self.table.heading('Position', text='Position')
        self.table.place(relx=0.03, rely=0.46)

        for col in self.table['columns']:
            self.table.column(col, anchor="center")

    def styling(self):
        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.17)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.42)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

    def get_List(self):
        BranchGet = self.b_no.get()
        # print('A' + BranchGet)
        q3 = "select s_no, fname, mname, lname, position from staff where b_no = '{0}';".format(BranchGet)
        # print(q3)
        curs.execute(q3)
        if len(self.table.get_children()) > 0:
            self.table.delete(*self.table.get_children())
        for i in curs.fetchall():
            if i[2] is None:
                self.table.insert('', 'end', values=[i[0], i[1] + " " + i[3], i[4]])
            else:
                self.table.insert('', 'end', values=[i[0], i[1] + " " + i[2] + " " + i[3], i[4]])

    def getBranchDetails(self):
        self.table.delete(*self.table.get_children())
        self.b_no.set('')
        self.tele_no.delete(0, 'end')
        self.b_address.delete(0, 'end')

        text = self.b_city.get()
        query = f"select b_no from branches where b_address like '%{text}%';"
        # print(query)
        curs.execute(query)
        val = []
        for i in curs.fetchall():
            val.append(i[0])
        self.b_no['values'] = val

        def getDetails(event=None):
            self.tele_no.delete(0, 'end')
            self.b_address.delete(0, 'end')
            txt2 = self.b_no.get()
            # print(txt2)
            query1 = f"select phone_no, B_address from telephone_nos natural join branches where b_no = '{txt2}';"
            # print(query1)
            curs.execute(query1)
            numbers = []
            adrs = ""
            details = curs.fetchall()
            print(details)
            for row in details:
                numbers.append(f"{row[0]}")
                adrs = row[1]
            num = " / ".join(numbers)

            self.b_address.insert(0, adrs)
            self.tele_no.insert(0, num)

        self.b_no.bind('<<ComboboxSelected>>', getDetails)


if __name__ == '__main__':
    S = Staff_List()
    S.mainloop()
