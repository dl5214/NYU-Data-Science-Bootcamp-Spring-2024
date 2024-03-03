#  Write a function  count_vowels(word) that takes a word as an argument
#  and returns the number of vowels in the word


def count_vowels(word):
    vowels = 'aeiouAEIOU'
    ret = sum(1 for letter in word if letter in vowels)
    return ret


def main():
    test_word = "DescribeTheCityYouLiveIn"
    result = count_vowels(test_word)
    print("# Vowels in test_word: " + str(result))


if __name__ == '__main__':
    main()