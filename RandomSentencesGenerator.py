import random

from colorama import Fore, Back, Style, init


def randomizer(word: list) -> str:
    return random.choice(word)


names = ['Angel', 'Ivan', 'Dimitar', 'Georgi', 'Nikolay',
         'Petar', 'Todor', 'Boris', 'Simeon', 'Krum', 'Maria',
         'Elena', 'Anna', 'Stefka', 'Ivanka', 'Desislava',
         'Tsvetana', 'Milena', 'Miglena', 'Nadezhda']

places = ["Sofia",
          "Plovdiv",
          "Varna",
          "Burgas",
          "Ruse",
          "Stara Zagora",
          "Pleven",
          "Sliven",
          "Dobrich",
          "Shumen"]

verbs = ["be", "have", "do", "say", "get", "make", "go", "know", "take", "see"]

nouns = ["stones", "cake", "apple", "laptop", "bikes"]

adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]

details = ["live at home", "work in the office", "walk on the street",
           "run in the park", "swim in the pool", "read at the library",
           "eat at the restaurant", "sleep in the bedroom", "study at school",
           "play in the garden"]

print("Hello, this is your first random sentences:")
while True:
    random_name = randomizer(names)
    random_places = randomizer(places)
    random_verbs = randomizer(verbs)
    random_nouns = randomizer(nouns)
    random_adverbs = randomizer(adverbs)
    random_details = randomizer(details)

    print(Fore.BLACK + Back.WHITE + Style.BRIGHT + f"{random_name} from {random_places} "
                                                   f"{random_adverbs} {random_verbs} {random_nouns}.\n")
    input("Click [Enter] button to generate a new one.\n")
