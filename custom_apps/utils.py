import re
import random
import string

def lowercase_names(*args):
    if  not args:
        return []

    postes = []
    new_poste = ''
    for arg in args:
        words = str(arg).split(' ')

        for word in words:
            new_poste += word.lower() + '-'
            new_poste_slug = re.search(r'([a-z\-]+)(\-)', new_poste).group(1)
        postes.append(new_poste_slug)
        new_poste = ''
    return postes

from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if  new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = '{slug}-{randstr}'.format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unslug_nom_poste(nom_poste):
    if not nom_poste:
        raise TypeError('%s' % nom_poste)
    
    words = str(nom_poste).split('-')
    word = ' '.join(words)

    return word

print(unslug_nom_poste('a-b-c'))


# models.py

# slug = models.SlugField(max_length=50)
# def save(self, *args, **kwargs):
#     if not self.id:
#         self.slug = slugify(unidecode(self.nom_poste))

#     super(test, self).save(*args, **kwargs)
