from django.shortcuts import render
from django.views import View


class Lessons(View):

    def get(self, request):
        return render(request, 'lessons/lessons.html')

