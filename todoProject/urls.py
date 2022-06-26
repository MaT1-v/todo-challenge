from django.contrib import admin
from django.urls import path
from todoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task/', views.task),
    path('api/task/<int:pk>', views.taskPK),
    path('api/task_detail/<str:nameTask>', views.taskDetail),
    path('', views.homePage),

]

handler404 = 'todoApp.views.notFound'