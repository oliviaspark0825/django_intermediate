from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/edit/', views.edit, name='edit'), # GET(edit), POST로 들어오면 (UPDATE)
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    path('new/', views.new, name='new'), # GET(NEW) 유저가 post 이면 써지는 요청이고 , new 는 띄워주는거구나 / POST(CREATE)
    path('', views.index, name='index'),
    ]
    