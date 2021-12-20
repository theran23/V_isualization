from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):

    template_name = 'home/templates/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request=request, template_name=self.template_name, context=context)


    def get_context_data(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context