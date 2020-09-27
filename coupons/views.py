from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CouponForm


@login_required
def add_coupon(request):
    """ Add a coupon to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = CouponForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added coupon!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add coupon. Please ensure the form is valid.')
    else:
        form = CouponForm(initial={'active': True})

    template = 'coupons/add_coupon.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
