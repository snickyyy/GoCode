from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.


class Error404(View):
    def get(self, request, exception):
        return render(request, "errors/404.html", status=404)


class Index(TemplateView):
    template_name = "index.html"
