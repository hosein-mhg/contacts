from customtkinter import CTkToplevel, CTkLabel, CTkButton, CTkEntry
from CTkMessagebox import CTkMessagebox
import json
import os

class DeleteContact(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.check_msg = None
        self.name_delete = None
        self.del_index = None
        self.notfound_bool = True
        self.parent = parent
        self.parent.iconify()
        self.title('delete contact')
        self.geometry('300x300')
        self.resizable(False, False)

        self.label1 = CTkLabel(
            self,
            text='phone number:',
            font=('arial', 20),
            text_color='white'
        )
        self.label1.place(x=75, y=50)

        self.phone_entry = CTkEntry(
            self,
            text_color='#E3E3E3',
            width=170,
            height=32
        )
        self.phone_entry.place(x=65, y=100)

        self.btn_del = CTkButton(
            self,
            text='Delete',
            font=('arial', 15),
            width=150,
            height=30,
            fg_color='#EA342B',
            text_color='black',
            hover_color='#990700',
            command=self.delete
        )
        self.btn_del.place(x=70, y=160)

        self.btn_quit = CTkButton(
            self,
            text='back',
            font=('arial', 15),
            width=150,
            height=30,
            fg_color='#DC7F16',
            text_color='black',
            hover_color='#8B4A02',
            command=self.quit_deletecontact
        )
        self.btn_quit.place(x=70, y=220)

    def quit_deletecontact(self):
        self.parent.deiconify()
        self.withdraw()

    def delete(self):
        number = self.phone_entry.get()
        PATH = './data.json'
        if os.path.exists(PATH):
            with open('data.json') as file:
                last_data = json.load(file)
                index_data = 0
                is_notfound = 0
                while index_data < len(last_data):
                    save_data = []
                    last_data_copy = last_data.copy()
                    for i in last_data[index_data].values():
                        save_data.append(i)
                    if number in save_data:
                        self.name_delete = last_data[index_data]['name']
                        last_data.pop(index_data)
                        self.check_msg = True
                        self.notfound_bool = False
                        break

                    else:
                        last_data_copy.pop(index_data)
                        index_data += 1
                        save_data = []
                        is_notfound += 1
                        self.notfound_bool = True

                if is_notfound == len(last_data) and self.notfound_bool:
                    self.phone_entry.delete(0, 'end')
                    CTkMessagebox(
                        title="Error",
                        message="Contact not found",
                        icon="warning",
                        option_1="OK"
                    )

            if self.check_msg and self.notfound_bool == False:
                msg = CTkMessagebox(
                    title="Delete?",
                    message=f"Do you want to delete {self.name_delete} contact?",
                    icon="warning",
                    option_1="No",
                    option_2="Yes"
                )
                response = msg.get()
                if response == "Yes":
                    with open('data.json', 'r+') as file:
                        file.seek(0)
                        # print(last_data, '  :dump')
                        json.dump(last_data, file, indent=6)
                        file.truncate()
                        file.close()
                        CTkMessagebox(
                            self,
                            title="Delete",
                            message=f'The contact ({self.name_delete}) was deleted',
                            icon="check",
                            option_1="OK"
                        )
                        self.phone_entry.delete(0, 'end')
                elif response == "No":
                    self.phone_entry.delete(0, 'end')
                else:
                    self.phone_entry.delete(0, 'end')
        else:
            CTkMessagebox(
                title="Error",
                message="You have not created a contact",
                icon="cancel",
                option_1="OK"
            )