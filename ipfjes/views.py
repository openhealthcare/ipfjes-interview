from django.http import HttpResponseNotFound
from django.views.generic import TemplateView

from ipfjes.models import SocCode


class SocCodeDetailView(TemplateView):
    template_name = 'soc_code_detail.html'

    def dispatch(self, *a, **k):
        title = self.request.GET['title']
        if title == 'undefined':
            return HttpResponseNotFound()
        return super(SocCodeDetailView, self).dispatch(*a, **k)

    def get_context_data(self, *a, **k):
        title = self.request.GET['title']
        soc_code = SocCode.objects.filter(title=title).first()
        ctx = super(SocCodeDetailView, self).get_context_data(*a, **k)
        ctx['soc'] = soc_code
        return ctx
