
# from django.conf import settings
# from django.shortcuts import redirect
# from django.contrib import messages


# from django.shortcuts import redirect
# from django.utils.deprecation import MiddlewareMixin


   
# from django.utils.deprecation import MiddlewareMixin
# from django.contrib import messages

# class SessionCheckMiddleware(MiddlewareMixin):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Retrieve user role from the session
#         user_role = request.session.get('role', None)

#         # Allow access to the login page without checking the role
#         if request.path == '/' or request.path == '/login/' or request.path == '/logout/':
#             return self.get_response(request)
        
#         # If the user is not authenticated (no role in session), redirect to the login page
#         if user_role is None:
#             messages.warning(request, "Please log in to access this page.")
#             return redirect('loginpage')

#         # Restrict access based on user role
#         if user_role == 'user':
#             # Redirect user role away from admin pages
#             if request.path.startswith('/admin/'):
#                 messages.warning(request, "You are not authorized to access this page.")
#                 return redirect('userindex')
#         elif user_role == '1':  # Assuming '1' represents admin
#             # Admin has full access, no restrictions needed
#             pass
#         else:
#             # If the role is unknown, log out the user and prompt them to log in again
#             messages.warning(request, "Unknown role. Please log in again.")
#             return redirect('loginpage')

#         # If no restrictions apply, allow the request to proceed
#         return self.get_response(request)



from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages

class SessionCheckMiddleware(MiddlewareMixin):
    def process_request(self, request): 
        
        # return None 
        # # Check if the user is logged in based on a session variable
        user_role = request.session.get('role', None)  # Assuming 'role' is stored in the session
        user_id = request.session.get('id', None)

        if request.path == '/':
            # If it's the landing page, allow the request to proceed
            return None
        if request.path == '/admin/' or request.path == '/Admin/' :
            # If it's the landing page, allow the request to proceed
            return None
        if request.path == '/admin/loginpage':
            # If it's the landing page, allow the request to proceed
            return None
        # if request.path == '/user/login/':
        #     # If it's the landing page, allow the request to proceed
        #     return None
        # if request.path == '/user/register/' or  request.path == '/user/register':
        #     # If it's the landing page, allow the request to proceed
        #     return None
        # if request.path == '/user/loginForm':
        #     # If it's the landing page, allow the request to proceed
        #     return None       
        # Check if the user is logged in based on a session variable
        # if 'id' in request.session:
        #     # User is logged in, continue processing the request
        #     return None
        if user_id:
            # User is logged in, check role
            if user_role == 1 or user_role == 'staff' or user_role == 'Admin' or user_role == 'Staff':
                return None  # Allow access for admin and staff
            elif user_role == 'user' or user_role == 'User':
                # Redirect regular users away from /Official/
                if request.path.startswith('/admin/') or request.path.startswith('/Admin/'):
                    messages.warning(request, "You are not authorized to access this page.")
                    return redirect(settings.DEERAPP_LOGIN_URL)
                else:
                    return None  # Allow access for regular users
            else:
                # If role is unknown, redirect to default login
                messages.warning(request, "Unknown role. Please login again.")
                return redirect(settings.DEFAULT_LOGIN_URL)
        else:
            
            if request.path.startswith('/admin/') or request.path.startswith('/Admin/'):
                messages.warning(request, "Please login before accessing this page.")
                return redirect(settings.CUSTOM_ADMIN_LOGIN_URL)
            elif request.path.startswith('/user/'):
                messages.warning(request, "Please login before accessing this page.")
                return redirect(settings.DEERAPP_LOGIN_URL)
            else:
                return None
        # Optionally, handle other paths or a default redirect
        return redirect(settings.DEFAULT_LOGIN_URL)