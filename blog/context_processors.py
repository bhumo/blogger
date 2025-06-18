# blog/context_processors.py

from .models import Category

def categories_processor(request):
    """
    Makes a list of all categories available to all templates.
    """
    return {'all_categories': Category.objects.all().order_by('name')}