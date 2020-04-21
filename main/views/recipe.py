from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from main.models.recipe import Recipe
from main.serializers.recipe import BasicRecipeSerializer, DetailedRecipeSerializer

class AllRecipesPagination(PageNumberPagination):
    page_size = 40
    page_size_query_param = 'page_size'
    max_page_size = 40


class AllRecipesListView(ListCreateAPIView):
  queryset = Recipe.objects.all()
  serializer_class = BasicRecipeSerializer
  pagination_class = AllRecipesPagination

  def get(self, request): 
      recipes = self.paginate_queryset(Recipe.objects.all())
      serializer = BasicRecipeSerializer(recipes, many=True)
      return self.get_paginated_response(serializer.data)

class RecipeDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Recipe.objects.all()
  serializer_class = DetailedRecipeSerializer

# this returns recipes that have main_protein that matches the search filter taken from the URL of the GET request
class MainProteinRecipeView(ListCreateAPIView):
  serializer_class = BasicRecipeSerializer
  pagination_class = AllRecipesPagination

  def get(self, request, query): 
      recipes = self.paginate_queryset(Recipe.objects.filter(main_protein__iexact=query))
      serializer = BasicRecipeSerializer(recipes, many=True)
      return self.get_paginated_response(serializer.data)

class MainProteinSummaryView(ListCreateAPIView):
  serializer_class = BasicRecipeSerializer
  pagination_class = AllRecipesPagination

  def get(self, request, query): 
      recipes = self.paginate_queryset(Recipe.objects.filter(main_protein__iexact=query)[:10])
      serializer = BasicRecipeSerializer(recipes, many=True)
      return self.get_paginated_response(serializer.data)

class DietLabelRecipeView(ListCreateAPIView):
  serializer_class = BasicRecipeSerializer
  pagination_class = AllRecipesPagination

  def get(self, request, query):
      recipes = self.paginate_queryset(Recipe.objects.filter(diet_Labels__icontains=query))
      serializer = BasicRecipeSerializer(recipes, many=True)
      return self.get_paginated_response(serializer.data)


# this takes up to 3 search terms from the URL of the GET request (named query - in the urls.py) and returns recipes that include these search terms in the ingredients list
class FridgeRecipeView(ListCreateAPIView):
  # queryset = Recipe.objects.filter(ingredients_lines__icontains='')
  serializer_class = BasicRecipeSerializer
  pagination_class = AllRecipesPagination 

  def get(self, request, query): 
      if query.count('&') == 2:
        query1 = query.split('&')[0]
        query2 = query.split('&')[1]
        query3 = query.split('&')[2]
      elif query.count('&') == 1:
        query1 = query.split('&')[0]
        query2 = query.split('&')[1]
        query3 = ''
      else:
        query1 = query
        query2 = ''
        query3 = ''

      recipes = self.paginate_queryset(Recipe.objects.filter(
        ingredients_lines__icontains=query1
        ).filter(
          ingredients_lines__icontains=query2
        ).filter(
          ingredients_lines__icontains=query3
        ))
      serializer = BasicRecipeSerializer(recipes, many=True)
      return self.get_paginated_response(serializer.data)

# class AllRecipeSearchList(ListCreateAPIView):
#   serializer_class = BasicRecipeSerializer
#   pagination_class = AllRecipesPagination 

#   def get(self, request, query): 
#     number_of_terms = len(query.split('&'))
#     termsArray = query.split('&')
#     # for term in termsArray:
#     #   return query(position in termsarray) = 
#     for x in range(0, number_of_terms):
#       return query(x) = termsArray[x]

#       if query.count('&') == 2:
#         query1 = query.split('&')[0]
#         query2 = query.split('&')[1]
#         query3 = query.split('&')[2]
#       elif query.count('&') == 1:
#         query1 = query.split('&')[0]
#         query2 = query.split('&')[1]
#         query3 = ''
#       else:
#         query1 = query
#         query2 = ''
#         query3 = ''

#       recipes = self.paginate_queryset(Recipe.objects.filter(
#         ingredients_lines__icontains=query1
#         ).filter(
#           ingredients_lines__icontains=query2
#         ).filter(
#           ingredients_lines__icontains=query3
#         ))
#       serializer = BasicRecipeSerializer(recipes, many=True)
#       return self.get_paginated_response(serializer.data)

# query = '&tomato&ham&cheese&potato'
# number_of_terms = len(query.split('&'))
# print(number_of_terms)
# termsArray = query.split('&')
# print(termsArray)
# for x in range(0, number_of_terms):
#   globals()['query%s' % x] = termsArray[x]
# print(query0)
# print(query1)
# print(query2)
# print(query3)
# print(query4)

# query = '&tomato&ham&cheese&potato'

# number_of_terms = len(query.split('&'))
# termsArray = query.split('&')
# termsDict = {}
# for x in range(0, number_of_terms):
#   termsDict['query{0}'.format(x)] = termsArray[x]
# print(termsDict)
  

