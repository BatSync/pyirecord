from pyirecord.taxa import taxa_search


def test_taxa(jwt):
    s_id = taxa_search(jwt)
    assert s_id is not None
    print(s_id)
