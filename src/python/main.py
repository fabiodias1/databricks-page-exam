# -*- coding: utf-8 -*-

from classes.exam import Exam

objExam = Exam()

str_input = ""

objExam.startExam()

while objExam.getStatus() != "F":

    bolR = False

    while bolR == False:

        str_input = input("")

        str_input = str_input[0]

        bolR = objExam.checkUserAnswer(str_input)






