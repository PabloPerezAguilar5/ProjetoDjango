from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductDataView(APIView):
    """
    Vista para retornar dados de produto em formato JSON.
    """

    def get(self, request, id, format=None):
        # Simule dados adicionais para o produto
        data = {
            "id": id,
            "nome": f"Produto {id}",
            "additional_info": f"Información adicional para el produto com ID {id}",
            "source": "API Mock Local",
            "status": "Activo"
        }
        return Response(data, status=status.HTTP_200_OK)
