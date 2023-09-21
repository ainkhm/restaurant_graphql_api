import graphene
from graphene_django import DjangoObjectType
from my_app.models import Restaurant

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
        fields =('id','name','address')
        
class Query(graphene.ObjectType):

    restaurants = graphene.List(RestaurantType)

    def resolve_restaurants(self, info, **kwards):
        return Restaurant.objects.all()
    
schema = graphene.Schema(query=Query)