from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset


urlpatterns = [
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/register/$', registration, name="registration"),
    url(r'^accounts/profile/$', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))

]
