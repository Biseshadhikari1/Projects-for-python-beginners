import random
def word_list():
    global word
    list_of_word = ["aback", "abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding", "object", ]
    word = random.choice(list_of_word)
    global picture
    picture = {
        4: """
            --------------        
            |            |
            |            |
                         |
                         |
                         |
                         |

                """,
        3: """
            --------------        
            |            |
            |            |
            O            |
                         |
                         |
                         |

                """,
        2: """
            --------------        
            |            |
            |            |
            O            |
           /|\           |
                         |
                         |

                """,

        1: """
            --------------        
            |            |
            |            |
            O            |
           /|\           |
            |            |
                         |

                """,
        0: """
            --------------        
            |            |
            |            |
            O            |
           /|\           |
            |            |
           / \           |


           Dead

            """
    }


def processing():
    global word
    word_list()
    null = list("-" * len(word))
    wordd = list(word)
    point = 5
    bisesh = ' '
    binil = ''
    while point > 0:
        join_list = bisesh.join(null)
        print(f"Your have {point} chances left")
        print(f"Current word {join_list}")

        choose = input("Guess the letter: ")
        binil += choose + " "
        print(f"The letter you choosed {binil} ")

        if choose in wordd:
            for i in range(len(word)):
                if choose == word[i]:
                    null[i] = choose
        else:
            point -= 1
            # print("\n")
            print("\n")
            print("--------------------------")
            # print(f"The letter is  not in given word")
            print(picture[point])
            print("--------------------------\n")
        if "-" not in null:
            print("--------------------------")
            print("You gussed the correct word")
            print("--------------------------")
            break
        # print(f"The letter you choosed {binil} ")

    if point == 0:
        print("--------------------------")
        print(f"Game over the correct word is |{word}|")
        print("--------------------------")

    ask_again = input("Do you want to play again| Yes | No :")
    if ask_again == "Yes".lower():
        processing()
        print("\n")


processing()