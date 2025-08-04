from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('admin_panel', admin_panel),
    path('admin_panel/post/<int:pid>', ap_post_detail),
    path('admin_panel/post/<int:pid>/edit', ap_post_edit),
    path('admin_panel/post/<int:pid>/delete', ap_post_delete),
    path('admin_panel/post/add', add_post),
    path('load_file/<int:pid>', load_file),
    path('login', login_view),
    path('logout', logout_view),
    path('about', about)
]
