def word_count(sentence):
    d = {}
    if sentence.strip() == "":
        return d
    sentence_part = sentence.split(" ")
    for word in sentence_part:
        if word == "":
            continue
        d[word] = d.get(word, 0) + 1
    return d

print word_count("This is a word a this hello hello    hello")
print word_count("   ")
