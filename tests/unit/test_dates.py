from datetime import datetime
from rebnypy.client import get_date_string

def test_date_string():
    date = datetime(1984, 8, 29, 11,22,33)
    assert get_date_string(date) == '08/29/1984 11:22 AM'

