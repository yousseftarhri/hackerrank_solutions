#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    # your code goes here
    sub_string = [string[i:i + k] for i in range(0, len(string), k)]

    for i in sub_string:
        output = ''.join([i[e] for e in range(len(i)) if i[e] not in i[:e]])

        print(output)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)