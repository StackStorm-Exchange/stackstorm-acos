import json
import mock

from acos_base_action_test_case import ACOSBaseActionTestCase
from ax_action_runner import AXActionRunner
from urllib.parse import urlparse

RESP_SUCCESS = {'response': {'status': 'success'}}


class TestSLBServiceGroup_v2_1(ACOSBaseActionTestCase):
    __test__ = True
    action_cls = AXActionRunner

    def setUp(self):
        super(TestSLBServiceGroup_v2_1, self).setUp()

        self.action = self.get_action_instance(self._full_config)
        self.action.logger.addHandler(self._log_handler)

    @mock.patch('acos_client.v21.axapi_http.Session')
    def test_list_slb_service_group_for_acos(self, mock_session):
        mock_session.return_value = self.get_mock_session(resp_data=RESP_SUCCESS)

        params = {
            'action': 'get',
            'object_path': 'slb.service_group',
            'one_target': True,
            'name': '',
            'appliance': 'appliance_acos_v2.1',
        }
        result = self.action.run(**params)

        # check action results
        self.assertEqual(result, (True, RESP_SUCCESS))

        # check sending request contents that acos_client,
        # which stackstorm-acos depends on, sends.
        self.assertEqual(len(self._sending_requests), 1)

        urlobj = urlparse(self._sending_requests[0]['url'])
        self.assertEqual(urlobj.hostname, 'appliance_acos_v2.1')
        self.assertIn('method=slb.service_group.search', urlobj.query)
        self.assertEqual(self._sending_requests[0]['method'], 'POST')

    @mock.patch('acos_client.v21.axapi_http.Session')
    def test_get_slb_service_group_for_acos(self, mock_session):
        mock_session.return_value = self.get_mock_session(resp_data=RESP_SUCCESS)

        params = {
            'action': 'get',
            'object_path': 'slb.service_group',
            'one_target': True,
            'name': 'test-slb-service-group',
            'appliance': 'appliance_acos_v2.1',
        }
        result = self.action.run(**params)

        # check action results
        self.assertEqual(result, (True, RESP_SUCCESS))

        # check sending request contents that acos_client,
        # which stackstorm-acos depends on, sends.
        self.assertEqual(len(self._sending_requests), 1)

        urlobj = urlparse(self._sending_requests[0]['url'])
        self.assertEqual(urlobj.hostname, 'appliance_acos_v2.1')
        self.assertIn('method=slb.service_group.search', urlobj.query)
        self.assertEqual(self._sending_requests[0]['params']['data'], json.dumps({
            "name": "test-slb-service-group"
        }))
        self.assertEqual(self._sending_requests[0]['method'], 'POST')

    @mock.patch('acos_client.v21.axapi_http.Session')
    def test_delete_slb_service_group_for_acos(self, mock_session):
        mock_session.return_value = self.get_mock_session(resp_data=RESP_SUCCESS)

        params = {
            'action': 'delete',
            'object_path': 'slb.service_group',
            'one_target': True,
            'name': 'test-slb-service-group',
            'appliance': 'appliance_acos_v2.1',
        }
        result = self.action.run(**params)

        # check action results
        self.assertEqual(result, (True, RESP_SUCCESS))

        # check sending request contents that acos_client,
        # which stackstorm-acos depends on, sends.
        urlobj = urlparse(self._sending_requests[0]['url'])
        self.assertEqual(urlobj.hostname, 'appliance_acos_v2.1')
        self.assertIn('method=slb.service_group.delete', urlobj.query)
        self.assertEqual(self._sending_requests[0]['params']['data'], json.dumps({
            "name": "test-slb-service-group"
        }))
        self.assertEqual(self._sending_requests[0]['method'], 'POST')

    @mock.patch('acos_client.v21.axapi_http.Session')
    def test_create_slb_service_group_for_acos(self, mock_session):
        mock_session.return_value = self.get_mock_session(resp_data=RESP_SUCCESS)

        params = {
            'action': 'create',
            'object_path': 'slb.service_group',
            'one_target': True,
            'name': 'test-slb-service-group',
            'protocol': 'tcp',
            'lb_method': 'round-robin',
            'appliance': 'appliance_acos_v2.1',
        }
        result = self.action.run(**params)

        # check action results
        self.assertEqual(result, (True, RESP_SUCCESS))

        # check sending request contents that acos_client,
        # which stackstorm-acos depends on, sends.
        urlobj = urlparse(self._sending_requests[0]['url'])
        self.assertEqual(urlobj.hostname, 'appliance_acos_v2.1')
        self.assertIn('method=slb.service_group.create', urlobj.query)
        self.assertEqual(self._sending_requests[0]['params']['data'], json.dumps({
            "service_group": {
                "name": "test-slb-service-group",
                "protocol": "tcp",
                "lb_method": "round-robin"
            }
        }))
        self.assertEqual(self._sending_requests[0]['method'], 'POST')


class TestSLBServiceGroup_v3_0(ACOSBaseActionTestCase):
    __test__ = True
    action_cls = AXActionRunner

    def setUp(self):
        super(TestSLBServiceGroup_v3_0, self).setUp()

        self.action = self.get_action_instance(self._full_config)
        self.action.logger.addHandler(self._log_handler)

    @mock.patch('acos_client.v30.axapi_http.Session')
    def test_list_slb_service_group_for_acos(self, mock_session):
        mock_session.return_value = self.get_mock_session(resp_data=RESP_SUCCESS)

        params = {
            'action': 'get',
            'object_path': 'slb.service_group',
            'one_target': True,
            'name': '',
            'appliance': 'appliance_acos_v3.0',
        }
        result = self.action.run(**params)

        # check action results
        self.assertEqual(result, (True, RESP_SUCCESS))

        # check sending request contents that acos_client,
        # which stackstorm-acos depends on, sends.
        self.assertEqual(len(self._sending_requests), 1)

        urlobj = urlparse(self._sending_requests[0]['url'])
        self.assertEqual(urlobj.hostname, 'appliance_acos_v3.0')
        self.assertEqual(urlobj.path, '/axapi/v3/slb/service-group/')
        self.assertEqual(self._sending_requests[0]['method'], 'GET')

    @mock.patch('acos_client.v30.axapi_http.Session')
    def test_get_slb_service_group_for_acos(self, mock_session):
        mock_session.return_value = self.get_mock_session(resp_data=RESP_SUCCESS)

        params = {
            'action': 'get',
            'object_path': 'slb.service_group',
            'one_target': True,
            'name': 'test-slb-service-group',
            'appliance': 'appliance_acos_v3.0',
        }
        result = self.action.run(**params)

        # check action results
        self.assertEqual(result, (True, RESP_SUCCESS))

        # check sending request contents that acos_client,
        # which stackstorm-acos depends on, sends.
        self.assertEqual(len(self._sending_requests), 1)

        urlobj = urlparse(self._sending_requests[0]['url'])
        self.assertEqual(urlobj.hostname, 'appliance_acos_v3.0')
        self.assertEqual(urlobj.path, '/axapi/v3/slb/service-group/test-slb-service-group')
        self.assertEqual(self._sending_requests[0]['method'], 'GET')

    @mock.patch('acos_client.v30.axapi_http.Session')
    def test_delete_slb_service_group_for_acos(self, mock_session):
        mock_session.return_value = self.get_mock_session(resp_data=RESP_SUCCESS)

        params = {
            'action': 'delete',
            'object_path': 'slb.service_group',
            'one_target': True,
            'name': 'test-slb-service-group',
            'appliance': 'appliance_acos_v3.0',
        }
        result = self.action.run(**params)

        # check action results
        self.assertEqual(result, (True, RESP_SUCCESS))

        # check sending request contents that acos_client,
        # which stackstorm-acos depends on, sends.
        urlobj = urlparse(self._sending_requests[0]['url'])
        self.assertEqual(urlobj.hostname, 'appliance_acos_v3.0')
        self.assertEqual(urlobj.path, '/axapi/v3/slb/service-group/test-slb-service-group')
        self.assertEqual(self._sending_requests[0]['method'], 'DELETE')

    @mock.patch('acos_client.v30.axapi_http.Session')
    def test_create_slb_service_group_for_acos(self, mock_session):
        mock_session.return_value = self.get_mock_session(resp_data=RESP_SUCCESS)

        params = {
            'action': 'create',
            'object_path': 'slb.service_group',
            'one_target': True,
            'name': 'test-slb-service-group',
            'protocol': 'tcp',
            'lb_method': 'round-robin',
            'appliance': 'appliance_acos_v3.0',
        }
        result = self.action.run(**params)

        # check action results
        self.assertEqual(result, (True, RESP_SUCCESS))

        # check sending request contents that acos_client,
        # which stackstorm-acos depends on, sends.
        urlobj = urlparse(self._sending_requests[0]['url'])
        self.assertEqual(urlobj.hostname, 'appliance_acos_v3.0')
        self.assertEqual(urlobj.path, '/axapi/v3/slb/service-group/')
        self.assertEqual(self._sending_requests[0]['params']['data'], json.dumps({
            "service-group": {
                "name": "test-slb-service-group",
                "protocol": "tcp",
                "health-check-disable": 0,
                "lb-method": "round-robin",
                "stateless-auto-switch": 0
            }
        }))
        self.assertEqual(self._sending_requests[0]['method'], 'POST')
