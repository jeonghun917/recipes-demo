"""A tiny stand-in for an ORM: QuerySet methods return a new QuerySet, like Django's."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Recipe:
    id: int
    household_id: int
    name: str
    tags: tuple


@dataclass(frozen=True)
class User:
    name: str
    household_id: int


class QuerySet:
    def __init__(self, rows):
        self._rows = tuple(rows)

    def filter(self, **conditions):
        def keep(row):
            for key, value in conditions.items():
                if key.endswith("__contains"):
                    if value not in getattr(row, key[: -len("__contains")]):
                        return False
                elif getattr(row, key) != value:
                    return False
            return True
        return QuerySet(r for r in self._rows if keep(r))

    def order_by(self, field):
        return QuerySet(sorted(self._rows, key=lambda r: getattr(r, field)))

    def __iter__(self):
        return iter(self._rows)


class Manager:
    def __init__(self, rows):
        self._rows = rows

    def all(self):
        return QuerySet(self._rows)


Recipe.objects = Manager([
    Recipe(1, 1, "Kimchi stew", ("korean", "spicy")),
    Recipe(2, 1, "Pancakes", ("breakfast",)),
    Recipe(3, 2, "Secret family lasagna", ("italian",)),
    Recipe(4, 2, "Grandma's curry", ("spicy",)),
])
