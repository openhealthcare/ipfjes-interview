"""
ipfjes - Our Opal Application
"""
from opal.core import application

class Application(application.OpalApplication):
    javascripts   = [
        'js/ipfjes/routes.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/ipfjes/flow.js',
    ]
    default_episode_category = "ipfjes"
