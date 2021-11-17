# -*- coding: utf-8 -*-

class Exam():
    __questions = [{
        "id":1,
        "description": "1. Escolha uma alternativa",
        "options": [
            "Alternativa A",
            "Alternativa B",
            "Alternativa C",
            "Alternativa D",
            "Alternativa E"
        ]
    }, {
        "id":2,
        "description": "2. Escolha uma alternativa",
        "options": [
            "Alternativa A",
            "Alternativa B",
            "Alternativa C",
            "Alternativa D",
            "Alternativa E"
        ]
    },{
        "id":3,
        "description": "3. Escolha uma alternativa",
        "options": [
            "Alternativa A",
            "Alternativa B",
            "Alternativa C",
            "Alternativa D",
            "Alternativa E"
        ]
    }
    ]
    __answers1 = [{"id":1, "answer": "B"}, {"id":2, "answer": "C"},  {"id":3, "answer": "C"}]
    __answers = ["B", "C", "C"]
    __status = "I"
    __userAnswers = []
    __showedQuestion = []
    __DateTimeStart = None

    ##Methods

    ##Set/Get
    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    ## Other methods
    def cleanScreen(self):
        from os import name, system

        if name.lower() == "nt":
            system("cls")
        else:
            system("clear")


    def startExam(self):
        import datetime

        self.__DateTimeStart = datetime.datetime.now()
        self.setStatus("R")
        self.cleanScreen()
        self.printQuestion()


    def stopExam(self):

        self.setStatus("F")

        userHits = []
        userTotalHits = 0

        for item in self.__userAnswers:

            if item["answer"].upper() == self.__answers[item["id"] - 1]:
                print("You answered correctly question ", item["id"])
                userTotalHits = userTotalHits + 1

        print("Your total hits:", userTotalHits)


    def printQuestion(self):
        import random

        ##Choise question
        while True:
            int_q = random.randint(0, len(self.__questions) -1 )

            if len(self.__showedQuestion) == 0 or int_q not in self.__showedQuestion:
                break

        self.__showedQuestion.append(int_q)

        print(self.__questions[int_q]["description"])
        print("\nOptions:\n")
        for int_i in range(5):
             print(self.__questions[int_q]["options"][int_i])

        print("\nType de letter of chose option or type 'Z' to finish the test")


    def checkUserAnswer(self, userAnswer):
        import datetime

        obj_DateTime = datetime.datetime.now()

        if  obj_DateTime.hour > (self.__DateTimeStart.hour + 2):
            print("Our time is over!")
            self.stopExam()
            return True

        if userAnswer.upper() == "Z":
            self.stopExam()
            return True

        if  userAnswer.upper() not in ("A", "B", "C", "D", "E"):
            print("Invalid option!")
            return False

        int_q = len(self.__showedQuestion) - 1

        self.__userAnswers.append(
            {"id": self.__questions[int_q]["id"], "answer":userAnswer}
        )

        if len( self.__userAnswers) == len(self.__questions):
            print("You answered all of questions!")
            self.stopExam()
            return True

        self.cleanScreen()
        self.printQuestion()

        return True

#End class        


