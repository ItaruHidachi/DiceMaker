#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
from PySide2 import QtWidgets


class DiceMaker(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ダイスソフト")

        self.build_ui()
        self.connect_signal_slot()

    def callback_file_dialog_button_clicked(self):
        if self.combobox.currentIndex() == 0:
            kaimoto = self.line_edit.text()
            strskai,intskai = Dices(kaimoto)
            if self.details_check.isChecked():
                disp = ["{}　⇒ 【{}】:{}".format(kaimoto,intskai,strskai)]
            else:
                disp = ["{}　⇒ 【{}】".format(kaimoto,intskai)]
            self.listwgt.insertItem(0,disp[0])
        elif self.combobox.currentIndex() == 1:
            kaimoto = self.line_edit.text()
            strskai,intskai = Dices(kaimoto)
            if self.details_check.isChecked():
                disp = [kaimoto,"　⇒ 【{}】:{}".format(intskai,strskai)]
            else:
                disp = [kaimoto,"　⇒ 【{}】".format(intskai)]
            self.listwgt.insertItem(0,disp[0])
            self.listwgt.insertItem(1,disp[1])

    def callback_create_dir_button_clicked(self):
        self.listwgt.clear()

    def build_ui(self):
        self.line_edit = QtWidgets.QLineEdit(self)

        self.wordList = ["1d4","1d6","1d10","1d20","1d100","3d6"]
        self.completer = QtWidgets.QCompleter(self.wordList)
        self.line_edit.setCompleter(self.completer)

        self.file_dialog_button = QtWidgets.QPushButton("計算する")
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItems(['1行表示', '2行表示'])
        self.details_check = QtWidgets.QCheckBox()
        self.line = QtWidgets.QFrame()
        self.line.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Sunken)
        self.line2 = QtWidgets.QFrame()
        self.line2.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Sunken)
        self.listwgt = QtWidgets.QListWidget()
        self.create_dir_button = QtWidgets.QPushButton("クリア")

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("式入力", self.line_edit)
        form_layout.addRow("", self.file_dialog_button)
        form_layout.addRow(self.line)
        form_layout.addRow("表示方法", self.combobox)
        form_layout.addRow("詳細表示", self.details_check)
        form_layout.addRow(self.line2)
        form_layout.addRow(self.listwgt)
        form_layout.addRow(self.create_dir_button)
        self.setLayout(form_layout)


    def connect_signal_slot(self):
        self.file_dialog_button.clicked.connect(self.callback_file_dialog_button_clicked)
        self.create_dir_button.clicked.connect(self.callback_create_dir_button_clicked)

def Dice(Ndn):
    int_kai=0
    str_kai=""
    if Ndn.count("d")==1:
        NdnDice = Ndn.split("d")
        str_kai += "("
        for i in range(int(NdnDice[0])):
            rmd = random.randint(1,int(NdnDice[1]))
            int_kai += rmd
            str_kai += str(rmd)
            if i+1 < int(NdnDice[0]):
                str_kai += "+"
        str_kai += ")"
    elif Ndn.count("D")==1:
        NdnDice = Ndn.split("D")
        str_kai += "("
        for cnt in range(int(NdnDice[0])):
            rmd = random.randint(1,int(NdnDice[1]))
            int_kai += rmd
            str_kai += str(rmd)
            if cnt+1 < int(NdnDice[0]):
                str_kai += "+"
        str_kai += ")"
    else:
        try:
            int_kai = float(Ndn)
            str_kai = Ndn
        except(ValueError):
            int_kai=0
            str_kai="Error"
    return int_kai,str_kai

def Dices(Ndns):
    NdnsAns =""
    int_kais = 0
    str_kais = ""
    NdnsKai = Ndns
    NdnsDices = (Ndns.replace("+","_").replace("-","_").replace("*","_").replace("/","_").replace("(","").replace(")","")).split("_")
    for gcnt in range(len(NdnsDices)):
        IntOnce , StrOnce = Dice(NdnsDices[gcnt])
        NdnsAns = NdnsKai.replace(NdnsDices[gcnt],StrOnce,1)
        NdnsKai = NdnsAns
    int_kais = float(eval(NdnsKai))
    if int_kais.is_integer():
        int_kais = int(int_kais)
    else:
        int_kais = int_kais
    str_kais = NdnsKai
    return str_kais,int_kais


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = DiceMaker()
    win.show()
    sys.exit(app.exec_())
