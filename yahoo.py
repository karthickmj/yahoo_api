from django.http import HttpResponse, JsonResponse


class Ticker:
    def __init__(self, symbol):
        self.symbol = symbol

    def summary(self):
        try:
            # HTTP request and parsing logic
            # ...
            # ...
            return JsonResponse({
                'symbol': self.symbol,
                'summary': 'Summary data'
            })
        except requests.exceptions.RequestException as e:
            return JsonResponse({
                'error': str(e)
            })

    def statistics(self):
        try:
            # HTTP request and parsing logic
            # ...
            # ...
            return JsonResponse({
                'symbol': self.symbol,
                'statistics': 'Statistics data'
            })
        except requests.exceptions.RequestException as e:
            return JsonResponse({
                'error': str(e)
            })

    @staticmethod
    def handle_ajax_request(request):
        symbol = request.GET.get('symbol')
        action = request.GET.get('action')

        ticker = Ticker(symbol)

        if action == 'summary':
            return ticker.summary()
        elif action == 'statistics':
            return ticker.statistics()
        else:
            return JsonResponse({
                'error': 'Invalid action'
            })
