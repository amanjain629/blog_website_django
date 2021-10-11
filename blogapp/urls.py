from django.urls import path
from django.views.generic.edit import DeleteView
# from blogapp import views
from blogapp.views import HomeView,ArticleView,AddPostView,EditPostView,DeletePostView,AddCatagoryView,CatagoryView,CategoryListView,LikeView

urlpatterns = [
    # path("",views.index,name='index')
    path("",HomeView.as_view(),name='index'),
    path("article/<int:pk>",ArticleView.as_view(),name='article-detail'),
    path('add_post',AddPostView.as_view(),name='add_post'),
    path('add_catagory',AddCatagoryView.as_view(),name='add_catagory'),
    path('article/edit/<int:pk>',EditPostView.as_view(),name='edit-post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name='delete-post'),
    path('catagory/<str:cats>/',CatagoryView,name='catagory'),
    path('categories/',CategoryListView,name='category-list'),
    path('like/<int:pk>',LikeView,name='like-post')
]