from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def month_challenge(request, month):
    month_text = None
    months = ["january", "february", "march", "april", "may", "june", "september", "october", "november",
              "december"
              ]
    challenge_text = ["Practice sport at leat 20 min",
               "Dont smoke 1 box cigarettes per day",
               "Practica Djang 20 min at leat per day"]

    if month in months:
        month_text = month
        return challenge_text[months.index(month_text)]

    return HttpResponse(month_text)
