from django.urls import path
from .views import DepartemenList, CategoryDetil

urlpatterns = [
  path("departemens", DepartemenList.as_view(), name='list-departemens'),
  path("departemens/<int:pk>", CategoryDetil.as_view(), name='detail-departemens'),
  # path('items/<int:item_id>/reviews', ReviewView.as_view(), name='detail-item'),
]