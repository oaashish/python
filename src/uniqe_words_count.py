def unique_words_count(sentence):
    if sentence.strip() == "":
        return 0
    sentence_part = sentence.split(" ")
    return len(set(sentence_part))


print unique_words_count("Hello Hello How are ARE ARe ARE Aashish")