
from rest_framework import serializers
from Two.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields = ( 'name', 'mark')




