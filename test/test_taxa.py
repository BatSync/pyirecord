from pyirecord.taxa import taxa_search 

def test_taxa(jwt):
    s_id = taxa_search(jwt)
    print(s_id.status_code)
    print(s_id.json())
    assert s_id is not None
