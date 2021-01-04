"""
어떻게 하나하나 코드로 디자인을 하고 있을까요? 굉장히 번거로운 일이 아닐 수 없습니다.

Qt Designer 프로그램을 이용해서 윈도우를 손쉽게 디자인해봅시다.
아나콘다를 설치했던 디렉터리에 그것이 있습니다.
C:\Anaconda3\Library\bin

또는 아나콘다 프롬프트창에서 designer를 입력하여 실행시킬 수 있습니다.
"""

import sys, math
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
form_class = uic.loadUiType("rechner.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.entry = []
        self.entry1 = []


        if self.numpad0.clicked:
            self.numpad0.clicked.connect(lambda :self.lcdNum_print(self.numpad0.text()))
        if self.numpad1.clicked:
            self.numpad1.clicked.connect(lambda :self.lcdNum_print(self.numpad1.text()))
        if self.numpad2.clicked:
            self.numpad2.clicked.connect(lambda :self.lcdNum_print(self.numpad2.text()))
        if self.numpad3.clicked:
            self.numpad3.clicked.connect(lambda :self.lcdNum_print(self.numpad3.text()))
        if self.numpad4.clicked:
            self.numpad4.clicked.connect(lambda :self.lcdNum_print(self.numpad4.text()))
        if self.numpad5.clicked:
            self.numpad5.clicked.connect(lambda :self.lcdNum_print(self.numpad5.text()))
        if self.numpad6.clicked:
            self.numpad6.clicked.connect(lambda :self.lcdNum_print(self.numpad6.text()))
        if self.numpad7.clicked:
            self.numpad7.clicked.connect(lambda :self.lcdNum_print(self.numpad7.text()))
        if self.numpad8.clicked:
            self.numpad8.clicked.connect(lambda :self.lcdNum_print(self.numpad8.text()))
        if self.numpad9.clicked:
            self.numpad9.clicked.connect(lambda :self.lcdNum_print(self.numpad9.text()))

        if self.equal.clicked:
            self.equal.clicked.connect(lambda :self.lcdNum_print(self.equal.text()))
        if self.plus.clicked:
            self.plus.clicked.connect(lambda :self.lcdNum_print(self.plus.text()))
        if self.minus.clicked:
            self.minus.clicked.connect(lambda :self.lcdNum_print(self.minus.text()))
        if self.multi.clicked:
            self.multi.clicked.connect(lambda :self.lcdNum_print(self.multi.text()))
        if self.div.clicked:
            self.div.clicked.connect(lambda :self.lcdNum_print('/'))
        if self.mod.clicked:
            self.mod.clicked.connect(lambda :self.lcdNum_print('mod'))
        if self.square.clicked:
            self.square.clicked.connect(lambda :self.lcdNum_print('square'))
        if self.sqrt.clicked:
            self.sqrt.clicked.connect(lambda :self.lcdNum_print('sqrt'))
        if self.dot.clicked:
            self.dot.clicked.connect(lambda :self.lcdNum_print('.'))
        if self.split.clicked:
            self.split.clicked.connect(lambda :self.lcdNum_print('split'))
        if self.addNot.clicked:
            self.addNot.clicked.connect(lambda :self.lcdNum_print('addNot'))
        if self.back.clicked:
            self.back.clicked.connect(lambda :self.lcdNum_print('BACK'))
        if self.clear.clicked:
            self.clear.clicked.connect(lambda :self.lcdNum_print('C'))
        if self.clearEnt.clicked:
            self.clearEnt.clicked.connect(lambda :self.lcdNum_print('CE'))

    ''' self.actionNew.toggled(self.backward('C'))
        self.actionExit.toggled(sys.exit())'''

    def lcdNum_print(self, what):
        print(self.entry)

        numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if what in numList: #입력값이 숫자인 경우
            self.entry.append(what)
            self.make_number()
        elif what in ['+', '-', '*', '/', '%']: #사칙연산 연산자인 경우
            self.calculator(what)
        elif what in ['square', 'sqrt', 'split', '.', 'addNot']: #다른 연산자인 경우
            self.cal_now(what)
        elif what in ['C', 'CE', 'BACK']: #지우는 버튼인 경우
            self.backward(what)
        elif what == '=': # 결론 버튼
            self.finish()
        else:
            pass

    def show_lcds(self): # 화면 표시
        print(self.entry, '쇼엘시디스')
        if len(self.entry) > 0:
            if self.entry[0] =='':
                a ='0'
            else:
                a = self.entry[0][:5]
                print(a)
                if (float(a)%1) == 0:
                    #self.entry[0] = str(int(float(self.entry[0])))
                    a = str(int(float(a)))
        else:
            a = '0'
        print(a)
        self.lcdNum1.display(a)
        print('디스플레이')

        if len(self.entry1) > 0:
            b = ''.join(self.entry1)[:5]
        else:
            b = '0'
        self.lcdNum2.display(b)


    def make_number(self): # 숫자 연결 함수
        if len(self.entry)==2:
            print(self.entry)
            if self.entry[-1] not in ['+', '-', '*', '/', '%']:
                prev = self.entry.pop()
                preprev = self.entry.pop()
                new = preprev + prev
                self.entry.append(new)


        if len(self.entry1) >= 2:
            print(self.entry1)
            if self.entry1[-1] in ['+', '-', '*', '/', '%']:
                self.entry[0] = self.entry[-1]
                self.entry1.append(self.entry.pop())

                self.finish()
            else:
                pass
        self.show_lcds()

    def calculator(self, what): #사칙 연산자
        if len(self.entry) == 0: #리스트가 빈 경우
            self.entry.append('0')
            self.entry.append(what)
        else:
            if self.entry[-1] in ['+','-','*','/','%']:
                pass
            else:
                self.entry.append(what)
                for i in self.entry:
                    self.entry1.append(i) # 위쪽 lcd를 위한 엔트리로 복사
        if self.entry.count(['+','-','*','/','%']) >= 2:
            self.finish()
            self.entry = []

        self.show_lcds()


    def cal_now(self, what): # 그외 연산자
        if what == 'square': # 제곱
            self.entry[0] = str(int(self.entry[0])*int(self.entry[0]))
        elif what == 'sqrt': # 제곱근
            self.entry[0] = str(math.sqrt(int(self.entry[0])))
        elif what == 'split': # n 분의 1
            self.entry[0] = str(1/int(self.entry[0]))
        elif what == '.': #소숫점
            if len(self.entry) < 1:
                self.entry.append('0')
            for i in self.entry:
                if '.' not in i:
                    self.entry[0] = str(float(self.entry[0]))[:-1]
        elif what == 'addNot': #음수 양수
            self.entry[0] = str(-float(self.entry[0]))
        else:
            pass
        self.show_lcds()


    def backward(self, what): # 지우는 버튼
        if what == 'C': #전체 리스트 비움
            self.entry = []
            self.entry1 = []
        elif what == 'CE': # Entry 만 비움
            self.entry = []
        elif what == 'BACK': # Entry 마지막 숫자 글자만 제거
            if len(self.entry)>0:
                self.entry[0] = self.entry[0][:-1]
            else:
                self.entry = []
        else:
            pass
        self.show_lcds()

    def finish(self): # 결론 버튼 entry에 있는 값들을 연산해서 entry 첫 값에 저장
        print(self.entry,self.entry1, '피니시')
        operandA = self.entry1.pop(0)
        operator = self.entry1.pop(0)
        operandB = self.entry1.pop(0)
        self.entry = []

        if operator == '+':
            self.entry.append(str(float(operandA) + float(operandB)))
        if operator == '-':
            self.entry.append(str(float(operandA) - float(operandB)))
        if operator == '*':
            self.entry.append(str(float(operandA) * float(operandB)))
        if operator == '/':
            if operandB == '0':
                self.entry.append('ERROR')
            else:
                self.entry.append(str(float(operandA)/float(operandB)))
        if operator == '%':
            self.entry.append(str(float(operandA)%float(operandB)))
        self.show_lcds()



app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
os.system('pause')