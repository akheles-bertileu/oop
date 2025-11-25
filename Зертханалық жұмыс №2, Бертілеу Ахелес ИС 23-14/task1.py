import math_utils

from string_utils import capitalize_words, count_letters


def main():
    print("Қосу:", math_utils.add(5, 3))
    print("Азайту:", math_utils.subtract(10, 4))
    print("Көбейту:", math_utils.multiply(6, 7))
    print("Бөлу:", math_utils.divide(20, 5))

    text = "salam aleikum dostar"
    print("Бас әріппен:", capitalize_words(text))
    print("Әріп саны:", count_letters(text))


if __name__ == "__main__":
    main()
