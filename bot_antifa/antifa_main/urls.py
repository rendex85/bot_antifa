from django.urls import path

from antifa_main.views import UsersListView, BotTurner

urlpatterns = [
path('users/all', UsersListView.as_view()),
path('bot/turner', BotTurner),


]