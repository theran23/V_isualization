from django.views.generic import TemplateView
from django.shortcuts import render
import random

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
        context['array'] = [10,22,50,41,36,11,17,19,20,100,99,12,14,15,19,29,35]

        # a = []
        # n = int(input('array의 크기 : '))
        # for i in range(n):
        #     num = random.randint(1, 99)
        #     a.append(num)
        # print(a)

        return context
