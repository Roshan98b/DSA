def can_construct(target_word: str, word_bank: list, memo = {}):
    if target_word == '':
        return True
    elif target_word in memo:
        return memo[target_word]
    else:
        for word in word_bank:
            if target_word.startswith(word):
                if can_construct(target_word[len(word):], word_bank):
                    memo[target_word[len(word):]] = True
                    return True
        memo[target_word] = False
        return False

if __name__ == "__main__":
    target_word = "abcdef"
    word_bank = ["ab", "abc", "cd", "de", "abcd"]
    print(can_construct(target_word, word_bank))

