from django.contrib.auth.decorators import login_required
from utils.util import render_to
from accounts.forms import UserProfileForm
from django.contrib.auth.models import User

@login_required
@render_to('accounts/profile.html')
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save(request.user.username)
            request.user = User.objects.get(username__iexact=request.user.username)
    else:
        data = {'first_name': request.user.first_name, 'last_name': request.user.last_name}
        form = UserProfileForm(data)
    return locals()
