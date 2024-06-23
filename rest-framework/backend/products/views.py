from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

# endpoint: api/products/


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #  the below is the built in method and will only be called if generics is createAPIView
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


# endpoint: api/products/id
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # NOTE: Terms like queryset and serializer_class are generics terms we have to follow this standard


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwagrs):

    if request.method == 'GET':
        if pk is not None:
            # If primary key exists then it willl act as detail view

            # unlike classbased views, in function based views we have to manually handle  page not found:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            # echoing/sending back the created data to the user
            return Response(data)

        # below code will run if primary key does not exists then this will act as get a list of all products
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        # echoing/sending back the created data to the user
        return Response(data)

    if request.method == 'POST':
        # If method is post this will act as product create view
        serializer = ProductSerializer(data=request.data)

        # below we are handling that if content doest not exists then fill it as the title (This is completely an optional step)

        # updating the content value
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)

        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            print("instance from functionbased product create view: ", instance)
            print(
                "serializer.data from functionbased product create view: ", serializer.data)

            # echoing/sending back the created data to the user
            return Response(serializer.data)
