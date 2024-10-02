
from django.urls import path
from .views import ProductDataView

urlpatterns = [
    path('produtos/<int:id>/', ProductDataView.as_view(), name='product-data'),
]
