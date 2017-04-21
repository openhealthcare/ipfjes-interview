from opal.core import api as opal_api
from opal.core.views import json_response
from ipfjes.models import SocCode


class SocCodeViewSet(opal_api.LoginRequiredViewset):
    """
    Provides applications with information about all system users
    """
    base_name = 'soc_code'

    def list(self, request):
        """
        Serialise all opal.models.UserProfile objects
        """
        return json_response(list(
            SocCode.objects.all().values(
                # "soc90",
                # "soc2000",
                "title",
                # "short_desc",
                # "entry",
                # "tasks",
                # "related"
            )
        ))

router = opal_api.OPALRouter()

router.register("soc_code_view_set", SocCodeViewSet)
