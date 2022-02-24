import mock
import re

from acos_base_action_test_case import ACOSBaseActionTestCase
from ax_action_runner import AXActionRunner


class GetSLBServerTestCase(ACOSBaseActionTestCase):
    __test__ = True
    action_cls = AXActionRunner

    def setUp(self):
        super(GetSLBServerTestCase, self).setUp()

        self.action = self.get_action_instance(self._full_config)
        self.action.logger.addHandler(self._log_handler)

    @mock.patch('acos_client.Client')
    def test_get_slb_server(self, mock_client):
        # set mock of action
        mock_action = mock.Mock()
        mock_action.slb.server.get.return_value = 'test-result'

        mock_client.return_value = mock_action

        params = {
            'object_path': 'slb.server',
            'action': 'get',
            'name': 'hoge',
            'one_target': True,
            'appliance': 'appliance_acos_v2.1',
        }
        result = self.action.run(**params)

        self.assertTrue(result[0])
        self.assertEqual(result[1], 'test-result')
        self.assertEqual(len(self._log_handler.messages['error']), 0)

    def test_get_slb_server_without_appliance(self):
        self.action.login = mock.Mock(return_value=None)

        # execute action without appliance parameter
        params = {
            'object_path': 'slb.server',
            'action': 'get',
            'name': 'hoge',
            'one_target': True,
        }
        result = self.action.run(**params)

        self.assertFalse(result[0])
        self.assertTrue(re.match('.*Failed to initilaize Client object of acos_client$', result[1]))
        self.assertEqual(len(self._log_handler.messages['error']), 0)
