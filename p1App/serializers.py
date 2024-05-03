from rest_framework import serializers
from p1App.models import *

class InventorRegSerial(serializers.ModelSerializer):
    class Meta:
        model=CustomUserdb
        fields=['username','full_name','mobile','country','designation','proff_bio','twitter','linkedin','']

