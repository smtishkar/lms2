from django.urls import path
from . import views


urlpatterns = [

    path('', views.get_site_sections, name = 'index'),
    path('<slug:part_slug>/', views.get_technician_content, name = 'section'),
    path('technicians/<slug:part_slug>/', views.get_education_part, name = 'part'),                  
    path('test/<slug:content_slug>/', views.get_training_content, name = 'content'),   
    # path('certification_appointment/app/<int:app_id>/', views.make_cert_appointment, name = 'cert_appointment'),  
    path('certification_appointment/<slug:app_id>/', views.make_cert_appointment, name = 'cert_appointment'),  
    # path('pdf/', views.pdf_view, name='pdf'),
    # path('entrypage/', views.entry_page, name='entry_page'),
    # path('', views.get_list_video, name = 'home'),
    # path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    # path('<int:pk>/', views.get_video, name='video'),
    # path('test/', views.test, name='test'),
    # path('cats/technicians/techcont', views.technicians_content, name = 'techcont'),
    # path('cats/service_advisors/sacont', views.service_advisors_content, name = 'sacont'),
    # path('technicians/', views.get_technician_content, name = 'techcont'),
    # path('technicians/tt-level/', views.get_tt_level_content, name = 'tt-level'),
    # path('part/<slug:post_slug>/', views.show_post, name = 'post'),                          #Это пример как мы используем слаг
]