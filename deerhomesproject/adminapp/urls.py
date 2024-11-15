from django.urls import path, re_path
from.import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


from deerhomesproject import settings 
from django.contrib.auth.views import LoginView


from django.contrib.auth import views as auth_views


urlpatterns = [
   path("",views.loginpage,name='loginpage'),
   path("loginpage",views.loginpage,name='loginpage'),
   path("logout",views.logout,name='logout'),

   
   # path("logout",views.logout,name='logout'),
   path("",views.dashboard,name='dashboard'),
   path("dashboard",views.dashboard,name='dashboard'),
   path("projects",views.projects,name='projects'),
   path("projects/<int:id>",views.projectview,name='projectview'),   
   path("projects/<int:id>/edit",views.projectedit,name='projectedit'),  
   path("project/create",views.projectcreate,name='projectcreate'),
   path("projects/<int:id>/delete",views.projectdelete,name='projectdelete'),  
   path("blogs",views.blogss,name='blogss'),
   path("blog/create",views.createBlogs,name='createBlogs'),
   path("blog/<int:id>",views.blogView,name='blogView'),   
   path("blog/<int:id>/edit",views.blogEdit,name='blogEdit'),
   path("blog/<int:id>/delete",views.blogDelete,name='blogDelete'),  
   path("contact-us",views.contact,name='contactus'),
   path("contact-us/<int:id>",views.contactview,name='contactview'),   
   path("contact-us/<int:id>/edit",views.contactedit,name='contactedit'),  
   path("category",views.category,name='category'),
   path("category-create",views.categorycreate,name='categorycreate'),
   path("change-password",views.changepassword,name='changepassword'),
   
   re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
   
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)