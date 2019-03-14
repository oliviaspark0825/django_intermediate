from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    # path('<int:pk>/update/', views.update, name='update'),
    path('<int:board_pk>/edit/', views.edit, name='edit'), # GET(edit), POST로 들어오면 (UPDATE)
    path('<int:board_pk>/delete/', views.delete, name='delete'), # POST(DELETE)
    path('<int:board_pk>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    path('new/', views.new, name='new'), # GET(NEW) 유저가 post 이면 써지는 요청이고 , new 는 띄워주는거구나 / POST(CREATE)
    path('', views.index, name='index'),
    ]
    