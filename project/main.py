from customtkinter import *
from CTkMessagebox import CTkMessagebox
from create_contact import NewContact
from delete_contact import DeleteContact
from show_all_contacts import ShowContact
from search_contacts import SearchContact


class App(CTk):
    def __init__(self):
        super().__init__()

        set_default_color_theme('dark-blue')

        self.title("Contacts")
        self.geometry("450x450")
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.display_msg)

        self.label1 = CTkLabel(
            self,
            text='App Contacts',
            font=("Helvetica", 25),
            text_color="white"
        )
        self.label1.place(x=140, y=15)

        self.button1 = CTkButton(
            self,
            text="Create Contact",
            font=('arial', 18),
            width=210,
            height=60,
            text_color='black',
            fg_color='#41F557',
            hover_color='#0D6418',
            border_width=2,
            border_color='black',
            command=self.create_contact
        )
        self.button1.place(x=120, y=80)

        self.button2 = CTkButton(
            self,
            text="Delete Contact",
            font=('arial', 18),
            width=210,
            height=60,
            text_color='black',
            fg_color='#F33939',
            hover_color='#B52323',
            border_width=2,
            border_color='black',
            command=self.delete_contact
        )
        self.button2.place(x=120, y=170)

        self.button3 = CTkButton(
            self,
            text='Show All Contacts',
            font=('arial', 18),
            width=210,
            height=60,
            text_color='black',
            fg_color='#2E64EA',
            hover_color='#1A44AD',
            border_width=2,
            border_color='black',
            command=self.show_all_contacts
        )
        self.button3.place(x=120, y=260)

        self.button4 = CTkButton(
            self,
            text='Search',
            font=('arial', 18),
            width=210,
            height=60,
            text_color='black',
            fg_color='#DEDB1D',
            hover_color='#A8A60E',
            border_width=2,
            border_color='black',
            command=self.search_contact
        )
        self.button4.place(x=120, y=350)

    def display_msg(self):
        msg = CTkMessagebox(
            title="Exit?",
            message="Do you want to close the program?",
            icon="question",
            option_1="Yes",
            option_2="No"
        )
        response = msg.get()

        if response == "Yes":
            self.destroy()
        else:
            pass

    def create_contact(self):
        NewContact(self)

    def delete_contact(self):
        DeleteContact(self)

    def show_all_contacts(self):
        ShowContact(self)

    def search_contact(self):
        SearchContact(self)


if __name__ == '__main__':
    app = App()
    app.mainloop()
