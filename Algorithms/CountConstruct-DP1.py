def count_construct(target_word: str, word_bank: list, memo = {}):
    if target_word == '':
        return 1
    elif target_word in memo:
        return memo[target_word]
    else:
        count = 0
        for word in word_bank:
            if target_word.startswith(word):
                count += count_construct(target_word[len(word):], word_bank)
        memo[target_word] = count
        return count


if __name__ == "__main__":
    target_word = "abcdef"
    word_bank = ["ab", "abc", "cd", "def", "abcd", "ef", "a"]
    print(count_construct(target_word, word_bank))
