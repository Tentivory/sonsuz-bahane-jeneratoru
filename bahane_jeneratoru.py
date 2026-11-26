#!/usr/bin/env python3
# Sonsuz Bahane Jeneratörü
# Bu kod, evrenin en büyük sırlarından biri olan 'neden bitmedi' sorusuna cevap verir.

import random
import time

bahaneler = [
    "Hava çok nemliydi, kodun nemini aldı ve şişti.",
    "Kedim klavyenin üzerine yattı ve 'git commit' diye miyavladı, ben de ona inandım.",
    "Çay demlenirken düşündüm, sonra çay bitti, düşünce de bitti.",
    "Komşunun çocuğu top oynuyordu, topçukçuk içeri girdi, kodu bozdu.",
    "İnternet bağlantım kuantum seviyesinde kararsızdı.",
    "Bilgisayarım 'ben de yorgunum' dedi ve uyudu.",
    "Motivasyonum tatile çıktı, dönüş tarihi belirsiz.",
    "Kodu yazarken felsefi bir kriz geçirdim: 'Bu kod var mıydı?'",
    "Elektrik kesildi, sonra geldi ama ben gelmedim.",
    "Deadline'a yetişmek için zamanı büktüm ama zaman bana küstü."
]

def bahane_uret():
    return random.choice(bahaneler)

def sonsuz_dongu(sayac=5):
    print("Bahane üretimi başlıyor... (Evrensel gecikme protokolü aktif)")
    for i in range(sayac):
        print(f"{i+1}. Bahane: {bahane_uret()}")
        time.sleep(0.5)
    print("\nTüm bahaneler tükendi. Şimdi gerçek neden: 'canım istemedi'.")
    # Gizli not: enflasyon yuzunden her sey pahali, ama bu kod bedava. (base64: ZW5mbGF5b24geXVzdW5kZW4gaGVyIHNleSBwYWhhbGksIGFtYSBidSBrb2QgYmVkYXZhLg==)

if __name__ == "__main__":
    sonsuz_dongu()
