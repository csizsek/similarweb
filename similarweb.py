import json

import requests

_API_BASE_URL_SITE = 'api.similarweb.com/Site/{domain}/{version}/{endpoint}'
_API_BASE_URL = 'api.similarweb.com/{version}/{endpoint}'


class Client(object):

    def __init__(self, user_key, use_https=True):
        protocol = 'http'
        if use_https:
            protocol = 'https'
        self.api_base_url_site = protocol + "://" + _API_BASE_URL_SITE
        self.api_base_url = protocol + "://" + _API_BASE_URL
        self.user_key = user_key

    def _get_simple_params(self):
        params = {
            'format': 'JSON',
            'userkey': self.user_key
        }
        return params

    def _get_granularity_params(self, start, end, granularity, main_domain):
        params = {
            'gr': granularity,
            'start': start,
            'end': end,
            'md': main_domain,
            'format': 'JSON',
            'userkey': self.user_key
        }
        return params

    def _get_page_params(self, start, end, page, main_domain):
        params = {
            'page': page,
            'start': start,
            'end': end,
            'md': main_domain,
            'format': 'JSON',
            'userkey': self.user_key
        }
        return params

    def _http_get(self, url, params):
        r = requests.get(url=url, params=params)
        if r.status_code != 200:
            raise Exception("HTTP {0} ".format(r.status_code) + r.text)
        return r.text

    def visits(self, domain, start, end, granularity, main_domain=False):
        params = self._get_granularity_params(
            start, end, granularity, main_domain)
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='visits'), params=params))

    def traffic(self, domain):
        params = self._get_simple_params()
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='traffic'), params=params))

    def page_views(self, domain, start, end, granularity, main_domain=False):
        params = self._get_granularity_params(
            start, end, granularity, main_domain)
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='pageviews'), params=params))

    def visit_duration(
            self, domain, start, end, granularity, main_domain=False):
        params = self._get_granularity_params(
            start, end, granularity, main_domain)
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='visitduration'), params=params))

    def bounce_rate(self, domain, start, end, granularity, main_domain=False):
        params = self._get_granularity_params(
            start, end, granularity, main_domain)
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='bouncerate'), params=params))

    def similar_sites(self, domain):
        params = self._get_simple_params()
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v2', endpoint='similarsites'), params=params))

    def also_visited(self, domain):
        params = self._get_simple_params()
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v2', endpoint='alsovisited'), params=params))

    def tags(self, domain):
        params = self._get_simple_params()
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v2', endpoint='tags'), params=params))

    def category(self, domain):
        params = self._get_simple_params()
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v2', endpoint='category'), params=params))

    def category_rank(self, domain):
        params = self._get_simple_params()
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v2', endpoint='categoryrank'), params=params))

    def adult(self, domain):
        params = self._get_simple_params()
        res = json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v2', endpoint='category'), params=params))
        return res['Category'] == 'Adult'

    def top_sites(self, category=None, country=None):
        params = self._get_simple_params()
        if category:
            params['Category'] = category
        if country:
            params['Country'] = country
        return json.loads(self._http_get(
            url=self.api_base_url.format(version='v1', endpoint='topsites'), params=params))

    def social_referring_sites(self, domain):
        params = self._get_simple_params()
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='socialreferringsites'), params=params))

    def organic_search(self, domain, start, end, page=1, main_domain=False):
        params = self._get_page_params(start, end, page, main_domain)
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='orgsearch'), params=params))

    def paid_search(self, domain, start, end, page=1, main_domain=False):
        params = self._get_page_params(start, end, page, main_domain)
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='paidsearch'), params=params))

    def leading_destination_sites(self, domain):
        params = self._get_simple_params()
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v2', endpoint='leadingdestinationsites'), params=params))

    def referrals(self, domain, start, end, page=1, main_domain=False):
        params = self._get_page_params(start, end, page, main_domain)
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='referrals'), params=params))

    def organic_keyword_competitors(
            self, domain, start, end, page=1, main_domain=False):
        params = self._get_page_params(start, end, page, main_domain)
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='orgkwcompetitor'), params=params))

    def paid_keyword_competitors(
            self, domain, start, end, page=1, main_domain=False):
        params = self._get_page_params(start, end, page, main_domain)
        return json.loads(self._http_get(url=self.api_base_url_site.format(
            domain=domain, version='v1', endpoint='paidkwcompetitor'), params=params))
