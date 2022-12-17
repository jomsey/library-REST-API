from . import models
from rest_framework import  serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ["id","name"]

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = ["id","name"]

class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    class Meta:
        model = models.Book
        fields = ["id","book_cover","type","authors","publisher","language","publication_date","description"]


class SimpleBookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    authors = AuthorSerializer(many=True)
    
    class Meta:
        model = models.Book
        fields = ["id","book_cover","type","authors","publisher","language"]


class BookInstanceSerializer(serializers.ModelSerializer):
    date_taken = serializers.ReadOnlyField()
    taken_by = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = models.BookInstance
        fields = ["id","book","date_taken","return_date","taken_by",]
        
    def create(self, validated_data):
        validated_data["taken_by"] = self.context["request"].user
        return super().create(validated_data)
   
        
class RegisterLibraryUserSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)
    
    
    class Meta:
        model =  User
        fields = ["username","email","password","confirm_password"]
    
    def validate(self, data):
        if data["password"] == data["confirm_password"]:
            validate_password(data["password"])
            return super().validate(data)
        raise serializers.ValidationError({"error":"Both password fields must be matching"})

    def create(self, validated_data):
       user = User.objects.create_user(username=validated_data["username"],
                                       email=validated_data["email"],
                                       password=validated_data["password"])
       return user

class LibraryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        read_only_fields = ["is_staff","date_joined"]
        fields = ["id","username","first_name","last_name","email","date_joined","is_active","is_staff"]


