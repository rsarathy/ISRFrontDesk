from django.shortcuts import render
from forms import ClerkLog

def make_log(request):
    if request.method == 'POST':
        form = ClerkLog(request.POST)
    else:
        form = ClerkLog()
    return render(request, "clerklog.html",
           {
               "form": form,
           })