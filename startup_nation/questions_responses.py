from random import choice

questions = {
    'A': {
        'question': 'This is a question ?',
        'answer': {
            '1': ['a', 0],
            '2': ['b', 0],
            '3': ['c', 5],
            '4': ['d', 0]
        }
    },
    'B': {
        'question': 'This is another question ?',
        'answer': {
            '1': ['a', 5],
            '2': ['b', 0],
            '3': ['c', 0],
            '4': ['d', 0]
        }
    }
}

def show_question():
    score = 0
    historique_des_questions = []

    # On récupère l'ensemble des actions
    q = [key for key, value in questions.items()]

    # On prend une question au
    # hasard dans la liste
    # des questions
    question_label = choice(q)
    question = questions[question_label]['question']
    print(question)

    # On stack la question dans l'historique
    if question_label not in historique_des_questions:
        historique_des_questions.append(question_label)
        print(historique_des_questions)

    # # On prend la réponse du candidat
    # user_answer = input(question)

    # # On extracte la réponse du dictionnaire
    # # à partir de la réponse de l'utilisateur
    # answer_list = questions[question_label]['answer']
    # s = answer_list[user_answer]

    # if s[1] > 0:
    #     # Si le score de la réponse
    #     # est supérieur à 0,
    #     # c'est une bonne réponse 
    #     score += s[1]
    #     print('Bonne réponse')
    # else:
    #     # Dans la cas contraire, on trouve
    #     # la bonne réponse parmis les réponse
    #     # possibles. On indique à l'utilisateur
    #     # quel était la bonne réponse
    #     for key, value in answer_list.items():
    #         if value[1] > 0:
    #             print('La bonne réponse était :', value[0])
    # print('Votre score est de %s:' % score)

while True:
    show_question()