# import graphene
import graphene

# format django object to graphql object
from graphene_django import DjangoObjectType

# Import our models
from ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    # Have access to few fields for graphql to use
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")
        
class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

# notice here is graphene object type        
class Query(graphene.ObjectType):
    # define our list
    all_ingredients = graphene.List(IngredientType)
    
    #   
    category_by_name = graphene.Field(CategoryType, name = graphene.String(required=True))
    
    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()
    
    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)