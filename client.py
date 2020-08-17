from utils import do_request, get_district, endpoints

__all__ = ["aylık_namaz_vakitleri", "günlük_namaz_vakitleri", "ilçe_bayram_namazı_vakitleri"]

# API
def aylık_namaz_vakitleri(il, ilçe = None):
    return do_request(endpoints["vakitler"], {"ilce": get_district(il, ilçe)})

def günlük_namaz_vakitleri(il, ilçe = None):
    return aylık_namaz_vakitleri(il, ilçe)[0]

def ilçe_bayram_namazı_vakitleri(il, ilçe = None):
    return do_request(endpoints["bayram"], {"ilce": get_district(il, ilçe)})
