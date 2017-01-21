from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page

from iteam import views
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^gender/(?P<gender>.+)/$', views.index, name="index"),
	url(r'^product/(?P<pk>\d+)/$', views.product_details, name='product_details'),
	url(r'^shopping-cart/(?P<pk>\d+)/$', views.shopping_cart, name='shopping_cart'),
	url(r'^remove-one-item/(?P<pk>\d+)/$', views.remove_item, name='remove_item'),
	url(r'^add-item/(?P<pk_cart>\d+)/(?P<pk_produs>\d+)/$', views.add_item, name='add_item'),
    url(r'^edit_info/(?P<pk>\d+)/', views.EditProfileView.as_view(), name="edit_user"),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

