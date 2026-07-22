from .services.railway_api import get_live_status, get_train_details
from django.shortcuts import render, redirect
from .models import FavoriteTrain
from .models import SearchHistory
from django.shortcuts import render
from django.http import JsonResponse
from .train_data import data
def home(request):

    search = request.GET.get("train", "").strip().lower()

    if search:

        train_number = None

        # Search in local dataset
        for train in data["features"]:

            train_data = train["properties"]

            if search == train_data["name"].lower() or search == train_data["number"]:
                train_number = train_data["number"]
                break

        # If user enters train number directly
        if search.isdigit():
            train_number = search

        if train_number:

            response = get_live_status(train_number)
            details_response = get_train_details(train_number)

            if response.status_code == 200 and details_response.status_code == 200:

                live = response.json()["data"]
                details = details_response.json()["data"]

                train = details["train"]

                # Convert duration from minutes to Hours & Minutes
                hours = train["duration"] // 60
                minutes = train["duration"] % 60

                journey_duration = f"{hours} hr {minutes} min"

                # Save Search History
                SearchHistory.objects.create(
                    train_number=train_number,
                    train_name=live.get("trainName", train["name"])
                )

                return render(request, "train_details.html", {
                    "live": live,
                    "details": details,
                    "train": train,
                    "journey_duration": journey_duration
                })

    return render(request, "index.html")
def search_train(request):

    query = request.GET.get("q", "").strip().lower()

    results = []

    if query:

        for train in data["features"]:

            train_data = train["properties"]

            name = train_data["name"].lower()

            if name.startswith(query):

                results.append({
                    "name": train_data["name"],
                    "number": train_data["number"]
                })

            if len(results) >= 10:
                break

    return JsonResponse(results, safe=False)
def add_favorite(request):

    train_number = request.GET.get("number")
    train_name = request.GET.get("name")

    FavoriteTrain.objects.create(
        train_number=train_number,
        train_name=train_name
    )

    return JsonResponse({
        "message": "Added to Favorites"
    })
def test_api(request):

    response = get_live_status("22436")

    if response.status_code == 200:

        live = response.json()["data"]

        return render(request, "live.html", {
            "live": live
        })

    return JsonResponse(response.json())
def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
def live_tracking(request):
    return render(request, "live_tracking.html")


def favorites(request):
    favorites = FavoriteTrain.objects.all()

    return render(request, "favorites.html", {
        "favorites": favorites
    })


def history(request):
    history = SearchHistory.objects.all()

    return render(request, "history.html", {
        "history": history
    })


def fast_search(request):
    return render(request, "fast_search.html")
from django.shortcuts import get_object_or_404

def remove_favorite(request, id):

    train = get_object_or_404(FavoriteTrain, id=id)

    train.delete()

    return redirect("favorites")
from django.shortcuts import get_object_or_404

def delete_history(request, id):

    history = get_object_or_404(SearchHistory, id=id)

    history.delete()

    return redirect("history")
def clear_history(request):

    SearchHistory.objects.all().delete()

    return redirect("history")
