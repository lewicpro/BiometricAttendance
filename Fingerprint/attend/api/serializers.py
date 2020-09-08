from rest_framework import serializers
from ..models import Workers, SmsModel, Posts, Register, suggestions, EventsDates, RealAtendance, RealSignOut, UploadNotes
from django.contrib.auth import get_user_model
from rest_framework.serializers import CharField, EmailField, ValidationError, SerializerMethodField
from django.db.models import Q
User = get_user_model()



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

class RegisterSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    finger_print = serializers.CharField(label='fingerprint')
    class  Meta:
        model = Register
        fields =[
            'pk',
            'title',
            'user',
            "Reg_number",
            'first_name',
            'second_name',
            'third_name',
            'depertment',
            'finger_print',
            'date_registered',
            'phone_number',
            'email',
            'age',

        ]
        read_only_fields = ['user']
    # def validate(self, data):   
    #     finger_print = data['finger_print']
    #     qs = Register.objects.filter(finger_print__iexact=finger_print)
    #     print(qs)
    #     if qs.exists():
    #         raise ValidationError("The device has already been used")
    #     return data
     

    def validate_finger_print(self, value):
        data = self.get_initial()
        finger_print = data.get("finger_print")
        finger_print = value
        print("here")
        finger_qs = Register.objects.filter(finger_print=finger_print)
        print(finger_qs)
        if finger_qs.exists():
            raise serializers.ValidationError("The device has already been used")
        return value




class RealAtendanceSerializer(serializers.ModelSerializer):
    class  Meta:
        model = RealAtendance
        fields =[
        'user',
        'Reg_number',
        'first_name',
        'second_name',
        'third_name',
        'depertment',
        'subjects',
        'finger_print',
        'date_registered',
        'phone_number',
        'time',
        ]



class RealSignOutSerializer(serializers.ModelSerializer):
    class  Meta:
        model = RealSignOut
        fields =[
        'user',
        'Reg_number',
        'first_name',
        'second_name',
        'third_name',
        'depertment',
        'subjects',
        'date_registered',
        'phone_number',
        'time',
        ]


class WorkersSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class  Meta:
        model = Workers
        fields =[
            'pk',
            'user',
            'title',
            'first_name',
            'second_name',
            'third_name',
            'time_arrived',
            'date_registered',
            'percentage',
            'depertment'

        ]
        read_only_fields = ['user']
    # def validate_second_name(self, value):
    #     qs = Workers.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError('The name aready exist')





class PostsSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Posts
        fields =[
            'pk',
            'author_name',
            'description',
            'image',
            'comments',
            # 'likes',
            'date'


        ]
        # read_only_fields = ["author_name"]




        def validate_second_name(self, value):
            qs = Workers.objects.filter(description__iexact=value)
            if qs.exists():
                raise serializers.ValidationError('The name aready exist')















class UploadNoteSerializer(serializers.ModelSerializer):
    class  Meta:
        model = UploadNotes
        fields =[
            'year',
            'semister',
            'field',
            'subject',
            'title',
            'filenotes',
            'time',
        ]




class SuggestionsSerializer(serializers.ModelSerializer):
    class  Meta:
        model = suggestions
        fields =[
            'pk',
            'name',
            'department',
            'suggest',
            'time',


        ]
        read_only_fields = ["name"]













class EventSerializer(serializers.ModelSerializer):
    class  Meta:
        model = EventsDates
        fields =[
            'Date',
            'Event',
            'Description',
        ]





class SmsSerializer(serializers.ModelSerializer):
    class  Meta:
        model = SmsModel
        fields =[
            'pk',
            'name',
            'phone',
        ]



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model =User
        fields = ('username', 'password')





class UserLoginSerializer(serializers.ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(allow_blank=True)
    email = EmailField(label="email ", allow_blank=True)
    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'password',
            'token',
        ]

        extra_kwargs = {"password":
                                {"write_only": True}
                                }

    def validate(self, data):
        user_obj =None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or Email is required to login")

        user =User.objects.filter(
            Q(email=email) |
            Q(username=username)
            ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect password")
        data["token"] = "SOME RANDOM TO"


        return data
