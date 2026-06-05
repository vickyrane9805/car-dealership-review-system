from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json
from textblob import TextBlob
from .models import Dealer, Review, Car


def home(request):
    return JsonResponse({
        "message": "Car Dealership API Running"
    })


@csrf_exempt
def register_user(request):

    if request.method == "POST":

        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")

        if User.objects.filter(username=username).exists():

            return JsonResponse({
                "status": False,
                "message": "User already exists"
            })

        User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        return JsonResponse({
            "status": True,
            "message": "Registration successful"
        })

    return JsonResponse({
        "message": "POST request required"
    })


@csrf_exempt
def login_user(request):

    if request.method == "POST":

        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return JsonResponse({
                "status": True,
                "username": username
            })

        return JsonResponse({
            "status": False,
            "message": "Invalid credentials"
        })

    return JsonResponse({
        "message": "POST request required"
    })


def logout_user(request):

    logout(request)

    return JsonResponse({
        "status": True,
        "message": "Logged out successfully"
    })

def test_api(request):
    return JsonResponse({
        "status": True,
        "message": "API working successfully"
    })

def get_dealers(request):

    dealers = Dealer.objects.all()

    data = []

    for dealer in dealers:

        data.append({
            "id": dealer.id,
            "name": dealer.name,
            "city": dealer.city,
            "state": dealer.state,
            "address": dealer.address
        })

    return JsonResponse(data, safe=False)


def get_dealer_by_id(request, dealer_id):

    try:

        dealer = Dealer.objects.get(id=dealer_id)

        return JsonResponse({
            "id": dealer.id,
            "name": dealer.name,
            "city": dealer.city,
            "state": dealer.state,
            "address": dealer.address
        })

    except Dealer.DoesNotExist:

        return JsonResponse({
            "error": "Dealer not found"
        }, status=404)


def get_dealers_by_state(request):

    state = request.GET.get('state')

    dealers = Dealer.objects.filter(state__iexact=state)

    data = []

    for dealer in dealers:

        data.append({
            "id": dealer.id,
            "name": dealer.name,
            "city": dealer.city,
            "state": dealer.state,
            "address": dealer.address
        })

    return JsonResponse(data, safe=False)

def get_dealer_reviews(request, dealer_id):

    reviews = Review.objects.filter(
        dealer_id=dealer_id
    )

    data = []

    for review in reviews:

        data.append({
            "reviewer_name": review.reviewer_name,
            "review_text": review.review_text,
            "purchase_date": str(review.purchase_date)
        })

    return JsonResponse(data, safe=False)

def get_all_cars(request):

    cars = Car.objects.all()

    data = []

    for car in cars:

        data.append({
            "id": car.id,
            "make": car.make,
            "model": car.model,
            "year": car.year
        })

    return JsonResponse(data, safe=False)

def analyze_review(request, review_text):

    analysis = TextBlob(review_text)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"

    elif polarity < 0:
        sentiment = "negative"

    else:
        sentiment = "neutral"

    return JsonResponse({
        "review": review_text,
        "sentiment": sentiment
    })