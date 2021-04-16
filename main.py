def word_wrap(word_lengths, line_length):
    num_words = len(word_lengths)

    for length in word_lengths:
        if length > line_length:
            print('At least one of the words is longer than a line.')
            return

    partial_costs = [[None] * num_words for i in range(num_words)]

    for start in range(num_words):
        for end in range(start, num_words):
            cost = (line_length - (end - start) - sum(word_lengths[start:end + 1])) ** 3
            if cost >= 0:
                partial_costs[start][end] = cost

    costs = []
    break_points = []

    costs[0] = partial_costs[0][0]
    for endWord in range(1, num_words):



wordLengths = [10, 5, 4, 7, 9, 5, 10, 4, 12, 3, 4, 6, 9, 20, 14]
lineLength = 50

word_wrap(wordLengths, lineLength)