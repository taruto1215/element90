
import os
import sys
#from pymatgen.core import periodic_table
from pymatgen.core.periodic_table import Element


def get_name():
    
    list = ['Atomic mass','Atomic no','Atomic radius','Atomic radius','Boiling point','Brinell hardness','Bulk modulus','Coefficient of linear thermal expansion','Electronic structure','ICSD oxi\
dation states','Liquid range','Melting point','Melting point','Mineral hardness','Molar volume','Molar volume','Oxidation states','Poissons ratio','Reflectivity','Refractive index','Rigidity modulus','Supercond\
ction temperature','Thermal conductivity', 'Van der waals radius','Velocity of sound','Vickers hardness','X','Youngs modulus','Metallic radius']  

    ele_name = open("element_name","w")

    with open("element_name_from_web","r") as file:
        for i in file:
            i = i.rstrip()
            i = i.split()
            i = i[2]
            ele_name.write(i + "\n")

    ele_name.close()

def main():
    list = ['Atomic mass','Atomic no','Atomic radius','Atomic radius','Boiling point','Brinell hardness','Bulk modulus','Coefficient of linear thermal expansion','Electronic structure','Liquid range','Melting point','Melting point','Mineral hardness','Molar volume','Molar volume','Poissons ratio','Reflectivity','Refractive index','Rigidity modulus','Supercondu\
ction temperature','Thermal conductivity', 'Van der waals radius','Velocity of sound','Vickers hardness','Youngs modulus','Metallic radius']

    f = open("element_name","r")
    ele_list = []
    for i in f:
#        print (i)
        i = i.rstrip()
        ele_list.append(i)
    
    with open("allall","w") as all:
        for j in ele_list:
            j = j.split('"')
        #        print(j[1])
            ele = Element(j[1])
            ele_str = str(ele)
            data = ele.data
            data = str(data)
#            data_str = data['Atomic mass','Atomic no','Atomic radius','Atomic radius','Boiling point','Brinell hardness','Bulk modulus','Coefficient of linear thermal expansion','Electronic structure','ICSD oxidation states','Liquid range','Melting point','Melting point','Mineral hardness','Molar volume','Molar volume','Oxidation states','Poissons ratio','Reflectivity','Refractive index','Rigidity modulus','Superconduction temperature','Thermal conductivity', 'Van der waals radius','Velocity of sound','Vickers hardness','X','Youngs modulus','Metallic radius']
#            data_str = ""
#            for x in list:
#                x = str(x)
#                data_str += str(data[x])
#                data_str += ","
            print(data)
            all.write(ele_str + " " +  data + "\n")


get_name()
main()        
    




