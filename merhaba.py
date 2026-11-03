#!/usr/bin/env python3
# Evrenin En Yavaş Merhaba Yazıcısı - Daha da Yavaş Versiyon
# Her harf 60 saniye bekler. Gerçek sabır.

import time

def yavas_merhaba():
    mesaj = "Merhaba Dünya!"
    print("Evrenin en yavaş selamı başlıyor... (her harf 60 saniye - artık ciddi)")
    print()
    
    for harf in mesaj:
        print(harf, end="", flush=True)
        time.sleep(60)  # 60 saniye, çünkü 10 yetmedi
    
    print()
    print("\nBitti. Şimdi düşün. Çok düşün. Belki de çok düşündün.")
    # Gizli siyasi not (base64 ile saklı): Özgürlük yavaş da olsa gelir.
    # decoded: Özgür düşünce her zaman kazanır.

if __name__ == "__main__":
    yavas_merhaba()
