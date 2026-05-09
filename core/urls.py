from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    
    # Auth
    path('dashboard/login/', views.admin_login, name='admin_login'),
    path('dashboard/logout/', views.admin_logout, name='admin_logout'),
    
    # Dashboard Home
    path('dashboard/', views.admin_home, name='admin_home'),
    
    # About Me
    path('dashboard/about/', views.admin_about, name='admin_about'),
    
    # Projects
    path('dashboard/projects/', views.admin_projects, name='admin_projects'),
    path('dashboard/projects/add/', views.admin_project_form, name='admin_project_add'),
    path('dashboard/projects/edit/<int:pk>/', views.admin_project_form, name='admin_project_edit'),
    path('dashboard/projects/delete/<int:pk>/', views.admin_project_delete, name='admin_project_delete'),
    
    # Certificates
    path('dashboard/certificates/', views.admin_certificates, name='admin_certificates'),
    path('dashboard/certificates/add/', views.admin_certificate_form, name='admin_certificate_add'),
    path('dashboard/certificates/edit/<int:pk>/', views.admin_certificate_form, name='admin_certificate_edit'),
    path('dashboard/certificates/delete/<int:pk>/', views.admin_certificate_delete, name='admin_certificate_delete'),
    
    # Skills
    path('dashboard/skills/', views.admin_skills, name='admin_skills'),
    path('dashboard/skills/add/', views.admin_skill_form, name='admin_skill_add'),
    path('dashboard/skills/edit/<int:pk>/', views.admin_skill_form, name='admin_skill_edit'),
    path('dashboard/skills/delete/<int:pk>/', views.admin_skill_delete, name='admin_skill_delete'),
    
    # Messages
    path('dashboard/messages/', views.admin_messages, name='admin_messages'),
    path('dashboard/messages/delete/<int:pk>/', views.admin_message_delete, name='admin_message_delete'),
]
