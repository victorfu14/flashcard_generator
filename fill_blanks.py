from nltk import tokenize
from random import choice, sample


def get_blank_questions(text, words, n_questions=10):
    sentences = tokenize.sent_tokenize(text)

    questions = []

    for s in sentences:
        used_words = [word for word in words if word in s]
        if used_words:
            blank_word = choice(used_words)
            blank_question = s.replace(blank_word, "___")
            questions.append((blank_question, blank_word))

    questions_sample = sample(questions, min(n_questions, len(questions)))

    return questions_sample
