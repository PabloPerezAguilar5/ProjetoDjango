from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Produto
from .serializers import ProdutoSerializer

class ProductDataView(APIView):
    """
    Vista para retornar dados de produto em formato JSON.
    """

    def get(self, request, id, format=None):
        try:
            # Obtém o produto pelo ID
            produto = Produto.objects.get(id=id)
            # Serializa o produto
            serializer = ProdutoSerializer(produto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Produto.DoesNotExist:
            return Response(
                {"error": "Produto não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )