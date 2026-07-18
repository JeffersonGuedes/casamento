from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ValidationError
from .models import Gift
from .serializers import GiftSerializer
from .services import reserve_gift

class GiftListCreateView(generics.ListCreateAPIView):
    """
    GET: Lista todos os presentes.
    POST: Cria um novo presente usando o GiftSerializer.
    """
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer

class ReserveGiftView(APIView):
    """
    POST: Trava o item no banco (Pessimistic Locking) e reserva para o comprador.
    """
    def post(self, request, gift_id):
        buyer_name = request.data.get('buyer_name')
        
        if not buyer_name:
            return Response(
                {"error": "O nome do comprador é obrigatório."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            gift = reserve_gift(gift_id, buyer_name)
            serializer = GiftSerializer(gift)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e.message)}, status=status.HTTP_409_CONFLICT)
        except Gift.DoesNotExist:
            return Response({"error": "Presente não encontrado."}, status=status.HTTP_404_NOT_FOUND)