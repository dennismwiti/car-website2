"""
Custom middlewares for the Django application.
"""

class HideServerMiddleware:
    """
    Middleware to hide the 'Server' header in HTTP responses.
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, get_response):
        """
        Initialize the middleware.

        Args:
            get_response (callable): The next middleware or view function in the chain.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Process the request and response.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The HTTP response.
        """
        response = self.get_response(request)
        response['Server'] = None
        return response
