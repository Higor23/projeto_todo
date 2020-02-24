from django.urls import path

from.import views

urlpatterns = [
    path('tasks/', views.helloword),
    path('', views.taskList, name = 'taskList'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('yourname/<str:name>', views.yourName, name='yourname')
]
