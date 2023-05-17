from django.http import Http404
from django.shortcuts import render

from django.shortcuts import render
from polls.models import Poll, AnwserOption


def polls_list_view(request):
    polls = Poll.objects.all()
    return render(request, "polls/list.html", {"polls": polls})


def polls_details_view(request, poll_id=None):
    try:
        poll = Poll.objects.filter(id=poll_id).values()[0]
    except IndexError:
        raise Http404

    options = AnwserOption.objects.filter(poll_id=poll_id).all()

    context = {**poll, "options": options, "voted": False}

    print(request.POST)
    if request.method == "POST":
        option_id = request.POST.get("vote")
        option = AnwserOption.objects.get(id=option_id)
        option.votes += 1
        option.save()
        context["voted"] = True

    return render(request, "polls/details.html", {"poll": context})
