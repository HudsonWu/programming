# models

## model relationship

+ [Examples of model relationship API usage](https://docs.djangoproject.com/en/2.2/topics/db/examples/)
+ [models](https://docs.djangoproject.com/en/2.2/topics/db/models/)
+ [modelforms](https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/)

### choices

```
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'SMALL'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SEZES)

>>> p = Person(name="Fred Flintstone", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
```

### ModelForm

```
from myapp.models import Article
from myapp.forms import ArticleForm

# Create a form instance from POST data
>>> f = ArticleForm(request.POST)

# Save a new Article object from the form's data
>>> new_article = f.save()

# Create a form to edit an existing Article, but use
# POST data to populate the form
>>> a = Article.objects.get(pk=1)
>>> f = ArticleForm(request.POST, instance=a)
>>> f.save()
```

#### commit=False

```
# Create a form instance with POST data
>>> f = AuthorForm(request.POST)

# Create, but don't save the new author instance
>>> new_author = f.save(commit=False)

# Modify the author in some way
>>> new_author.some_field = 'some_value'

# Save the new instance
>>> new_author.save()

# Now, save the many-to-many data for the form
>>> f.save_m2m()
```
Calling `save_m2m()` is only required if you use `save(commit=False`).
When you use a simple `save()` on a form, all data including many-to-many data 
is saved without the need for any additional method calls
