__all__ = ["yardım"]

_kıble_saati_metni = """Kıble Saati; Kabenin bulunduğu nokta, güneşin günlük deklinasyonundaki yeri ve bulunduğumuz nokta arasında olusan küresel üçgenin trigonometrik çözümünün zaman cinsinden ifadesidir. Güneşin deklinasyonu değiştikçe kıble saatleri de günlük olarak değişmektedir.

Yurtiçi takvimlerimizde namaz vakitlerinin son sütununda günlük olarak şehirlerimizin kıble saatleri bulunmaktadır. 
Kıble tesbiti yapacağımız gün takvimlerinizde bulunan kıble saatinde yeryüzüne dik duran cisimlerin gölgelerinin güneşe taraf olan uzantısı kıble yönünü göstermektedir. O saatte yüzünü güneşe dönen kıbleye dönmüş olur.

Kıble saatleri sadece adı geçen şehir için geçerlidir. Konuyu ülkemiz dışında düşündüğümüz zaman; kıblenin tespit edileceği yerin enlemi ve boylamı gereği ya yüzünü veya sırtını güneşe dönen kıbleye dönmüş olacağından bu konunun bu sütunda genel anlatımı, yanlış anlamalara ve hatalı uygulamalara sebep olacağından yurtdışı için talep edilen her şehre göre özel açıklamalar yapılmaktadır. """


# Şuanda kıble açısı hakkında veri alma özelliği yok.
##_kıble_açısı_metni = """
##"""

help_dict = {"Kıble Saati":
                 {"Metin": _kıble_saati_metni,
                  "links": ["https://www2.diyanet.gov.tr/DinHizmetleriGenelMudurlugu/Sayfalar/KibleSaatiNedir.aspx",
                            "https://vakithesaplama.diyanet.gov.tr/kible_saati.php"]
                  }
##             "Kıble Açısı":
             }

yardım = help_dict.__getitem__
                
