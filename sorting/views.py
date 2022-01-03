from django.views.generic import TemplateView
from django.shortcuts import render

class SortingPageView(TemplateView):

    template_name = 'home/templates/sorting.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request=request, template_name=self.template_name, context=context)


    def get_context_data(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['array'] = [1,2,5,4,3,11,7,19,20]
        return context