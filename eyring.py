#----------------------------------------------------------------------------!
# Calculate Free Energy Barrier ΔF from rate constant using Eyring equation
# Written by: Rahul Verma
#----------------------------------------------------------------------------!
import math as m
import numpy as np

kB = 1.38E-23 # J K^-1
h  = 6.626E-34 #J s
R  = 8.314  # J mol^-1 K^-1
kappa = 1

print("enter rate of the reaction (s^-1)")
k = float(input())  # rate of the reaction in s^-1
print('Reaction temperature (in K)')
T = float(input())
#Eyring equation
#k = kappa*(kBT/h) e{-(DeltaF/RT)}

DeltaF = -R*T*(m.log((k*h)/(kB*T*kappa)))

print("Reaction free energy at", {T}, "K is =", {DeltaF/4.18E3},"kcal/mol")
