from django.conf.urls import url, include
from django.contrib import admin
from summerTests.views import login_redirect


urlpatterns = [
    url(r'^$', login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),  # We don't want to make this messy. Therefore we create a whole new
                                                   # urls.py file for our apps and include it over here.
                                                   # whenever there is a call starting with a particular app name,
                                                   # it is directed from here to it's own urls.py file
]
