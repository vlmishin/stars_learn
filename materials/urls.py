from django.urls import path
from . import views

urlpatterns = [
    # path('<slug:section_slug>/<slug:topic_slug>/<slug:lesson_slug>/', views.lesson_detail, name='lesson_detail'),
    path('<slug:section_slug>/<slug:topic_slug>/', views.topic_detail, name='topic_detail')
]