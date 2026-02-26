# PyiRecord

A minimal library aiming to offer a similar interface to [pyinaturalist](https://pyinaturalist.readthedocs.io/) but for the UK's [iRecord](https://irecord.org.uk) national observatory.

Very much a work in progress - working functionality consists of:

* Authenticate with OAuth and get a JWT token for a user

Planned minimum functioning includes:

* Upload media for an occurrence
* Create a new occurrence
* Show the taxon list for the current survey
* Find a list of occurrences created by the logged in user

## Get started 

### Set up environment 

Recommend use of `uv` to manage python environment. This creates a new virtualenv, installs the dependencies and the package:

```
uv sync
. ./.venv/bin/activate
```

Or more traditionally without uv:

```
python -m venv .venv
. ./venv/bin/activate
pip install -e .
```

### Add config file

We use `.env` to hold config environment variables. 

This is `.env.example` - save a copy of it as .env and fill in the values.

```
IRECORD_CLIENT_ID=""
IRECORD_CLIENT_SECRET=""
IRECORD_USER="[optional, for tests]"
IRECORD_PASSWD="[optional, for tests]"
IRECORD_BASE_URL="https://warehouse1.indicia.org.uk"
```

iRecord Client ID and Secret are used for OAuth identification, and are *obtained by contacting the iRecord developers*.

iRecord User and Password are for temporary testing purposes only - in normal use they would be commandline options or passed through a web application.

`IRECORD_BASE_URL` is the *warehouse* address, distinct from the iRecord URL we use to request the token.

### Run integration test

We have a test which tries to hit a few endpoints (appears passing, just to check the responses).

`py.test test/integration/test_e2e.py`


## iRecord REST API

* [Indicia docs - RESTful web service resources](https://indicia-docs.readthedocs.io/en/latest/developing/rest-web-services/resources.html#index-php-services-rest)
* [Indicia warehouse REST endpoint](https://warehouse1.indicia.org.uk/index.php/services/rest) - generated documentation
* [RESTful web service authentication](https://indicia-docs.readthedocs.io/en/latest/developing/rest-web-services/authentication.html)



## Contributing

If you're reading this on the Github mirror, please navigate to the [pyirecord project on Codeberg](https://codeberg.org/BatSync/pyirecord/).


