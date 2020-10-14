from tkinter import *
import pandas as pd

global dat

dat = pd.read_xlsx("용어사전예2_20200916.xlsx")


# 사전에서 단어를 찾아 뜻을 보여준다.
def click():
    word = entry.get()  # 우리가 입력한 단어.

    # 특정 시작 지점부터 텍스트 엔트리 위젯의 끝까지(END) 지우겠다.
    output.delete(0.0, END)  # (결과) 텍스트 박스을 지워준다.

    try:
        # def_word = dict_all[word]
        # def_word = dat.loc[행, 열]
        def_word = dat.loc[dat['한글단어이름'] == word, '한글내용'].values[0]

    except:
        def_word = "단어의 뜻을 찾을 수 없다."

    # END : 문자열이 입력된 최종 지점을 의미한다.
    output.insert(END, def_word)


# 메인
w = Tk()
w.title("My Dictionary")

# 설명 레이블
label = Label(w, text="원하는 단어를 입력 후, 엔터키 눌러주세요")
label.grid(row=0, column=0, sticky=W)

# 입력 상자(텍스트 입력) - Entry
entry = Entry(w, width=15, bg="light green")
entry.grid(row=1, column=0, sticky=W)

# '단어 뜻 확인'  버튼 추가
btn = Button(w, text="뜻 확인", width=5, command=click)
btn.grid(row=2, column=0, sticky=W)

# 설명(뜻 보여주는 상자에 대한) 레이블
label2 = Label(w, text="\n의미:")
label2.grid(row=3, column=0, sticky=W)

# 텍스트 상자 입력
output = Text(w, width=50, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# 단어:뜻 (딕셔너리)
dict_all = {
    '알고리즘': "문제를 푸는 방법",
    '비지도학습': '머신러닝의 한 방법'
}

w.mainloop()
