"""
ipfjes - Our Opal Application
"""
from opal.core import application, menus

class Application(application.OpalApplication):

    javascripts   = [
        'js/ipfjes/routes.js',
        'js/ipfjes/occupational_history.js',
        'js/ipfjes/asbestos_exposure_history.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/ipfjes/flow.js',
    ]
    default_episode_category = "ipfjes"
    styles = [
        'css/ipfjes.css'
    ]

    @classmethod
    def get_menu_items(klass, user=None):
        items = [
            menus.MenuItem(
                href="/pathway/#/new", activepattern="/pathway/#/new",
                icon="fa-plus", display="Add participant",
                index=0
            ),
            menus.MenuItem(
                href="/#/list/interviews/", activepattern="/#/list/interviews",
                icon="fa-phone", display="Interview list",
                index=2
            )

        ]
        if user.is_staff:
            items.append(
                menus.MenuItem(
                    href="/admin/", icon="fa-cogs", display="Admin",
                    index=999
                )
            )
        return items
