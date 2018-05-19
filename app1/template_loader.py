def get_template(template_name, using=None):
    print('I loaded', template_name)

def select_template(template_name_list, using=None):
    pass


def render_to_string(template_name, context=None, request=None, using=None):
    pass

def _engine_list(using=None):
    return engines.all() if using is None else [engines[using]]
    