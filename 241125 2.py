import tkinter as t

window = None
display_label = None
expression = ''

# 글자 입력 함수
def press(char):
    global expression
    expression += char
    display_label['text'] = expression

# 글자 지우기 (백스페이스 기능)
def press_backspace():
    global expression
    expression = expression[:-1]  # 마지막 문자 제거
    display_label['text'] = expression

# 키보드 이벤트 처리 함수
def key_press(event):
    char = event.char
    if char.isalpha():  # 알파벳 문자 입력
        press(char)
    elif char == ' ':  # 스페이스바 입력
        press(' ')
    elif event.keysym == 'BackSpace':  # 백스페이스 입력
        press_backspace()

# 타자기 UI 설정 함수
def setup_GUI():
    global window
    global display_label

    window = t.Tk()
    window.title('영어 타자기')
    
    # 텍스트 출력 라벨
    display_label = t.Label(window, text='', anchor='w', relief=t.SUNKEN, width=30, height=3, font='Arial 20')
    display_label.grid(row=0, columnspan=10)

    # 영어 알파벳 버튼들
    buttons = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
        'u', 'v', 'w', 'x', 'y', 'z', ' ', 'BackSpace'
    ]

    row = 1
    col = 0
    for char in buttons:
        if char == 'BackSpace':  # 'BackSpace'는 백스페이스 버튼
            button = t.Button(window, text=char, width=5, height=2, font='Arial 15', command=press_backspace)
        else:  # 각 문자는 press 함수에 연결
            button = t.Button(window, text=char, width=5, height=2, font='Arial 15', command=lambda c=char: press(c))
        
        button.grid(row=row, column=col)
        col += 1
        if col > 9:  # 10개씩 배치되도록 한 줄에 10개의 버튼만 배치
            col = 0
            row += 1
    
    # 키보드 이벤트 바인딩
    window.bind('<Key>', key_press)

setup_GUI()

window.mainloop()
