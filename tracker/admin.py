from django.contrib import admin
from .models import FavoriteTrain, SearchHistory

admin.site.register(FavoriteTrain)
admin.site.register(SearchHistory)