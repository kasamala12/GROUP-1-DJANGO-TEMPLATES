"""
Views for the University News Portal.

Every view below follows the same pattern required by the assignment:
    1. Gather / prepare some data (from news/data.py).
    2. Package it into a "context" dictionary.
    3. Call render(request, template_name, context) to render a
       Django template with that data.

This is the core mechanism of "passing data from views to templates".
"""

from django.http import Http404
from django.shortcuts import render

from .data import get_all_news, get_latest_news, get_news_by_id


def home(request):
    """Home page: shows a welcome banner and the latest 3 news items."""
    context = {
        'page_title': 'Welcome to Ardhi University News',
        'latest_news': get_latest_news(3),
    }
    return render(request, 'news/home.html', context)


def about(request):
    """About page: static info about the (fictional) university."""
    context = {
        'page_title': 'About Ardhi University',
        'founded_year': 2007,
        'motto': 'professionalism and prosperity',
    }
    return render(request, 'news/about.html', context)


def contact(request):
    """Contact page: static contact details for the university."""
    context = {
        'page_title': 'Contact Us',
        'email': 'link@aru.ac.tz',
        'phone': '+255 738357',
        'address': 'PO Box 35176, Observation Hill, Plot No.3, Block L'
    }
    return render(request, 'news/contact.html', context)


def news_list(request):
    """News listing page: shows every article as a list."""
    context = {
        'page_title': 'All News',
        'news_items': get_all_news(),
    }
    return render(request, 'news/news_list.html', context)


def news_detail(request, news_id):
    """News details page: shows a single article by its id."""
    article = get_news_by_id(news_id)
    if article is None:
        raise Http404('News article not found')

    context = {
        'page_title': article['title'],
        'article': article,
    }
    return render(request, 'news/news_detail.html', context)
