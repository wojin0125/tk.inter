import tkinter as tk

def on_button_click():
    if button["text"]=="클릭":
        button.config(text="닫기")
        label.confing(text="버튼이 클릭되었습니다!")
    else:
        window.destroy()

window = tk.Tk()
window.title("서민재 바보")

label = tk.Label(window, text="버튼을 클릭하세요!", font=('Arial, 14'))
label.pack(pady=20)

button = tk.Button(window, text="클릭", command=on_button_click, font=('Arial', 14))
button.pack(pady=10)

window.mainloop()
