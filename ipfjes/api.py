from opal.core import api as opal_api
from opal.core.views import json_response
from ipfjes.models import SocCode


RISK_PRONE_CODES = [
    "541", "534", "532", "570", "896", "311", "520", "521", "893",
    "533", "301", "506", "913", "211", "571"
]


class SocCodeRiskViewSet(opal_api.LoginRequiredViewset):
    """
    Provides applications with information about all system users
    """
    base_name = 'soc_code'

    def list(self, request):
        """
        Serialise all opal.models.UserProfile objects
        """
        return json_response(list(
            SocCode.objects.filter(soc90__in=RISK_PRONE_CODES).values(
                "title",
            )
        ))

router = opal_api.OPALRouter()

router.register("soc_code_at_risk", SocCodeRiskViewSet)
