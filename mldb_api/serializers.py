import uuid

from rest_framework import serializers
from .models import models_repo

class model_serializers(serializers.ModelSerializer):
    class Meta:
        model = models_repo
        fields = '__all__'
class model_serializers_except_base64(serializers.ModelSerializer):
    class Meta:
        model = models_repo
        fields = 'model_name','model_type','model_file','created_at','updated_at'
