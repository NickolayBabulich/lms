from rest_framework import serializers
from users.models import User
from course.models import Payments
from course.serializers import PaymentsSerializer


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('email', 'phone', 'country', 'avatar',)
