from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from .forms import AddEmailForm, RemoveEmailForm
from .forms import VisitorForm

def edit_visitor_profile(request):
    visitor = request.user.visitor
    if request.method == 'POST':
        form = VisitorForm(request.POST, request.FILES, instance=visitor)
        if form.is_valid():
            form.save()
    else:
        form = VisitorForm(instance=visitor)
    return render(request, 'edit_visitor_profile.html', {'form': form})

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
    return render(request, 'account_email.html', context)
