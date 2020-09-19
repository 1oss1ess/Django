from rest_framework import serializers
from ..models import ParliamentMembers


class ParliamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParliamentMembers
        fields = [
            'name',
            'date_birth',
            'place_birth',
            'profession',
            'languages',
            'selected_with',
            'email',
            'image'
        ]
