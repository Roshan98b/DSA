def can_construct(target_word: str, word_bank: list):
    table = [False for i in range(len(target_word) + 1)]
    table[0] = True
    for i in range(len(table)):
        if table[i]:
            for word in word_bank:
                if target_word[i:].startswith(word):
                    table[i + len(word)] = True
    return table[-1]


if __name__ == "__main__":
    target_word = "abcdef"
    word_bank = ["ab", "abc", "cd", "def", "abcd", "ef", "a"]
    print(can_construct(target_word, word_bank))
