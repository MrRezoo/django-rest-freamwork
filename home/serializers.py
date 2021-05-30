from rest_framework import serializers

# class PersonSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=200)
#     age = serializers.IntegerField()
#     email = serializers.EmailField()
#
#     def update(self, instance, validated_data):
#         pass
#
#     def create(self, validated_data):
#         pass
from home.models import Person


class PersonSerializer(serializers.ModelSerializer):
    # car = serializers.StringRelatedField()
    # car = serializers.PrimaryKeyRelatedField(read_only=True)
    car = serializers.SlugRelatedField(slug_field='model', read_only=True)

    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'email', 'car')
        extra_kwargs = {
            'email': {'write_only': True},
            'name': {'help_text': "this is your name"}
        }

    def validate_name(self, value):
        if value.lower() == 'admin':
            raise serializers.ValidationError('name cant be admin')
        return value
