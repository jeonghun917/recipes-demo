"""No view may show one household's recipes to another. Every public function in app.views is checked."""
import inspect
import unittest

from app import views
from app.models import Recipe, User


class HouseholdIsolation(unittest.TestCase):
    def test_every_view_stays_in_the_users_household(self):
        alice = User("alice", household_id=1)
        theirs = {r.name for r in Recipe.objects.all() if r.household_id != 1}
        for name, view in inspect.getmembers(views, inspect.isfunction):
            if name.startswith("_") or view.__module__ != views.__name__:
                continue
            params = list(inspect.signature(view).parameters)
            args = [alice] + ["spicy"] * (len(params) - 1)
            shown = set(view(*args))
            self.assertFalse(shown & theirs, f"{name} shows another household's recipes: {sorted(shown & theirs)}")


if __name__ == "__main__":
    unittest.main()
