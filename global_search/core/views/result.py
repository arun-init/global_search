from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def result_page(request):
    """
    Renders the result page for authenticated users.
    """
    return render(request, "result.html")
