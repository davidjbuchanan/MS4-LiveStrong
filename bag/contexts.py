from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
# from django.utils import timezone  #
from coupons.models import Coupon  #
# from coupons.forms import CouponApplyForm  #
# from coupons.views import coupon_apply  # Coupon


def bag_contents(request):

    bag_items = []
    sub_total = 0  #
    total = 0
    product_count = 0
    discount_total = 0  #
    discount_percentage = 0  #
    bag = request.session.get('bag', {})
    coupon_id = request.session.get('coupon_id', int())  #

    try:
        code = Coupon.objects.get(id=coupon_id)

    except Coupon.DoesNotExist:
        code = None

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        #  total += quantity * product.price
        sub_total += quantity * product.price  #

        if code is not None:
            discount_percentage = code.discount
            discount_total = (discount_percentage/Decimal('100'))*sub_total
            total = sub_total - discount_total
        else:
            total = sub_total

        #  coupon_form = CouponApplyForm(request.POST)
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # coupon_form = CouponApplyForm(request.POST)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = Decimal(settings.FREE_DELIVERY_THRESHOLD) - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'sub_total': sub_total,
        'code': code,
        'discount_total': discount_total,
        'discount_percentage': discount_percentage,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

    """def bag_contents(request):    Scott

    bag_items = []
    bag = request.session.get('bag', {})
    code = request.POST.get('discount')  #
    if not code:  #
        code = request.session.get('discount', {})  #
        try:  #
            if bag_items == {}:  #
                del request.session['discount']  #
        except KeyError:  #
            pass  #

    now = timezone.now()
    total = 0
    product_count = 0
    sub_total = 0  #
    discount_total = 0  #
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        #  total += quantity * product.price
        sub_total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if code:  #
        try:  #
            promocode = Coupon.objects.get(code__iexact=code,  #
                                           valid_from__lte=now,  #
                                           valid_to__gte=now,  #
                                           active=True)  #

            discount_total = sub_total * Decimal(promocode.discount / 100)  #
            print("Promo Code is valid")  #
        except Coupon.DoesNotExist:  #
            print("Promo Code is invalid")  #
    request.session['discount'] = code  #
    total = sub_total - discount_total  #

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'discount_total': discount_total,  #
    }

    return context
"""


"""  original


from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

"""
