from PIL import Image
from typing import List, Tuple


class Resim:
    def __init__(self, resim_adresi):
        self.resim = Image.open(resim_adresi, 'r')
        self.boyut: tuple = self.resim.size  # (en, boy)
        self.mode: str = self.resim.mode  # 'RGB'
        self.piksel_listesi = list(self.resim.getdata())

    @property
    def bit_sayisi(self) -> int:
        """
        API üzerinden şifre istemek için belirtmemiz gereken boyutu hesaplayan method.
        :return: Potansiyel bit sayısı.
        """
        bit_sayisi = self.boyut[0] * self.boyut[1] * 3 * 8  # En(piksel) * Boy(piksel) * 3(Boyut - RGB) * 8(Bit)

        return bit_sayisi

    @property
    def bit_listesi(self) -> List[int]:
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
    def bit_piksel_donusumu(bit_listesi: List) -> List[Tuple[int, int, int]]:
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

    def resim_olusturma(self, piksel_listesi: List):
        """
        Verilen pikseller ile yeni bir resim oluşturma methodu.
        :param piksel_listesi: Yeni piksellerden oluşan liste.
        :return: Yeni resim
        """
        resim = Image.new(self.mode, self.boyut)
        resim.putdata(piksel_listesi)

        return resim


resim = Resim('image.jpeg')  # Temsili olarak bir resim kullanıyorum.

bit_listesi = resim.bit_listesi

yeni_piksel_listesi = resim.bit_piksel_donusumu(bit_listesi)

yeni_resim = resim.resim_olusturma(yeni_piksel_listesi)
yeni_resim.save('new_image.jpeg')
