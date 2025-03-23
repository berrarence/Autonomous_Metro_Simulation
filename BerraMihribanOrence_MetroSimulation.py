from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))


class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    # en az aktarmalı seçeneği bulan çözüm
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur

        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın

        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """

        # Başlangıç ve hedef istasyonları al
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # Ziyaret edilenleri tut (orijinal hali)
        ziyaret_edildi = {baslangic}

        # Kuyruk orijinal yapıda: (istasyon, rota)
        kuyruk = deque([(baslangic, [baslangic])])

        # Her istasyon için minimum aktarma sayısını takip edecek sözlük
        min_aktarma = {baslangic: 0}

        while kuyruk:
            siradaki = kuyruk.popleft()
            mevcut_istasyon = siradaki[0]
            rota = siradaki[1]

            # Hedefe ulaşılırsa rotayı dön
            if mevcut_istasyon == hedef:
                return rota

            # Şu anki aktarma sayısını al
            suanki_aktarma = min_aktarma[mevcut_istasyon]

            for komsu, _ in mevcut_istasyon.komsular:
                # Hat değişikliği olup olmadığını kontrol et
                hat_degisti = (komsu.hat != mevcut_istasyon.hat)
                yeni_aktarma = suanki_aktarma + hat_degisti

                # Komşuyu ilk kez ziyaret ediyorsak veya daha az aktarma ile bulduysak
                if komsu not in ziyaret_edildi or yeni_aktarma < min_aktarma.get(komsu, float('inf')):
                    ziyaret_edildi.add(komsu)
                    min_aktarma[komsu] = yeni_aktarma
                    kuyruk.append((komsu, rota + [komsu]))

        # Rota bulunamadıysa None döndür
        return None

    # en az aktarmalı seçeneği değil, en az istasyon gezerek hedefe giden çözüm
    def en_az_aktarma_bul2(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """

        # Başlangıç ve hedef istasyonların var olup olmadığını kontrol et
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {baslangic}

        # Başlangıç ve hedef aynı ise, doğrudan dön
        if baslangic_id == hedef_id:
            return [baslangic]

        # Kuyruğa başlangıç istasyonunu ekliyoruz.
        # Başlangıç Kızılay ise, kuyruk = [(Kızılay, [Kızılay])] olur.
        # deque veri yapısında bir tuple saklıyoruz bu şekilde yaptığımızda. Kuyruktaki her eleman bir tuple oluyor.
        # Tuple'da saklanan ilk değer istasyon, ikinci değer ise istasyonlar listesi oluyor. İkinci değer olan istasyonlar listesini rota olarak düşünebiliriz.
        kuyruk = deque([(baslangic, [baslangic])])

        while kuyruk:
            # popleft fonksiyonu kuyruğun en başındaki elemanı döner, kuyruktaki elemanlar tuple olduğu için popleft ile dönen şey de bir tuple olacak.
            siradaki = kuyruk.popleft()

            # Mevcut istasyonu ve rotayı ayır
            mevcut_istasyon = siradaki[0]
            rota = siradaki[1]

            # Hedef istasyona ulaşıldığında rotayı döndür
            if mevcut_istasyon == hedef:
                return rota

            # Mevcut istasyonun tüm komşularını keşfet
            # normalde mevcut_istasyon.komsular geriye (komsu, süre) olarak dönüş yapar ama süre ile ilgilenmediğimiz için _ ile ignore ediyoruz bu değişkeni.
            for komsu, _ in mevcut_istasyon.komsular:
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    kuyruk.append((komsu, rota + [komsu]))

        # Hedef istasyona ulaşılamadıysa None döndür
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """

        # Başlangıç ve hedef istasyon var mı kontrol et
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {}

        # Öncelikli kuyruk oluştur (toplam_süre, id, istasyon, rota)
        pq = [(0, id(baslangic), baslangic, [baslangic])]

        while pq:
            # En düşük toplam süreye sahip rotayı kuyruktan al
            toplam_sure, _, mevcut_istasyon, rota = heapq.heappop(pq)

            # Eğer bu istasyonu daha önce ziyaret ettik ve daha kısa bir yol varsa, atla
            if mevcut_istasyon in ziyaret_edildi and ziyaret_edildi[mevcut_istasyon] <= toplam_sure:
                continue

            # İstasyonu ziyaret edildi olarak işaretle
            ziyaret_edildi[mevcut_istasyon] = toplam_sure

            # Hedefe ulaşıldıysa sonucu döndür
            if mevcut_istasyon == hedef:
                return (rota, toplam_sure)

            # Komşuları kontrol et
            for komsu_bilgisi in mevcut_istasyon.komsular:
                komsu = komsu_bilgisi[0]
                komsuya_sure = komsu_bilgisi[1]

                # Komşu daha önce ziyaret edilmemiş ya da daha hızlı bir rota bulunduysa
                if komsu not in ziyaret_edildi or toplam_sure + komsuya_sure < ziyaret_edildi[komsu]:
                    yeni_toplam_sure = toplam_sure + komsuya_sure
                    yeni_rota = rota + [komsu]
                    heapq.heappush(pq, (yeni_toplam_sure, id(komsu), komsu, yeni_rota))

        # Hedefe ulaşılamadıysa None döndür
        return None


# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB

    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar

    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören

    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    # Test senaryoları
    print("\n=== Test Senaryoları ===")

    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
