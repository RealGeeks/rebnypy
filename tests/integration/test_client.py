from os import environ
from rebnypy.client import RebnyClient

def test_client_one_listing():
    client = RebnyClient('http://idx-api.olr.com/api', environ['REBNY_API_KEY'])
    results = client.get_listing_by_id('RPLU-641314385854')
    assert len(results)

def test_client_new_listings():
    client = RebnyClient('http://idx-api.olr.com/api', environ['REBNY_API_KEY'])
    results = client.get_new_listings()
    assert len(results)

def test_client_all_listings():
    client = RebnyClient('http://idx-api.olr.com/api', environ['REBNY_API_KEY'])
    results = client.get_all_listings()
    assert len(results)

