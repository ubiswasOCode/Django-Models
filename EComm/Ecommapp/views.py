from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from.serializers import RegisterSerializer, UserSerializerWithToken, productSerializer, categorySerializer
from.models import Product, RegisterUser, Category

# Create your views here.

# Get User


@api_view(['GET'])
def getuser(request):
    user = RegisterUser.objects.all()
    serializer = RegisterSerializer(user, many=True)
    return Response(serializer.data)


# For login Token

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Create User


@api_view(['POST'])
def createuser(request):
    data = request.data
    user = RegisterUser.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        gender=data['gender'],
        username=data['email'],
        email=data['email'],
        phone_number=data['phone_number'],
        password=make_password(data['password'])
    )

    serializer = UserSerializerWithToken(user, many=False)
    return Response(serializer.data)



# Delete user
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUser(request, pk):
    userForDeletion = RegisterUser.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')



# Update user
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateuser(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)
    data = request.data
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.username = data['email']
    user.email = data['email']
    user.age = data['age']
    user.phone_number = data['phone_number']
    user.gender = data['gender']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()
    return Response(serializer.data)



# Create Product
@api_view(['POST'])
def createproduct(request):
    data = request.data
    product = Product.objects.create(
        category=data['category'],
        brand=data['brand'],
        description=data['description'],
        price=data['price'],
    )

    serializer = productSerializer(product, many=False)
    return Response(serializer.data)


# Get Product

@api_view(['GET'])
def getproduct(request):
    products = Product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)


# Delete Product
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteproduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product was deleted')


#Update Product
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateproduct(request,pk):
    updateproducts=Product.objects.get(id=pk)
    serializer=productSerializer(updateproducts, partial=True)
    return Response('Product Updated')


# Create Category  
@api_view(['POST'])
def createcategory(request):
    data= request.data
    category=Category.objects.create(
        name=data['name'],
    )
    serializer = categorySerializer(category, many=False)
    return Response(serializer.data)

#get Category
@api_view(['GET'])
def getcategory(request):
    category= Category.objects.all()
    serializer=categorySerializer(category, many=True)
    return Response(serializer.data)


#delete Category
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCategory(request, pk):
    category= Category.objects.get(id=pk)
    category.delete()
    return Response('Category Delete')


#Update Category
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updatecategory(request,pk):
    updatecategory1=Category.objects.get(id=pk)
    serializer=categorySerializer(updatecategory1, many=True)
    return Response('Category Updated')
