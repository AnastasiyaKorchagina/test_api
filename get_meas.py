import requests

class apiClient:

    def __init__(self):
        self.host = 'http://puv-dev-int-auth-admin.otr.ru:8080'
        self.headers = \
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.77 YaBrowser/20.11.0.918 Yowser/2.5 Safari/537.36'}

    def bearer_token(self, username, password):
        params = {'username': username, 'password': password}
        url = '/token'
        responce = requests.post(self.host + url, params=params, headers=self.headers)
        return responce.json()['accessToken']


class PaymentsController(apiClient):

    token = apiClient().bearer_token('Drevov', 'd12345')

    def __init__(self):
        super(PaymentsController, self).__init__()
        self.headers.update({'Authorization': 'Bearer {}'.format(self.token)})
        self.host = 'http://puv-dev-int-elk-01.otr.ru:18080/'

    def get_meas(self):
        url = 'api_payment/payroll/settings'
        responce = requests.get(self.host + url, headers=self.headers)
        print(responce.request.headers)
        print(responce.text)
        return responce


