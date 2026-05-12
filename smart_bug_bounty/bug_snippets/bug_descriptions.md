Bug Descriptions
bug1.py
Intended Behavior: Listenin son n elemanını bir liste olarak döndürmek.

Current Issue: Dilimleme (slicing) işleminde + 1 kullanıldığı için indeks kayması (off-by-one error) oluşuyor ve beklenen ilk eleman atlanıyor.

bug2.js
Intended Behavior: Bir dizi içerisindeki tüm sayısal fiyatları toplamak.

Current Issue: Döngü koşulu i <= prices.length şeklinde yazıldığı için dizi sınırlarının dışına çıkılıyor. Son adımda undefined değeri toplama eklendiği için sonuç NaN dönüyor.

bug3.cpp
Intended Behavior: Bir tam sayı vektörünün hassas (ondalıklı) ortalamasını hesaplamak.

Current Issue: sum / nums.size() işlemi sırasında her iki değişken de int türünde olduğu için "integer division" (tam sayı bölmesi) gerçekleşiyor ve ondalık kısım veri kaybına uğruyor.

bug4.py
Intended Behavior: Fonksiyon her çağrıldığında yeni bir skoru listeye ekleyip güncel listeyi döndürmek.

Current Issue: Python'da "mutable default argument" (değişebilir varsayılan argüman) kullanımı nedeniyle, scores listesi fonksiyon çağrıları arasında hafızada tutuluyor ve her çağrıda eski verilerin üzerine ekleme yapılıyor.

bug5.js
Intended Behavior: Bir API'den kullanıcı verilerini asenkron olarak çekmek ve kullanıcı adını döndürmek.

Current Issue: fetch ve .json() işlemleri sırasında await anahtar kelimesi unutulmuştur. Bu durum, veri yerine bir Promise objesi üzerinde işlem yapılmaya çalışılmasına ve hataya neden olmaktadır.
