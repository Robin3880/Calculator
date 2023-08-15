import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("Calculator")
app.geometry("350x500")
app.resizable(False, False)

#button function to show in display
def button_function(x):
    text = label.cget("text")
    label.configure(text= str(text) + str(x))

def button_equals():
    text = label.cget("text")
    result = eval(text)
    label.configure(text=str(result))

def button_reset():
    label.configure(text= "")

def button_backspace():
    text = label.cget("text")
    label.configure(text= text[:-1])
    
#create white background for display
frame = customtkinter.CTkFrame(master=app, width=270, height=70, fg_color="white")
frame.place(relx=0.11, rely=0.2, anchor=customtkinter.W)

#create display
label = customtkinter.CTkLabel(frame, text="", text_color="black", font=("Arial", 24))
label.place(relx=0.875, rely=0.5, anchor=customtkinter.E)

# calculator buttons
button0 = customtkinter.CTkButton(master=app, text="0", command=lambda: button_function(0), width=60)
button0.place(relx=0.4, rely=0.8, anchor=customtkinter.CENTER)

button1 = customtkinter.CTkButton(master=app, text="1", command=lambda: button_function(1), width=60)
button1.place(relx=0.2, rely=0.7, anchor=customtkinter.CENTER)

button2 = customtkinter.CTkButton(master=app, text="2", command=lambda: button_function(2), width=60)
button2.place(relx=0.4, rely=0.7, anchor=customtkinter.CENTER)

button3 = customtkinter.CTkButton(master=app, text="3", command=lambda: button_function(3), width=60)
button3.place(relx=0.6, rely=0.7, anchor=customtkinter.CENTER)

button4 = customtkinter.CTkButton(master=app, text="4", command=lambda: button_function(4), width=60)
button4.place(relx=0.2, rely=0.6, anchor=customtkinter.CENTER)

button5 = customtkinter.CTkButton(master=app, text="5", command=lambda: button_function(5), width=60)
button5.place(relx=0.4, rely=0.6, anchor=customtkinter.CENTER)

button6 = customtkinter.CTkButton(master=app, text="6", command=lambda: button_function(6), width=60)
button6.place(relx=0.6, rely=0.6, anchor=customtkinter.CENTER)

button7 = customtkinter.CTkButton(master=app, text="7", command=lambda: button_function(7), width=60)
button7.place(relx=0.2, rely=0.5, anchor=customtkinter.CENTER)

button8 = customtkinter.CTkButton(master=app, text="8", command=lambda: button_function(8), width=60)
button8.place(relx=0.4, rely=0.5, anchor=customtkinter.CENTER)

button9 = customtkinter.CTkButton(master=app, text="9", command=lambda: button_function(9), width=60)
button9.place(relx=0.6, rely=0.5, anchor=customtkinter.CENTER)

buttonplus = customtkinter.CTkButton(master=app, text="+", command=lambda: button_function("+"), width=60, fg_color="gray", hover_color="dark gray")
buttonplus.place(relx=0.8, rely=0.8, anchor=customtkinter.CENTER)

buttonminus = customtkinter.CTkButton(master=app, text="-", command=lambda: button_function("-"), width=60, fg_color="gray", hover_color="dark gray")
buttonminus.place(relx=0.8, rely=0.7, anchor=customtkinter.CENTER)

buttonx = customtkinter.CTkButton(master=app, text="x", command=lambda: button_function("*"), width=60, fg_color="gray", hover_color="dark gray")
buttonx.place(relx=0.8, rely=0.6, anchor=customtkinter.CENTER)

buttondivide = customtkinter.CTkButton(master=app, text="÷", command=lambda: button_function("/"), width=60, fg_color="gray", hover_color="dark gray")
buttondivide.place(relx=0.8, rely=0.5, anchor=customtkinter.CENTER)

buttonreset = customtkinter.CTkButton(master=app, text="   RESET    ", command=lambda: button_reset(), width=60, fg_color="gray", hover_color="dark gray")
buttonreset.place(relx=0.215, rely=0.4, anchor=customtkinter.CENTER)

buttonbackspace = customtkinter.CTkButton(master=app, text="DEL", command=lambda: button_backspace(), width=60, fg_color="gray", hover_color="dark gray")
buttonbackspace.place(relx=0.8, rely=0.4, anchor=customtkinter.CENTER)


buttondot = customtkinter.CTkButton(master=app, text=".", command=lambda: button_function("."), width=60, fg_color="gray", hover_color="dark gray")
buttondot.place(relx=0.2, rely=0.8, anchor=customtkinter.CENTER)

buttonequals = customtkinter.CTkButton(master=app, text="=", command=lambda: button_equals(), width=60, fg_color="gray", hover_color="dark gray")
buttonequals.place(relx=0.6, rely=0.8, anchor=customtkinter.CENTER)

app.mainloop()

