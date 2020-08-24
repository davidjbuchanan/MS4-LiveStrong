from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product
from django.views.decorators.http import require_http_methods
from coupons.models import Coupon
from coupons.forms import CouponApplyForm
#  from django.views.decorators.http import require_POST
from django.utils import timezone  # updates


#  @require_POST
@require_http_methods(["GET", "POST"])
def coupon_apply(request):
    now = timezone.now()  # updates
    if request.method == 'POST':
        coupon_form = CouponApplyForm(request.POST)
        if coupon_form.is_valid():
            code = coupon_form.cleaned_data['code']
            try:
                # updates   coupon = Coupon.objects.get(code=code, active=True)
                coupon = Coupon.objects.get(code__iexact=code,  # updates
                                            valid_from__lte=now,  # updates
                                            valid_to__gte=now,  # updates
                                            active=True)  # updates
                request.session['coupon_id'] = coupon.id
                request.session['discount'] = coupon.discount  #
                request.session['code'] = coupon.code  #
                messages.success(request, 'Coupon applied')
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None
                messages.warning(request, 'Coupon not accepted')
                return redirect('view_bag')
    else:
        coupon_form = CouponApplyForm()
    
    template = 'bag/bag.html'
    context = {
        'code': code,
        'coupon_id': coupon.id,
        'coupon_discount': coupon.discount,
        'coupon_form': coupon_form
    }
    #  return render(request, 'bag/bag.html', {'coupon_form': coupon_form})
    return render(request, template, context)


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


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    bag = request.session.get('bag', {})
    try:
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
