def all_construct(target_word: str, word_bank: list):
    table = [[] for i in range(len(target_word) + 1)]
    table[0].append([])
    for i in range(len(table)):
        if table[i] != []:
            for word in word_bank:
                if target_word[i:].startswith(word):
                    target_construct = [construct + [word]
                                        for construct in table[i]]
                    table[i + len(word)] += target_construct
    return table[-1]


if __name__ == "__main__":
    target_word = "abcdef"
    word_bank = ["ab", "abc", "cd", "def", "abcd", "ef", "c"]
    print(all_construct(target_word, word_bank))
