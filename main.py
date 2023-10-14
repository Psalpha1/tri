

'''
██████╗ ██╗   ██╗    ██████╗ ███████╗ █████╗ ██╗  ██╗███████╗
██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝██╔════╝
██████╔╝ ╚████╔╝     ██████╔╝█████╗  ███████║ ╚███╔╝ █████╗  
██╔══██╗  ╚██╔╝      ██╔═══╝ ██╔══╝  ██╔══██║ ██╔██╗ ██╔══╝  
██████╔╝   ██║       ██║     ███████╗██║  ██║██╔╝ ██╗███████╗
╚═════╝    ╚═╝       ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝  
'''


from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi
from numpy import array
from random import uniform, randint
from time import time
from os import popen


# SAVE t5_2ULTS IN LOG.txt
def save(file_name, mode, data):
    with open(file_name, mode) as file:
        if mode == 'w':
            file.write(data)


# AFFICHAGE()
def custom_output(n, ch):
    if n > 7 :
        ch = ch[:24] + ' ..'+ ' ]'
    else:
        ch = ch[:len(ch)-2] + ']'
    return ch


# GENERATE RANDOM LISTE
def check(t, i, z):         # Checking For Any Repeated Numbers
    for x in range(i):
        if t[x] == z:
            return False
    return True

def rempli():

    ch = '['
    for i in range(n):
        v= False
        while v == False:
            t[i] = randint(-999999999, 9999999999)
            v = check(t, i, t[i])
        ch += str(t[i]) + ', '
 

    ch= custom_output(n, ch)
    fen.label_1.setText(ch)
    save('unsort/main_list.txt', 'w', str(t))

# LES TRI FUNCTIONS ####################################################


def selection():
    t1 = t.copy()

    start = time()
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if t1[mini] > t1[j]:
                mini = j
        if i != mini :
            aux = t1[i]
            t1[i] = t1[mini]
            t1[mini] = aux
        
    fin = time()
    
    ch = str(t1)
    fen.label_2.setText('Finish in '+str(fin-start)[:20])
    save('sort/selection.txt', 'w', ch)
    

def bulle():
    t2 = t.copy()
    start = time()
    v=False
    while v == False:
        vv = False
        for i in range(n-1):
            if t2[i] > t2[i+1]:
                aux = t2[i]
                t2[i] = t2[i+1]
                t2[i+1] = aux
                vv = True
        v = vv == False
    fin = time()
    ch = str(t2)
    fen.label_3.setText('Finish in '+str(fin-start)[:20])
    save('sort/bulles.txt', 'w', ch)

def insertion():
    t3 = t.copy()
    start = time()
    for i in range(1, n):
        aux = t3[i]
        j = i
        while j > 0 and t3[j-1] > aux:
            t3[j] = t3[j-1]
            j -= 1
        t3[j] = aux
    fin = time()
    ch = str(t3)
    fen.label_4.setText('Finish in '+str(fin-start)[:20])
    save('sort/insertion.txt', 'w', ch)


def shell():
    t4 = t.copy()

    start = time()
    p = 0
    while p < n:
        p = (p * 3) + 1
    
    while p != 0:
        p = p // 3
        for i in range(p, n):
            value = t4[i]
            j = i
            while j > 0 and t4[j-p] > value:
                t4[j] = t4[j-p]
                j -= p
            t4[j] = value
    fin = time()

    fen.label_5.setText('Finish in '+str(fin-start)[:20])
    save('sort/shell.txt', 'w', str(t4))

    

# FUCNTION THAT RETURN valeur MAX=(m=0) OR valeur Min=(m=1)
def indmin(t5_1, n, m):
    mini = 0
    for x in range(n):
        if t5_1[mini] > t5_1[x] and m == 1:
            mini = x
        elif t5_1[mini] < t5_1[x] and m == 0:
            mini = x
    return mini


def creation():
    t5_1 = t.copy()
    t5_2 = array([int]*n)

    start = time()

    x = indmin(t5_1, n, 1) # Min Indice Valeur mode = 1
    
    y = indmin(t5_1, n, 0) # Max Indice Valeur mode = 0
    

    t5_2[0] = t5_1[x]
    for i in range(1, n):
        mini = t5_1[y]
        for j in range(n):
            if t5_1[j]<= mini and t5_1[j] > t5_2[i-1] :
                mini = t5_1[j]
                x = j
            t5_2[i] = t5_1[x]

    fin = time()
    
    fen.label_7.setText('Finish in '+str(fin-start)[:20])
    save('sort/creation.txt', 'w', str(t5_2))


# A Function That Returns A Number Of Specified Recurring Numbers
def occur(t6_1, i, n):
    oc = 0
    for x in range(n):
        if i == t6_1[x]:
            oc += 1
    return oc



def comptage():
    t6_1 = t.copy()

    if  not str(t6_1[0]).isdecimal() :
        fen.label_6.setText('[Error] Positive Integers Only !')
        return 
    
        
    start = time()
    maxi = t6_1[indmin(t6_1, n, 0)]

    if maxi > 2000:
        fen.label_6.setText('[Error] Large Liste ['+str(maxi)+'] !')
        return
    
    t6_2 = array([int]*(maxi+1))

    for k in range(maxi+1):
        t6_2[k] = 0

    for i in range(maxi+1):
        t6_2[i] = occur(t6_1, i, n)
    
    i = 0
    for j in range(maxi+1):
        if j != 0 :
            for k in range(t6_2[j]):
                t6_1[i] = j
                i += 1
    fin = time()
    
    fen.label_6.setText('Finish in '+str(fin-start)[:20])
    save('sort/comptage.txt', 'w', str(t6_1))


#########################################################################



# RUN ALL FUNCTIONs
def run_all():
    selection()
    bulle()
    insertion()
    shell()
    creation()
    comptage()


# CLEAR ALL OUTPUTS AND log FILES
def t5_2et():
    # fen.label_1.setText('')
    fen.label_2.setText('')
    fen.label_3.setText('')
    fen.label_4.setText('')
    fen.label_5.setText('')
    fen.label_6.setText('')
    fen.label_7.setText('')

    
    file_path = [r'del .\unsort\main_list.txt', r'del .\sort\shell.txt', r'del .\sort\comptage.txt', r'del .\sort\selection.txt', r'del .\sort\bulles.txt', r'del .\sort\insertion.txt', r'del .\sort\creation.txt']
    create_new_file_path = ['echo '' >  .\\unsort\\main_list.txt', 'echo '' >  .\\sort\\shell.txt', 'echo '' >  .\\sort\\comptage.txt', 'echo '' >  .\\sort\\selection.txt', 'echo '' >  .\\sort\\bulles.txt', 'echo '' >  .\\sort\\insertion.txt', 'echo '' >  .\\sort\\creation.txt']

    for file in file_path:
        popen(file)
    for new_file in create_new_file_path:
        popen(new_file)

# PARAMETER FOR Horizontal Slider. Get value(n) and set to global varaible also Table(t)
def setSize():
    global t, n
    n = fen.h_slider.value()

    t=array([int]*n)
    rempli()
    fen.label_n.setText(str(n))


##########Program Principal##############
app = QApplication([])
fen = loadUi('app.ui')

    #====> GLObal Variables <=====#
n = 1
t=array([int]*n)
    #=============================#

#BUTTONS SETTINGS
fen.btn_gen.clicked.connect(rempli)
fen.btn1.clicked.connect(selection)
fen.btn2.clicked.connect(bulle)
fen.btn3.clicked.connect(insertion)
fen.btn4.clicked.connect(shell)
fen.btn5.clicked.connect(comptage)
fen.btn6.clicked.connect(creation)

fen.btn_all.clicked.connect(run_all)
fen.btn_clear.clicked.connect(t5_2et)

fen.h_slider.valueChanged.connect(setSize)

#OPEN LOG FILES 
fen.log_liste.clicked.connect(lambda : popen(r'C:\Windows\system32\notepad.exe unsort\main_list.txt'))
fen.log_selection.clicked.connect(lambda : popen(r'C:\Windows\system32\notepad.exe sort\selection.txt'))
fen.log_bulles.clicked.connect(lambda : popen(r'C:\Windows\system32\notepad.exe sort\bulles.txt'))
fen.log_shell.clicked.connect(lambda : popen(r'C:\Windows\system32\notepad.exe sort\shell.txt'))
fen.log_creation.clicked.connect(lambda : popen(r'C:\Windows\system32\notepad.exe sort\creation.txt'))
fen.log_comptage.clicked.connect(lambda : popen(r'C:\Windows\system32\notepad.exe sort\comptage.txt'))


# LAUNCH THE PROGRAM
fen.show()
app.exec_()

