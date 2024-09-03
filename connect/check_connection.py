import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8,af;q=0.7"
}

class HttpResponse:
    def get_response(self, url, headers=None):
        """
        Get response to url
        """
        response = requests.request(
            method="GET",
            url=url,
            headers=HEADERS
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
