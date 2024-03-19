from rest_framework import serializers

class loginResponse(serializers.Serializer):
    status = serializers.IntegerField()
    message= serializers.CharField(max_length = 100)
    data = serializers.CharField(max_length=100)

class errorResponse(serializers.Serializer):
    status = serializers.IntegerField()
    message= serializers.CharField(max_length = 100)