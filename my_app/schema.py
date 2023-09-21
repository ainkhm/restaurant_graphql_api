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

class CreateRestaurant(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        address = graphene.String()

    ok = graphene.Boolean()
    restaurant = graphene.Field(RestaurantType)

    def mutate(self, info, name, address):
        restaurant = Restaurant(name=name, address=address)
        restaurant.save()
        return CreateRestaurant(ok=True, restaurant=restaurant)

class DeleteRestaurant(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(self, info, id):
        restaurant = Restaurant.objects.get(id=id)
        restaurant.delete()
        return DeleteRestaurant(ok=True)

class Mutation(graphene.ObjectType):
    create_restaurant = CreateRestaurant.Field()
    delete_restaurant = DeleteRestaurant.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)