from rest_framework import viewsets,permissions,mixins,generics
from django.contrib.auth.models import User
from  . import serializers,models,permissions as perms


class BookViewSet(viewsets.ModelViewSet):
     """
    Returns a list of all **active** accounts in the system.

    For more details on how accounts are activated please [see here][ref].

    [ref]: http://example.com/activating-accounts
    """
     queryset=models.Book.objects.select_related("publisher").prefetch_related("authors").all()
     serializer_class = serializers.BookSerializer
     permission_classes = [perms.IsAdminOrReadOnly]

   
class AuthorViewSet(viewsets.ModelViewSet):
     queryset = models.Author.objects.all()
     serializer_class = serializers.AuthorSerializer
     permission_classes = [perms.IsAdminOrReadOnly]
     
         
class PublisherViewSet(viewsets.ModelViewSet):
     queryset = models.Publisher.objects.all()
     serializer_class = serializers.PublisherSerializer
     permission_classes = [perms.IsAdminOrReadOnly]

     
class BookInstanceViewSet(viewsets.ModelViewSet):
     queryset=models.BookInstance.objects.select_related("book","taken_by").all()
     serializer_class = serializers.BookInstanceSerializer
     permission_classes = [permissions.IsAuthenticated]
     
     def get_queryset(self):
          if self.request:
               return models.BookInstance.objects.filter(taken_by=self.request.user)
          
     
class LibraryUserViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
     serializer_class = serializers.LibraryUserSerializer
     permission_classes = [permissions.IsAuthenticated]
     
     def get_queryset(self):
          if self.request:
                return User.objects.filter(id=self.request.user.id)
           

class RegisterLibraryUserViewSet(viewsets.GenericViewSet,generics.CreateAPIView):
     serializer_class = serializers.RegisterLibraryUserSerializer
     queryset = User.objects.all()       