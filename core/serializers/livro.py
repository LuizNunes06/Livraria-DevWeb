from rest_framework.serializers import ModelSerializer

from core.models import Livro


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1 # Permite a apresentação dos dados relacionados, mostras nos valores no lugar do id.
