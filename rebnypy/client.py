import requests
import datetime
import logging
from . import lookups

logger = logging.getLogger(__name__)

def get_date_string(date):
    """
    Converts a python DateTime into the date string used by REBNY
    """
    return date.strftime("%m/%d/%Y %H:%M %p")

def strip_nones(row):
    """
    Remove all items with None for a value, because why include it if there's
    no value?
    """
    return dict([(k,v) for k, v in row.items() if v is not None])

class RebnyClient(object):

    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint
        self.api_key = api_key

    def _request(self, url):
        resp = requests.get(url, headers={"ApiKey": self.api_key})
        resp.raise_for_status()
        return resp.json()

    def _get(self, url):
        rows = self._request(url)
        return [strip_nones(lookups.expand_row(r)) for r in rows]

    def get_all_listings(self):
        url = self.endpoint + '/listings'
        return self._get(url)

    def get_new_listings(self, hours_previous=24):
        start_date = datetime.datetime.utcnow() - datetime.timedelta(hours=hours_previous)
        return self.get_listings_by_date(start_date)

    def get_listing_by_id(self, listing_id):
        url = self.endpoint + '/listings/' + listing_id
        return self._get(url)

    def get_listings_by_date(self, date):
        """
        Return listings modified after date
        """
        date_string = get_date_string(date)
        url = self.endpoint + '/listings/filter?ListingDate=' + date_string
        return self._get(url)
