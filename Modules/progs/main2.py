# main2.py

from sys import path

#path.append('..\\packages') #segue estrutura de diretório
path.append('..\\packages\\extrapack.zip') #segue estrutura do zip file

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())
