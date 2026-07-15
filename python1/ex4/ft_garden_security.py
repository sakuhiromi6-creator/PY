class Plant:
    def __init__(self, nome: str, height: float, days: int):
        self._nome = nome
        self._height = height
        self._days = days

    def get_height(self):
        return self._height
    
    def set_height(self, new_height):
        if new_height < 0:
            print(
                f"{self._nome}: "
                f"Error, height can't be negative \nHeight update reject"
            )
        else:
            self._height = new_height