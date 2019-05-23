import pytest
import i18n
import os


i18n.load_path.append(os.path.join(os.path.dirname(__file__), '../support/translations'))
i18n.set('locale', os.environ["TEST_LANG"])

pytest_plugins = ['common_fixtures']
