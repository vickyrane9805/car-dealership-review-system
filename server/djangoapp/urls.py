from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('test', views.test_api, name='test'),
    path('dealers', views.get_dealers, name='get_dealers'),
    path('dealer/<int:dealer_id>', views.get_dealer_by_id, name='get_dealer_by_id'),
    path('dealersByState', views.get_dealers_by_state, name='get_dealers_by_state'),
    path('reviews/<int:dealer_id>',views.get_dealer_reviews,name='get_dealer_reviews',),
    path('cars', views.get_all_cars, name='get_all_cars'),
    path('analyze/<str:review_text>',views.analyze_review,name='analyze_review'),
]