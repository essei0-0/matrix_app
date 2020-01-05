import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np

def changePage(page):
    page.tkraise()


def topPage(event):
    startPage.tkraise()
    print("enterが押されたのでスタート画面に戻ります")

def createMatrix(page):
    page.tkraise()
    global i1,j1,i2,j2
    i1 = int(rowsNumber1.get())
    j1 = int(columnsNumber1.get())

    global elements1
    elements1 = []
    for i in range(0, i1):
        element = []
        for j in range(0, j1):
            element.append(tk.Entry(page, width=3))
        elements1.append(element)

    for i in range(0, i1):
        for j in range(0, j1):
            elements1[i][j].grid(row=i, column=j)

    i2 = int(rowsNumber2.get())
    j2 = int(columnsNumber2.get())

    global elements2
    elements2 = []
    for i in range(0, i2):
        element = []
        for j in range(0, j2):
            element.append(tk.Entry(page, width=3))
        elements2.append(element)

    for i in range(0, i2):
        for j in range(0, j2):
            elements2[i][j].grid(row=i, column=j+j1+3)

    mulSign = tk.Label(page, text = '×')
    mulSign.grid(row=int((i1+i2-2)/2), column=j1+1)


    if i1 > i2:
        nextRowNum = i1
    else:
        nextRowNum = i2

    nextButton = tk.Button(page, text = 'next', command = lambda : multipulResult(page3))
    nextButton.grid(row=nextRowNum, column=1)

    prevButton = tk.Button(page, text = 'prev', command = lambda : changePage(page1))
    prevButton.grid(row=nextRowNum, column=0)

def multipulResult(page):
    page.tkraise()
    matrix_a = np.array([])
    matrix_b = np.array([])

    for i in range(0, i1):
        for j in range(0, j1):
            matrix_a =  np.append(matrix_a , int(elements1[i][j].get()))

    for i in range(0, i2):
        for j in range(0, j2):
            matrix_b =  np.append(matrix_b , int(elements2[i][j].get()))

    matrix_a = matrix_a.reshape(i1, j1)
    matrix_b = matrix_b.reshape(i2, j2)
    mulResult = matrix_a @ matrix_b
    mulResult = mulResult.tolist()
    print(mulResult[0][0])
    print('--------------------')
    print(matrix_a)
    print('--------------------')
    print(matrix_b)
    print('--------------------')

    print(matrix_a @ matrix_b)
    print(mulResult[0][1])

    mulResultStr = []
    resultElement = []
    for i in range(0, i1):
        for j in range(0, j2):
            mulResultStr.append(str(mulResult[i][j]))
            resultElement.append(tk.Entry(page, width=3))
            resultElement[i][j].insert(tk.END, mulResultStr[i][j])
            resultElement[i][j].grid(row=i, column=j)

    nextButton = tk.Button(page, text = 'next', command = lambda : multipulResult(page3))
    nextButton.grid(row=i1, column=1)

    prevButton = tk.Button(page, text = 'prev', command = lambda : changePage(page3))
    prevButton.grid(row=j2, column=0)

def main():
    root = tk.Tk()
    root.title("matrix_app")
    root.geometry("400x300")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    global startPage
    startPage = tk.Frame(root)
    #lambdaがないとボタンを押す前に関数が呼び出される
    startButton = tk.Button(startPage, text = 'Start', command = lambda : changePage(page1))

    startButton.grid()

    startPage.grid(row=0, column=0, sticky="nsew")


#------------------------------------------------------------
    global page1
    page1 = tk.Frame(root)

    inputNumber = tk.Label(page1, text=u'行と列の数を入力してください')
    inputNumber.grid(columnspan=4)

    global rowsNumber1
    global columnsNumber1
    global rowsNumber2
    global columnsNumber2

    rowsNumber1 = tk.Entry(page1, width=3)
    mulSign = tk.Label(page1, text = '×')
    columnsNumber1 = tk.Entry(page1, width=3)
    text1 = tk.Label(page1, text = u'の行列と')

    rowsNumber1.grid(row=1)
    mulSign.grid(row=1, column=1)
    columnsNumber1.grid(row=1, column=2)
    text1.grid(row=1, column=3)

    rowsNumber2 = tk.Entry(page1, width=3)
    mulSign2 = tk.Label(page1, text = '×')
    columnsNumber2 = tk.Entry(page1, width=3)
    text2 = tk.Label(page1, text = u'の行列の')

    rowsNumber2.grid(row=2)
    mulSign2.grid(row=2, column=1)
    columnsNumber2.grid(row=2, column=2)
    text2.grid(row=2, column=3)

    method = tk.Label(page1, text = u'掛け算を計算する')
    method.grid(row=3, columnspan=4, sticky=tk.W)

    nextButton = tk.Button(page1, text = 'next', command = lambda : createMatrix(page2))
    nextButton.grid(row=4, column=1)

    prevButton = tk.Button(page1, text = 'prev', command = lambda : changePage(startPage))
    prevButton.grid(row=4, column=0)

    page1.grid(row=0, column=0, sticky="nsew")


#----------------------------------------------------
    page2 = tk.Frame(root)


    page2.grid(row=0, column=0, sticky="nsew")

#----------------------------------------------------
    global page3
    page3 = tk.Frame(root)


    page3.grid(row=0, column=0, sticky="nsew")
#------------------------
    startPage.tkraise()

    root.bind('<Return>', topPage)

    root.mainloop()

if __name__ == "__main__":
    main()


"""
#issue
解決
1.page1からpage2に飛ぶときのみに関数createMatrixを実行させる
--------------------------------------------------------
未解決
2.行列の計算結果をframeに表示　→ tk.entry + insert?
3.数字以外の入力がされた場合のエラー処理
4.逆行列、行列式、ランクなどの計算オプション
5.ランダム関数でinputに数字を入力し高速でテストできるようにする
6.inputの操作簡易化　→ ex. 入力したら自動で次の入力欄へ移動する

"""


"""
参考（行列の計算）

rows_number=int(input())
columns_number=int(input())
for i in range(0, columns_number)
    for i in range(0, rows_number)
        element1 = tk.Entry(width=3)
        element1.place(x=100+ rows_number * 3, y=5)

value = element1.get() # エントリに入力されたデータを取得
print("行列を入力してください")

a,b=int(input())

matrix_a = np.array([[a,b],[1,1]])
matrix_b = np.array([[1,1],[1,1]])

mul_result = matrix_a @ matrix_b
mul_text =("行列の乗算の結果は\n{}\nです")
print(mul_text.format(mul_result))
"""
