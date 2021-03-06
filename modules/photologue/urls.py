from django.conf.urls import url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from .views import PhotoListView, PhotoDetailView, GalleryListView, \
    GalleryDetailView, PhotoArchiveIndexView, PhotoDateDetailView, PhotoDayArchiveView, \
    PhotoYearArchiveView, PhotoMonthArchiveView, GalleryArchiveIndexView, GalleryYearArchiveView, \
    GalleryDateDetailView, GalleryDayArchiveView, GalleryMonthArchiveView, GalleryDateDetailOldView, \
    GalleryDayArchiveOldView, GalleryMonthArchiveOldView, PhotoDateDetailOldView, \
    PhotoDayArchiveOldView, PhotoMonthArchiveOldView

"""NOTE: the url names are changing. In the long term, I want to remove the 'pl-'
prefix on all urls, and instead rely on an application namespace 'photologue'.

At the same time, I want to change some URL patterns, e.g. for pagination. Changing the urls
twice within a few releases, could be confusing, so instead I am updating URLs bit by bit.

The new style will coexist with the existing 'pl-' prefix for a couple of releases.

"""


urlpatterns = [
    url(r'^gallery/(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\w{1,2})/(?P<slug>[\-\d\w]+)/$',
        GalleryDateDetailView.as_view(month_format='%m'),
        name='gallery-detail'),
    url(r'^gallery/(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\w{1,2})/$',
        GalleryDayArchiveView.as_view(month_format='%m'),
        name='gallery-archive-day'),
    url(r'^gallery/(?P<year>\d{4})/(?P<month>[0-9]{2})/$',
        GalleryMonthArchiveView.as_view(month_format='%m'),
        name='gallery-archive-month'),
    url(r'^gallery/(?P<year>\d{4})/$',
        GalleryYearArchiveView.as_view(),
        name='pl-gallery-archive-year'),
    url(r'^gallery/$',
        GalleryArchiveIndexView.as_view(),
        name='pl-gallery-archive'),
    url(r'^$',
        RedirectView.as_view(
            url=reverse_lazy('blog:photologue:pl-gallery-archive'), permanent=True),
        name='pl-photologue-root'),

    url(r'^gallery/detail/(?P<slug>[\-\d\w]+)/$',
        GalleryDetailView.as_view(), name='pl-gallery'),

    url(r'^gallerylist/$',
        GalleryListView.as_view(),
        name='gallery-list'),

    url(r'^photo/(?P<slug>[\-\d\w]+)/$',
        PhotoDetailView.as_view(),
        name='pl-photo'),
]
