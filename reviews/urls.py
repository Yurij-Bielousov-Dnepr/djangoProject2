from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.contrib import admin
# from telegram_bot.views import webhook, telegram_bot
#from telegram_bot.telegram_bot import set_webhook, webhook
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from . import views
from .views import review_helper, ReviewCreateView, ModerateView, VIPView, review_list_helper, my_view, review_detail

app_name = 'helpy'  # добавьте это, если используете пространства имен


urlpatterns = [

    path( 'admin/', admin.site.urls ),
    path( 'review_helper/', review_helper.as_view(), name='review_helper' ),
    path( 'reviews/add/', ReviewCreateView.as_view(), name='reviews_add' ),
    path( 'reviews/', review_list_helper, name='reviews_list' ),
    path('reviews/<int:pk>/', review_detail, name='review_detail'),
    path( 'moderate/', staff_member_required( ModerateView.as_view() ), name='moderate' ),
    path( 'vip/', VIPView.as_view(), name='vip' ),
    path('success/', views.success, name='success'),
    #    path( 'set_webhook/', set_webhook ),
    #    path('webhook/', webhook, name='webhook'),
    #    path('telegram_bot/', telegram_bot, name='telegram_bot'),
    path('menu/', my_view, name='my_menu'),
]
if settings.DEBUG:
    urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
