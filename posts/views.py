from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Video, Vote
from .forms import VideoForm, ContactForm


def index(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return render(request, 'posts/video_added.html')

    else:
        form = VideoForm()

    posts = Video.objects.all()
    trends = posts.order_by('-upvotes')[:3]
    news = posts.order_by('-date')[:6]

    return render(request, 'posts/index.html', {'trends': trends, 'news': news, 'form': form})


def post_details(request, pk):
    post = get_object_or_404(Video, pk=pk)
    return render(request, 'posts/video_post.html', {'post': post})


@login_required
def post_details_upvote(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Video, pk=pk)
        try:
            vote = Vote.objects.get(user=request.user, video=post)
            if vote.value == -1:
                post.upvotes += 1
                post.downvotes -= 1
                vote.value = 1
                vote.save()
                post.save()

        except Vote.DoesNotExist:
            Vote.objects.create(user=request.user, video=post, value=1)
            post.upvotes += 1
            post.save()

        finally:
            return redirect('post_details', pk=pk)

    else:
        raise Http404


@login_required
def post_details_downvote(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Video, pk=pk)
        try:
            vote = Vote.objects.get(user=request.user, video=post)
            if vote.value == 1:
                post.upvotes -= 1
                post.downvotes += 1
                vote.value = -1
                vote.save()
                post.save()

        except Vote.DoesNotExist:
            Vote.objects.create(user=request.user, video=post, value=-1)
            post.downvotes += 1
            post.save()

        finally:
            return redirect('post_details', pk=pk)
    else:
        raise Http404


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'posts/message_sent.html')

    else:
        form = ContactForm()

    return render(request, 'posts/contact.html', {'form': form})
