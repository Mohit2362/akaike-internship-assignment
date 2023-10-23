# -*- coding: utf-8 -*-
"""MOHIT_NLP_ASSIGNMENT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/136xbizonZcPBzv8cYAs4OPP037H0YyNG

**Creation of mcq with multiple answers**
"""

import spacy
import random


nlp = spacy.load("en_core_web_sm")

def get_mca_questions(context: str, num_questions: int):
    doc = nlp(context)

    def generate_mcq(question, correct_answers, other_options, num_options=4):
        options = correct_answers + other_options
        random.shuffle(options)

        mcq = {
            "question": question,
            "options": options,
            "correct_answers": correct_answers
        }

        return mcq

    def generate_random_question():
        sentence = random.choice(list(doc.sents))
        blank_word = random.choice([token for token in sentence if not token.is_punct])

        question_text = sentence.text.replace(blank_word.text, "______")
        correct_answers = [blank_word.text]

        other_options = [token.text for token in doc if token.is_alpha and token.text != correct_answers[0]]
        num_correct_options = random.randint(1, 2)  # Generate 1 or 2 correct options
        correct_answers.extend(random.sample(other_options, num_correct_options))

        num_other_options = min(4 - num_correct_options, len(other_options))
        other_options = random.sample(other_options, num_other_options)

        mcq = generate_mcq(question_text, correct_answers, other_options)
        return mcq

    questions = [generate_random_question() for _ in range(num_questions)]

    mcq_questions = []
    for i, question in enumerate(questions, start=1):
        question_str = f"Q{i}: {question['question']}\n"
        options_str = ""
        for j, option in enumerate(question['options']):
            options_str += f"{j+1}. {option}\n"

        correct_options_formatted = " & ".join([f"({chr(97+question['options'].index(ans))})" for ans in question['correct_answers']])
        correct_options_str = f"Correct Options: {correct_options_formatted}"

        mca_question = f"{question_str}{options_str}{correct_options_str}\n"
        mcq_questions.append(mca_question)

    return mcq_questions

data = input("Enter the Data: ")
number_questions = int(input("Enter the number of questions: "))
mcq_questions = get_mca_questions(data, number_questions)
for question in mcq_questions:
    print(question)