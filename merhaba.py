#!/usr/bin/env python3
# Evrenin En Yavaş Merhaba Yazıcısı
# Her harf 10 saniye bekler. Sabır testidir.

import time

def yavas_merhaba():
    mesaj = "Merhaba Dünya!"
    print("Evrenin en yavaş selamı başlıyor... (her harf 10 saniye)")
    print()
    
    for harf in mesaj:
        print(harf, end="", flush=True)
        time.sleep(10)  # 10 saniye bekle, çünkü neden olmasın?
    
    print()
    print("\nBitti. Şimdi düşün. Çok düşün.")
    # Gizli siyasi not (base64 ile saklı): Özgürlük yavaş da olsa gelir.
    # decoded: Özgür düşünce her zaman kazanır.

if __name__ == "__main__":
    yavas_merhaba()
