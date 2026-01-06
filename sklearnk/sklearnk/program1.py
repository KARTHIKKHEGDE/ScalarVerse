class TicTacToe: 
    def __init__(self): 
        self.board = [[' ']*3 for _ in range(3)] 
        self.player = 'X' 
 
    def print_board(self): 
        for row in self.board: 
            print(' | '.join(row)) 
        print('-' * 5) 
 
    def is_winner(self, player): 
        for row in self.board: 
            if row.count(player) == 3: 
                return True 
        for col in zip(*self.board): 
            if list(col).count(player) == 3: 
                return True 
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2-i] == player for i in 
range(3)): 
            return True 
        return False 
 
    def is_draw(self): 
        return all(cell != ' ' for row in self.board for cell in row) 
 
    def dfs(self, player): 
        winner = 'X' if self.is_winner('X') else ('O' if self.is_winner('O') else None) 
        if winner: 
            return {'score': 1 if winner == 'X' else -1} 
        if self.is_draw(): 
            return {'score': 0} 
 
        best = {'score': -float('inf')} if player == 'X' else {'score': float('inf')} 
        for i in range(3): 
            for j in range(3): 
                if self.board[i][j] == ' ': 
                    self.board[i][j] = player 
                    score = self.dfs('O' if player == 'X' else 'X') 
                    self.board[i][j] = ' ' 
                    score['row'], score['col'] = i, j 
 
                    if player == 'X' and score['score'] > best['score']: 
                        best = score 
                    elif player == 'O' and score['score'] < best['score']: 
                        best = score 
        return best 
 
    def play(self): 
        while True: 
            self.print_board() 
            if self.is_winner('X'): 
                print("Player X wins!") 
                break 
            if self.is_winner('O'): 
                print("Player O wins!") 
                break 
            if self.is_draw(): 
                print("It's a draw!") 
                break 
            if self.player == 'X': 
                best_move = self.dfs('X') 
                self.board[best_move['row']][best_move['col']] = 'X' 
            else: 
                while True: 
                    try: 
                        i, j = map(int, input("Enter row and column (0-2): ").split()) 
                        if self.board[i][j] == ' ': 
                            self.board[i][j] = 'O' 
                            break 
                        else: 
                            print("Invalid move. Try again.") 
                    except (ValueError, IndexError): 
                        print("Enter valid numbers between 0 and 2.") 
            self.player = 'O' if self.player == 'X' else 'X' 
 
if __name__ == '__main__':
    game = TicTacToe() 
    game.play()
