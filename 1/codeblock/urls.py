from django.conf.urls import patterns, include, url
from press.views import HomeView,TagView,CategoryView,ArticleView,ArchiveView
from feeds.feeds import LatestPress
from press.models import Press
from django.views.generic.dates import ArchiveIndexView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

archive_dict = {
                'queryset':Press.objects.all(),
                'date_field':'date_pub',
                }

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codeblock.views.home', name='home'),
    # url(r'^codeblock/', include('codeblock.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^$',HomeView),
    (r'^tag/(\d*)/$',TagView),
    (r'^category/$',CategoryView),
    url(r'^(\d*)/$',ArticleView,name="article"),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'feed/$',LatestPress()),
    url(r'^archive/$',
        ArchiveIndexView.as_view(model=Press, date_field="date_pub"),
        name="article_archive"),
)

            
urlpatterns += staticfiles_urlpatterns()