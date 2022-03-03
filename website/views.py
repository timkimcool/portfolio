from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'home.html'

class OriginalView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'baseO.html', {})