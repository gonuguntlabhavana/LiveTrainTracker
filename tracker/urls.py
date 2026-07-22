from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("search/", views.search_train, name="search_train"),

    path("favorite/", views.add_favorite, name="add_favorite"),

    path("test-api/", views.test_api, name="test_api"),

    path("about/", views.about, name="about"),

    path("contact/", views.contact, name="contact"),

    # New Pages
    path("live-tracking/", views.live_tracking, name="live_tracking"),

    path("favorites/", views.favorites, name="favorites"),

    path("history/", views.history, name="history"),

    path("fast-search/", views.fast_search, name="fast_search"),
    path("remove-favorite/<int:id>/", views.remove_favorite, name="remove_favorite"),
    path("delete-history/<int:id>/", views.delete_history, name="delete_history"),
    path("clear-history/", views.clear_history, name="clear_history"),
    
]