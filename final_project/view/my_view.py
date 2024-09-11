import tkinter
import tkinter.ttk
import tkinter.messagebox
from final_project.db.client_db import *
from final_project.db.room_db import *
from final_project.entity.client import *
from final_project.entity.room import *
from final_project.tools.logger import *
import datetime


class FirstWindow:
    def __init__(self):
        self.client_db = ClientDb()
        self.window = tkinter.Tk()
        self.window.geometry("550x400")
        self.window.title("Personal Info")
        self.window.config(background="grey20")
        self.current_info = None
        self.max_id = None
        self.ids = None

        # Additional Text!!!
        tkinter.Label(self.window, text="Welcome to Hotel Transylvania reservation system!", font=("Arial Black", 12),
                      bg="grey20",
                      fg="grey63").place(x=36, y=0)
        tkinter.Label(self.window, text="Done?Let's go for other info!\nDon't forget to save your info!",
                      font=("Arial Black", 10), bg="grey20", fg="grey63").place(x=0, y=250)

        # Name
        tkinter.Label(self.window, text="Name", bg="grey20", fg="grey63").place(x=0, y=50)
        self.name = tkinter.StringVar()
        tkinter.Entry(self.window, textvariable=self.name, bg="grey20", fg="grey63").place(x=80, y=50)
        # Family
        tkinter.Label(self.window, text="Family", bg="grey20", fg="grey63").place(x=0, y=100)
        self.family = tkinter.StringVar()
        tkinter.Entry(self.window, textvariable=self.family, bg="grey20", fg="grey63").place(x=80, y=100)
        # Birthdate
        tkinter.Label(self.window, text="Birthdate", bg="grey20", fg="grey63").place(x=0, y=150)
        self.birth_date = tkinter.StringVar()
        tkinter.Entry(self.window, textvariable=self.birth_date, bg="grey20", fg="grey63").place(x=80, y=150)
        # Gender
        tkinter.Label(self.window, text="Gender", bg="grey20", fg="grey63").place(x=300, y=50)
        self.gender = tkinter.StringVar()
        tkinter.Radiobutton(self.window, text="Male", variable=self.gender, value="Male", bg="grey20",
                            fg="grey63").place(x=378, y=50)
        tkinter.Radiobutton(self.window, text="Female", variable=self.gender, value="Female", bg="grey20",
                            fg="grey63").place(x=448, y=50)
        # Nationality
        tkinter.Label(self.window, text="Nationality", bg="grey20", fg="grey63").place(x=300, y=100)
        self.nationality = tkinter.StringVar()
        tkinter.Entry(self.window, textvariable=self.nationality, bg="grey20", fg="grey63").place(x=380, y=100)
        # NationalId
        tkinter.Label(self.window, text="NationalId", bg="grey20", fg="grey63").place(x=300, y=150)
        self.national_id = tkinter.StringVar()
        tkinter.Entry(self.window, textvariable=self.national_id, bg="grey20", fg="grey63").place(x=380, y=150)
        # start_date
        tkinter.Label(self.window, text="StartDate", bg="grey20", fg="grey63").place(x=0, y=200)
        self.start_date = tkinter.StringVar()
        tkinter.Entry(self.window, textvariable=self.start_date, bg="grey20", fg="grey63").place(x=80, y=200)
        # end_date
        tkinter.Label(self.window, text="EndDate", bg="grey20", fg="grey63").place(x=300, y=200)
        self.end_date = tkinter.StringVar()
        tkinter.Entry(self.window, textvariable=self.end_date, bg="grey20", fg="grey63").place(x=380, y=200)
        # Button
        tkinter.Button(self.window, text="Next", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.next_button).place(x=3, y=300)

        tkinter.Button(self.window, text="Save", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.save_button).place(x=43, y=300)

        tkinter.Button(self.window, text="Want to Edit", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.edit_button).place(x=83, y=300)
        tkinter.Button(self.window, text="Edit is Done", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.edit_done).place(x=163, y=300)
        tkinter.Button(self.window, text="Cancel", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.cancel).place(x=243, y=300)
        self.window.mainloop()

    def save_button(self):
        client = Client(self.name.get(), self.family.get(), self.birth_date.get(), self.gender.get(),
                        self.nationality.get(), self.national_id.get(), self.max_id, self.start_date.get(),
                        self.end_date.get())
        self.client_db.save(client)
        self.current_info = [self.name.get(), self.family.get(), self.birth_date.get(), self.gender.get(),
                             self.nationality.get(), self.national_id.get(), self.start_date.get(), self.end_date.get()]
        self.reset_form()
        tkinter.messagebox.showinfo("Saved Successfully!", f"Your info has been saved successfully!")

    def edit_button(self):
        self.name.set(self.current_info[0])
        self.family.set(self.current_info[1])
        self.birth_date.set(self.current_info[2])
        self.gender.set(self.current_info[3])
        self.nationality.set(self.current_info[4])
        self.national_id.set(self.current_info[5])
        self.start_date.set(self.current_info[6])
        self.end_date.set(self.current_info[7])
        self.ids = self.client_db.find_id()
        self.max_id = max(self.ids)

    def edit_done(self):
        try:
            client = Client(self.name.get(), self.family.get(), self.birth_date.get(), self.gender.get(),
                            self.nationality.get(), self.national_id.get(), self.max_id,
                            self.start_date.get(), self.end_date.get())
            self.client_db.edit(client, self.max_id)
            tkinter.messagebox.showinfo(title="Edit", message="Client Edited")
            logging.info(f"Client Edited {client}")
        except Exception as e:
            tkinter.messagebox.showerror("Edit Error", str(e))
            logging.error("Client Edited")

    def reset_form(self):
        self.name.set("")
        self.family.set("")
        self.birth_date.set("")
        self.nationality.set("")
        self.national_id.set("")
        self.start_date.set("")
        self.end_date.set("")

    def cancel(self):
        self.name.set(self.current_info[0])
        self.family.set(self.current_info[1])
        self.birth_date.set(self.current_info[2])
        self.gender.set(self.current_info[3])
        self.nationality.set(self.current_info[4])
        self.national_id.set(self.current_info[5])
        self.start_date.set(self.current_info[6])
        self.end_date.set(self.current_info[7])
        self.client_db.remove(self.max_id)
        tkinter.messagebox.showinfo(title="cancel reservation", message="CANCELED")
        self.reset_form()

    def next_button(self):
        if self.current_info:
            self.window.destroy()
            second_window = SecondWindow(self.current_info[7])
        else:
            tkinter.messagebox.showerror("Info Error", "Please Enter Your Info")


class SecondWindow:
    def __init__(self, end_date):
        self.room_db = RoomDb()
        self.win = tkinter.Tk()
        self.win.geometry("550x300")
        self.win.title("Room Info")
        self.win.config(background="grey20")
        tkinter.Label(self.win, text="Let's find an appropriate room for you!", font=("Arial Black", 10),
                      bg="grey20", fg="grey63").place(x=36, y=0)
        self.kitchen_num = 20
        self.max_id = None
        self.ids = None
        self.current_info = None
        self.end_date = end_date
        # Bed
        tkinter.Label(self.win, text="Bed", bg="grey20", fg="grey63").place(x=0, y=50)
        self.bed = tkinter.StringVar()
        tkinter.Radiobutton(self.win, text="One", variable=self.bed, value="One", background="grey20",
                            foreground="grey63").place(x=80, y=50)
        tkinter.Radiobutton(self.win, text="Two", variable=self.bed, value="Two", background="grey20",
                            foreground="grey63").place(x=140, y=50)
        # Tv
        tkinter.Label(self.win, text="Tv", bg="grey20", fg="grey63").place(x=0, y=100)
        self.tv = tkinter.StringVar()
        tkinter.Radiobutton(self.win, text="Yes", variable=self.tv, value="Yes", background="grey20",
                            foreground="grey63").place(x=80, y=100)
        tkinter.Radiobutton(self.win, text="No", variable=self.tv, value="No", background="grey20",
                            foreground="grey63").place(x=140, y=100)
        # Refrigerator
        tkinter.Label(self.win, text="Refrigerator", bg="grey20", fg="grey63").place(x=0, y=150)
        self.refrigerator = tkinter.StringVar()
        tkinter.Radiobutton(self.win, text="Yes", variable=self.refrigerator, value="Yes", background="grey20",
                            foreground="grey63").place(x=80, y=150)
        tkinter.Radiobutton(self.win, text="No", variable=self.refrigerator, value="No", background="grey20",
                            foreground="grey63").place(x=140, y=150)
        # Room Service
        tkinter.Label(self.win, text="Room Service", bg="grey20", fg="grey63").place(x=280, y=50)
        self.room_service = tkinter.StringVar()
        tkinter.Radiobutton(self.win, text="Yes", variable=self.room_service, value="Yes", background="grey20",
                            foreground="grey63").place(x=360, y=50)
        tkinter.Radiobutton(self.win, text="No", variable=self.room_service, value="No", background="grey20",
                            foreground="grey63").place(x=420, y=50)
        # Kitchen
        tkinter.Label(self.win, text="Kitchen", bg="grey20", fg="grey63").place(x=280, y=100)
        self.kitchen = tkinter.StringVar()
        tkinter.Radiobutton(self.win, text="Yes", variable=self.kitchen, value="Yes", background="grey20",
                            foreground="grey63").place(x=360, y=100)
        tkinter.Radiobutton(self.win, text="No", variable=self.kitchen, value="No", background="grey20",
                            foreground="grey63").place(x=420, y=100)
        if self.kitchen_num == 0:
            tkinter.messagebox.showinfo("Kitchen", "Not Available At Current Time!")
        if self.kitchen == "Yes":
            self.kitchen_num -= 1
        if datetime.date.today() == self.end_date:
            self.kitchen += 1

        # Phone
        tkinter.Label(self.win, text="Phone", bg="grey20", fg="grey63").place(x=280, y=150)
        self.phone = tkinter.StringVar()
        tkinter.Radiobutton(self.win, text="Yes", variable=self.phone, value="Yes", background="grey20",
                            foreground="grey63").place(x=360, y=150)
        tkinter.Radiobutton(self.win, text="No", variable=self.phone, value="No", background="grey20",
                            foreground="grey63").place(x=420, y=150)
        # Button
        tkinter.Button(self.win, text="Next", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.next_button).place(x=3, y=210)
        tkinter.Button(self.win, text="Save", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.save_button).place(x=40, y=210)
        tkinter.Button(self.win, text="Want to Edit", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.edit_button).place(x=80, y=210)
        tkinter.Button(self.win, text="Edit is Done", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.edit_done).place(x=160, y=210)
        tkinter.Button(self.win, text="Back", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.back).place(x=240, y=210)
        self.win.mainloop()

    def edit_button(self):
        self.ids = self.room_db.find_id()
        self.max_id = max(self.ids)
        self.bed.set("")
        self.tv.set("")
        self.refrigerator.set("")
        self.room_service.set("")
        self.kitchen.set("")
        self.phone.set("")

    def edit_done(self):
        try:
            room = Room(self.bed.get(), self.tv.get(), self.refrigerator.get(), self.room_service.get(),
                        self.kitchen.get(), self.phone.get(), self.max_id)

            self.room_db.edit(room)

            tkinter.messagebox.showinfo(title="Edit", message="Person Edited")
            logging.info(f"Room Edited {room}")

        except Exception as e:
            tkinter.messagebox.showerror("Edit Error", str(e))
            logging.error("Client Edited")

    def save_button(self):
        room = Room(self.bed.get(), self.tv.get(), self.refrigerator.get(), self.room_service.get(),
                    self.kitchen.get(), self.phone.get(), self.max_id)
        self.current_info = [self.bed.get(), self.tv.get(), self.refrigerator.get(), self.room_service.get(),
                             self.kitchen.get(), self.phone.get()]
        self.room_db.save(room)
        tkinter.messagebox.showinfo("Saved Successfully!", f"Your info has been saved successfully!")

    def next_button(self):
        if self.current_info:
            self.win.destroy()
            room = Room(self.bed.get(), self.tv.get(), self.refrigerator.get(), self.room_service.get(),
                        self.kitchen.get(), self.phone.get(), self.max_id)
            self.room_db.save(room)
            third_window = ThirdWindow(self.end_date)
        else:
            tkinter.messagebox.showerror("Info Error", "Please enter your info")

    def cancel(self):
        self.bed.set(self.current_info[0])
        self.tv.set(self.current_info[1])
        self.refrigerator.set(self.current_info[2])
        self.room_service.set(self.current_info[3])
        self.kitchen.set(self.current_info[4])
        self.phone.set(self.current_info[5])
        self.room_db.remove(self.max_id)
        tkinter.messagebox.showinfo(title="cancel reservation", message="CANCELED")
        self.bed.set("")
        self.tv.set("")
        self.refrigerator.set("")
        self.room_service.set("")
        self.kitchen.set("")
        self.phone.set("")

    def back(self):
        self.win.destroy()
        first_window = FirstWindow()


class ThirdWindow:
    def __init__(self, end_date):
        self.client_db = ClientDb()
        self.window = tkinter.Tk()
        self.window.geometry("300x200")
        self.window.title("Personal Info")
        self.window.config(background="grey20")
        self.end_date = end_date

        # Additional Text!!!
        tkinter.Label(self.window, text="Successfully Reserved!\nEnjoy your time in our hotel!",
                      font=("Arial Black", 12),
                      bg="grey20",
                      fg="grey63").place(x=0, y=0)
        # Button
        tkinter.Button(self.window, text="Back", font=("Arial Black", 7), bg="grey20",
                       fg="grey63", command=self.back).place(x=0, y=100)

    def back(self):
        self.window.destroy()
        second_window = SecondWindow(self.end_date)
