import app_settings
from collections import Counter, OrderedDict
import app_exceptions
from utils_functionnal import cached_property

class EngineHandler:
    def __init__(self, templates=None):
        self._templates = templates
        self._engines = {}

    def templates(self):
        if self._templates is None:
            self._templates = app_settings.TEMPLATES

            templates = OrderedDict()
            backend_names = []

            for tpl in self._templates:
                tpl = tpl.copy()

                try:
                    default_name = tpl['BACKEND'].rsplit('.', 2)[-2]
                except Exception:
                    app_exceptions.ImproperlyConfigured()
                    raise

            tpl.setdefault('NAME', default_name)
            tpl.setdefault('DIRS', [])
            tpl.setdefault('APP_DIRS', False)
            tpl.setdefault('OPTIONS', {})

            templates[tpl['NAME']] = tpl
            backend_names.append(tpl['NAME'])

            counts = Counter(backend_names)
            duplicates = [alias for alias, count in counts.most_common() if count > 1]
            if duplicates:
                app_exceptions.ImproperlyConfigured()
                raise

            return templates

    def __getitem__(self, alias):
        try:
            return self._engines[alias]
        except KeyError:
            try:
                params = self.templates[alias]
            except KeyError:
                raise

    def all(self):
        return [self[alias] for alias in self]