# middlewares.py

class HideServerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Server'] = None  # Set this to whatever you want, e.g., 'Custom Server'
        return response
