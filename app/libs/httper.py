import requests


class HTTP:
    @staticmethod
    def get(url,return_json= True):
        r = requests.get(url, headers={'Connection': 'close','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"})

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

