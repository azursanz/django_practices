from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


monthly_challenges = {
    "january": "Practice sport at leat 20 min",
    "february": "Dont smoke 1 box cigarettes per day",
    "march": "Practice Djang 20 min at leat per day",
    "april": "Practice git at least 20 min per day",
    "may": "Go walk at least 20 min per day,rememmber is you HB",
    "june": "Try to reach the divine medal in Dota 2",
    "july": "Try yo improve in your project",
    "september": "Go out with your girlfriend to new places",
    "october": "Go and drink some beers at weeked",
    "november": "Buy some things to your family what end of year partys are near",
    "december": "Spend quality time with your family"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("This is an invalid number of month, dudeeee")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month]) # /challenge/january
    # The function reverse give the origin of the url and add the next path
    return HttpResponseRedirect(redirect_path)


def month_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not a valid")
