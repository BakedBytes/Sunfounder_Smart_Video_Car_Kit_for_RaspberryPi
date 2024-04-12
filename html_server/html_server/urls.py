"""html_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.urls import include, re_path, path
from django.contrib import admin
from . import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'motor/forward', views.motor_forward),
    path(r'motor/backward', views.motor_backward),
    path(r'motor/stop', views.motor_stop),
    path(r'camera/increase/y', views.camera_increase_y),
    path(r'camera/decrease/y', views.camera_decrease_y),
    path(r'camera/increase/x', views.camera_increase_x),
    path(r'camera/decrease/x', views.camera_decrease_x),
    path(r'camera/home', views.camera_home),
    path(r'motor/set/speed/(\d{1,3})', views.motor_set_speed),
    path(r'turning/(\d{1,3})', views.turning),
    path(r'calibrate/getconfig', views.calibrate_get_config),
    path(r'runmode', views.run_mode),
    path(r'calibrationmode', views.calibration_mode),
    path(r'calibrate/turning/(.)/(\d{1,3})', views.calibrate_turning),
    path(r'calibrate/motor/run', views.calibrate_motor_run),
    path(r'calibrate/motor/stop', views.calibrate_motor_stop),
    path(r'calibrate/motor/left/reverse', views.calibrate_motor_left_reverse),
    path(r'calibrate/motor/right/reverse', views.calibrate_motor_right_reverse),
    path(r'calibrate/confirm', views.calibrate_confirm),
    path(r'calibrate/pan/(.)/(\d{1,3})', views.calibrate_pan),
    path(r'calibrate/tile/(.)/(\d{1,3})', views.calibrate_tile),
    path(r'test/(.)/(\d{0,3})', views.test),
    path(r'client/', views.client),
]
