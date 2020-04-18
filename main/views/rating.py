from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from main.models.rating import Rating
from main.serializers.rating import BasicRatingSerializer

from main.models.recipe import Recipe

class RatingListView(ListCreateAPIView):
  queryset = Rating.objects.all()
  serializer_class = BasicRatingSerializer

  def post(self, request):
      # Turn the json into data we can store in psql. PROBABLY NEED A POPULATESERIALIZER
      serializer = BasicRecipeSerializer(data=request.data)
      # I'll have validation on the frontend. as in only rating using the stars will post to this endpoint anyway
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)