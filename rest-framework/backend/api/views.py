from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from products.models import Product

# # Get request
# @api_view(["GET"])  # <-- here you can define the list of allowed methods
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data)

# POST request


@api_view(["POST"])  # <-- here you can define the list of allowed methods
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True): #here raise_exception=True is just for saving a good error info
        instance = serializer.save()
        print("Instance: ", instance)
        print("serializer.data: ", serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
