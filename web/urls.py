# /web/urls.py
from django.urls import path
from . import views  # ایمپورت ویوهای اپلیکیشن web

urlpatterns = [
    # URL برای صفحه اصلی (مثال: /web/)
    path('expense', views.expense, name='expense'),

    # شما می‌توانید URLهای بیشتری اضافه کنید مانند:
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]
