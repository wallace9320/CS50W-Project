from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("attempt/<int:quiz_id>", views.attempt, name="attempt"),
    path("result/<int:quiz_id>", views.result, name="result"),
    path("otherresult/<int:quiz_id>", views.otherresult, name="otherresult"),

    # API
    path("display/<str:type>", views.display, name="display"),
    path("search/<str:type>/<str:keyword>", views.search, name="search")
]
