from rest_framework import serializers
from .models import User
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):

    current_datetime = serializers.SerializerMethodField()
    class Meta:
        model =  User
        fields = [
            'email',
            'current_datetime',
            'github_url'
        ]

    def get_current_datetime(self, obj):
        return datetime.utcnow().isoformat() + 'Z'