from django import forms

SORT_CHOICES = (
    ('', 'Relevance'),
    ('price_asc', 'Price: Low to High'),
    ('price_desc', 'Price: High to Low'),
    ('newest', 'Newest'),
)

class ProductFilterForm(forms.Form):
    q = forms.CharField(required=False, label='Search')
    price_min = forms.DecimalField(required=False, min_value=0, decimal_places=2, label='Min ₹')
    price_max = forms.DecimalField(required=False, min_value=0, decimal_places=2, label='Max ₹')
    sort = forms.ChoiceField(required=False, choices= SORT_CHOICES)
