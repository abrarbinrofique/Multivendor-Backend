from django.db import transaction, IntegrityError
from django.db.models import F
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.permissions import ReadOnly, IsVendor
from core.utils import throw_unauthenticated
from .serializers import ProductSerializer, ProductImageSerializer,OrderItemSerializer,OrderSerializer
from .models import Product, Order, OrderItem, ProductImage

import traceback

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsVendor | ReadOnly]

class ProductImageViewset(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsVendor | ReadOnly]
    



    
@api_view(http_method_names=["POST"])
def create_order(request):
    shortage = False
    available = {}
    try:
        res = throw_unauthenticated(request)
        if res: return res
        cart = request.data["cart"]

        for id in cart:
            qty = cart[id]
            product = Product.objects.get(id=id)
            if product.quantity < qty:
                shortage = True
                available[id] = product.quantity

        if shortage:
            return Response({
                "error": "Some items are less in stock than the demand",
                "shortage_items_availability": available,
            })

        try:
            with transaction.atomic():
                order = Order.objects.create(
                    user = request.user
                )
                order_items = []
                for id in cart:
                    qty = cart[id]
                    product = Product.objects.get(id=id)
                    order_items.append(OrderItem(
                        order = order,
                        item = product,
                        quantity = qty,
                    ))
                    product.quantity = F("quantity") - qty
                    product.save()
                OrderItem.objects.bulk_create(order_items)

                return Response({
                    "message": "success",
                    "order_id": order.id,
                })

        except IntegrityError:
            traceback.print_exc()
            return Response({
                "error": "There was a problem handling your request."
            })
    except Product.DoesNotExist:
        return Response({
            "error": "There exists invalid product id(s) in your request"
        })
    except:
        return Response({
            "error": "There was a problem handling your request"
        })


class Orderitemviewset(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


    def get_queryset(self):
          queryset= super().get_queryset()

          item_id=self.request.query_params.get('item_id')
       

          if item_id:
               queryset=queryset.filter(item_id=item_id)
        

          return queryset
         


class Orderviewset(ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

