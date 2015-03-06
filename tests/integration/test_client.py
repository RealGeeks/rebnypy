from os import environ
from rebnypy.client import RebnyClient

def test_client_all_listings():
    client = RebnyClient('http://idx-api.olr.com/api', environ['REBNY_API_KEY'])
    results = client.get_all_listings()
    assert len(results)
