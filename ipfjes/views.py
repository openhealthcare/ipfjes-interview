from django.views.generic import TemplateView

from ipfjes.models import SocCode

class SocCodeDetailView(TemplateView):
    template_name = 'soc_code_detail.html'

    def get_context_data(self, *a, **k):
        soc_code = SocCode.objects.filter(soc2000=k['code']).first()
        ctx = super(SocCodeDetailView, self).get_context_data(*a, **k)
        ctx['soc'] = soc_code
        return ctx
