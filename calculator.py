# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:47:24 2021

@author: CZR
"""

Gecerli_kelimeler = "0123456789+-/*="

print("""
Basit bir hesap makinesi uygulaması.
İşleçler:
+ toplama
- çıkarma
* çarpma
/ bölme
Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")

while True:
    veri = input("İşleminiz: ")
    if veri == "q":
        print("tamamlanıyor...")
        break
    
    for s in veri:
        if s not in Gecerli_kelimeler:
            print("Yanlış veri seti...")
            #quit()
            
        hesap = eval(veri)
        
        print(hesap)