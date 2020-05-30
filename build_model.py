
def process_character(m, text, position, k):
    kgram = get_kgram(text, position, k)
    if kgram not in m:
        m[kgram] = {}
    if text[position+k] in m[kgram]:
        m[kgram][text[position+k]] += 1
    else:
        m[kgram][text[position+k]] = 1

def get_kgram(text, position, k):
    return text[position:position+k]

def build_markov_model(text, k):
    markov_model = {}
    for l in range(len(text)-k):
        process_character(markov_model, text, l, k)
    final = get_kgram(text, len(text)-k-1, k)
    if final not in markov_model:
        markov_model[final] = {}
    if text[0] not in markov_model[final]:
        markov_model[final][text[0]] = 1
    else:
        markov_model[final][text[0]] += 1
    return markov_model
