import tkinter
window = tkinter.Tk()
window.title("Kалькулятор")
window.geometry("300x300")
window.configure(bg = "black")

def add():
    print("Выполняем сложение ")
    num1 = int(text_num1.get()) 
    num2 = int(text_num2.get())
    result = num1 + num2
    output(result)
def sub():
    print("Выполняем вычитание ")
    num1 = int(text_num1.get())
    num2 = int(text_num2.get())
    result = num1 - num2
    output(result)

def mul():
    print("Выполняем умножение ")
    num1 = int(text_num1.get())
    num2 = int(text_num2.get())
    result = num1 * num2
    output(result)

def truediv():
    print("Выполняем деление ")
    num1 = int(text_num1.get())
    num2 = int(text_num2.get())
    if num2 == 0:
        result = "ошибка,деления на ноль"
    else:
        result = num1 / num2
    output(result)
   

def output(result):
    print(result)
    text_answer.delete(0, "end")
    text_answer.insert(0, result)
    text_num1.delete(0, "end")
    text_num2.delete(0, "end")
    
button_add = tkinter.Button(window, text = "+", width = 7, height = 2, command = add, bg = "yellow")
button_add.place(x = 95, y = 110)
button_sub = tkinter.Button(window, text = "-", width = 7, height = 2, command = sub, bg = "yellow")
button_sub.place(x = 160, y = 110)
button_mul = tkinter.Button(window, text = "*", width = 7, height = 2, command = mul, bg = "yellow")
button_mul.place(x = 95, y = 154)
button_truediv = tkinter.Button(window, text = "/", width = 7, height = 2, command = truediv, bg = "yellow")
button_truediv.place(x = 160, y = 154)
text_num1 = tkinter.Entry(window, width = 20)
text_num1.place(x = 95, y = 40)
text_num2 = tkinter.Entry(window, width = 20)
text_num2.place(x = 95, y = 81)
text_answer = tkinter.Entry(window, width = 20)
text_answer.place(x = 95, y = 221)
label_num1 = tkinter.Label(window, text = "Введите первое число:", bg = "silver")
label_num1.place(x = 95, y = 20)
label_num2 = tkinter.Label(window, text = "Введите второе число:", bg = "silver")
label_num2.place(x = 95, y = 61)
label_answer = tkinter.Label(window, text = "Ответ", bg = "silver")
label_answer.place(x = 95, y = 200)















window.mainloop()
