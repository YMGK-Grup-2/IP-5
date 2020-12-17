# Resim Şifreleme Algoritması Tasarımı

## Kütüphaneler:
### Pillow:
Program içerisinde resim manipülasyonu yapabilmek için 'Pillow' kütüphanesinin 
'Image' modülü kullanılmıştır.

## Sınıflar
### Resim:
Resim sınıfı 'resim adresi' parametresi ile tanımlanır.\
<code>resim = Resim('image.jpg')</code>
#### Sınıf özellikleri:
1. <code>.resim</code>: Image modulü ile oluşturulan nesne.
2. <code>.boyut</code>: Resmin en ve boy bilgisi. 
3. <code>.mode</code>: Resmin mod bilgisi.
4. <code>.piksel_listesi</code>: Resmin piksellerinden oluşan listedir.
5. <code>.piksel_erisimi</code>: Resmin piksel bilgilerini tutan nesne.
6. <code>.piksel_dizisi</code>: Resmin piksellerinden oluşan iki boyutlu dizi. 
7. <code>.bit_sayisi</code>: Resmin potansiyel bit sayısıdır.
8. <code>.bit_listesi</code>: Resmin bitlerinden oluşan bir liste.
#### Sınıf methodları:
1. <code>.bit_piksel_donusumu(bit_listesi)</code>: Verilen bit listesini piksellerden oluşan bir listeye dönüştüren static method.
2. <code>.piksel_dizisi_liste_donusumu(piksel_dizisi)</code>: Verilen iki boyutlu piksel dizisini tek boyutlu piksel listesine dönüştürür.
3. <code>.resim_olusturma(piksel_listesi)</code>: Verilen piksel listesi ile resmin boyut ve mod bilgileri ile yeni bir resim nesnesi oluşturan method.

