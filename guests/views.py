from django.shortcuts import render
from guests.models import GuestPost
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

# Create your views here.
def index(req):
      
    post_latest = GuestPost.objects.order_by("-createDate")[:6]
    context = {
        "post_latest": post_latest
    }


    return render(req, "guests.html",  context=context)