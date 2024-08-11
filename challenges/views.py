from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


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

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        campitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{
            campitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    reponse_data = f"<ul>{list_items}</ul>"

    return HttpResponse(reponse_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This is an invalid number of month, dudeeee")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    # The function reverse give the origin of the url and add the next path
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            "text":challenge_text, #Considerar usar "" comillas dobles para que funcione dentro de render
            "month_name":month.capitalize()
            }) # (argument. En este caso usamos el template path)
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not a valid</h1>")
