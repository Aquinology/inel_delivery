from django import template
from products.models import Order, Deliveryman

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user.id, ordered=False)
        if qs.exists():
            return qs[0].products.count()
    return 0


@register.filter
def ordered_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(ordered=True, deliveryman=None)
        if qs.exists():
            return qs.count()
    return 0


@register.filter
def my_order_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user.id, ordered=True)
        if qs.exists():
            return qs.count()
    return 0


@register.filter
def orders_taken_count(user):
    if user.is_authenticated:
        deliveryman = Deliveryman.objects.get(user=user.id)
        qs = Order.objects.filter(deliveryman=deliveryman)
        if qs.exists():
            return qs.count()
    return 0
