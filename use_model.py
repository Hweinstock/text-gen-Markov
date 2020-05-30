import random as r
from build_model import build_markov_model

def next_character_frequency(m, kgram, c):
    return m[kgram][c]

def random_character(m, text):
    choices = []
    for k in m[text].keys():
        choices += [k]*m[text][k]
    return r.choice(choices)

def generate_random_text(text, k, N):
    m = build_markov_model(text, k)
    seed = r.choice(list(m.keys()))

    text = ''
    text += seed
    for i in range(N-k):
        text += seed[len(seed)-1]
        seed += random_character(m, seed)
        seed = seed[1:]
    return text
