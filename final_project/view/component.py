import tkinter
import tkinter.ttk
import tkinter.messagebox


class TextWithLabel:
    def __init__(self, window, text, x, y, data_type="str"):
        tkinter.Label(window, text=text, bg="Cyan3").place(x=x, y=y)
        match data_type:
            case "str":
                self.value = tkinter.StringVar()
            case "int":
                self.value = tkinter.IntVar()
            case "float":
                self.value = tkinter.DoubleVar()
            case "bool":
                self.value = tkinter.BooleanVar()
        text_box = tkinter.Entry(window, textvariable=self.value)
        text_box.place(x=x + 70, y=y)

    def get_value(self):
        return self.value.get()
