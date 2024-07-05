from customtkinter import CTkToplevel, CTkLabel, CTkButton, CTkEntry
from CTkMessagebox import CTkMessagebox
import json
import os

class SearchContact(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.number_search = None
        self.notfound_bool = True
        self.parent.iconify()
        self.title('search contact')
        self.geometry('300x300')
        self.resizable(False, False)

        self.label1 = CTkLabel(
            self,
            text='name:',
            font=('arial', 20),
            text_color='white'
        )
        self.label1.place(x=110, y=53)

        self.name_entry = CTkEntry(
            self,
            text_color='#E3E3E3',
            width=170,
            height=32
        )
        self.name_entry.place(x=65, y=100)

        self.btn_search = CTkButton(
            self,
            text='Search',
            font=('arial', 15),
            width=150,
            height=30,
            fg_color='#3FE6CF',
            text_color='black',
            hover_color='#05A892',
            command=self.search
        )
        self.btn_search.place(x=70, y=160)

        self.btn_quit = CTkButton(
            self,
            text='back',
            font=('arial', 15),
            width=150,
            height=30,
            fg_color='#DC7F16',
            text_color='black',
            hover_color='#8B4A02',
            command=self.quit_search
        )
        self.btn_quit.place(x=70, y=220)

    def quit_search(self):
        self.parent.deiconify()
        self.withdraw()

    def search(self):
        name = self.name_entry.get()
        PATH = './data.json'
        if os.path.exists(PATH):
            with open('data.json') as file:
                search_data = json.load(file)
                index_data = 0
                is_notfound = 0
                while index_data < len(search_data):
                    save_data = []
                    for i in search_data[index_data].values():
                        save_data.append(i)
                    if name in save_data:
                        self.number_search = search_data[index_data]['phone_number']
                        self.notfound_bool = False
                        CTkMessagebox(
                            title="Found",
                            message=f"{name}=> phone number: {self.number_search}",
                            font=("Arial", 14, "bold"),
                            icon="check",
                            option_1="OK"
                        )
                        break

                    else:
                        index_data += 1
                        save_data = []
                        is_notfound += 1
                        self.notfound_bool = True

                if is_notfound == len(search_data) and self.notfound_bool:
                    self.name_entry.delete(0, 'end')
                    CTkMessagebox(
                        title="Error",
                        message="Contact not found",
                        icon="warning",
                        option_1="OK"
                    )
        else:
            CTkMessagebox(
                title="Error",
                message="You have not created a contact",
                icon="cancel",
                option_1="OK"
            )