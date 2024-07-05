from customtkinter import CTkToplevel, CTkLabel, CTkButton, CTkEntry, CTkTextbox
from CTkMessagebox import CTkMessagebox
import json
import os
from re import sub

class ShowContact(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.iconify()
        self.title('show all contacts')
        self.geometry('500x500')
        self.resizable(False, False)
        self.textbox = CTkTextbox(
            self,
            width=500,
            height=500,
            fg_color='#31342F',
            text_color='white',
            font=('arial', 18)
        )
        self.textbox.place(x=0, y=0)
        PATH = './data.json'
        if os.path.exists(PATH):
            with open('data.json') as file:
                show_data = json.load(file)
                file.close()

            text = json.dumps(show_data, indent=4).replace('[', '').replace(']', '') \
                .replace('{', '').replace('}', '') \
                .replace('"', '').replace('_', ' ')
            final_text = sub(' +', ' ', text)
            self.textbox.insert("0.0", final_text)
        else:
            CTkMessagebox(
                title="Error",
                message="You have not created a contact",
                icon="cancel",
                option_1="OK"
            )

        self.btn_quit = CTkButton(
            self,
            text='back',
            font=('arial', 15),
            width=145,
            height=25,
            fg_color='#DA3535',
            text_color='black',
            hover_color='#9E0000',
            command=self.quit_showallcontact
        )
        self.btn_quit.place(x=145, y=15)

    def quit_showallcontact(self):
        self.parent.deiconify()
        self.withdraw()