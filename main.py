from __future__ import print_function
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import random
import math
import mydesign
import random

class Hash(QMainWindow, mydesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.size_mytable()
        self.ok_btn.clicked.connect(self.create_hash)
        self.pushButton.clicked.connect(self.find_in_myhash)
        #self.linear_btn.clicked.connect(self.linear)
        #self.linear_btn.clicked.connect(self.linear)
        #self.linear_btn.clicked.connect(self.linear)

    def size_mytable(self):
        self.size_of_dict = 0
        self.num_5.clicked.connect(self.btn_num5)
        self.num_10.clicked.connect(self.btn_num10)
        self.num_25.clicked.connect(self.btn_num25)
        self.num_50.clicked.connect(self.btn_num50)
        self.num_75.clicked.connect(self.btn_num75)
        self.random_table()

    def btn_num5(self):
        print('=',10000)
        self.size_of_dict = 10000
        self.free_place.setText('10000')
        self.occ_place.setText('0')
    def btn_num10(self):
        print(13000)
        self.size_of_dict = 13000
        self.free_place.setText('13000')
        self.occ_place.setText('0')
    def btn_num25(self):
        print(15000)
        self.size_of_dict = 15000
        self.free_place.setText('15000')
        self.occ_place.setText('0')
    def btn_num50(self):
        print(17000)
        self.size_of_dict = 17000
        self.free_place.setText('17000')
        self.occ_place.setText('0')
    def btn_num75(self):
        print(20000)
        self.size_of_dict = 20000
        self.free_place.setText('20000')
        self.occ_place.setText('0')

    def random_table(self):
        self.fullness = 0
        self.perc_25.clicked.connect(self.btn_perc25)
        self.perc_50.clicked.connect(self.btn_perc50)
        self.perc_70.clicked.connect(self.btn_perc75)
        self.perc_99.clicked.connect(self.btn_perc99)

        self.my_table.setHorizontalHeaderLabels(["Ключ", "Значение"])
        self.my_table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.my_table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)

        #self.my_table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        #self.my_table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        self.create_hash()

    def btn_perc25(self):
        self.fullness = int(self.set_percents(self.size_of_dict, 25))
        self.free_place.setText(str(self.size_of_dict-self.fullness))

        self.occ_place.setText(str(self.fullness))
        print('25%')
    def btn_perc50(self):
        self.fullness = int(self.set_percents(self.size_of_dict, 50))
        self.free_place.setText(str(self.size_of_dict - self.fullness))
        self.occ_place.setText(str(self.fullness))
        print('50%')
    def btn_perc75(self):
        self.fullness = int(self.set_percents(self.size_of_dict, 75))
        self.free_place.setText(str(self.size_of_dict - self.fullness))
        self.occ_place.setText(str(self.fullness))
        print('75%')
    def btn_perc99(self):
        self.fullness = int(self.set_percents(self.size_of_dict, 100))
        self.free_place.setText(str(self.size_of_dict - self.fullness))
        self.occ_place.setText(str(self.fullness))
        print('100%')
    def set_percents(self,value,perc):
        return perc*value/100



    def create_hash(self):
        self.names_for_random = "Матвей,Дмитрий,Максим,Марк,Александр," \
                                "Артем,Андрей,Иван,Владислав,Злата," \
                                "София,Ева,Кира,Яна,Мария," \
                                "Виктория,Анастасия,Полина,Святослав,Доброжир," \
                                "Тихомир,Ратибор,Ярополк,Гостомысл,Велимудр," \
                                "Всеволод,Богдан,Доброгнева,Любомила,Миролюб," \
                                "Светозар,Милонег,Ждан,Неждан,Зотен," \
                                "Matvey,Dmitry,Maxim,Mark,Alexander," \
                                "Artem,Andrey,Ivan,Vladislav,Zlata," \
                                "Sofia,Eva,Kiera,Yana,Maria," \
                                "Victoria,Anastasia,Polina,Svyatoslav," \
                                "Dobrozhyr,Tikhomir,Ratibor,Yaropolk,Gostomysl," \
                                "Vsevolod,Bogdan,Dobrogneva,Lubomila,Mirolyub," \
                                "Svetozar,Miloneg,Zhdan,Nezhdan,Zoten," \
                                "UMatthew,uDmitry,Maxim,Mark,Alexander,Elis"
        self.names_for_random = self.names_for_random.split(',')
        print(len(self.names_for_random))

        self.my_table.setRowCount(self.size_of_dict)
        self.my_hash = []
        self.list_of_keys = []
        self.list_of_values = []
        pust = []
        for i in range(self.fullness):
            my_hash = self.func_for_hash(self.names_for_random[random.randint(0,74)],self.size_of_dict)
            self.list_of_keys.append(my_hash)
            self.my_table.setItem(i, 0, QTableWidgetItem(str(my_hash)))
            value = self.names_for_random[random.randint(0,74)]
            self.my_table.setItem(i, 1, QTableWidgetItem(value))
            self.list_of_values.append(value)
        for i in range(self.size_of_dict-self.fullness):
            pust.append(-7)
        self.allk = self.list_of_keys + pust
        self.allv = self.list_of_values + pust

        print('+',self.my_hash)

    def func_for_hash(self,s,q):
        f = 0
        L = len(s)
        for l in range(L):
            f = f+ord(s[l])*31
        return f%q

    def find_in_myhash(self):
        list_for_find = []
        myid = 0
        stepsLinear = []
        stepsQuadrat = []
        for i in range(self.size_of_dict):
            if self.allk[i] != '':
                stepsLinear.append(self.linear(self.allk[i]))
                print(stepsLinear)
                #stepsQuadrat.append(self.quadraticue(self.allk[i]))

        self.label_4.setText(str(sum(stepsLinear)/len(stepsLinear)))
        print(sum(stepsLinear)/len(stepsLinear))

        #self.label_6.setText(str(sum(stepsQuadrat) / len(stepsQuadrat)))
        #print(sum(stepsQuadrat) / len(stepsQuadrat))

    def linear(self, key):
        step = 1
        count = 0
        sum = 0
        print('-',len(self.list_of_keys))
        for i in range(self.size_of_dict):
            #print(self.list_of_keys[i])
            myid = 0
            id = ((i * step + int(key))%self.size_of_dict)
            #print(id)
            if int(self.allk[id]) > 0:
                if int(key) == int(self.allk[id]):
                    myid += 1
                    return count
            count += 1

    def quadraticue(self, key):
        step = 1
        count = 0
        sum = 0
        for i in range(self.size_of_dict):
            #print(self.list_of_keys[i])
            myid = 0
            id = ((key + (i**2))%self.size_of_dict)
            #print(id)
            if str(key).isdigit():
                if int(key) == int(self.allk[id]):
                    myid += 1
                    return count
            count += 1







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Hash()
    window.setFixedSize(607,457)
    window.show( )
    sys.exit(app.exec_())

