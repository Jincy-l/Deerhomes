from django.shortcuts import render, get_object_or_404, redirect

from . models import *
from .models import login,projectss,tbl_blogs
get_object_or_404
# Create your views here.
def userindex(request):
    
    projects = projectss.objects.all() #.order_by('-created_at')[:4]
    
    Categories = Category.objects.all()
    context = {
        "projects" : projects,
        "categories" : Categories
    }
    return render(request,'main/userindex.html',context)
def mainindex(request): 
    projects = projectss.objects.all().order_by('-created_at')[:4]
    
    Categories = Category.objects.all()
    context = {
        "projects" : projects,
        "categories" : Categories
    }
    return render(request,'mainindex.html',context)
def about(request):
    return render(request,'about.html')
def project(request):
    cat_id = request.GET.get('category')
    print(cat_id)
        
    if cat_id:
        projects = projectss.objects.filter(cat_id_id=cat_id)
    else:
        projects = projectss.objects.all()
    Categories = Category.objects.all()
    context = {
        "projects" : projects,
        "categories" : Categories,
        "cat_id" : cat_id
    }
  
    
    return render(request,'project/project.html',context)
def project_detail(request, id):
    projects = get_object_or_404(projectss, id=id) 
    # projects = projectss.objects.all()   

    # projects = projectss.objects.filter(slug=slug).first()
    Categories = Category.objects.all()
    
    recent_blogs = tbl_blogs.objects.all().order_by('-created_at')[:3]
    context = {
        "projects" : projects,
        "categories" : Categories,
        "recent_blogs" : recent_blogs
        # "cat_id" : projects.cat_id_id
    }
    return render(request,'project/projectdetail.html',context)



def service(request):
    return render(request,'service.html')
def contact(request):
    if request.method == "POST":
        # Get the data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        
                
        

        # Save the data to the Message model
        Contactus.objects.create(name=name, email=email,  phone=phone, message=message)        
        return redirect('contact')
        
    return render(request,'contact.html')
    
def blog(request):
   
    blog=tbl_blogs.objects.all()  
    Categories = Category.objects.all()
    recent_blogs = tbl_blogs.objects.all().order_by('-created_at')[:3]    
    context = {
        "blogs": blog,
        "categories" : Categories,
        "recent_blogs" : recent_blogs
    }

    return render(request, 'blog/blog.html', context)
  
def blog_detail(request,id):
    blog = get_object_or_404(tbl_blogs, id=id)   
    Categories = Category.objects.all()
    # context = {
    #         "blog" : blog,
    #         "categories" : Categories,
    #     }
    
    recent_blogs = tbl_blogs.objects.all().order_by('-created_at')[:3]    
    context = {
        "blog": blog,
        "categories" : Categories,
        "recent_blogs" : recent_blogs
    }

    return render(request,'blog/blogdetail.html',context)


