from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from . import views
from .views import review_helper, ReviewCreateView, ModerateView, VIPView, review_list_helper, my_view, review_detail

app_name = 'helpy'  # добавьте это, если используете пространства имен


urlpatterns = [

    path( '', views.index, name='index' ),
    path( 'admin/', admin.site.urls ),
    path('help/', views.search_helpers, name='help'),
    path('helpmy/', views.HelpMyView.as_view(), name='helpmy'),
    path( 'set_language/', RedirectView.as_view( url='/' ), name='set_language' ),
    path( 'helpers/', views.HelperListView.as_view(), name='helper_list' ),
    path( 'helpers/add/', views.helper_form, name='add_helper' ),
    path( 'helpers/<int:pk>/update/', views.HelperUpdateView.as_view(), name='update_helper_info' ),
    path( 'helpers/<int:pk>/delete/', views.HelperDeleteView.as_view(), name='delete_helper' ),
    path( 'about/', views.about, name='about' ),
    path( 'donate/', views.donate_view, name='donate' ),
    path( 'moderate/', staff_member_required( ModerateView.as_view() ), name='moderate' ),
    path( 'vip/', VIPView.as_view(), name='vip' ),
    path('success/', views.success, name='success'),
    path('menu/', my_view, name='my_menu'),
]
if settings.DEBUG:
    urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
