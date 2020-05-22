# for i in range(20):
#     question = "{0:02d}. {question}".format(i, question="questions[i]") # i + ". " + questions[i]
#
#     print(question)
from pprint import pprint

from util.xlsxreader import XlsxReader

file = "questions.xlsx"
form = XlsxReader.useSheet(xlsx_file=file)

answers = [None for k in range(len(form["FORM"]))]

# for key, value in file_dict.items():
#     # print(key + "\t\t:\t" + str(value))
#     print('{:25} : {}'.format(key, str(value)))

# pprint(file_dict)

print("\n#FORM")
for line in form["FORM"]:
    print(line)
    print(line["SCORE"])

# print("\n#ANSWERS")
# for line in answers:
#     print(line)

# print(form["FORM"][2])