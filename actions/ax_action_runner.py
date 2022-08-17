import acos_client as acos

from acoslib.action import BaseAction


class AXActionRunner(BaseAction):
    def do_run(self, action, object_path, target, **kwargs):
        if kwargs.get('specified_target'):
            target = kwargs.get('specified_target').get("target")
        client = self.login(target, kwargs.get('specified_target'))
        if client:
            try:
                # transforms user parameters as needed
                kwargs = self._transform_params(client, object_path, action, **kwargs)

                _target_obj = self.get_object(client, object_path)

                return (True, getattr(_target_obj, action)(**self._filter_args(kwargs)))
            except acos.errors.AuthenticationFailure:
                return (False, '[%s] An authentication error is occurr' % (target))
            except acos.errors.NotFound as e:
                return (False, e)
            except AttributeError:
                return (False, '[%s] The acos_client has no interfaces for %s' %
                               (target, object_path))
        else:
            return (False, '[%s] Failed to initilaize Client object of acos_client' % target)

    def run(self, action, object_path, one_target, **kwargs):
        if kwargs.get('specified_target'):
            return self.do_run(action, object_path, None, **kwargs)
        if one_target or kwargs.get('appliance'):
            return self.do_run(action, object_path, kwargs.get('appliance'), **kwargs)
        else:
            results = []
            for config in self.config['appliance']:
                results.append(self.do_run(action, object_path, config['target'], **kwargs))

                if not results[-1][0]:
                    return (False, results)

            return (True, [x[1] for x in results])

    def _transform_params(self, client, object_path, action, **kwargs):
        if object_path == 'slb.service_group.member' and action == 'create':
            # transforms status parameter from boolean to the internal constant of acos-client
            if kwargs['status']:
                kwargs['status'] = client.slb.UP
            else:
                kwargs['status'] = client.slb.DOWN

        return kwargs

    """
    This filters parameters for ACOS pack to pass only available parameters to the ACOS Client.
    """
    def _filter_args(self, kwargs):
        return {k: v for (k, v) in kwargs.items() if k not in self.PARAMS_FOR_PACK}
