from django.contrib import admin
from django.urls import path
from products.views import product_list
from django.conf import settings
from django.conf.urls.static import static
from courses.views import course_list
from users.views import signup_view, login_view, logout_view
from products.views import buy_product
from courses.views import buy_course
from locations.views import location_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list),
    path('courses/', course_list),
    path('signup/', signup_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('buy/product/<int:product_id>/', buy_product, name='buy_product'),
    path('buy/course/<int:course_id>/', buy_course, name='buy_course'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout/', logout_view),
    path('locations/', location_list, name='locations'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

