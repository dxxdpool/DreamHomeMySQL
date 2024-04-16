import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import mysql.connector as msql

db = msql.connect(host='localhost', user='root', password='Benchmark@25678', database='study')
curs = db.cursor()


class Property_Report(tk.Toplevel):
    def __init__(self, master):
        super().__init__()

        self.p_no = None
        self.type = None
        self.rent = None
        self.p_address = None
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
        sub_text = tk.Label(self, text='Property Viewing Report', font=('Times New Roman', 19), bg='pink')
        sub_text.place(relx=0.36, rely=0.075)

        ttk.Button(self, text='Cancel', command=self.destroy).place(relx=0.70, rely=0.92)
        ttk.Button(self, text='Get Comments', command=self.get_List).place(relx=0.85, rely=0.92)
        ttk.Button(self, text='Get Details', command=self.get_details).place(relx=0.30, rely=0.225)

        self.insert_labels()
        self.insert_Entry()
        self.insert_table()
        self.styling()

    def insert_labels(self):
        tk.Label(self, text='Property Number', bg='pink').place(relx=0.035, rely=0.23)
        tk.Label(self, text='Type', bg='pink').place(relx=0.035, rely=0.29)
        tk.Label(self, text='Rent', bg='pink').place(relx=0.035, rely=0.35)
        tk.Label(self, text='Property Address', bg='pink').place(relx=0.65, rely=0.23)

    def insert_Entry(self):
        self.p_no = ttk.Entry(self, width=7)
        self.p_no.place(relx=0.20, rely=0.23)

        self.type = ttk.Entry(self, width=20)
        self.type.place(relx=0.095, rely=0.29)

        self.rent = ttk.Entry(self, width=15)
        self.rent.place(relx=0.095, rely=0.35)

        self.p_address = ttk.Entry(self, width=30)
        self.p_address.place(relx=0.65, rely=0.29)

    def insert_table(self):
        self.table = ttk.Treeview(self, height=9, columns=('c_no', 'name', 'date', 'comment'))

        self.table.column('#0', width=0, stretch=False)
        self.table.heading('#0', text='')

        self.table.heading('c_no', text='Client no.')
        self.table.heading('name', text='Name')
        self.table.heading('date', text='Date')
        self.table.heading('comment', text='Comments')
        self.table.place(relx=0.03, rely=0.46)

        col = self.table['columns']
        self.table.column(col[0], anchor="center", width=80)
        self.table.column(col[1], anchor="center", width=120)
        self.table.column(col[2], anchor="center", width=96)
        self.table.column(col[3], anchor="center", width=310)

    def styling(self):
        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.17)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

        cv = tk.Canvas(self, width=640, height=0.5, bg='black')
        cv.place(relx=0, rely=0.42)
        cv.create_line(0, 200, 640, 200, fill='pink', width=2)

    def get_details(self):
        self.rent.delete(0, tk.END)
        self.type.delete(0, tk.END)
        self.p_address.delete(0, tk.END)

        P_no_get = self.p_no.get()
        query = "select type, rent, p_address from properties where p_no = '{0}';".format(P_no_get)
        curs.execute(query)
        res = curs.fetchall()
        print(res)
        self.type.insert(0, res[0][0])
        self.rent.insert(0, res[0][1])
        self.p_address.insert(0, res[0][2])

    def get_List(self):
        self.get_details()
        self.table.delete(*self.table.get_children())
        P_no_get = self.p_no.get()
        query = "select c_no, fname, mname, lname, date, comments from report natural join clients where p_no = '{0}';".format(P_no_get)
        curs.execute(query)
        for i in curs.fetchall():
            if i[2] is None:
                self.table.insert('', 'end', values=(i[0], i[1] + " " + i[3], i[4], i[5]))
            else:
                self.table.insert('', 'end', values=(i[0], i[1] + " " + i[2] + " " + i[3], i[4], i[5]))


