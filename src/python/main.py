# -*- coding: utf-8 -*-

from classes.exam import Exam

objExam = Exam()

objExam.loadQuestionsData("./data/questions_data.json", "./data/answers.txt")

str_input = "A"

objExam.startExam()

while objExam.getStatus() != "F":

    if str_input.upper() in ("A", "B", "C", "D", "E"):
        objExam.showNextQuestion()

    str_input = input("")

    str_input = str_input[0]

    objExam.processUserAnswer(str_input)






