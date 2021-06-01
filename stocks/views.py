from rest_framework import generics
from rest_framework.response import Response

from .stock import Stock


# Create your views here.
class IntradayStock(generics.GenericAPIView):
    def get(self, request, symbol):
        return Response(Stock(output_format='json').getIntraday(symbol=symbol))


class DailyStock(generics.GenericAPIView):
    def get(self, request, symbol):
        return Response(Stock(output_format='json').getDaily(self.kwargs.get('symbol')))


class SearchStock(generics.GenericAPIView):
    def get(self, request, symbol):
        return Response(Stock(output_format='json').getSymbolSearch(self.kwargs.get('symbol')))