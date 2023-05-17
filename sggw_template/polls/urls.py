from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.polls_list_view, name="index"),
    # ex: /polls/5/
    path("<int:poll_id>/", views.polls_details_view, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]
