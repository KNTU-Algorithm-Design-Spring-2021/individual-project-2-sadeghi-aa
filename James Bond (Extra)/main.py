import numpy as np


def print_parsings(sentence, break_points, sub_sentence='', cur=0):
    if cur == len(sentence) - 1:
        if sub_sentence:
            print(f"{sub_sentence} {sentence[-1]}")
        else:
            print(f"{sentence[-1]}")
        return
    else:
        for point in break_points[cur][len(sentence)]:
            if point == -1:
                if sub_sentence:
                    print(f"{sub_sentence} {sentence[cur:len(sentence)]}")
                else:
                    print(f"{sentence[cur:len(sentence)]}")
                continue
            if sub_sentence:
                next_sub = f"{sub_sentence} {sentence[cur:point]}"
            else:
                next_sub = f"{sentence[cur:point]}"
            print_parsings(sentence, break_points, next_sub, point)


def parse(sentence):
    valid = np.zeros((len(sentence) + 1, len(sentence) + 1), dtype=int)
    break_points = [[[] for i in range(len(sentence) + 1)] for j in range(len(sentence) + 1)]
    sentence = sentence.lower()
    for end in range(1, len(sentence) + 1):
        for start in reversed(range(end)):
            for mid in range(start + 1, end):
                if valid[start, mid] == 1 and valid[mid, end]:
                    valid[start, end] = 2
                    break_points[start][end].append(mid)
                elif valid[start, end] and valid[mid, end]:
                    valid[start, end] = 2
            if sentence[start:end] in wordSet:
                valid[start, end] = 1
                break_points[start][end].append(-1)
    if not valid[0, len(sentence)]:
        print('This sentence cannot be parsed!')
        return
    else:
        print_parsings(sentence, break_points)


if __name__ == '__main__':
    f = open('The_Oxford_3000.txt', 'r')
    wordSet = set([s.lower() for s in f.read().split()])

    sentence = "AWAY"
    parse(sentence)
    print('')

    sentence = "IHOPETHISISOURLASTPROJECTINTHISCOURSE"
    parse(sentence)
    print('')

    sentence = 'WEAREVERYTIREDRIGHTNOW'
    parse(sentence)
    print('')

    sentence = 'SLEEPISINTHEDICTIONARY'
    parse(sentence)
    print('')

    sentence = 'SLEEPYISNOTINTHEDICTIONARY' # Sleepy is not in the dictionary
    parse(sentence)
    print('')
