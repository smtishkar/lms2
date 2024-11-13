from django.urls import path
from . import views


urlpatterns = [

    path('', views.get_site_sections, name = 'index'),
    path('appointment_done/', views.success_appointment, name = 'success_appointment'),  
    path('cert_results/', views.certification_results, name = 'cert_results'),
    path('team/', views.get_team, name = 'team'),
    path('info/', views.get_info, name = 'info'),
    path('quiz/', views.quiz, name = 'quiz'),
    path('quiz_start_page/', views.quiz_start_page, name = 'quiz_start_page'),
    path('info/<slug:info_slug>/', views.get_info_details, name = 'info_detailes'),
    path('<slug:part_slug>/', views.get_technician_content, name = 'section'),
    path('area/<slug:part_slug>/', views.get_education_part, name = 'part'),                  
    path('edu_program/<slug:content_slug>/', views.get_training_content, name = 'content'),   
    path('edu_content/<slug:fin_content_slug>/', views.get_content_to_study, name = 'study'),
    path('certification_appointment/<slug:app_id>/', views.make_cert_appointment, name = 'cert_appointment'),  
    path('training_appointment/<slug:app_id>/', views.make_training_appointment, name = 'training_appointment'),



    
    

]