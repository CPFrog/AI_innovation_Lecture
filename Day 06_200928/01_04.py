from tkinter import *


def click():
    word=entry.get()
    print(word)

    ##
    output.delete(0.0, END)     # 삭제
    output.insert(END, "설명")  # 추가

    def_word=dict_all[word]  # 딕셔너리의 키값을 이용하여 값을 가져옴
    output.insert(END, def_word)


window = Tk()  # 하나의 화면 생성
window.title = "Dictionary"

# 01 입력 상자 설명 레이블
label = Label(window, text="단어 입력 : ")
label.grid(row=0, column=0, sticky='')

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg='light yellow')
entry.grid(row=1, column=0, sticky='')

# 03 제출 버튼 추가
btn = Button(window, text='입력', width=5, command=click)
btn.grid(row=2, column=0, sticky='')

# 04 설명 레이블
label2 = Label(window, text='\n 의미')
label2.grid(row=3, column=0, sticky='')

# 05 텍스트 박스 입력 상자
output = Text(window, width=30, height=6, wrap=WORD, bg="light yellow")
output.grid(row=4, column=0, columnspan=2, sticky='')

# 06 단어, 뜻
dict_all = {"알고리즘": "문제를 해결하는 논리",
            "비지도학습": '머신러닝의 한 방법으로 목표값이 존재하지 않음',
            '딥러닝': '신경망에 은닉층이 1개 이상을 갖는 신경'
            }

window.mainloop()
