def all_construct(target_word: str, word_bank: list, memo={}):
    if target_word == '':
        return [[]]
    elif target_word in memo:
        return memo[target_word]
    else:
        result = []
        for word in word_bank:
            if target_word.startswith(word):
                ways = all_construct(target_word[len(word):], word_bank)
                targets = [way + [word] for way in ways]
                result += [target for target in targets]
        memo[target_word] = result
        return result


if __name__ == "__main__":
    target_word = "abcdef"
    word_bank = ["ab", "abc", "cd", "def", "abcd", "ef", "a"]
    print(all_construct(target_word, word_bank))
