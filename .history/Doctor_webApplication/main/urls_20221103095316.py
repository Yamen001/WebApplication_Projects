from django.urls import include, path

from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_member/', views.register, name='addrecord'),
    path('login/', views.login, name = 'login'),
        url(r'^$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^backoffice/$', login_required(TemplateView.as_view(template_name='backoffice/index.html'))),
]
#! mostly done here!