def mapper(_, text, writer):
    count = 0
    for word in text.split(" "):
        if count % 2 == 0:
            chave = word.lower()
        elif word.isdigit():
            qtd = int(word)
            writer.emit(chave, qtd)
        count +=1

def reducer(word, icounts, writer):
    writer.emit(word, sum(map(int,icounts)))
