from django.urls import path
from . import views


urlpatterns = [
    # path('', views.get_list_video, name = 'home'),
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path('<int:pk>/', views.get_video, name='video'),
    path('test/', views.test, name='test'),
    path('entrypage/', views.entry_page, name='entry_page'),
    # path('cats/technicians/techcont', views.technicians_content, name = 'techcont'),
    path('cats/service_advisors/sacont', views.service_advisors_content, name = 'sacont'),
    path('pdf/', views.pdf_view, name='pdf'),
    path('', views.get_site_sections, name = 'index'),
    path('technicians/', views.get_technician_content, name = 'techcont'),
]