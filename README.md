# PyiRecord

A minimal library aiming to offer a similar interface to [pyinaturalist](https://pyinaturalist.readthedocs.io/) but for the UK's [iRecord](https://irecord.org.uk) national observatory. We currently support these actions:

- Authenticate with OAuth and get a JWT token for a user
- Read the list of surveys available and retrieve their identifiers
- Read the JSON metadata for an occurrence (limited to those the user has created)
- Retrieve the "Occurrence Attributes" (controlled equivalent of iNat's "Observation Fields")
- Search through taxonomies for IDs to label and link observations
- Upload media for an occurrence
- Create a new occurrence

Planned minimum functioning includes:

- Find a list of occurrences created by the logged in user
- Search for recent occurrences within a radius (for de-duplication).

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

iRecord Client ID and Secret are used for OAuth identification, and are _obtained by contacting the iRecord developers_.

iRecord User and Password are for temporary testing purposes only - in normal use they would be commandline options or passed through a web application.

`IRECORD_BASE_URL` is the _warehouse_ address, distinct from the iRecord URL we use to request the token.

### Run the tests

The integration tests are not (currently) intended to run continuously - we don't have a mock version of the iRecord API, the real requests are all linked to client application + an individual's permissions.

However they do provide a way of checking your own permissions should you use `pyirecord` to make an application! Access to data via the API is restricted to the person who created it. We know this isn't ideal! And would definitely set up a mock API to run the tests against if others want `pyirecord` in their workflows.

```
IRECORD_TEST_SAMPLE_ID=[ID of a record, integer]
IRECORD_TEST_SURVEY=[name of a survey, string]
```

`py.test`

`py.test test/integration/test_e2e.py`

## iRecord REST API

iRecord runs on a platform called Indicia Warehouse. It has a REST API that's provided by Indicia. Obtain a token from the iRecord developers - authentication is via iRecord and requests for data are directly against Indicia.

- [Indicia docs - RESTful web service resources](https://indicia-docs.readthedocs.io/en/latest/developing/rest-web-services/resources.html#index-php-services-rest)
- [Indicia warehouse REST endpoint](https://warehouse1.indicia.org.uk/index.php/services/rest) - generated documentation
- [RESTful web service authentication](https://indicia-docs.readthedocs.io/en/latest/developing/rest-web-services/authentication.html)

## Contributing

If you're reading this on the Github mirror, please navigate to the [pyirecord project on Codeberg](https://codeberg.org/BatSync/pyirecord/).
