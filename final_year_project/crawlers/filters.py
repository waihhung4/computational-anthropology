import django_filters
from models import Content

class crawlersFilter(django_filters.FilterSet):

    class Meta:
        model = Content
        fields = {
            'source': ['icontain'],
            'text' : ['icontain'],
            'url': ["icontain"],
            'search_keyword': ["icontain"]
        }