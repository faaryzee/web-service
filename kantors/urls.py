from django.urls import path
from .views import kantorsListView, KantorsDetailView

urlpatterns = [
  path('kantors', kantorsListView.as_view(), name='list-item'),
  path('kantors/<int:pk>', KantorsDetailView.as_view(), name='detail-item')
]