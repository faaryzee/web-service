from django.urls import path
from .views import KaeyanwanView, DetailKaryawan

urlpatterns = [
  path("karyawans", KaeyanwanView.as_view(), name='list-review'),
  path("karyawans/<int:pk>", DetailKaryawan.as_view(), name='detail-review'),
  # path('kantors/<int:item_id>/karyawans', ReviewView.as_view(), name='detail-item'),
]