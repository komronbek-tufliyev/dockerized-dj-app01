from .base import *
# import environs
# env = environs.Env()
# env.read_env()


ENV_NAME = env('ENV_NAME', 'local')

if ENV_NAME == 'local':
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True
    }
    from .local import *
elif ENV_NAME == 'production':
    from .production import *
else:
    from .local import *
