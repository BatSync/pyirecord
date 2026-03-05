Thank you for thinking about contributing to pyirecord!

The library is a spin-out from [BatSync](https://codeberg.org/BatSync/batsync) and really focuses on our narrow needs for posting bat call audio data with standards-oriented metadata though to NBN Atlas via [iRecord](https://irecord.org.uk/). But it should work as a generic interface library for any installation of [Indicia Warehouse](https://github.com/Indicia-Team/warehouse), the platform that powers iRecord.

## Code style

- We use `ruff` for linting and autoformatting python code:

```
uv pip install ruff
ruff check --fix
ruff format
```

- We use `prettier` for formatting if needed:

```
npx prettier README --write
```

## Design decisions

The aim of this project is "minimum complexity", to remain as self-contained as possible in terms of dependencies that might change.
