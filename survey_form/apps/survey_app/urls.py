from django.conf.urls import url
from . import views

        # This line is new!
urlpatterns = [
  url(r'^$', views.index),
  url(r'^survey/process$', views.process_form),
  url(r'^results$', views.display_results),     # This line has changed!
]