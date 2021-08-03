def count_construct(target_word: str, word_bank: list):
    table = [0 for i in range(len(target_word) + 1)]
    table[0] = 1
    for i in range(len(target_word)):
        if target_word[i]:
            for word in word_bank:
                if target_word[i:].startswith(word):
                    table[i + len(word)] += table[i]
    return table


if __name__ == "__main__":
    target_word = "purple"
    word_bank = ["purp", "p", "ur", "le", "purpl"]
    print(count_construct(target_word, word_bank))
