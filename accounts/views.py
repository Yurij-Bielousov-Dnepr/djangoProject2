from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views import generic
from .forms import AddEmailForm, RemoveEmailForm, EditVisitorProfileForm
from .forms import VisitorForm
from .forms import CustomAuthenticationForm


class LoginView(generic.FormView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')


@login_required
def edit_visitor_profile(request):
    visitor = request.user.visitor
    if request.method == 'POST':
        form = EditVisitorProfileForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditVisitorProfileForm(instance=visitor)
    return render(request, 'accounts/edit_visitor_profile.html', {'form': form})

@login_required
def account_email(request):
    visitor = request.user
    visitor_form = AddEmailForm(request.POST or None)
    remove_form = RemoveEmailForm(request.POST or None)

    if request.method == 'POST':
        if 'action_add' in request.POST and visitor_form.is_valid():
            email = visitor_form.cleaned_data['email']
            visitor.email_user(
                subject=_('Verify your email address'),
                message=_('Please click on the following link to verify your email address: {0}{1}').format(
                    request.build_absolute_uri(reverse_lazy('account_email_verify')),
                    '?email={}'.format(email)
                ),
                from_email='no-reply@example.com'
            )
            messages.success(request, _('Verification email sent to {0}').format(email))
            return redirect(reverse_lazy('account_email'))

        if 'action_remove' in request.POST and remove_form.is_valid():
            email = remove_form.cleaned_data['email']
            if email == visitor.email:
                messages.error(request, _('You cannot remove your primary email address'))
            else:
                visitor.emailaddress_set.filter(email=email).delete()
                messages.success(request, _('Email address {0} removed').format(email))
            return redirect(reverse_lazy('account_email'))

    context = {
        'visitor': visitor,
        'visitor_form': visitor_form,
        'remove_form': remove_form,
    }
    return render(request, 'accounts/email.html', context)


def signup_closed(request):
    return None


def verification_sent(request):
    return None


def verified_email_required(request):
    return None


def sign_in(request):
    return None


def signup(request):
    return None


def password_set(request):
    return None


def password_reset_from_key_done(request):
    return None


def password_reset_from_key(request):
    return None


def password_reset_done(request):
    return None


def password_reset(request):
    return None


def password_change(request):
    return None


def login(request):
    return None


def account_inactive(request):
    return None


def email_confirm(request):
    return None


def email(request):
    return None


def logout(request):
    return None