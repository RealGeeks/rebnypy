from rebnypy.lookups import expand_row

def test_lookups():
    data = {
        "Status": "A",
        "LeaseType": None,
        "Rent": None,
        "PetPolicy": "N",
        "Building": {
            "Borough": "BK"
        }
    }
    out = expand_row(data)
    assert out == {
        'Status': 'Active',
        'Rent': None,
        'LeaseType': 'UNKNOWN',
        'PetPolicy': 'No Pets',
        'Building': {
            'Borough': 'Brooklyn',
        },
    }
