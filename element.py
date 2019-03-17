import os
import sys
import pymatgen
from pymatgen.core.periodic_table import Element

try:
    element = str(sys.argv[1])
except:
    pass

label_eng = []
label_jpn = []
with open('datalabel','r') as f:
    for i in f:
        i.rstrip()
        i_sp = i.split(':')
        label_eng.append(i_sp[0])
        label_jpn.append(i_sp[1])

#for x,y in zip(label_eng,label_jpn):
#    print(x + '   ' + y)

def get_ele(element):
    message = ''
    try:
        ele = Element(element)
        data = ele.data
    #    print(data)
        for i in data:
            count = 0
            for label in label_eng:
                if i == label:
                    i_jpn = label_jpn[count]
                    message += i_jpn.rstrip() + ' : ' + str(data[i]) + '\n'
                count += 1
        return(message.rstrip())

    except:
        return('入力された元素記号[' + element + ']に該当するものはありません。')

    if len(element) > 3:
        message = element * 3
        return(message)

    elif (element == 'ヘルプ') or (element == 'help'):
        return('以下の元素情報を取得できます。\nH He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr')

if __name__ == '__main__':
    get_ele()
