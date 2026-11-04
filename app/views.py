"""Every function here answers a request from a signed-in user."""
from app.models import Recipe


def list_recipes(user):
    qs = Recipe.objects.all()
    qs = qs.filter(household_id=user.household_id)
    return [r.name for r in qs.order_by("name")]


def search_by_tag(user, tag):
    qs = Recipe.objects.all()
    qs.filter(household_id=user.household_id)
    qs = qs.filter(tags__contains=tag)
    return [r.name for r in qs.order_by("name")]
