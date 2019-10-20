from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^new/project$',views.new_project,name='new-project'),
    url(r'^project/review/(\d+)',views.project_review,name='project_review'),
    url(r'^search/',views.search_project, name='search_results'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit/profile/$',views.profile_edit,name = 'edit_profile'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),

 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
