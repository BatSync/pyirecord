Thank you for thinking about contributing to BatSync!

The project has an issues list of new or in-progress features, which it's worth reading through.

As of writing, it's a solo-developer effort - please contact zool to figure out where input is most needed!

## Code style

* We use `ruff` for linting and autoformatting python code:

```
uv pip install ruff
ruff check --fix
ruff format
```

* We use `eslint` for rough JS linting and `prettier` for formatting:

```
npx prettier web/html/main.js --write
```

## Design decisions

The ethos of this project is to remain as self-contained as possible in terms of dependencies that might change.

For the python API this means `librosa` and `matplotlib` rather than the enormously powerful, but also enormous `opensoundscape`.

For the Javascript front-end this means no npm, no framework or build system, static files that delegate the hard work to the API and can run anywhere.


