from django.urls import path,include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()

#general routes
router.register("books",views.BookViewSet)
router.register("borrowed-books",views.BookInstanceViewSet)
router.register("authors",views.AuthorViewSet)
router.register("publishers",views.PublisherViewSet)
router.register("users",views.LibraryUserViewSet,basename="users")
router.register("register",views.RegisterLibraryUserViewSet)

#author routes
author_routers = routers.NestedDefaultRouter(router,"authors",lookup="authors")
author_routers.register("books",views.BookViewSet,basename="books")

#user route
user_routers= routers.NestedDefaultRouter(router,"users")
user_routers.register("borrowed-books",views.BookInstanceViewSet)
 
urlpatterns = [
   path("",include(router.urls)),
   path("",include(author_routers.urls)),
   path("",include(user_routers.urls)),
   
   ]