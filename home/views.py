from django.views.generic import TemplateView
from django.shortcuts import render

from home.models import *

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
        schedule = Schedule.objects.all()
        mentor = Participant.objects.filter(name='김세란').get()
        mentee = Participant.objects.filter(name='오수정').get()
        context['mentor'] = mentor
        context['mentee'] = mentee
        # context = {
        #     'mentor': mentor,
        #     'mentee': mentee,
        # }
        return context

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

        a = []
        n = random.randint(1,20)
        for i in range(n):
            num = random.randint(1, 99)
            a.append(num)
        print(a)

        context['array'] = a

        return context


class SearchPageView(TemplateView):
    template_name = 'home/templates/search.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request=request, template_name=self.template_name, context=context)

    def get_context_data(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        a = []
        n = random.randint(1, 20)
        for i in range(n):
            num = random.randint(1, 99)
            a.append(num)
        print(a)

        context['array'] = a

        return context





