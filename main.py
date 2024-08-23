import random
import time

words = ['pies', 'kot', 'aligator', 'borsuk', 'ciele', 'delfin', 'fretka', 'gepard', 'hipopotam', 'kangur']
test = random.choice(words)


def guess_letters(word, guessed_letters):
    start_time = time.time()
    lettr = input("Wpisz literę: ").lower()

    if time.time() - start_time >10:
        print("Czas na odgadnięcie minął!")
        return False

    if len(lettr) != 1 or not lettr.isalpha():
        print("Proszę wpisać jedną literę.")
        return True  # Proszę wpisać poprawną literę, więc nie zmniejszaj liczby prób.

    if lettr in guessed_letters:
        print("Już zgadywałeś tę literę")
    elif lettr in word:
        print(f"Gratulacje! Litera '{lettr}' jest w słowie.")
        guessed_letters.append(lettr)
    else:
        print(f"Niestety, litera '{lettr}' nie jest w słowie.")
        guessed_letters.append(lettr)
        return False

    print(f"Zgadywane litery: {guessed_letters}")
    return True


def display_word(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    return display_word.strip()


def give_hint(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            print(f"Podpowiedź: Pierwsza nieodgadnięta litera to '{letter}'")
            break


def main():

    wins=0
    loses=0

    while True:
        guessed_letters = []
        attempts = 6
        test = random.choice(words)

        while attempts > 0:
            print(display_word(test, guessed_letters))
            correct_guess = guess_letters(test, guessed_letters)

            if not correct_guess:
                attempts -= 1
                print(f"Zostało ci {attempts} strzałów")
                choice = input("Chcesz podpowiedź? (tak/nie): ").lower()
                if choice == "tak":
                    give_hint(test, guessed_letters)

            if '_' not in display_word(test, guessed_letters).replace(' ', ''):
                print("Gratulacje, wygrałeś!")
                wins+=1
                print(f"Wygrałeś już {wins} razy")
                break

        if attempts == 0:
            print(f"Przegrałeś. Słowo to: {test}")
            print(f"to już {loses} twoja przegrana")

        play_again = input("Czy chcesz zagrać ponownie? (tak/nie): ").lower()
        if play_again != 'tak':
            print("Dziękujemy za grę!")
            break


if __name__ == "__main__":
    main()
