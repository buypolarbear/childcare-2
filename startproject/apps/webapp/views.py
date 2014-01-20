# Create your views here.
from django.views.generic import TemplateView


class HomePage(TemplateView):

    template_name = "Home.html"

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['student_set'] = []
        if self.request.user.is_authenticated():
            context['student_set'] = self.request.user.student_set.filter(is_active=True)