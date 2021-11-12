#-*- coding: UTF-8 -*-

import json

dct_temp = {}
lst_questions = []
lst_options = []
str_a1 = ""
int_i = 0
bol1 = True

f = open("questions_cert_spark.txt","rt")
for linha in f:
	if linha.find("Question") != -1:
		if bol1 == False:
			lst_options.append(str_a1)
			dct_temp["alterantives"] = lst_options
			lst_questions.append( dct_temp.copy() )
		
		lst_options = []
		str_a1 = ""
		dct_temp["description"] = ""
		str_a1 = ""
		int_i = int_i + 1
		dct_temp["id"] = int_i
		bol1 = True
		
	elif linha.find("A.") != -1:
		dct_temp["description"] = str_a1
		str_a1 = ""
	elif linha.find("B.") != -1:
		lst_options.append(str_a1)
		str_a1 = ""
	elif linha.find("C.") != -1:
		lst_options.append(str_a1)
		str_a1 = ""
	elif linha.find("D.") != -1:
		lst_options.append(str_a1)
		str_a1 = ""
	elif linha.find("E.") != -1:
		lst_options.append(str_a1)
		str_a1 = ""
		bol1 = False
		
	if bol1 == False:
		str_a1 = str_a1 + linha
		
	bol1 = False
	
f.close()

str_json = json.dumps({"questions": lst_questions}, indent=4)
f = open("euestoes_cert_spark.json", "wt")
f.write(str_json)
f.close()

print("Fim normal do processamento.")

	