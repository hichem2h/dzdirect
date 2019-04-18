from django.shortcuts import render
from .forms import ChangeProfile


def profile(request):
    if request.method == 'POST':
        form = ChangeProfile(request.POST)
        if form.is_valid():
            form.save(request.user)
            return render(request, 'account/profile.html')

    else:
        form = ChangeProfile()

    return render(request, 'account/profile.html', {'form': form})
