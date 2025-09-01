from .models import Category

def categories_processor(request):
    return {'site_name': 'The Dewy Ritual', 'categories': Category.objects.all()}


