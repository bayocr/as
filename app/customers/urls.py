from django.urls.conf import path

from customers import views


urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer-list'),
    path('create', views.CustomerCreate.as_view(), name='customer-create'),
    path('<pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('<pk>/update/', views.CustomerUpdate.as_view(), name='customer-update'),
    path('<pk>/delete/', views.CustomerDetele.as_view(), name='customer-delete'),
]
