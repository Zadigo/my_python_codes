import template_loader
import http_response

def render(request, template_name, context=None, content_type=None, status=None, using=None):
    content = template_loader.get_template('test.txt', using=using)
    return http_response.HttpResponse(content, caller='render', status=200)

def redirect(to, *args, permanent=False, **kwargs):
    pass

def _get_queryset(klass):
    pass

def get_object_or_404(klass, *args, **kwargs):
    pass

def get_list_or_404(klass, *args, **kwargs):
    pass

def resolve_url(to, *args, **kwargs):
    pass

print(render('request','text.txt'))