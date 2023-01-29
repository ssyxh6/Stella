Date: 2023-1-24


# coding: utf-8
from sympy import *
import numpy as np


# import module
from tabulate import tabulate

# assign data
mydata = [{429,"silver"},{"copper",401},{"gold",317},{"aluminum",237},{"iron",80},{"tin",67},{"plumbum",34.8},{"PVC",0.14},{"PP",0.21},{"PE",0.41},{"glass",0.14},{"wood",0.14},{"beton",1.28},{"brick",0.7},{"steel",36}]

# create header
head = ["λ","tpye of material"]

# display table
print(tabulate(mydata,headers = head, tablefmt = "grid"))


 
# Define our symbol
U = symbols('U')
R = symbols('R')
d = symbols('d')
λ = symbols('λ')
r = symbols('r')
# Let's define this equation. The right-hand side has to be equal to 0
eq = U - λ/d
 
# Solve (use program simplification to calculate r formula)
result = solve(eq, r)
 
# print the result
print('r:', result)

d = float(input('the thickness of material(m):'))
λ = float(input('the thermal conductivity of a material(W/(m.k)):'))
U = λ/d
print ('U is equal to :{}'.format(U))