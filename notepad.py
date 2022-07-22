import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm


window = tk.Tk()
window.title("Мой блокнот")
window.geometry("400x400")
file_name = ""


def open_file():
    global file_name
    content_text.delete(1.0, "end")
    file_name = tfd.askopenfilename()
    file_label["text"] = "Файл: " + file_name
    with open(file_name) as file:
        content_text.insert(1.0, file.read())


def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename()
    file_label["text"] = "Файл: " + file_name
    write_to_file(file_name)

def save_file():
    global file_name
    file_label["text"] = "Файл: " + file_name
    if file_name == "":
       save_as_file()
    else:        
        write_to_file(file_name)
   

 
def new_file():
    global file_name
    if tkm.askokcancel("Создание нового файла", "Вы уверены? Несохраненный текст будет удален"):
       file_name = ""
       file_label["text"] = "Файл: " + file_name
       content_text.delete(1.0, "end")

def write_to_file(file_name):
    content = content_text.get(1.0, "end")
    with open (file_name, "w") as file:
        file.write(content)
    



        
content_text = tk.Text(window, wrap = "word")
content_text.place(x = 0, y = 0, relwidth = 1, relheight = 1)
main_menu = tk.Menu(window)
window.configure(menu = main_menu)
file_menu = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "Файл", menu = file_menu)
main_menu.add_cascade(label = "редактировать",menu = file_menu)
file_label = tk.Label(window, text = "Файл: "+ file_name )
file_label.place(x = 0, rely = 1, anchor = "sw")
new_file_icon = tk.PhotoImage(file = "new_.png")
open_file_icon = tk.PhotoImage(file = "open_.png")
save_file_icon = tk.PhotoImage(file = "save_.png")
# Файл
file_menu.add_command(label = "Новый", image = new_file_icon, compound = "left",command = new_file)
file_menu.add_command(label = "Открыть", image = open_file_icon, compound = "left", command = open_file)
file_menu.add_command(label = "Сохранить", image = save_file_icon, compound = "left", command = save_file)
file_menu.add_command(label = "Сохранить как", image = save_file_icon, compound = "left", command = save_as_file)












