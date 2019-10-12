from nltk import tokenize
from random import choice, sample
import re


def get_blank_questions(text, words, n_questions=20, n_blanks=3):
    sentences = tokenize.sent_tokenize(text)

    questions = []
    for s in sentences:
        if len(s) > 30:
            removed_words = []
            used_words = [word for word in words if re.search("\\b" + word + "\\b", s)]
            if used_words:
                used_words = sample(used_words, min(n_blanks, len(used_words)))
                count = 0
                for word in used_words:
                    regex = "\\b" + word + "\\b"
                    if re.search(regex, s):
                        s = re.sub(regex, "__" + str(count) + "__", s)
                        removed_words.append((count, word))
                        assert (len(word) > 1)
                        count += 1

                questions.append((s, removed_words))

    questions_sample = sample(questions, min(n_questions, len(questions)))

    return questions_sample
