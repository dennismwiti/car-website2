from django.shortcuts import render, redirect
from .forms import AdminRegistrationForm
from django.contrib.auth.views import PasswordResetConfirmView


def admin_registration(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():

            # Debugging statements
            print(f"Form data: {form.cleaned_data}")

            # Save the form data (this also creates an entry in admin_registration_adminuser)
            form.save()

            # Redirect to a success page or login page
            return redirect('admin:login')

        else:
            # Print form errors for debugging
            print(form.errors)

    else:
        form = AdminRegistrationForm()

    return render(request, 'admin/registration.html', {'form': form})


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'admin/password_reset_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email_template_name'] = 'admin/password_reset_email.html'
        return context
