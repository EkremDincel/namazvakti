from urllib.parse import urlencode
from urllib.request import urlopen
import urllib
import json
from .cache import Cache

class TooManyRequestsError(ConnectionError): pass

__all__ = ["do_post_request", "do_get_request", "get_district", "endpoints"]

def do_request(url, data = ()):
    try:
        return json.loads(urlopen(url + "?" + urlencode(data)).read())
    except urllib.error.HTTPError as e:
        if e.code == 429:
            raise TooManyRequestsError("API limit is passed. Wait for 15 minutes.")
        raise

#---
base_url = "https://ezanvakti.herokuapp.com/"
endpoints = {"ülkeler": base_url + "ulkeler",
             "şehirler": base_url + "sehirler",
             "ilçeler": base_url + "ilceler",
             "vakitler": base_url + "vakitler",
             "bayram": base_url + "bayram"}
TR_NO = 2

trans_table = str.maketrans("abcçdefgğhıijklmnoöprşstuüvyz",
                            "ABCÇDEFGĞHIİJKLMNOÖPRŞSTUÜVYZ")

cache = Cache("il_ve_ilçeler.pickle")

def get_district(il, ilçe = None):
    if ilçe is None: ilçe = il
    il, ilçe = il.translate(trans_table), ilçe.translate(trans_table)
    cache_value = cache.get((il, ilçe))
    if cache_value is not None:
        return cache_value
    
    iller = do_request(endpoints["şehirler"], {"ulke": TR_NO})
    for i in iller:
        if i["SehirAdi"] == il:
            il_no = i["SehirID"]
            break
    else:
        raise ValueError(f"'{il}' ili bulunamadı.")
    
    ilçeler = do_request(endpoints["ilçeler"], {"sehir": il_no})
    for i in ilçeler:
        if i["IlceAdi"] == ilçe:
            ilçe_no = i["IlceID"]
            break
    else:
        raise ValueError(f"'{ilçe}' ilçesi bulunamadı.")
    
    cache[(il, ilçe)] = ilçe_no
    return ilçe_no
