from tkinter import *
from tkinter import filedialog

class TextEditor:

    def __init__(self, master):
        self.master = master
        master.title("Text Editor v.2 by rakuzan2weak")

        # Create the text area
        self.text_area = Text(master)
        self.text_area.pack(fill=BOTH, expand=YES)

        # Create the menu bar
        self.menu_bar = Menu(master)
        self.master.config(menu=self.menu_bar)

        # Create the file menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Create the edit menu
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as f:
                self.text_area.delete('1.0', END)
                self.text_area.insert(END, f.read())

    def save_file(self):
        file_path = self.master.filename
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.text_area.get('1.0', END))

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            self.master.filename = file_path
            with open(file_path, 'w') as f:
                f.write(self.text_area.get('1.0', END))

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def select_all(self):
        self.text_area.tag_add(SEL, "1.0", END)
        self.text_area.mark_set(INSERT, "1.0")
        self.text_area.see(INSERT)

root = Tk()
editor = TextEditor(root)
root.mainloop()