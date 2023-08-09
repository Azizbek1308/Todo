from django.urls import path
from .views import HomePage,StudentPage,DetailPage,EditPage,DeletePage,CreatePage



urlpatterns=[
    path('',HomePage, name='home'),
    path('student/',StudentPage.as_view(), name='Student'),
    path('student/create',CreatePage.as_view(), name='create'),
    path('student/<int:pk>',DetailPage.as_view(), name='detail'),
    path('student/<int:pk>/edit',EditPage.as_view(), name='edit'),
    path('student/<int:pk>/delete',DeletePage.as_view(), name='delete'),

]