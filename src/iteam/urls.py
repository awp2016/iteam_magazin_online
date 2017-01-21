from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from iteam import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^gender/(?P<gender>.+)/$', views.index, name="index"),
	url(r'^product/(?P<pk>\d+)/$', views.product_details, name='product_details'),
	url(r'^shopping-cart/(?P<pk>\d+)/$', views.shopping_cart, name='shopping_cart'),
	url(r'^place-order/(?P<pk>\d+)/$', views.place_order, name='place_order'),
	url(r'^remove-one-item/(?P<pk>\d+)/$', views.remove_item, name='remove_item'),
	url(r'^add-item/(?P<pk_cart>\d+)/(?P<pk_produs>\d+)/$', views.add_item, name='add_item'),
    url(r'^edit_info/(?P<pk>\d+)/', views.EditProfileView.as_view(), name="edit_user"),
	url(r'^shopping-history/(?P<pk>\d+)/$', views.shopping_history, name='shopping_history'),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
