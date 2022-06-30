class Position:
    def __init__(self, row, col, stand):
        self.row = row
        self.col = col
        self.stand = stand

    def __str__(self):
        return f'{self.row} - {self.col} - {self.stand}'
