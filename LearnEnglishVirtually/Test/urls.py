from django.urls import path
from .views import *

urlpatterns = [
    path('', TestManagementListView.as_view(), name='main-view'),
    path('<pk>/', test_management_view, name='quiz-view'),
    path('<pk>/save/', save_test_management_view, name='save-view'),
    path('<pk>/data/', test_data_details_view, name='quiz-data-view'),
]