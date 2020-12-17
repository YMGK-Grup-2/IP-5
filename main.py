from PIL import Image


class Resim:
    def __init__(self, resim_adresi):
        self.resim = Image.open(resim_adresi, 'r')
        self.boyut = self.resim.size  # (en, boy)
        self.mode = self.resim.mode  # 'RGB'
        self.piksel_listesi = list(self.resim.getdata())
        self.piksel_erisimi = self.resim.load()

    @property
    def piksel_dizisi(self):
        """
        Resmin piksel tuple'larından oluşan iki boyutlu dizisini oluşturur.
        :return: İki boyutlu dizi.
        """
        piksel_dizisi = [[] for i in range(self.boyut[1])]  # Resmin en boyutu kadar boş liste içeren bir liste.

        # Oluşturulan listeyi dolaşarak pikselleri liste elemanlarına ekleyen döngüler:
        for i in range(self.boyut[1]):
            for j in range(self.boyut[0]):
                piksel_dizisi[i].append(self.piksel_erisimi[j, i])

        return piksel_dizisi

    @property
    def bit_sayisi(self):
        """
        API üzerinden şifre istemek için belirtmemiz gereken boyutu hesaplayan method.
        :return: Potansiyel bit sayısı.
        """
        bit_sayisi = self.boyut[0] * self.boyut[1] * 3 * 8  # En(piksel) * Boy(piksel) * 3(Boyut - RGB) * 8(Bit)

        return bit_sayisi

    @property
    def bit_listesi(self):
        """
        Resmi bitlerine ayırarak 'self.bit_sayisi' boyutunda bir liste oluşturur.
        :return: Oluşturulan bitlerin listesi.
        """
        bit_listesi = []  # Bitler ile doldurulacak liste.

        for piksel in self.piksel_listesi:  # Piksellerde dolaşma
            for renk in piksel:  # Renk tuple'larında dolaşma
                # bin() fonksiyonu '0b101' gibi bir string döndürür.
                renk_biti = bin(renk)[2:]  # İndeksleme işlemi baştaki '0b' ibaresini kaldırır.

                # bin() fonksiyonu, eğer her zaman 8 bit döndürmez.
                if len(renk_biti) != 8:  # Eğer renk biti 8 bitlik bir değer değilse,
                    sifir_sayisi = 8 - len(renk_biti)

                    # Eksik olan değer kadar '0' değişkenin başına yazılır.
                    renk_biti = sifir_sayisi * '0' + renk_biti

                for bit in renk_biti:  # Oluşturulan bit dizesi okunarak, doğru değerler listeye kaydedilir.
                    if bit == '0':
                        bit_listesi.append(0)

                    elif bit == '1':
                        bit_listesi.append(1)

        return bit_listesi

    @staticmethod
    def bit_piksel_donusumu(bit_listesi):
        """
        Bitlerden oluşan liste parametresini, piksellerden oluşan bir listeye çevirir.
        :param bit_listesi: Bitlerden oluşan liste.
        :return: Piksel tuple'larının listesi.
        """
        b_l = iter(bit_listesi)  # İçerisinde daha fonksiyonel olarak dolaşmak için listeyi bir iterator'e çeviriyoruz.
        renk_listesi = []  # Bitlerden elde edilecek ilk liste; renk değerlerinin listesi.
        piksel_listesi = []  # Renk listesi gruplandırılarak elde edilecek ve return edilecek olan liste.

        # Piksel listesinde 8'li dolaşmak için iterator kullanımı:
        for a, s, d, f, g, h, j, k in zip(b_l, b_l, b_l, b_l, b_l, b_l, b_l, b_l):
            bit = str(a) + str(s) + str(d) + str(f) + str(g) + str(h) + str(j) + str(k)  # Bit string'i

            decimal = int(bit, 2)  # Bit string'inin integer değere dönüşümü
            renk_listesi.append(decimal)

        r_l = iter(renk_listesi)  # Daha fonksiyonel dolaşma için oluşturulan listeyi de itarator'e çeviriyoruz.

        # Listeyi 3'lü dolaşma ve her üçlüyü tuple'a ekleme:
        for r, g, b in zip(r_l, r_l, r_l):
            piksel = (r, g, b)

            piksel_listesi.append(piksel)

        return piksel_listesi

    def piksel_dizisi_liste_donusumu(self, piksel_dizisi):
        """
        Verilen iki boyutlu diziyi tek boyutlu piksel listesine dönüştüren method.
        :param piksel_dizisi: İki boyutlu piksel tuple'larından oluşan dizi.
        :return: Tek boyutlu piksel tuple'larından oluşan liste.
        """
        piksel_listesi = []

        for i in piksel_dizisi:
            for j in i:
                piksel_listesi.append(j)

        return piksel_listesi

    def resim_olusturma(self, piksel_listesi):
        """
        Verilen pikseller ile yeni bir resim oluşturma methodu.
        :param piksel_listesi: Yeni piksellerden oluşan liste.
        :return: Yeni resim
        """
        resim = Image.new(self.mode, self.boyut)
        resim.putdata(piksel_listesi)

        return resim


resim = Resim('image.jpeg')  # Temsili olarak bir resim kullanıyorum.

img_new = resim.resim_olusturma(resim.piksel_dizisi_liste_donusumu(resim.piksel_dizisi))
img_new.show()


"""bit_listesi = resim.bit_listesi

yeni_piksel_listesi = resim.bit_piksel_donusumu(bit_listesi)
yeni_resim = resim.resim_olusturma(yeni_piksel_listesi)
yeni_resim.save('new_image.jpeg')
"""



"""Fraktalın uygulanması
nboyut= resim.boyut[0]
mboyut= resim.boyut[1]

fraktal = []
say = 0
Y = 0
X = 0
ortanokta = math.floor(math.sqrt(nboyut * nboyut)) - 1
Adimlimit = ortanokta * 2 + 1, Y, X
ortaknt = True
Z = 0

for Z in Adimlimit:
    adimmod = Z % ortanokta
if ortaknt:
    if (Z % 2) == 0:
        X = mboyut - 1
        Y = Z
for i in range(0, Z + 1):

    fraktal[say] = bit_listesi[Y][x]
    say += 1
    X -= 1
    Y -= 1
else:

    X = mboyut - 1 - Z
    Y = 0

for i in Z + 1:
    fraktal[say] = bit_listesi[Y][X]
    say += 1
    X += 1
    Y += 1

if (Z == ortanokta):

    ortaknt = False

else:

    if (adimmod % 2 == 0):

        if (say == nboyut * mboyut - 1):

            X = 0
            Y = nboyut - 1
            adimmod = ortanokta

        else:

            X = 0
            Y = adimmod

for i in (ortanokta - adimmod + 1):

    fraktal[say] = bit_listesi[Y][X]
    say += 1
    X += 1
    Y += 1
else:

    if (say == nboyut * mboyut - 1):

        X = 0
        Y = nboyut - 1
        adimmod = ortanokta

    else:

        X = mboyut - adimmod
        Y = nboyut - 1

for i in (ortanokta - adimmod + 1):
    fraktal[say] = bit_listesi[Y][X]
    say += 1
    X -= 1
    Y -= 1

yeni_piksel_listesi = resim.bit_piksel_donusumu(fraktal)

yeni_resim = resim.resim_olusturma(yeni_piksel_listesi)
yeni_resim.save('new_image.jpeg')"""