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

    path( '', views.index, name='index' ),
    path( 'admin/', admin.site.urls ),
    path('help/', views.search_helpers, name='help'),
    path('helpmy/', views.HelpMyView.as_view(), name='helpmy'),
    path( 'set_language/', RedirectView.as_view( url='/' ), name='set_language' ),
    path( 'articles/', views.ArticleListView.as_view(), name='articles' ),
    path( 'articles/add/', views.add_article, name='add_article' ),
    path( 'articles/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='update_article' ),
    path( 'events/', views.events, name='events' ),
    path( 'events/add/', views.EventCreateView.as_view(), name='add_event' ),
    path( 'events/<int:pk>/update/', views.EventUpdateView.as_view(), name='update_event' ),
    path( 'events/<int:pk>/delete/', views.EventDeleteView.as_view(), name='delete_event' ),
    path( 'helpers/', views.HelperListView.as_view(), name='helper_list' ),
    path( 'helpers/add/', views.helper_form, name='add_helper' ),
    path( 'helpers/<int:pk>/update/', views.HelperUpdateView.as_view(), name='update_helper_info' ),
    path( 'helpers/<int:pk>/delete/', views.HelperDeleteView.as_view(), name='delete_helper' ),
    path( 'add-review/', views.add_review, name='add_review' ),
    path( 'about/', views.about, name='about' ),
    path( 'donate/', views.donate_view, name='donate' ),
    path( 'account_inactive/', views.account_inactive, name='account_inactive' ),
    path( 'email/', views.email, name='email' ),
    path( 'email_confirm/', views.email_confirm, name='email_confirm' ),
    path( 'login/', views.login, name='account_login' ),
    path( 'logout/', views.logout, name='account_logout' ),
    path( 'password_change/', views.password_change, name='password_change' ),
    path( 'password_reset/', views.password_reset, name='password_reset' ),
    path( 'password_reset_done/', views.password_reset_done, name='password_reset_done' ),
    path( 'password_reset_from_key/', views.password_reset_from_key, name='password_reset_from_key' ),
    path( 'password_reset_from_key_done/', views.password_reset_from_key_done, name='password_reset_from_key_done' ),
    path( 'password_set/', views.password_set, name='password_set' ),
    path( 'sign_in/', views.sign_in, name='account_sign_in' ),
    path( 'signup/', views.signup, name='account_signup' ),
    path( 'signup_closed/', views.signup_closed, name='signup_closed' ),
    path( 'verification_sent/', views.verification_sent, name='verification_sent' ),
    path( 'verified_email_required/', views.verified_email_required, name='verified_email_required' ),
    path( 'review_helper/', review_helper, name='review_helper' ),
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
