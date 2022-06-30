class Part:
    def __init__(self, part_id, name, category, stock, position):
        self.part_id = part_id
        self.name = name
        self.category = category
        self.stock = stock
        self.position = position

    def __str__(self):
        return f'{self.part_id} - {self.name} - {self.category} - {self.stock} - {self.position}'
