import json
from django.http import HttpResponse


class Ticker:
    def __init__(self, symbol, request):
        self.symbol = symbol
        self.request = request

    def summary(self):
        try:
            # existing code to fetch and parse summary data
            # ...
            return (True, dictionary)
        except Exception as e:
            return (False, str(e))

    def statistics(self):
        try:
            # existing code to fetch and parse statistics data
            # ...
            return (True, dictionary)
        except Exception as e:
            return (False, str(e))

    def get_response(self, data):
        if data[0]:
            return HttpResponse(json.dumps(data[1]), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'error': data[1]}), status=500, content_type='application/json')
