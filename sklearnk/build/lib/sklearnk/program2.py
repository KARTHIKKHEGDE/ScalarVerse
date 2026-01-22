INF = 1000

def minimax(depth, index, is_max, values, alpha, beta):
    # Leaf node
    if depth == 3:
        return values[index]

    # MAX player's turn
    if is_max:
        best = -INF
        for child in range(2):
            value = minimax(depth + 1, index * 2 + child,
                            False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:   # pruning
                break
        return best

    # MIN player's turn
    else:
        best = INF
        for child in range(2):
            value = minimax(depth + 1, index * 2 + child,
                            True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:   # pruning
                break
        return best


if __name__ == '__main__':
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("Optimal value:", minimax(0, 0, True, values, -INF, INF))
