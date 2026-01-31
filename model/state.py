from dataclasses import dataclass

@dataclass
class Stato:
    id : str
    name : str

    def __eq__(self, other):
        return isinstance(other, Stato) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f'{self.id} {self.name}'

    def __repr__(self):
        return f'{self.id} {self.name}'