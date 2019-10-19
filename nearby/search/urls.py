from django.urls import path
from .views import SearchNearby

urlpatterns = [
	path('', SearchNearby.as_view())
]