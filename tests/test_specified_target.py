import mock

from acos_base_action_test_case import ACOSBaseActionTestCase
from ax_action_runner import AXActionRunner


class SpecifiedTargetTestCase(ACOSBaseActionTestCase):
    __test__ = True
    action_cls = AXActionRunner

    def setUp(self):
        super(SpecifiedTargetTestCase, self).setUp()

        self.action = self.get_action_instance(self._full_config)
        self.action.logger.addHandler(self._log_handler)

    @mock.patch('acos_client.Client')
    def test_specified_target_without_one_target(self, mock_client):
        def side_effect(*args, **extra_params):
            # This checks authentication information that is passed to acos.Client
            self.assertEqual(args, ('appliance_acos_v2.1', 'v2.1', 'admin', 'hoge'))

            # This checks default extra params are set
            self.assertEqual(extra_params, {
                'max_retries': 3, 'port': 443, 'protocol': 'https', 'timeout': 5
            })

            # set mock of action
            mock_action = mock.Mock()
            mock_action.slb.server.get.return_value = 'test-result'

            return mock_action

        mock_client.side_effect = side_effect

        # execute action
        params = {
            'object_path': 'slb.server',
            'action': 'get',
            'name': 'hoge',
            'one_target': False,
            'specified_target': {
                'target': 'appliance_acos_v2.1',
                'userid': 'admin',
                'passwd': 'hoge',
                'api_version': 'v2.1',
            }
        }
        result = self.action.run(**params)

        self.assertTrue(result[0])
        self.assertEqual(result[1], 'test-result')
        self.assertEqual(len(self._log_handler.messages['error']), 0)

    @mock.patch('acos_client.Client')
    def test_specified_target_with_extra_params(self, mock_client):
        def side_effect(*args, **extra_params):
            # This checks authentication information that is passed to acos.Client
            self.assertEqual(args, ('appliance_acos_v2.1', 'v2.1', 'admin', 'hoge'))

            # This checks extra params are set as user specified
            self.assertEqual(extra_params, {
                'max_retries': 10, 'port': 80, 'protocol': 'http', 'timeout': 10
            })

            # set mock of action
            mock_action = mock.Mock()
            mock_action.slb.server.get.return_value = 'test-result'

            return mock_action

        mock_client.side_effect = side_effect

        # execute action
        params = {
            'object_path': 'slb.server',
            'action': 'get',
            'name': 'hoge',
            'one_target': False,
            'specified_target': {
                'target': 'appliance_acos_v2.1',
                'userid': 'admin',
                'passwd': 'hoge',
                'api_version': 'v2.1',
                'max_retries': 10,
                'port': 80,
                'protocol': 'http',
                'timeout': 10,
            }
        }
        result = self.action.run(**params)

        self.assertTrue(result[0])
        self.assertEqual(result[1], 'test-result')
        self.assertEqual(len(self._log_handler.messages['error']), 0)

    @mock.patch('acos_client.Client')
    def test_specified_target_with_one_target(self, mock_client):
        # set mock of action
        mock_action = mock.Mock()
        mock_action.slb.server.get.return_value = 'test-result'

        mock_client.return_value = mock_action

        params = {
            'object_path': 'slb.server',
            'action': 'get',
            'name': 'hoge',
            'one_target': True,
            'appliance': 'fuga',
            'specified_target': {
                'target': 'appliance_acos_v2.1',
                'userid': 'admin',
                'passwd': 'hoge',
                'api_version': 'v2.1',
            }
        }
        result = self.action.run(**params)

        self.assertTrue(result[0])
        self.assertEqual(result[1], 'test-result')
        self.assertEqual(len(self._log_handler.messages['error']), 0)
