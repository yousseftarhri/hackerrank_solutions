def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]

    kevin_score = 0
    stuart_score = 0
    kevin_sublist = []
    stuart_sublist = []

    for i in range(len(string)):
        if string[i] in vowels:
            # Sub string that start with a vowel
            kevin_sub_string = string[i:]
            kevin_sublist = kevin_sublist + [kevin_sub_string[0:e + 1] for e in range(len(kevin_sub_string))]

        else:
            # Sub string that start with a vowel
            stuart_sub_string = string[i:]
            stuart_sublist = stuart_sublist + [stuart_sub_string[0:a + 1] for a in range(len(stuart_sub_string))]

    for i in list(set(kevin_sublist)):
        length_i = len(i)
        for e in range(len(string)):
            if string[e:e + length_i] == i:
                kevin_score = kevin_score + 1

    for i in list(set(stuart_sublist)):
        length_i = len(i)
        for e in range(len(string)):
            if string[e:e + length_i] == i:
                stuart_score = stuart_score + 1

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")

    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")

    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)