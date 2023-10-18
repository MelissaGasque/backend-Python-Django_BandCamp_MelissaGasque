from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth.hashers import make_password


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(
#         validators=[
#             UniqueValidator(
#                 queryset=User.objects.all(),
#                 message="A user with that username already exists.",
#             )
#         ],
#     )
#     email = serializers.EmailField(
#         validators=[UniqueValidator(queryset=User.objects.all())],
#     )
#     password = serializers.CharField(write_only=True)
#     full_name = serializers.CharField(max_length=50, required=False)
#     artistic_name = serializers.CharField(max_length=50)

#     def create(self, validated_data: dict) -> User:
#         return User.objects.create_user(**validated_data)

#     def update(self, instance: User, validated_data: dict) -> User:
#         for key, value in validated_data.items():
#             if key == "password":
#                 setattr(instance, key, make_password(value))

#         instance.save()

#         return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'full_name',
            'artistic_name'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'username': {
                'validators': [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists."
                    )
                ]
            },
            'email': {
                'validators': [UniqueValidator(queryset=User.objects.all())]
            },
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                setattr(instance, key, make_password(value))
            else:
                setattr(instance, key, value)
                
        instance.save()

        return instance