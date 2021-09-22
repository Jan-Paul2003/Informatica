# -*- coding: utf-8 -*-
"""
Spyder Editor

Made by Jan-Paul van der Zouwen
@_janpa 
"""
#Opdracht 2.7 Informatica;
#Voor meer info over de opdracht ga naar itsLearning -> Bronnen -> Python reader. 

import numpy as np


r = 50         #maximale variable in de loop-formule
period = 20    #veranderd de periode (bijv. bij period = 7, uitkomst is dag 42 -49)

random_array = np.random.rand(r)

#loop-formule
for i in range(period,len(random_array)):
    array = random_array[i-period:i]
    

   #print de formule met tekst in de console onder elkaar
    print("Gemiddelde van dag", i-period,"-",i,"is", np.mean(array));


   