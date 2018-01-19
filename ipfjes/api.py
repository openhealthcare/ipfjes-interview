from opal.core import api as opal_api
from ipfjes.models import SocCode
from rest_framework import filters
from ipfjes.serializers import SocCodeSerializer
from rest_framework import viewsets


class SocCodeListView(viewsets.ModelViewSet):
    queryset = SocCode.objects.all().order_by("soc2000").order_by("soc90").order_by("title")
    serializer_class = SocCodeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^title',)


router = opal_api.OPALRouter()
router.register("soc_code_list", SocCodeListView)
