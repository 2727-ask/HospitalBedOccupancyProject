from django.urls import path
from . import views
urlpatterns=[
    path('api/',views.HospitalAPIView.as_view(),name="getHospitals"),
    path('api/<int:pk>',views.HospitalAPIView.as_view(),name="getHospitals")
]