from django.urls import path
from . import views

urlpatterns = [
    path('start/<int:course_id>/', views.start_test, name='start_test'),
    path('take/<int:attempt_id>/', views.take_test, name='take_test'),
    path('result/<int:attempt_id>/', views.test_result, name='test_result'),
    path('attempts/', views.attempt_list, name='attempt_list'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('', views.home, name='home'),
]