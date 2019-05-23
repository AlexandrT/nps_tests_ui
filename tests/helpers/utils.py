import i18n
import json
import os
import re

from random import randrange


class CustomTranslator:
    def __init__(self):
        self.locale = i18n.config.get('locale')
        i18n.resource_loader.load_directory(os.path.join(os.path.dirname(__file__), 'support/translations'), self.locale)

    def get_translation(self, key):
        result = i18n.translations.container[self.locale][key]

        return result

translator = CustomTranslator()

def current_locale():
    locale = os.environ['TEST_LANG']
    return locale

def list_to_set(arr):
    dset = set()

    for elem in arr:
        dset.add(json.dumps(elem, sort_keys=True))

    return dset

def get_int(string):
    num = int(re.search(r'\d+', string).group())
    return num
