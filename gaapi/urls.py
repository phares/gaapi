from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'Ga API'
admin.site.index_title = 'ga kenya'
admin.site.site_title = 'API Admin'

urlpatterns = [

    path('v1/assist/', include('assistamerica.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('allow_me/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('express/', admin.site.urls),
]

