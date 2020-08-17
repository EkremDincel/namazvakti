# Namaz Vakitleri için API istemcisi

Kütüphane şu API'yı kullanmaktadır: https://github.com/furkantektas/EzanVaktiAPI

# Kullanım

Öncelikle modülü içe aktarıyoruz:

```python
>>> import namazvakti
```

## Günlük Namaz Vakitleri 

```python
>>> namazvakti.günlük_namaz_vakitleri("istanbul", "silivri")
{'Aksam': '20:10', 'AyinSekliURL': 'https://namazvakti.diyanet.gov.tr/images/sd6.gif', 'Gunes': '06:12', 'GunesBatis': '20:03', 'GunesDogus': '06:19', 'HicriTarihKisa': '27.12.1441', 'HicriTarihUzun': '27 Zilhicce 1441', 'Ikindi': '17:04', 'Imsak': '04:36', 'KibleSaati': '12:10', 'MiladiTarihKisa': '17.08.2020', 'MiladiTarihKisaIso8601': '17.08.2020', 'MiladiTarihUzun': '17 Ağustos 2020 Pazartesi', 'MiladiTarihUzunIso8601': '2020-08-17T00:00:00.0000000+03:00', 'Ogle': '13:16', 'Yatsi': '21:40'}
>>>
````

## Aylık Namaz Vakitleri

```python
>>> len(namazvakti.aylık_namaz_vakitleri("istanbul")) # sadece ilçe vererek istanbul merkezin değerlerini de alabiliriz
31
>>> namazvakti.aylık_namaz_vakitleri("istanbul")[:5]
{('İSTANBUL', 'SİLİVRİ'): '9548', ('İSTANBUL', 'İSTANBUL'): '9541'}
[{'Aksam': '20:07', 'AyinSekliURL': 'https://namazvakti.diyanet.gov.tr/images/sd6.gif', 'Gunes': '06:09', 'GunesBatis': '20:00', 'GunesDogus': '06:16', 'HicriTarihKisa': '27.12.1441', 'HicriTarihUzun': '27 Zilhicce 1441', 'Ikindi': '17:01', 'Imsak': '04:33', 'KibleSaati': '12:11', 'MiladiTarihKisa': '17.08.2020', 'MiladiTarihKisaIso8601': '17.08.2020', 'MiladiTarihUzun': '17 Ağustos 2020 Pazartesi', 'MiladiTarihUzunIso8601': '2020-08-17T00:00:00.0000000+03:00', 'Ogle': '13:13', 'Yatsi': '21:37'}, {'Aksam': '20:06', 'AyinSekliURL': 'https://namazvakti.diyanet.gov.tr/images/sd7.gif', 'Gunes': '06:10', 'GunesBatis': '19:59', 'GunesDogus': '06:17', 'HicriTarihKisa': '28.12.1441', 'HicriTarihUzun': '28 Zilhicce 1441', 'Ikindi': '17:01', 'Imsak': '04:34', 'KibleSaati': '12:10', 'MiladiTarihKisa': '18.08.2020', 'MiladiTarihKisaIso8601': '18.08.2020', 'MiladiTarihUzun': '18 Ağustos 2020 Salı', 'MiladiTarihUzunIso8601': '2020-08-18T00:00:00.0000000+03:00', 'Ogle': '13:13', 'Yatsi': '21:35'}, {'Aksam': '20:05', 'AyinSekliURL': 'https://namazvakti.diyanet.gov.tr/images/ruyet.gif', 'Gunes': '06:11', 'GunesBatis': '19:58', 'GunesDogus': '06:18', 'HicriTarihKisa': '29.12.1441', 'HicriTarihUzun': '29 Zilhicce 1441', 'Ikindi': '17:00', 'Imsak': '04:36', 'KibleSaati': '12:10', 'MiladiTarihKisa': '19.08.2020', 'MiladiTarihKisaIso8601': '19.08.2020', 'MiladiTarihUzun': '19 Ağustos 2020 Çarşamba', 'MiladiTarihUzunIso8601': '2020-08-19T00:00:00.0000000+03:00', 'Ogle': '13:13', 'Yatsi': '21:33'}, {'Aksam': '20:03', 'AyinSekliURL': 'https://namazvakti.diyanet.gov.tr/images/r1.gif', 'Gunes': '06:12', 'GunesBatis': '19:56', 'GunesDogus': '06:19', 'HicriTarihKisa': '1.1.1442', 'HicriTarihUzun': '1 Muharrem 1442', 'Ikindi': '16:59', 'Imsak': '04:37', 'KibleSaati': '12:09', 'MiladiTarihKisa': '20.08.2020', 'MiladiTarihKisaIso8601': '20.08.2020', 'MiladiTarihUzun': '20 Ağustos 2020 Perşembe', 'MiladiTarihUzunIso8601': '2020-08-20T00:00:00.0000000+03:00', 'Ogle': '13:13', 'Yatsi': '21:31'}, {'Aksam': '20:02', 'AyinSekliURL': 'https://namazvakti.diyanet.gov.tr/images/r2.gif', 'Gunes': '06:13', 'GunesBatis': '19:55', 'GunesDogus': '06:20', 'HicriTarihKisa': '2.1.1442', 'HicriTarihUzun': '2 Muharrem 1442', 'Ikindi': '16:58', 'Imsak': '04:39', 'KibleSaati': '12:08', 'MiladiTarihKisa': '21.08.2020', 'MiladiTarihKisaIso8601': '21.08.2020', 'MiladiTarihUzun': '21 Ağustos 2020 Cuma', 'MiladiTarihUzunIso8601': '2020-08-21T00:00:00.0000000+03:00', 'Ogle': '13:12', 'Yatsi': '21:29'}]
>>>
```

## Bayram Namazı Vakitleri

```python
>>> namazvakti.ilçe_bayram_namazı_vakitleri("ankara", "akyurt")
{'KurbanBayramNamaziHTarihi': '10 Zilhicce 1441', 'KurbanBayramNamaziSaati': '06:18:00', 'KurbanBayramNamaziTarihi': '31 Temmuz 2020 Cuma', 'RamazanBayramNamaziHTarihi': '1 Şevval 1441', 'RamazanBayramNamaziSaati': '05:59:00', 'RamazanBayramNamaziTarihi': '24 Mayıs 2020 Pazar'}
>>> 
```

# Yapılacaklar

* Cache sistemini geliştirmek.
* Dönüş değerleri için daha kolay bir kullanım sağlamak.