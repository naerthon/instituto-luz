from django.conf.urls          import include, url
from django.contrib.auth.views import login,logout
from .views                    import register

urlpatterns = [
    url(r'^login', login, {'template_name':'accounts/login.html'},name='login'),
    url(r'^logout/$', logout, {'next_page': 'core:index'}, name='logout'),
    url(r'^instrutor/add/$', register, name='register'),
]