"""Every function here answers a request from a signed-in user."""
from app.models import Recipe


def list_recipes(user):
    qs = Recipe.objects.all()
    qs = qs.filter(household_id=user.household_id)
    return [r.name for r in qs.order_by("name")]
