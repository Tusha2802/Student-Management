from django.urls import path
from .import views

urlpatterns=[
path("login/profile/",views.profile),
path("login/",views.login),
path("admin_index/",views.admin_index),
path("user_admin/",views.user_index),
#path("login/profile/pcm/",views.pcm),
#path("login/profile/pcb/",views.pcb),
#path("login/profile/commerce/",views.commerce),
#path("login/profile/humanities/",views.humanities),
path("login/allUsers/",views.allUsers),
path("login/allUsers/remove/<int:stdid>",views.remove,name="rem"),
path("login/allUsers/update/<int:stdid>",views.update,name="upd"),
path("login/remove_all/",views.remove_all),
path("login/course_start/",views.course_start),
path("login/profile/abc/",views.abc),
path("login/profile/abc/pcm/",views.pcm),
path("login/profile/abc/pcb/",views.pcb),
path("login/profile/abc/commerce/",views.commerce),
path("login/profile/abc/humanities/",views.humanities),
path("",views.homepagemenu),
path("about_us/",views.about_us),
path("contact_us/",views.contact_us),



]
