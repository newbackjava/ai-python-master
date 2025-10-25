from tkinter import *
from tkinter import messagebox


class Cal:
    numstr = []
    result = 0

    def __str__(self):
        return str(self.numstr)

    def plus(self,n1):

        self.result += n1


    def minus(self, n1):
        self.result -= n1



    def multi(self,  n1):
        self.result *= n1


    def div(self,  n1):
        self.result /= n1