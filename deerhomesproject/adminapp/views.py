# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from deerhomesapp.models import login as log,projectss,Category,Contactus,tbl_blogs,tbl_blog_sub,tbl_sub_image
from django.core.files.storage import FileSystemStorage
import hashlib
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.http import HttpResponse
from django.shortcuts import render, redirect
import os  
from django.db import transaction
from django.utils.text import slugify

def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Authenticate user using Django's built-in authentication
        auth = log.objects.filter(email=email).first()
        # auth.password=hash_password(password)
        # auth.save()
        # print(auth.email)
        if auth is not None:
            if validate_password(password, auth.password):
                # Log in the user and set session variables
                # login(request, auth)
                request.session['role'] = auth.role  # Assuming your User model has a 'role' field
                request.session['id'] = auth.id  # Assuming your User model has a 'role' field
                print(auth.role)
                if auth.role == 'user':
                    return redirect('userindex')
                elif auth.role == 1:
                    return redirect('dashboard')
                else:
                    return render(request, 'main/loginpage.html')
            else:
                message = "Invalid password"
                return render(request, 'main/loginpage.html', {'message': message})
        else:
            message = "Invalid username"
            return render(request, 'main/loginpage.html', {'message': message})
    
    return render(request, 'main/loginpage.html')
def hash_password(raw_password):
    return make_password(raw_password)
def validate_password(raw_password, hashed_password):
    return check_password(raw_password, hashed_password)

def dashboard(request):
    project=projectss.objects.all()
    totalprojects=len(project)
    blog=tbl_blogs.objects.all()
    totalblogs=len(blog)
    contacts=Contactus.objects.all()
    totalcontacts=len(contacts)
    context={
       'project':project,
       'totalprojects':totalprojects,
        'blog':blog,
        'totalblogs':totalblogs,
        'contacts':contacts,
        'totalcontacts':totalcontacts,
    }
    
    return render(request,'dashboard.html',context)
def projectcreate(request):
    categories = Category.objects.all()
    if request.method =="POST":
        try:
            with transaction.atomic(): 
                name= request.POST['name']
                address= request.POST['address']
                amount= request.POST['amount']
                description= request.POST['description']
                location= request.POST['location']
                area= request.POST['area']
                image=request.FILES.get('projectimages')
                cat_id= request.POST['cat_id']
                category = Category.objects.filter(id=cat_id).first()                
                project_image_filename = '' 
                if image:
                    base_name, extension = os.path.splitext(image.name)
                    base_name = base_name.replace(" ", "_")
                    safe_base_name = slugify(base_name)
                    fs = FileSystemStorage(location='media/projectimages', base_url='/media/')
                    project_image_filename = f"{safe_base_name}{extension}"
                    project_image_filename = fs.save( project_image_filename, image)            
                    
                pro = projectss(
                    name=name,
                    address=address,
                    amount=amount,
                    description=description,
                    location=location,
                    image=project_image_filename,                
                    area = area,
                    cat_id = category
                )        
                pro.save()  
                sub_images = request.FILES.getlist('subimages[]')                
                for sub_image in sub_images:
                    base_name, extension = os.path.splitext(sub_image.name)
                    base_name = base_name.replace(" ", "_")
                    safe_base_name = slugify(base_name)
                    fs = FileSystemStorage(location='media/projectsubimages', base_url='/media/')
                    project_sub_image_filename = f"{safe_base_name}{extension}"
                    project_sub_image_filename = fs.save( project_sub_image_filename, sub_image)       
                    sub = tbl_sub_image(
                        subimage=project_sub_image_filename, 
                        project_id=pro 
                    )
                    sub.save()                    
                return redirect('projectedit', pro.id)            
                
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect(request.META.get('HTTP_REFERER', '/'))
    context={
        'edit':True,
        'categories':categories
    }
    return render(request,'project/projectcreate.html',context)

def projects(request):
    projects1 = projectss.objects.all()
    return render(request,'project/projectlist.html',{'projects':projects1})
    # return HttpResponse('<h1>Please, enter your username</h1>')
 
def projectview(request, id):
    project = get_object_or_404(projectss, id=id)    
    categories = Category.objects.all()
    context={
        'view' : True,
        'project':project,
        'categories':categories,
    }
    return render(request,'project/projectcreate.html',context)
def projectedit(request, id):
    project = get_object_or_404(projectss, id=id)
    categories = Category.objects.all()  
    if request.method =="POST":
        try:
            with transaction.atomic(): 
                name= request.POST['name']
                address= request.POST['address']
                amount= request.POST['amount']
                description= request.POST['description']
                location= request.POST['location']
                area= request.POST['area']
                image=request.FILES.get('projectimages')
                cat_id= request.POST['cat_id']
                # category = Category.objects.filter(id=cat_id).first()
                category = get_object_or_404(Category, id=cat_id)
                project_image_filename = '' 
                if image:
                    base_name, extension = os.path.splitext(image.name)
                    base_name = base_name.replace(" ", "_")
                    safe_base_name = slugify(base_name)
                    fs = FileSystemStorage(location='media/projectimages', base_url='/media/')
                    project_image_filename = f"{safe_base_name}{extension}"
                    project_image_filename = fs.save( project_image_filename, image)                    
                    project.image=project_image_filename           
             
                project.name = name
                project.address = address
                project.amount = amount
                project.description = description
                project.location = location
                project.cat_id = category  
                project.area = area 
                project.save()
                sub_images = request.FILES.getlist('subimages[]')
                for sub_image in sub_images:                    
                    project_sub_image_filename = '' 
                    base_name, extension = os.path.splitext(sub_image.name)
                    base_name = base_name.replace(" ", "_")
                    safe_base_name = slugify(base_name)
                    fs = FileSystemStorage(location='media/projectsubimages', base_url='/media/')
                    project_sub_image_filename = f"{safe_base_name}{extension}"
                    project_sub_image_filename = fs.save( project_sub_image_filename, sub_image)       
                    sub = tbl_sub_image(
                        subimage=project_sub_image_filename, 
                        project_id=project 
                    )
                    sub.save()                   
                return redirect('projectedit', project.id)      
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect(request.META.get('HTTP_REFERER', '/'))    
        
    context={
        'edit':True,
        'project':project,
        'categories':categories
    }
    return render(request,'project/projectcreate.html',context)

def projectdelete(request, id):
    project = get_object_or_404(projectss, id=id)
    if request.method =="POST":
        project.soft_delete()
    return redirect('projects')

def createBlogs(request):
    if request.method =="POST":
        try:
            with transaction.atomic():  
                name= request.POST['name']
                # slug= request.POST['slug']
                image=request.FILES.get('blog_image')
                subtitles = request.POST.getlist('subtitlename[]')  # Fetching list of subtitles
                sub_contents = request.POST.getlist('subtitlecontent[]')
                description= request.POST['description']
                metatag= request.POST['metatag']
                metakeyword= request.POST['metakeyword']
                metadescription= request.POST['metaDescription']
                
                blog_image_filename = '' 
                if image:
                    base_name, extension = os.path.splitext(image.name)
                    base_name = base_name.replace(" ", "_")
                    safe_base_name = slugify(base_name)
                    fs = FileSystemStorage(location='media/blogimages', base_url='/media/')
                    blog_image_filename = f"{safe_base_name}{extension}"
                    blog_image_filename = fs.save( blog_image_filename, image)    
                    # blog_image_filename = os.path.join("blogimages", blog_image_filename)
                    new_blog = tbl_blogs(
                        name=name,
                        # slug=slug,           
                        blog_image=blog_image_filename,
                        description=description,
                        metatag=metatag,
                        metakeyword=metakeyword,
                        metadescription=metadescription
                    )
                    new_blog.save()
                    if new_blog:
                        for subtitle, sub_content in zip(subtitles, sub_contents):
                            if subtitle and sub_content: 
                                tbl_blog_sub.objects.create(blog_id=new_blog, sub_title=subtitle, sub_title_content=sub_content)

        except Exception as e:
              messages.error(request, f"An error occurred: {str(e)}")
              return redirect(request.META.get('HTTP_REFERER', '/')) 
        return redirect('blogss')
        
    context={
        'edit':True
    }
    return render(request,'blog/createblogs.html',context)

def blogView(request, id):
    blog = get_object_or_404(tbl_blogs, id=id)    
   
    context={
        'view' : True,
        'blog':blog,
     
    }
    return render(request,'blog/createblogs.html',context)
def blogEdit(request, id):
    blog = get_object_or_404(tbl_blogs, id=id)
    sub_blog = tbl_blog_sub.objects.filter(blog_id_id = id).all()
    if request.method =="POST":
        try:
            with transaction.atomic():  
                name= request.POST['name']
                description= request.POST['description']
                metatag= request.POST['metatag']
                metakeyword= request.POST['metakeyword']
                metadescription= request.POST['metaDescription']                
                subtitles = request.POST.getlist('subtitlename[]')  # Fetching list of subtitles
                sub_contents = request.POST.getlist('subtitlecontent[]')
                blog_image_filename = ''
                image=request.FILES.get('blog_image')
                if image:            
                    base_name, extension = os.path.splitext(image.name)
                    base_name = base_name.replace(" ", "_")
                    safe_base_name = slugify(base_name)
                    fs = FileSystemStorage(location='media/blogimages', base_url='/media/')
                    blog_image_filename = f"{safe_base_name}{extension}"
                    blog_image_filename = fs.save( blog_image_filename, image)                    
                    blog.blog_image=blog_image_filename
              
                blog.name = name
                blog.description = description
                blog.metatag = metatag
                
                blog.metakeyword = metakeyword
                blog.metadescription = metadescription  
                blog. blog_image=image     
                blog.save()
                
    #             if blog:
    #                 for subtitle, sub_content in zip(subtitles, sub_contents):
    #                     # if subtitle and sub_content: 
    #                     #     tbl_blog_sub.objects.create(blog_id=blog, sub_title=subtitle, sub_title_content=sub_content)
    #                     if subtitle and sub_content:
    #                         try:
    #                             # Update the record where blog_id matches and the current subtitle matches
    #                             tbl_blog_sub.objects.filter(blog_id=blog).update(
    #                                 sub_title=subtitle,
    #                                 sub_title_content=sub_content
    #                             )
    #                         # tbl_blog_sub(
    #                         #             blog_id=new_blog, 
    #                         #             sub_title=subtitle,
    #                         #             sub_title_content=sub_content
    #                         #         ).save()     
    #     except Exception as e:
    #         messages.error(request, f"An error occurred: {str(e)}")
    #         return redirect(request.META.get('HTTP_REFERER', '/'))        
    # context={
    #     'edit':True,
    #     'blog':blog,
    #     'sub_blogs':sub_blog,
        
    # }
    # Update or create subtitles and contents
                existing_subtitles = {record.sub_title: record for record in sub_blog}
                processed_subtitles = set()

                for subtitle, sub_content in zip(subtitles, sub_contents):
                    if subtitle and sub_content:
                        if subtitle in existing_subtitles:
                            # Update existing record
                            existing_subtitles[subtitle].sub_title_content = sub_content
                            existing_subtitles[subtitle].save()
                        else:
                            # Create new record
                            tbl_blog_sub.objects.create(blog_id=blog, sub_title=subtitle, sub_title_content=sub_content)
                        processed_subtitles.add(subtitle)

                # Delete any subtitles that were not processed (i.e., deleted)
                for subtitle in existing_subtitles.keys():
                    if subtitle not in processed_subtitles:
                        existing_subtitles[subtitle].delete()

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        context = {
        'edit': True,
        'blog': blog,
        'sub_blogs': sub_blog,
        }
        return redirect('blogEdit', id)
    context = {
        'edit': True,
        'blog': blog,
        'sub_blogs': sub_blog,
    }
    return render(request,'blog/createblogs.html',context)

def blogDelete(request, id):
    blog = get_object_or_404(tbl_blogs, id=id)
    if request.method =="POST":
        blog.soft_delete()
    return redirect('blogss')
def blogss(request):
    blog = tbl_blogs.objects.all()
    context={
        'blogs':blog
    }
    return render(request,'blog/blogss.html',context)
 
def category(request):
    return render(request,'category/categorylist.html')
def categorycreate(request):
    return render(request,'category/categorycreate.html')


def changepassword(request):
        if request.method == 'POST':
            # Get the user input
            id = request.session['id']
            old_password = request.POST.get('oldpassword')
            new_password = request.POST.get('newpassword')
            confirm_password = request.POST.get('confirmpassword')
            user = log.objects.filter(id=id).first()
            if user and validate_password(old_password, user.password):
                if new_password == confirm_password:
                    user.password = hash_password(new_password)                      
                    user.save()                    
                    update_session_auth_hash(request, user)                    
                    request.session['id'] = user.id                    
                    messages.success(request, "Password updated successfully.")
                    return redirect('changepassword')  
                else:
                    messages.error(request, "New password and confirm password do not match.")
                    return redirect('changepassword')
            else:
                messages.error(request, "Old password is incorrect or user not found.")
                return redirect('changepassword') 
        return render(request, 'changepassword.html')


def contact(request):
    contact = Contactus.objects.all()
    context={
        'contacts':contact
    }
    return render(request,'contactus/contactus.html',context)

def contactview(request, id):
    contactus = get_object_or_404(Contactus, id=id)   
    context={
        'view' : True,
        'contactus':contactus
    }
    return render(request,'contactus/contactuscreate.html',context)
def contactedit(request, id):
    contactus = get_object_or_404(Contactus, id=id)
    if request.method =="POST":
        reply= request.POST['reply']
        if contactus.status == 1:
            contactus.reply = reply 
            contactus.status = 2       
            contactus.save()        
    context={
        'edit':True,
        'contactus':contactus,
    }
    return render(request,'contactus/contactuscreate.html',context)
def logout(request):
    request.session.flush()
    return redirect('loginpage')