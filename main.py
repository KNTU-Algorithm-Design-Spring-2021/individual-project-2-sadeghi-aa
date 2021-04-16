# def result(break_points):
#


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

    if num_words == 1:
        costs.append(0)
        break_points = [0]
    else:
        costs.append(partial_costs[0][0])
        break_points = []
    for end_word in range(1, num_words):
        cur_cost = None
        if end_word != num_words - 1:
            for back_jump in range(1, end_word + 1):
                if partial_costs[end_word - (back_jump - 1)][end_word] is not None:
                    if cur_cost is None or cur_cost > costs[end_word - back_jump] + partial_costs[end_word - (back_jump - 1)][end_word]:
                        cur_cost = costs[end_word - back_jump] + partial_costs[end_word - (back_jump - 1)][end_word]
                        break_point = end_word - back_jump
                else:
                    costs.append(cur_cost)
                    break_points.append(break_point)
                    break
                if back_jump == end_word:
                    if partial_costs[0][end_word] is not None and cur_cost > partial_costs[0][end_word]:
                        costs.append(partial_costs[0][end_word])
                        break_points.append(end_word)
                    else:
                        costs.append(cur_cost)
                        break_points.append(break_point)
        else:
            for back_jump in range(1, end_word + 1):
                if partial_costs[end_word - (back_jump - 1)][end_word] is not None:
                    if cur_cost is None or (cur_cost > costs[end_word - back_jump] and partial_costs[end_word - (back_jump - 1)][end_word] is not None):
                        cur_cost = costs[end_word - back_jump]
                        break_point = end_word - back_jump
                else:
                    costs.append(cur_cost)
                    break_points.append(break_point)
                    break
                if back_jump == end_word:
                    if partial_costs[0][end_word] is not None and cur_cost > 0:
                        costs.append(0)
                        break_points.append(end_word)
                    else:
                        costs.append(cur_cost)
                        break_points.append(break_point)

    print('All Costs:', costs)
    print('All Breakpoints:', break_points)
    print('Final Cost:', costs[-1])


wordLengths = [9, 2, 5, 3]
lineLength = 10

word_wrap(wordLengths, lineLength)
