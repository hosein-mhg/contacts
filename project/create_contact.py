from customtkinter import CTkToplevel, CTkLabel, CTkButton, CTkEntry
from CTkMessagebox import CTkMessagebox
import json
import os

data = []
class NewContact(CTkToplevel):
    def __init__(self, parent):
        self.name = None
        self.number = None
        super().__init__(parent)
        self.parent = parent
        # تنظیمات اولیه
        self.parent.iconify()
        self.title("Create Contact")
        self.geometry('500x500')
        self.resizable(False, False)

        self.label1 = CTkLabel(
            self,
            text='Name:',
            font=('arial', 20),
            text_color='white'
        )
        self.label1.place(x=150, y=50)

        self.name_entry = CTkEntry(
            self,
            text_color='#E3E3E3',
            width=170,
            height=32
        )
        self.name_entry.place(x=150, y=80)

        self.label2 = CTkLabel(
            self,
            text='Phone Number:',
            font=('arial', 20),
            text_color='white'
        )
        self.label2.place(x=150, y=135)

        self.phone_entry = CTkEntry(
            self,
            text_color='#E3E3E3',
            width=170,
            height=32
        )
        self.phone_entry.place(x=150, y=165)

        self.btn_save = CTkButton(
            self,
            text='Save',
            font=('arial', 14),
            width=120,
            height=32,
            fg_color='#4BEE27',
            text_color='black',
            hover_color='#126500',
            command=self.add
        )
        self.btn_save.place(x=175, y=250)

        self.btn_quit = CTkButton(
            self,
            text='back',
            font=('arial', 15),
            width=150,
            height=30,
            fg_color='#DA3535',
            text_color='black',
            hover_color='#9E0000',
            command=self.quit_newcontact
        )
        self.btn_quit.place(x=162, y=320)

    def quit_newcontact(self):
        self.parent.deiconify()
        self.withdraw()

    def add(self):
        self.tmp = {}
        self.name = self.name_entry.get()
        self.number = self.phone_entry.get()
        PATH = './data.json'
        if os.path.exists(PATH):
            with open('data.json', 'r+') as file:
                last_data = json.load(file)
                self.tmp['name'] = self.name
                self.tmp['phone_number'] = self.number
                last_data.append(self.tmp)
                file.seek(0)
                json.dump(last_data, file, indent=6)
                file.truncate()
                self.tmp = {}
                file.close()

                CTkMessagebox(title='Success', message="Successfully saved",
                              icon="check", option_1="OK")
                self.name_entry.delete(0, 'end')
                self.phone_entry.delete(0, 'end')


        else:
            self.tmp['name'] = self.name
            self.tmp['phone_number'] = self.number
            data.append(self.tmp)
            self.tmp = {}
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=6)
                file.close()

                CTkMessagebox(title='Success', message="Successfully saved",
                              icon="check", option_1="OK")
                self.name_entry.delete(0, 'end')
                self.phone_entry.delete(0, 'end')

