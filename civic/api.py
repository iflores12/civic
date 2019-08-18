"""Python Library For Facebook Ads Archive API"""

import json
import requests
import logging

logger = logging.getLogger(__name__)


class FBAdsApi(object):
    """Python Interface For the Facebook Ads Archive API"""

    def __init__(
        self,
        access_token=None,
        base_url=None,
    ):

        self.access_token = access_token
        self.base_url = base_url or 'https://graph.facebook.com/v4.0/ads_archive'

        self.auth_url = self.base_url + f"?access_token={self.access_token}"

    def ad_search(
        self,
        search_terms=None,
        ad_type='POLITICAL_AND_ISSUE_ADS',
        ad_reached_countries="['US']",
        ad_active_status=None,
        search_page_ids=None,
        return_json=False
    ):
        if search_terms is None:
            return []

        params = {
            'search_terms': search_terms,
            'ad_type': ad_type,
            'ad_reached_countries': ad_reached_countries,
            'ad_active_status': ad_active_status,
            'search_page_id': search_page_ids,
        }

        search_params = {k: v for k, v in params.items() if v is not None}
        resp = self._RequestUrl(self.auth_url, data=search_params)

        data = self._ParseAndCheckFacbeook(resp.content.decode('utf-8'))
        if return_json:
            return data

    def _ParseAndCheckFacbeook(self, json_data):
        try:
            data = json.loads(json_data)
        except ValueError:
            print("And I Oop")

        return data

    def _RequestUrl(self, url, data=None, json=None):
        if not data:
            data = {}

        url = self._BuildURL(url, extra_params=data)
        resp = requests.get(url)

        return resp

    def _BuildURL(self, url, extra_params=None):
        if extra_params:
            for k, v in extra_params.items():
                url += '&' + k + "=" + v
            return url
        else:
            return url
