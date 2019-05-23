import os
import importlib

ENVIRONMENT_VARIABLE = 'TEST_LANG'
DEFAULT_LANG = 'ru-RU'

def set_package():
    return 'imhio'

def current_locale():
    env = os.environ.get('TEST_LANG')
    return DEFAULT_LANG if env == None else env

class ExpectedData:
    def __init__(self, settings_module):
        self.SETTINGS_MODULE = settings_module

        try:
            mod = importlib.import_module(self.SETTINGS_MODULE)
        except ModuleNotFoundError:
            mod = importlib.import_module("fixtures." + current_locale(),
                    __package__)

        self._explicit_settings = set()
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)

                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)

    def is_overridden(self, setting):
        return setting in self._explicit_settings

    def __repr__(self):
        return f'<{self.__class__.__name__}s "{self.SETTINGS_MODULE}s">'

settings_module = set_package() + '.fixtures.' + current_locale()
expected_data = ExpectedData(settings_module)
