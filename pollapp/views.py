from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll
from django.contrib.auth.decorators import login_required
from .forms import PollForm, ChoiceForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


import random

def home(request):
    polls = Poll.objects.all()[:2]
    return render(request, 'pollapp/home.html', {'polls': polls})

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(f"User profile created for {instance.username}")
        profile = UserProfile.objects.create(user=instance)
        profile.assign_random_avatar()
        profile.save()

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            # 重定向回注册页面
            return redirect(reverse('register'))
    else:
        form = RegisterForm()
    return render(request, 'pollapp/register.html', {'form': form})


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return HttpResponseRedirect(reverse('login')) 

    return render(request, 'pollapp/login.html', {'form': form})


def random_poll(request):
    polls = Poll.objects.all()
    if polls.exists():
        random_poll = random.choice(polls)
        return redirect('polls_detail', poll_id=random_poll.id)
    else:
        return redirect('polls_list')


@login_required
def create_poll(request):
    if request.method == 'POST':
        poll_form = PollForm(request.POST)

        choice_texts = [value for key, value in request.POST.items() if 'choice_text' in key]
        choice_forms = [ChoiceForm({'choice_text': text}) for text in choice_texts]

        if poll_form.is_valid() and all(cf.is_valid() for cf in choice_forms):
            poll = poll_form.save(commit=False)
            poll.created_by = request.user
            poll.save()
            
            for cf in choice_forms:
                choice = cf.save(commit=False)
                choice.poll = poll
                choice.save()
            
            return redirect('polls_list')
    else:
        poll_form = PollForm()
        choice_forms = [ChoiceForm(prefix=str(i)) for i in range(3)]
        
        for i, choice_form in enumerate(choice_forms, start=1):
            choice_form.fields['choice_text'].widget.attrs.update({'placeholder': f"Option {i}", 'class': 'choice-input'})

    return render(request, 'pollapp/create_poll.html', {
        'poll_form': poll_form,
        'choice_forms': choice_forms,
    })

@login_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == 'POST':
        poll.delete()
        return redirect('polls_list')
    messages.success(request, "Poll deleted successfully!")
    return redirect('polls_list')

def polls_list(request):
    query = request.GET.get('q')
    polls = Poll.objects.all().order_by('-created_at')

    if query:
        polls = polls.filter(Q(title__icontains=query))

    paginator = Paginator(polls, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'pollapp/polls_list.html', {'page_obj': page_obj, 'query': query})

def polls_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        choice = poll.choices.get(pk=choice_id)
        choice.votes += 1
        choice.save()
        return redirect('poll_results', poll_id=poll.id)
    return render(request, 'pollapp/polls_detail.html', {'poll': poll})

def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    share_link = request.build_absolute_uri(f'/{poll_id}/')
    choices = poll.choices.all()
    choice_data = [{'text': choice.choice_text, 'votes': choice.votes} for choice in choices]
    
    return render(request, 'pollapp/poll_results.html', {
        'poll': poll,
        'choice_data': choice_data,
        'share_link': share_link,
    })

