def all_construct(target_word: str, word_bank: list, memo={}):
    if target_word == '':
        return [[]]
    elif target_word in memo:
        return memo[target_word]
    else:
        result = []
        for word in word_bank:
            if target_word.startswith(word):
                word_construct = all_construct(
                    target_word[len(word):], word_bank)
                target_consruct = [
                    [word] + construct for construct in word_construct]
                result += target_consruct
        memo[target_word] = result
        return result


if __name__ == "__main__":
    target_word = "abcdef"
    word_bank = ["ab", "abc", "cd", "def", "abcd", "ef", "c"]
    print(all_construct(target_word, word_bank))
