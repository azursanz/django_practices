from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def month_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Practice sport at leat 20 min"
    elif month == "february":
        challenge_text = "Dont smoke 1 box cigarettes per day"
    elif month == "march":
        challenge_text = "Practice Djang 20 min at leat per day"
    else:
        return HttpResponseNotFound("This month is not a valid")
    return HttpResponse(challenge_text)
