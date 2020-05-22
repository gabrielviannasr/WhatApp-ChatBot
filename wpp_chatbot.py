from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

from util.xlsxreader import XlsxReader

app = Flask(__name__)

# Ler as perguntas do arquivo Excel.
file = "questions.xlsx"
excel = XlsxReader.useSheet(xlsx_file=file)
questions = excel["FORM"]

# Criar um vetor de respostas: -1: None, 1: Sim, 2: Não.
answers = [None for k in range(len(questions))]

# Vetor de dados
data = {"i": 0, "score": 0}


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Avaliação de Sintomas
    i = data["i"]
    # Se a resposta está vazia | nula.
    if answers[i] is None:
        # Se a resposta é válida.
        if incoming_msg in ["1", "2"]:
            answers[i] = incoming_msg
            # Se existe uma próxima pergunta.
            if (i + 1) < len(questions):
                question = questions[i + 1]["QUESTION"]
                question = "{0:02d}. {question}".format((i + 2), question=question) # (i + 2): +1 da próxima questão e +1 pq i começa em zero.
                question = question + "\n\t1: Sim.\n\t2: Não."
                msg.body(question)
                data["i"] = data["i"] + 1 # i++
            # Confirmar e respostas e (THEN) Calcular score.
            else:
                for (answer, question) in zip(answers, questions):
                    if answer == "1": # Resposta: Sim.
                        data["score"] = data["score"] + question["SCORE"]
                message = "Seu score é: " + str(data["score"])
                msg.body(message)
        # Repete a pergunta.
        else:
            question = questions[i]["QUESTION"]
            question = "{0:02d}. {question}".format((i + 1), question=question)
            question = question + "\n\t1: Sim.\n\t2: Não."
            msg.body(question)

    return str(resp)


if __name__ == '__main__':
    app.run()
