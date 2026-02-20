# Notes on integration

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

When creating an occurrence in an existing sample, you POST to /index.php/services/rest/occurrences:
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

