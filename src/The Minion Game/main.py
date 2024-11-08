#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]

    kevin_score = stuart_score = 0
    length = len(string)
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += length - i

        else:
            stuart_score += length - i


    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")

    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")

    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)