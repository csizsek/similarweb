import copy
import json
import unittest

import requests_mock

import similarweb


class TestClient(unittest.TestCase):

    def setUp(self):
        self.user_key = 'asd'
        self.response_data = {
            'foo': 'bar'
        }
        self.test_data = [
            {
                'protocol': 'https',
                'domain': 'example.com',
                'user_key': self.user_key,
                'start': '9-2013',
                'end': '10-2013',
                'granularity': 'daily',
                'page': 1,
                'main_domain': True
            },
            {
                'protocol': 'http',
                'domain': 'example.com',
                'user_key': self.user_key,
                'start': '3-2015',
                'end': '4-2015',
                'granularity': 'weekly',
                'page': 5,
                'main_domain': False
            }
        ]
        self.api_base_url = {
            'generic': '{protocol}://api.similarweb.com/{version}/{endpoint}',
            'site': '{protocol}://api.similarweb.com/Site/{domain}/{version}/{endpoint}'
        }
        self.query_param = {
            'simple': '?format=JSON&userkey={user_key}',
            'granularity': '?format=JSON&userkey={user_key}&start={start}&end={end}&gr={granularity}&md={main_domain}',
            'page': '?format=JSON&userkey={user_key}&start={start}&end={end}&page={page}&md={main_domain}',
            'top_sites': '?format=JSON&userkey={user_key}&category={category}&country={country}'
        }

    def test_visits(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'visits'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['granularity'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.visits(
                    data['domain'],
                    data['start'],
                    data['end'],
                    data['granularity'],
                    data['main_domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_traffic(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'traffic'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['simple'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.traffic(data['domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_page_views(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'pageviews'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['granularity'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.page_views(
                    data['domain'],
                    data['start'],
                    data['end'],
                    data['granularity'],
                    data['main_domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_visit_duration(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'visitduration'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['granularity'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.visit_duration(
                    data['domain'],
                    data['start'],
                    data['end'],
                    data['granularity'],
                    data['main_domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_bounce_rate(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'bouncerate'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['granularity'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.bounce_rate(
                    data['domain'],
                    data['start'],
                    data['end'],
                    data['granularity'],
                    data['main_domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_similar_sites(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v2'
                data['endpoint'] = 'similarsites'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['simple'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.similar_sites(data['domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_also_visited(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v2'
                data['endpoint'] = 'alsovisited'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['simple'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.also_visited(data['domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_tags(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v2'
                data['endpoint'] = 'tags'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['simple'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.tags(data['domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_category(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v2'
                data['endpoint'] = 'category'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['simple'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.category(data['domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_category_rank(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v2'
                data['endpoint'] = 'categoryrank'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['simple'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.category_rank(data['domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_adult(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v2'
                data['endpoint'] = 'category'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['simple'].format(**data),
                    text=json.dumps({'Category': 'Adult'}))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.adult(data['domain'])
                self.assertEqual(res, True)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_top_sites(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'topsites'
                data['category'] = 'foo'
                data['country'] = 'neverwhere'
                m.register_uri(
                    'GET',
                    self.api_base_url['generic'].format(
                        **data) + self.query_param['top_sites'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.top_sites(data['category'], data['country'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_social_referring_sites(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'socialreferringsites'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['simple'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.social_referring_sites(data['domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_organic_search(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'orgsearch'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['page'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.organic_search(
                    data['domain'],
                    data['start'],
                    data['end'],
                    data['page'],
                    data['main_domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_paid_search(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'paidsearch'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['page'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.paid_search(
                    data['domain'],
                    data['start'],
                    data['end'],
                    data['page'],
                    data['main_domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_leading_destination_sites(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v2'
                data['endpoint'] = 'leadingdestinationsites'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['simple'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.leading_destination_sites(data['domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_referrals(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'referrals'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['page'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.referrals(
                    data['domain'],
                    data['start'],
                    data['end'],
                    data['page'],
                    data['main_domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_organic_keyword_competitors(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'orgkwcompetitor'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['page'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.organic_keyword_competitors(
                    data['domain'],
                    data['start'],
                    data['end'],
                    data['page'],
                    data['main_domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_paid_keyword_competitors(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'paidkwcompetitor'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['page'].format(**data),
                    text=json.dumps(self.response_data))
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                res = c.paid_keyword_competitors(
                    data['domain'],
                    data['start'],
                    data['end'],
                    data['page'],
                    data['main_domain'])
                self.assertEqual(res, self.response_data)
        self.assertEquals(m.call_count, len(self.test_data))

    def test_non_200_http_response(self):
        with requests_mock.mock() as m:
            for d in self.test_data:
                data = copy.deepcopy(d)
                data['version'] = 'v1'
                data['endpoint'] = 'visits'
                m.register_uri(
                    'GET',
                    self.api_base_url['site'].format(
                        **data) + self.query_param['granularity'].format(**data),
                    text=json.dumps(self.response_data),
                    status_code=400)
                c = similarweb.Client(
                    user_key=self.user_key,
                    use_https=(
                        data['protocol'] == 'https'))
                with self.assertRaises(Exception):
                    res = c.visits(
                        data['domain'],
                        data['start'],
                        data['end'],
                        data['granularity'],
                        data['main_domain'])
        self.assertEquals(m.call_count, len(self.test_data))

if __name__ == '__main__':
    unittest.main()
