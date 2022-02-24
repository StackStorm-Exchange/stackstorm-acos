import logging
import mock
import yaml

from st2tests.base import BaseActionTestCase


class ACOSBaseActionTestCase(BaseActionTestCase):
    __test__ = False

    def setUp(self):
        super(ACOSBaseActionTestCase, self).setUp()

        self._full_config = yaml.safe_load(self.get_fixture_content('full.yaml'))
        self._log_handler = self.LogHandler()

    class LogHandler(logging.StreamHandler):
        """Mock logging handler to check log output"""

        def __init__(self, *args, **kwargs):
            self.reset()
            logging.StreamHandler.__init__(self, *args, **kwargs)

        def emit(self, record):
            self.messages[record.levelname.lower()].append(record.getMessage())

        def reset(self):
            self.messages = {
                'debug': [],
                'info': [],
                'warning': [],
                'error': [],
                'critical': [],
            }

    def get_mock_session(self, resp_data):
        """This returns mock instance of request.Session to inspect
        whether sending requests from each test have expected destination endpoint
        and expected parameters.
        """
        ACOS_API_AUTH_PATH = [
            '/services/rest/v2.1/?format=json&method=authenticate',
            '/axapi/v3/auth'
        ]
        self._sending_requests = []

        def _save_sending_request(api_url, method, params):
            self._sending_requests.append({
                'url': api_url,
                'method': method,
                'params': params,
            })

        def _mock_sending_request(api_url, method, params):
            mock_resp = mock.Mock()
            if method == 'POST' and any([x in api_url for x in ACOS_API_AUTH_PATH]):
                mock_resp.json.return_value = {
                    'authresponse': {'signature': 'token'},  # This is mock value for ACOS v3.0
                    'session_id': 'token',  # This is mock value for ACOS v2.1
                }
            else:
                mock_resp.json.return_value = resp_data

                # This saves what kind of request was send
                _save_sending_request(api_url, method, params)

            return mock_resp

        def get_side_effect(api_url, **kwargs):
            return _mock_sending_request(api_url, 'GET', kwargs)

        def post_side_effect(api_url, **kwargs):
            return _mock_sending_request(api_url, 'POST', kwargs)

        def delete_side_effect(api_url, **kwargs):
            return _mock_sending_request(api_url, 'DELETE', kwargs)

        mock_session = mock.Mock()
        mock_session.get.side_effect = get_side_effect
        mock_session.post.side_effect = post_side_effect
        mock_session.delete.side_effect = delete_side_effect

        return mock_session
