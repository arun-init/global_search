from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard_page(request):
    """
    Renders the dashboard page for authenticated users.
    """
    return render(request, "dashboard.html")
