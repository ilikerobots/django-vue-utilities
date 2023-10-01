from __future__ import unicode_literals

from django.template import Context, Template
from django.test import TestCase, override_settings


class LoadBundleTestCase(TestCase):
    def test_load_bundle_static(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'vue/foo.js')

    @override_settings(VUE_FRONTEND_STATIC_PATH='bar')
    def test_load_bundle_static_custom_path_1(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'bar/foo.js')

    @override_settings(VUE_FRONTEND_STATIC_PATH='bar/')
    def test_load_bundle_static_custom_path_2(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'bar/foo.js')

    @override_settings(VUE_FRONTEND_STATIC_PATH='biz/baz/')
    def test_load_bundle_static_custom_path_3(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'biz/baz/foo.js')

    @override_settings(VUE_FRONTEND_USE_DEV_SERVER=True)
    def test_load_bundle_devserver(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'http://localhost:5173/src/foo.js')

    @override_settings(VUE_FRONTEND_USE_DEV_SERVER=True)
    @override_settings(VUE_FRONTEND_DEV_SERVER_PATH='bar')
    def test_load_bundle_devserver_custom_path_1(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'http://localhost:5173/bar/foo.js')

    @override_settings(VUE_FRONTEND_USE_DEV_SERVER=True)
    @override_settings(VUE_FRONTEND_DEV_SERVER_PATH='bar/')
    def test_load_bundle_devserver_custom_path_2(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'http://localhost:5173/bar/foo.js')

    @override_settings(VUE_FRONTEND_USE_DEV_SERVER=True)
    @override_settings(VUE_FRONTEND_DEV_SERVER_PATH='biz/bar/')
    def test_load_bundle_devserver_custom_path_2(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'http://localhost:5173/biz/bar/foo.js')

    @override_settings(VUE_FRONTEND_USE_DEV_SERVER=True)
    @override_settings(VUE_FRONTEND_DEV_SERVER_URL='http://127.0.0.1:5333')
    @override_settings(VUE_FRONTEND_DEV_SERVER_PATH='biz/bar/')
    def test_load_bundle_devserver_custom_path_2(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'http://127.0.0.1:5333/biz/bar/foo.js')

    @override_settings(VUE_FRONTEND_USE_TYPESCRIPT=True)
    def test_load_bundle_devserver_custom_path_2(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'http://localhost:5173/src/foo.js')

    @override_settings(VUE_FRONTEND_USE_DEV_SERVER=True)
    @override_settings(VUE_FRONTEND_USE_TYPESCRIPT=True)
    def test_load_bundle_devserver_custom_path_2(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_bundle_url 'foo' %}"
        ).render(Context())
        self.assertEqual(out, 'http://localhost:5173/src/foo.ts')


class VueProvideTestCase(TestCase):
    def test_load_bundle_static_foo(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_provide 'foo' 'bar' %}"
        ).render(Context())
        self.assertEqual(out,
                         '<script>window.vueProvided = window.vueProvided || {}; vueProvided["foo"] = "bar";</script>')

    def test_load_bundle_static_32(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_provide 'foo' 32 %}"
        ).render(Context())
        self.assertEqual(out,
                         '<script>window.vueProvided = window.vueProvided || {}; vueProvided["foo"] = "32";</script>')

    def test_load_bundle_static_32_unquoted(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_provide 'foo' 32 False %}"
        ).render(Context())
        self.assertEqual(out,
                         '<script>window.vueProvided = window.vueProvided || {}; vueProvided["foo"] = 32;</script>')

    def test_load_bundle_static_str_unquoted(self):
        out = Template(
            "{% load vue_utils %}"
            "{% vue_provide 'foo' 'window.CSRF_TOKEN' False %}"
        ).render(Context())
        self.assertEqual(out,
                         '<script>window.vueProvided = window.vueProvided || {}; vueProvided["foo"] = window.CSRF_TOKEN;</script>')
