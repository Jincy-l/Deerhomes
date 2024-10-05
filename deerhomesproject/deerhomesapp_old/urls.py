from django.urls import path, re_path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
   path("",views.mainindex,name='mainindex'),
   path("mainindex",views.mainindex,name='mainindex'),
   path("userindex",views.userindex,name='userindex'),
   path("about",views.about,name='about'),
   path("project",views.project,name='project'),   
   path('project/<int:id>/', views.project_detail, name='project_detail'),
   path("service",views.service,name='service'),
   path("contact",views.contact,name='contact'),
   path("blog",views.blog,name='blog'),   
   path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
   
   re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)