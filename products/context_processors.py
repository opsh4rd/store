from products.models import Baskets


def baskets(request):
    user = request.user
    return {'baskets': Baskets.objects.filter(user=user) if user.is_authenticated else []}
