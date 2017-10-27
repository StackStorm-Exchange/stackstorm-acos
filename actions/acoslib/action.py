import acos_client as acos
import logging

from st2common.runners.base_action import Action


class BaseAction(Action):
    DEFAULT_AXAPI_VERSION_STR = 'v3.0'
    DEFAULT_AXAPI_VERSION = acos.AXAPI_30

    # These are the parameters for acos pack, not used by the ACOS Client
    PARAMS_FOR_PACK = ['appliance', 'action', 'object_path', 'one_target']

    def __init__(self, config):
        super(BaseAction, self).__init__(config)

        self._set_loglevel(logging.INFO)

        self.config = config

    def login(self, appliance):
        try:
            config = next(x for x in self.config['appliance'] if x['target'] == appliance)
            return acos.Client(config['target'],
                               config['api_version'],
                               config['userid'],
                               config['passwd'])
        except acos.errors.ACOSUnsupportedVersion as e:
            self.logger.error(e)
        except KeyError as e:
            self.logger.error(e)
        except StopIteration:
            self.logger.error("Specified appliance(%s) doesn't exist in the configuration file " %
                              appliance)

    def get_object(self, base_obj, object_path):
        obj = base_obj
        for path in object_path.split('.'):
            obj = getattr(obj, path)

        return obj

    def _set_loglevel(self, level):
        for key, logger in logging.Logger.manager.loggerDict.items():
            if isinstance(logger, logging.Logger):
                logger.setLevel(level)
