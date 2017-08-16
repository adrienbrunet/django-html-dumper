from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'example_app/home.html'
