import mock

from acos_base_action_test_case import ACOSBaseActionTestCase
from ax_action_runner import AXActionRunner


class ListSLBServersTestCase(ACOSBaseActionTestCase):
    __test__ = True
    action_cls = AXActionRunner

    def setUp(self):
        super(ListSLBServersTestCase, self).setUp()

        self.action = self.get_action_instance(self._full_config)
        self.action.logger.addHandler(self._log_handler)

    @mock.patch('acos_client.Client')
    def test_list_slb_servers(self, mock_client):
        # set mock of action
        mock_action = mock.Mock()
        mock_action.slb.server.get.return_value = 'test-result'

        mock_client.return_value = mock_action

        # execute action
        params = {
            'object_path': 'slb.server',
            'action': 'get',
            'name': 'hoge',
            'one_target': False,
        }
        result = self.action.run(**params)

        self.assertTrue(result[0])
        self.assertEqual(len(result[1]), 2)
        self.assertEqual(result[1], ['test-result', 'test-result'])
        self.assertEqual(len(self._log_handler.messages['error']), 0)

    @mock.patch('acos_client.Client')
    def test_list_slb_specific_server(self, mock_client):
        # set mock of action
        mock_action = mock.Mock()
        mock_action.slb.server.get.return_value = 'test-result'

        mock_client.return_value = mock_action

        # execute action
        params = {
            'object_path': 'slb.server',
            'action': 'get',
            'name': 'hoge',
            'one_target': False,
            'appliance': 'appliance_hostname1',
        }
        result = self.action.run(**params)

        self.assertTrue(result[0])
        self.assertEqual(result[1], 'test-result')
        self.assertEqual(len(self._log_handler.messages['error']), 0)

    def test_list_slb_servers_with_invalid_appliance_parameter(self):
        # execute action
        appliance = 'invisible-appliance'
        params = {
            'object_path': 'slb.server',
            'action': 'get',
            'name': 'hoge',
            'one_target': False,
            'appliance': appliance,
        }
        result = self.action.run(**params)
        self.assertFalse(result[0])
        self.assertEqual("[%s] Failed to initilaize Client object of acos_client" % appliance,
                         result[1])
        self.assertEqual(len(self._log_handler.messages['error']), 1)
