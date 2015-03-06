from rebnypy.lookups import expand_row

def test_lookups():
    data = {
        "LeaseType": None,
        "Rent": None,
        "PetPolicy": "N",
    }
    out = expand_row(data)
    assert out == {'Rent': None, 'LeaseType': 'UNKNOWN', 'PetPolicy': 'No Pets'}
