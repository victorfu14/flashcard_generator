from nltk import tokenize
from random import choice, sample
import re

def get_blank_questions(text, words, n_questions=10, n_blanks=1):
    sentences = tokenize.sent_tokenize(text)

    questions = []
    word_set = set(words)
    for s in sentences:
        removed_words = []
        used_words = [word for word in word_set if re.search("\\b" +  word + "\\b",s)]
        used_words = sample(used_words, min(n_blanks, len(used_words)))
        count = 0
        for index, word in enumerate(used_words):
            regex = "\\b" +  word + "\\b"
            if re.search("\\b" +  word + "\\b",s):
                s = re.sub(regex, "__" + str(index - count) + "__", s)
                removed_words.append((index - count, word))
            else:
                count += 1
        questions.append((s, removed_words))

    questions_sample = sample(questions, min(n_questions, len(questions)))

    return questions_sample
