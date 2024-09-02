import requests


class HttpResponse:
    def get_response(self, url, headers=None):
        """
        Get response to url
        """
        response = requests.request(
            method="GET",
            url=url,
            headers=headers
        )
        return self.check_response(response)

    @staticmethod
    def check_response(response: requests.Response):
        """
        Check status response
        """
        if response.status_code == 200:
            return response
        else:
            error_message = f"Your request returned {response.status_code} status code."
            if response.status_code == 404:
                error_message += " The requested resource wasn't found."
            elif response.status_code == 500:
                error_message += " The server encountered an internal error."
            raise Exception(error_message)
