from django.urls import path
from . import views

urlpatterns = [
    path("page/", views.projects_status_index, name="projects_status_index"),
    path("json/", views.projects_status_json,  name="projects_status_json"),
    path("json_cleaned/", views.projects_status_json_cleaned,  name="projects_status_json_cleaned"),
    path("chart/", views.chart,  name="chart"),
	path("chart_admin_title/", views.chart_admin_title,  name="chart_admin_title"),
	path("chart_admin_userreq/", views.chart_admin_userreq,  name="chart_admin_userreq"),
	path("chart_admin_dev/", views.chart_admin_dev,  name="chart_admin_dev"),
	path("chart_admin_sit/", views.chart_admin_sit,  name="chart_admin_sit"),
	path("chart_admin_uat/", views.chart_admin_uat,  name="chart_admin_uat"),
	path("chart_admin_implementation/", views.chart_admin_implementation,  name="chart_admin_implementation"),


]
