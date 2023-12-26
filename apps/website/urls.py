from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('sobre-nos/', views.about_us, name="about-us"),
    path('nossos-servicos/', views.services, name="services"),
    path('perguntas-frequentes/', views.faqs, name="faqs"),
    path('contactos/', views.contacts, name="contacts"),

    path('nossos-artigos/', views.blog, name="blog"),
    path('nossos-artigos/<slug:slug>', views.blog_article, name="blog-article"),
    path('nossos-artigos/categorias/<slug:slug>', views.filter_by_category, name="filter-category-new"),
    path('subscrever-newsletter/', views.newsletter, name="newsletter"),
    path('lavabwe/membro-de-equipe/<slug:slug>', views.team_member, name="team-member-detail"),
]