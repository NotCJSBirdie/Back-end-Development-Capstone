from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    path("songs/", views.songs, name="songs"),     # Fixed earlier
    path("photos/", views.photos, name="photos"),  # Fixed earlier
    path("login/", views.login_view, name="login"),   # Fixed earlier
    path("logout/", views.logout_view, name="logout"), # Fixed earlier
    path("signup/", views.signup, name="signup"),  # Fixed earlier
    path("concert/", views.concerts, name="concerts"),  # FIXED: now /concert/
    path("concert-detail/<int:id>", views.concert_detail, name="concert_detail"),
    path("concert_attendee/", views.concert_attendee, name="concert_attendee"),
]
