from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
posts = [
  {
    "id": 1,
    "title": "How to Set Up Django",
    "content": "This article provides a step-by-step guide to setting up Django on your local machine, covering installation and initial configuration."
  },
  {
    "id": 2,
    "title": "Django Models Overview",
    "content": "This article explains the Django ORM (Object-Relational Mapping) system and how to define models, relationships, and migrations."
  },
  {
    "id": 3,
    "title": "Django Views and Templates",
    "content": "In this guide, we explore how to create views in Django and use templates for rendering dynamic HTML content."
  },
  {
    "id": 4,
    "title": "Django Authentication System",
    "content": "This guide covers the Django authentication system, including user login, registration, and session management."
  },
  {
    "id": 5,
    "title": "Django Deployment Best Practices",
    "content": "A comprehensive guide to deploying Django applications, covering various strategies, server configurations, and security tips."
  }
]


def home(request):
    html = ""
    for post in posts:
        html += f'''
                <div>
                <a href="/post/{post['id']}/">
                    <h1>{post['id']}:{post['title']}</h1></a>
                    <p>{post['content']}</p>
                </div>
'''
    #return HttpResponse(html)
    return render(request,'home.html')


def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        html =f'''
            <h1>{post_dict['title']}</h1>
            <p>{post_dict['content']}</p>
    '''
        
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("Post Not Available....!")


def direct(request,id):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)