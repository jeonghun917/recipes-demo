# recipes-demo

A tiny multi-household recipe app for a readfirst demo. Each household must only ever see its own recipes.
The rule and the trap that guard that live in `.readfirst/map.json`; `python3 -m unittest` checks every view.

Modeled on a real bug: in Mealie, a per-household filter was written as `query.filter(...)` without assigning the
result, so it never applied (mealie-recipes/mealie#8964, fixed by the maintainers).
