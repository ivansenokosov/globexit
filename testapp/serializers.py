from rest_framework import serializers
from testapp.models import GlobexUsers

class GlobexUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobexUsers
        fields = '__all__'