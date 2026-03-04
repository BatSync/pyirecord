# Notes on integration

## Taxa 

https://github.com/Indicia-Team/indicia-docs/blob/531ba71cbd18ac41bc4bd0772b67803b4106c5a8/developing/data-model/taxa.rst

- describes how the taxonomy database is set up 

There is not a REST endpoint for search but there are "Data Services"

Described here:
https://github.com/Indicia-Team/indicia-docs/blob/531ba71cbd18ac41bc4bd0772b67803b4106c5a8/developing/web-services/data-services-taxon-search.rst

Going from the code comment here, the endpoint is /services/data/taxa_search
https://github.com/Indicia-Team/warehouse/blob/748ee5bbd99b7b4e76aa1751c7720bef444cb368/modules/indicia_svc_data/controllers/services/data.php#L607

The code here shows a query string https://github.com/Indicia-Team/warehouse/blob/748ee5bbd99b7b4e76aa1751c7720bef444cb368/application/views/taxa_search/index.php#L40

taxa_search?filter-taxon_list_id=$defaultListId&filter-taxa_taxon_list_id={taxa_taxon_list_id}

We should use the /rest/ over the older /data/ endpoints.

There is an elasticsearch endpoint, which is here:

_Using the endpoint https://warehouse1.indicia.org.uk/index.php/services/rest/es-occurrences/_search with a body containing_

{"query":{"bool":{"must":[
  {"match_phrase": {
    "event.date_start": "2026-03-02"
  }},
  {"match_phrase": {
    "location.output_sref": "SD470599"
  }},
  {"match_phrase": {
    "metadata.trial": true
  }}
]}}}

_returns all my records on a particular date in a particular grid square with an added parameter to select only training records._

Try this, authenticating first, report back.


as documented at https://warehouse1.indicia.org.uk/index.php/services/rest, the taxon_list_id is required.
The UK Species Inventory list has id=15

https://warehouse1.indicia.org.uk/index.php/services/rest/taxa/search?taxon_list_id=15 without a search term returns maybe a hundred random taxa.

https://warehouse1.indicia.org.uk/index.php/services/rest/taxa/search?taxon_list_id=15&searchQuery=Myotis nattereri&preferred=true returns a single taxon (plus some metadata) like
"data": [{
  "taxa_taxon_list_id": "165379",
  "searchterm": "Myotis nattereri (Kuhl, 1817)",
  "highlighted": "'''<b>Myotis</b> <b>nattereri</b>'''",
  "taxon": "Myotis nattereri",
  "authority": "(Kuhl, 1817)",
  "language_iso": "lat",
  "preferred_taxon": "Myotis nattereri",
  "preferred_authority": "(Kuhl, 1817)",
  "default_common_name": "Natterer's Bat",
  "taxon_group": "terrestrial mammal",
  "preferred": "t",
  "preferred_taxa_taxon_list_id": "165379",
  "taxon_meaning_id": "70366",
  "external_key": "NHMSYS0000080184",
  "search_code": "NHMSYS0000080184",
  "organism_key": "NBNORG0000049704",
  "taxon_group_id": "150",
  "parent_id": "91963",
  "identification_difficulty": "4",
  "id_diff_verification_rule_id": "2",
  "taxon_rank_sort_order": "300",
  "taxon_rank": "Species"
}],

## Occurrences

To POST an occurrence the endpoint is https://warehouse1.indicia.org.uk/index.php/services/rest/samples and my payload 
{
  "values": {
    "survey_id": 42,
    "entered_sref": "SD470599",
    "entered_sref_system": "OSGB",
    "date": "02\/03\/2026",
    "training": "t"
  },
  "occurrences": [{
    "values": {
      "taxa_taxon_list_id": 98607,
      "occAttr:54": 859,
      "training": "t"
    }
  }]
}

returns the response (which may be missing a closing brace?)
{
  "values":{
    "id":"34415925","
    Created_on":"2026-03-02T11:23:24+00:00","
    Updated_on":"2026-03-02T11:23:24+00:00"},
    "href":"https:\/\/warehouse1.indicia.org.uk\/index.php\/services\/rest\/samples\/34415925",
    "occurrences":[{
      "values":{
        "id":50388663,
        "created_on":"2026-03-02T11:23:24+00:00",
        "updated_on":"2026-03-02T11:23:24+00:00"
      },
      "href":"https:\/\/warehouse1.indicia.org.uk\/index.php\/services\/rest\/occurrences\/50388663"
    }]
}


This is doing exactly the same as the mobile apps and all works for me as documented. I am using Postman to make these requests but this is the Curl equivalent.

curl --location 'https://warehouse1.indicia.org.uk/index.php/services/rest/samples' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token> \
--data '{
  "values": {
    "survey_id": 42,
    "entered_sref": "SD470599",
    "entered_sref_system": "OSGB",
    "date": "02\/03\/2026",
    "training": "t"
  },
  "occurrences": [{
    "values": {
      "taxa_taxon_list_id": 98607,
      "occAttr:54": 859,
      "training": "t"
    }
  }]
}
'

_end of Jim's notes_

The "occAttr" integer sets correspond to [Occurrence Attributes](https://irecord.org.uk/help/import-fields) - you can infer what they are by looking at the guidelines for spreadsheet import to Indicia but this doesn't give a mapping to integer codes for terms and their values. The value ranges are defined as [term lists](https://irecord.org.uk/help/import-termlists) where they are set. It's all similar to iNat's "Observation Fields" but not user-editable.

We can't look at other bat records to see commonly used occattrs and I can't bring myself to ask Jim again



## General


A very reluctantly CoPilot-generated walkthrough of the JSON requests and responses that _should_ work with this API, if we can figure out where to find the endpoints.

Upload to Media Queue

https://github.com/Indicia-Team/warehouse/blob/748ee5bbd99b7b4e76aa1751c7720bef444cb368/modules/rest_api/controllers/services/rest.php#L455

    POST your audio file to: /index.php/services/rest/media-queue
    Allowed audio formats: mp3, wav (plus images and PDF)
    The server returns a name property (e.g., "18/60/23/5f3698a2e587c1.59610000.mp3")

Reference in Submission Include the queued filename in your record submission using the queued field:
JSON

{
  "values": {
    "survey_id": 1,
    "entered_sref": "SU1234",
    "entered_sref_system": "OSGB",
    "date": "01/08/2020"
  },
  "media": [
    {
      "values": {
        "queued": "18/60/23/5f3698a2e587c1.59610000.mp3",
        "caption": "Audio recording"
      }
    }
  ]
}


When you GET occurrences from the REST API, the response structure looks like this:
JSON

{
  "values": {
    "id": "123",
    "occurrence_id": "123",
    "sample_id": "456",
    "taxa_taxon_list_id": "789",
    "taxon": "Species name",
    "preferred_taxon": "Accepted species name",
    "default_common_name": "Common name",
    "taxon_group": "Group name",
    "taxa_taxon_list_external_key": "external_key",
    "certainty": "C",
    "comment": "Optional comment",
    "record_status": "V",
    "record_substatus": null,
    "machine_involvement": "3",
    "sensitivity_precision": null,
    "confidential": "f",
    "release_status": "R",
    "training": "f",
    "created_on": "2025-06-10T10:35:32+00:00",
    "created_by_id": "1",
    "updated_on": "2025-06-10T10:35:32+00:00",
    "updated_by_id": "1",
    "website_id": "1"
  }
}

When creating an occurrence in an existing sample[? survey?], you POST to /index.php/services/rest/occurrences:
JSON

{
  "values": {
    "taxa_taxon_list_id": 2,
    "machine_involvement": 3,
    "comment": "Optional notes"
  },
  "media": [
    {
      "values": {
        "queued": "18/60/23/abcdefg.jpg",
        "caption": "Occurrence image"
      }
    }
  ]
}


{
  "values": {
    "survey_id": 1,
    "entered_sref": "SU1234",
    "entered_sref_system": "OSGB",
    "date": "01/08/2020"
  },
  "occurrences": [
    {
      "values": {
        "taxa_taxon_list_id": 2,
        "occAttr:8": "4 adults"
      },
      "media": [
        {
          "values": {
            "queued": "18/60/23/5f36a6d2b51472.42086512.jpg",
            "caption": "Occurrence image"
          }
        }
      ]
    }
  ]
}

{
  "values": {
    "id": "3",
    "created_on": "2020-08-14T17:57:32+02:00",
    "updated_on": "2020-08-14T17:57:32+02:00"
  },
  "href": "http://localhost/warehouse-test/index.php/services/rest/samples/3",
  "occurrences": [
    {
      "values": {
        "id": "3",
        ...
      }
    }
  ]
}

