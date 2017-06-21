from django.shortcuts import render

def difference(request):
    results = []
    return render(request, 'landing/result.html', {
        'results':results
    })