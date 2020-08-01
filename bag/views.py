from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product
from django.views.decorators.http import require_http_methods
from coupons.models import Coupon
from coupons.forms import CouponApplyForm
#  from django.views.decorators.http import require_POST


#  @require_POST
@require_http_methods(["GET", "POST"])
def coupon_apply(request):
    if request.method == 'POST':
        coupon_form = CouponApplyForm(request.POST)
        if coupon_form.is_valid():
            code = coupon_form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code=code, active=True)
                request.session['coupon_id'] = coupon.id
                messages.success(request, 'Coupon applied')
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None
                messages.warning(request, 'Coupon not accepted')
                return redirect('view_bag')
    else:
        coupon_form = CouponApplyForm()

    return render(request, 'bag/bag.html', {'coupon_form': coupon_form})


def view_bag(request):

    coupon_form = CouponApplyForm()  # added to view as you had noticed absence

    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html', {'coupon_form': coupon_form})


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
