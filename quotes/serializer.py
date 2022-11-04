from rest_framework import serializer
from quotes.models import Quotes

class QuotesSerializer(serializer.ModelSerializer):
    
    class Meta:
        model = Quotes
        fields = ('Id_quotes',
                  'Date',
                  'Time',
                  'Img',
                  'Description')