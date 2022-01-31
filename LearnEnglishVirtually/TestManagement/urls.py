from django.urls import path
from .views import *

urlpatterns = [
    path('testListView/', testManagement, name='main-view'),
    path('testListView/<pk>/', test_management_view, name='quiz-view'),
    path('testListView/<pk>/save/', save_test_management_view, name='save-view'),
    path('testListView/<pk>/data/', test_data_details_view, name='quiz-data-view'),
]