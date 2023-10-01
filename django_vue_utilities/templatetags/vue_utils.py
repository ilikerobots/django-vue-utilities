import os
from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.html import mark_safe
import urllib.parse

register = template.Library()

SETTING_DEFAULT_USE_TYPESCRIPT = False
SETTING_DEFAULT_USE_DEV_SERVER = settings.DEBUG
SETTING_DEFAULT_DEV_SERVER_URL = 'http://localhost:5173'
SETTING_DEFAULT_DEV_SERVER_PATH = 'src'
SETTING_DEFAULT_STATIC_DIR = 'vue'


@register.simple_tag()
def vue_bundle_url(bundle: str) -> str:
    """
    Return the url to a vue bundle. 'bundle' should match the input name as defined in vite.config.js.
    """
    use_ts = getattr(settings, 'VUE_FRONTEND_USE_TYPESCRIPT', SETTING_DEFAULT_USE_TYPESCRIPT)
    use_dev_server = getattr(settings, 'VUE_FRONTEND_USE_DEV_SERVER', SETTING_DEFAULT_USE_DEV_SERVER)
    dev_server_url = getattr(settings, 'VUE_FRONTEND_DEV_SERVER_URL', SETTING_DEFAULT_DEV_SERVER_URL)
    dev_server_path = getattr(settings, 'VUE_FRONTEND_DEV_SERVER_PATH', SETTING_DEFAULT_DEV_SERVER_PATH)
    static_dir = getattr(settings, 'VUE_FRONTEND_STATIC_PATH', SETTING_DEFAULT_STATIC_DIR)

    extension = '.ts' if use_ts and use_dev_server else '.js'
    if use_dev_server:
        return urllib.parse.urljoin(dev_server_url, os.path.join(dev_server_path,  bundle + extension))
    else:
        return static(os.path.join(static_dir, bundle + extension))


@register.simple_tag()
def vue_provide(key: str, value: any, quote=True) -> str:
    quote = '"' if quote else ''
    quoted_val = f'{quote}{value}{quote}'
    """
    Specify a key value pair which will be 'provided' to the Vue application. It can later be injected in most places,
    such as components or Pinia stores, with `inject('key_name')`
    """
    return mark_safe(
        f'<script>window.vueProvided = window.vueProvided || {{}}; vueProvided["{key}"] = {quoted_val};</script>'
    )
