import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk
from Staff_Registration import Staff_Form
from Staff_List import Staff_List
from Property_View import Property_Report
from Property_Registration import Property_Form
from Client_Registration import Client_Form
from Lease_Form import Lease_Form
from Property_Listing import Property_List


class MyApp(tk.Tk):
    def __init__(self, w_width, w_height):
        super().__init__()
        self.resizable(False, False)
        c_x = int((self.winfo_screenwidth() - w_width) / 2)
        c_y = int((self.winfo_screenheight() - w_height) / 2)
        print(c_x, c_y)
        self.geometry(f'{w_width}x{w_height}+{c_x}+{c_y}')
        self.config(bg='white')

        self.title('DreamHome Rental Services')
        self.iconbitmap('DreamHome Logo.ico')

        self.logo = tk.PhotoImage(file="DreamHome Logo Final.png")
        logo_label = tk.Label(self, image=self.logo, bg='white')
        logo_label.grid(row=int(w_width / 2), column=0, padx=5, pady=5)
        logo_label.pack()

        self.T = tk.Label(self, text='DreamHome', font=('Times New Roman', 35), bg='white')
        self.T.pack()

        tk.Label(self, text='Rental Services Pvt Ltd.', font=('Times New Roman', 15), bg='white').pack()

        self.staff = ttk.Button(self, text='Staff registration', command=self.open_StaffForm, padding=(21, 10))
        self.staff_list = ttk.Button(self, text='List of Staff', command=self.open_StaffList, padding=(21, 10))
        self.property = ttk.Button(self, text='Property Registration', command=self.open_PropertyForm, padding=(21, 10))
        self.client = ttk.Button(self, text='Client Registration', command=self.open_ClientForm, padding=(21, 10))
        self.property_listing = ttk.Button(self, text='Property Listing', command=self.open_PropertyList, padding=(21, 10))
        self.property_view = ttk.Button(self, text='View Property', command=self.open_PropertyView, padding=(21, 10))
        self.lease = ttk.Button(self, text='Lease Form', command=self.open_LeaseForm, padding=(21, 10))

        self.staff.place(relx=0.02, rely=0.65)
        self.staff_list.place(relx=0.25, rely=0.65)
        self.property.place(relx=0.45, rely=0.65)
        self.client.place(relx=0.72, rely=0.65)
        self.property_listing.place(relx=0.13, rely=0.76)
        self.property_view.place(relx=0.62, rely=0.76)
        self.lease.place(relx=0.38, rely=0.76)

    def open_StaffForm(self):
        st = Staff_Form(self)
        st.grab_set()

    def open_PropertyView(self):
        pv = Property_Report(self)
        pv.grab_set()

    def open_StaffList(self):
        st = Staff_List(self)
        st.grab_set()

    def open_PropertyForm(self):
        st = Property_Form(self)
        st.grab_set()

    def open_ClientForm(self):
        st = Client_Form(self)
        st.grab_set()

    def open_LeaseForm(self):
        st = Lease_Form(self)
        st.grab_set()

    def open_PropertyList(self):
        st = Property_List(self)
        st.grab_set()


if __name__ == '__main__':
    App = MyApp(640, 480)
    App.mainloop()
