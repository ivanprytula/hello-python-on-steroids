from rest_framework import serializers

from .models import BaseModel  # noqa


class CustomSerializer(serializers.Serializer):
    # define your fields here
    field1 = serializers.CharField(max_length=100)
    field2 = serializers.IntegerField()

    # --------- CASE 1 with model ---------------
    # define any custom validation or create/update methods here
    # def validate_field1(self, value):
    #     # custom validation logic for field1
    #     if value == "invalid":
    #         raise serializers.ValidationError("Invalid value for field1")
    #     return value

    # def create(self, validated_data):
    #     # custom create logic
    #     instance = BaseModel.objects.create(**validated_data)
    #     return instance

    # def update(self, instance, validated_data):
    #     # custom update logic
    #     instance.field1 = validated_data.get("field1", instance.field1)
    #     instance.field2 = validated_data.get("field2", instance.field2)
    #     instance.save()
    #     return instance

    # --------- CASE 2 w/o model ---------------
    # serializer only accepts some request data, doesn’t save a model instance, just returns a response

    # override the create method to prevent saving a model instance
    def create(self, validated_data):
        return validated_data
