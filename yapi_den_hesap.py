from tkinter import *

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

window = Tk(screenName="Yapı Denetim Ücreti Hesaplama Programı")
window.title("Yapı Denetim Ücreti Hesaplama Programı")

window.resizable(False, False)

t1 = Label(window, text="Yapının inşaat alanı (m\u00b2):", font='SegoeUI 10 bold')
t1.grid(row=0, column=0)

t2 = Label(window, text="Sözleşme oranı (%):", font='SegoeUI 10 bold')
t2.grid(row=1, column=0)

t3 = Label(window, text="Yapı Sınıfları:", font='SegoeUI 10 bold')
t3.grid(row=2, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, width=30, borderwidth=3, font='SegoeUI 10 bold')
e1.grid(row=0, column=1)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value, width=30, borderwidth=3, font='SegoeUI 10 bold')
e2.insert(0, "1.43")
e2.grid(row=1, column=1)

text = Text(window, height=23, width=100, font='SegoeUI 11 bold')
ybar = Scrollbar(window, orient=VERTICAL)
ybar.config(command=text.yview)
text.config(yscrollcommand=ybar.set)
text.grid(row=3, column=0, columnspan=4)
ybar.grid(row=3, column=4, sticky="ns")



def yapi_siniflari_print():
        text.delete(1.0,END)
        text.insert(END, """
                        I. SINIF YAPILAR

                A GRUBU YAPILAR

        - Kâgir veya betonarme ihata duvarı (3 metre yüksekliğe kadar)
        - Basit kümes ve basit tarım yapıları
        - Plastik örtülü seralar
        - Mevcut yapılar arası bağlantı-geçiş yapıları
        - Geçici kullanımı olan küçük yapılar
        - Kalıcı kullanımı olan yardımcı yapılar
        - Gölgelikler-çardaklar
        - Üstü kapalı yanları açık dinlenme, oyun ve gösteri alanları
        - Depo amaçlı kayadan oyma yapılar
        - Bu gruptakilere benzer yapılar.

                B GRUBU YAPILAR

        - Cam örtülü seralar
        - Basit padok, büyük ve küçük baş hayvan ağılları
        - Kâgir ve betonarme su depoları
        - İş yeri depoları
        - Bu gruptakilere benzer yapılar.



                        II. SINIF YAPILAR

                A GRUBU YAPILAR

        - Kuleler, ayaklı su depoları
        - Palplanj ve ankrajlı perde ve istinat duvarları
        - Kayıkhane
        - Bu gruptakilere benzer yapılar.

                B GRUBU YAPILAR

        - Şişirme (Pnömatik) yapılar
        - Tek katlı ofisler, dükkân ve basit atölyeler
        - Semt sahaları, küçük semt parkları, çocuk oyun alanları ve eklentileri
        - Tarımsal endüstri yapıları (Tek katlı, prefabrik beton, betonarme veya çelik depo ve atölyeler, tesisat
 ağırlıklı ağıllar, fidan yetiştirme ve bekletme tesisleri)
        - Yat bakım ve onarım atölyeleri, çekek yerleri
        - Jeoloji, botanik ve tema parkları
        - Mezbahalar
        - Bu gruptakilere benzer yapılar.

                C GRUBU YAPILAR
                
        - Hangar yapıları (Uçak bakım ve onarım amaçlı)
        - Sanayi yapıları (Tek katlı, bodrum ve asma katı da olabilen prefabrik beton,
 betonarme ve çelik yapılar) 
        - Bu gruptakilere benzer yapılar.



                        III. SINIF YAPILAR

                A  GRUBU YAPILAR

        - Okul ve mahalle spor tesisleri (Temel eğitim okullarının veya işletme ve tesislerin spor salonları,
 jimnastik salonları, semt salonları)
        - Katlı garajlar
        - Ticari amaçlı binalar (üç kata kadar üç kat dâhil – asansörsüz- 2/11/1985 tarihli ve 18916 mükerrer sayılı 
 Resmi Gazete’de yayımlanan Planlı Alanlar Tip İmar Yönetmeliğinin 45. maddesine göre asansör yeri bırakılacak)
        - Alışveriş merkezleri (semt pazarları, küçük ve büyük hal binaları, marketler, v.b.)
        - Basımevleri, matbaalar
        - Soğuk hava depoları
        - Konutlar (üç kata kadar- üç kat dâhil- asansörsüz – 2/11/1985 tarihli ve 18916 mükerrer sayılı Resmi
 Gazete’de yayımlanan Planlı Alanlar Tip İmar Yönetmeliğinin 45. maddesine göre asansör yeri bırakılacak) 
        - Akaryakıt ve gaz istasyonları
        - Kampingler
        - Küçük sanayi tesisleri (Donanımlı atölyeler, imalathane, dökümhane)
        - Semt postaneleri
        - Kreş ve Gündüz bakımevleri, Hobi ve Oyun salonları
        - Bu gruptakilere benzer yapılar.

                B GRUBU YAPILAR

        - Entegre tarımsal endüstri yapıları, Büyük çiftlik yapıları
        - Gençlik Merkezleri, Halk evleri
        - Lokanta, kafeterya ve yemekhaneler
        - Temel eğitim okulları
        - Küçük kitaplık ve benzeri kültür tesisleri
        - Jandarma ve emniyet karakol binaları
        - Sağlık ocakları, kamu sağlık dispanserleri
        - Ticari amaçlı binalar (Yapı yüksekliği 21,50 m’ye kadar olan)
        - 150 kişiye kadar cezaevleri
        - Fuarlar
        - Sergi salonları
        - Konutlar (Yapı yüksekliği 21,50 m’den az yapılar)
        - Marinalar
        - Gece kulübü, diskotekler
        - Misafirhaneler, Pansiyonlar
        - Bu gruptakilere benzer yapılar.



                        IV. SINIF YAPILAR

                A  GRUBU YAPILAR

        - Özelliği olan büyük okul yapıları (Spor salonu, konferans salonu ve ek tesisleri olan eğitim yapıları)
        - Poliklinikler
        - Liman binaları
        - İdari binalar (ilçe tipi hükümet konakları, vergi daireleri, vb.)
        - İlçe Belediyeleri
        - 150 kişiyi geçen cezaevleri
        - Kaplıcalar, şifa evleri vb. termal tesisleri
        - İbadethaneler (1500 kişiye kadar)
        - Entegre sanayi tesisleri
        - Aqua parklar
        - Müstakil spor köyleri (Yüzme havuzları, spor salonları ve statları bulunan)
        - Yaşlılar Huzurevi, kimsesiz çocuk yuvaları, yetiştirme yurtları
        - Büyük alışveriş merkezleri
        - Yüksekokullar ve eğitim enstitüleri
        - Apartman tipi konutlar (Yapı yüksekliği 30,50 m.’den az yapılar)
        - Oteller (1 ve 2 yıldızlı)
        - Bu gruptakilere benzer yapılar.

                B GRUBU YAPILAR

        - Araştırma binaları, laboratuvarlar ve sağlık merkezleri
        - İl tipi belediyeler
        - İl tipi idari kamu binaları
        - Metro istasyonları
        - Stadyum, spor salonları ve yüzme havuzları
        - Büyük postaneler (merkez postaneleri)
        - Otobüs terminalleri
        - Eğlence amaçlı yapılar (çok amaçlı toplantı, eğlence ve düğün salonları)
        - Banka binaları
        - Normal radyo ve televizyon binaları
        - Özelliği olan genel sığınaklar
        - Müstakil veya ikiz konutlar (Bağımsız bölüm brüt alanı 151 m2 ~ 600 m2 villalar, teras evleri, dağ evleri,
 kaymakam evi vb.)
        - Bu gruptakilere benzer yapılar.

                C GRUBU YAPILAR

        - Büyük kütüphaneler ve kültür yapıları
        - Bakanlık binaları
        - Yüksek öğrenim yurtları
        - Arşiv binaları
        - Radyoaktif korumalı depolar
        - Büyük Adliye Sarayları
        - Otel (3 yıldızlı) ve moteller
        - Rehabilitasyon ve tedavi merkezleri
        - İl tipi hükümet konakları ve büyükşehir belediye binaları
        - İş merkezleri (Yapı yüksekliği 21,50 m ile 30,50 m arası -30,50 m dâhil yapılar)
        - Konutlar (Yapı yüksekliği 30,50 m ile 51,50 m arası -51,50 m dâhil yapılar)
        - Bu gruptakilere benzer yapılar.



                        V. SINIF YAPILAR

                A GRUBU YAPILAR

        - Televizyon, Radyo İstasyonları, binaları
        - Orduevleri
        - Büyükelçilik yapıları, vali konakları ve brüt alanı 600 m2 üzerindeki özel konutlar
        - Borsa binaları
        - Üniversite kampüsleri
        - İş merkezleri (Yapı yüksekliği 30,50 m aşan yapılar)
        - Yapı yüksekliği 51,50 metreyi aşan yapılar
        - Alışveriş kompleksleri (İçerisinde sinema, tiyatro, sergi salonu, kafe, restoran, market, v.b. bulunan) 
        - Bu gruptakilere benzer yapılar.

                B GRUBU YAPILAR

        - Kongre merkezleri
        - Olimpik spor tesisleri – hipodromlar
        - Bilimsel araştırma merkezleri, AR-GE binaları
        - Hastaneler
        - Havalimanları
        - İbadethaneler  (1500 kişinin üzerinde)
        - Oteller (4 yıldızlı)
        - Bu gruptakilere benzer yapılar.

                C GRUBU YAPILAR

        - Oteller ve tatil köyleri (5 yıldızlı)
        - Müze ve kütüphane kompleksleri
        - Bu gruptakilere benzer yapılar.

                D GRUBU YAPILAR

        - Opera, tiyatro ve bale yapıları, konser salonları ve kompleksleri
        - Tarihi eser niteliğinde olup restore edilerek veya yıkılarak aslına uygun olarak yapılan yapılar
        - Bu gruptakilere benzer yapılar.
 """)

def hesap(birim_fiyat):
    try:
        text.delete(1.0,END)
        insaat_maliyeti = float(e1_value.get()) * birim_fiyat
        if var1.get() == 1:
            den_ucreti = float(e1_value.get()) * float(e2_value.get()) / 100 * birim_fiyat * 0.65
        else:
            den_ucreti = float(e1_value.get()) * float(e2_value.get()) / 100 * birim_fiyat
        if var2.get() == 1:
            kdv = 0.18 * den_ucreti * 0.10
        else:
            kdv = 0.18 * den_ucreti
        toplam_den_ucreti = den_ucreti + kdv
        text.insert(END, "\n Yapının inşaat maliyeti = " + f"{round(insaat_maliyeti, 2):,}" + " TL")
        text.insert(END, "\n Yapı denetim ücreti = " + f"{round(den_ucreti, 2):,}" + " TL")
        text.insert(END, "\n KDV = " + f"{round(kdv, 2):,}" + " TL")
        text.insert(END, "\n\n Toplam yapı denetim ücreti = " + f"{round(toplam_den_ucreti, 2):,}" + " TL")
        text.insert(END, "\n\n\n Ruhsat alındıktan sonra yapılacak hakediş(%10) = " + f"{round(toplam_den_ucreti*0.1, 2):,}" + " TL")
        text.insert(END, "\n\n Yapı subasman seviyesine geldikten sonra yapılacak hakediş(%10) = " + f"{round(toplam_den_ucreti*0.1, 2):,}" + " TL")
        text.insert(END, "\n\n Taşıyıcı sistem tamamlandıktan sonra yapılacak hakediş(%40) = " + f"{round(toplam_den_ucreti*0.4, 2):,}" + " TL")
        text.insert(END, """\n\n Çatı örtüsü, dolgu duvarları, kapı ve pencere kasaları, tesisat alt yapısı dâhil 
 yapı sıvaya hazır duruma getirildikten sonra yapılacak hakediş(%20) = """ + f"{round(toplam_den_ucreti*0.2, 2):,}" + " TL")
        text.insert(END, """\n\n Mekanik ve elektrik tesisat ile kalan yapı bölümü tamamlandıktan sonra yapılacak
 hakediş(%15) = """ + f"{round(toplam_den_ucreti*0.15, 2):,}" + " TL")
        text.insert(END, """\n\n İş bitirme tutanağının ilgili idare tarafından onaylanması sonrası yapılacak 
 hakediş(%5) = """ + f"{round(toplam_den_ucreti*0.05, 2):,}" + " TL")
    except ValueError:
        text.delete(1.0,END)
        text.insert(END, """\n Yapının inşaat alanını ve sözleşme oranını doğru girdiğinizden emin olun.
 Program nokta ile çalışmaktadır. Sayıları girerken virgül kullanmayın.""")

var1 = IntVar()
Checkbutton(window, text="OSB", variable=var1).grid(row=0, column=3, sticky=W)

var2 = IntVar()
Checkbutton(window, text="Tevkifatlı Fatura", variable=var2).grid(row=1, column=3, sticky=W)

b1 = Button(window, text="1A, 1B, 2A, 2B", width=25, command=lambda: hesap(537), font='SegoeUI 10 bold')
b1.grid(row=2, column=1)
b2 = Button(window, text="3A, 3B", width=25, command=lambda: hesap(1305), font='SegoeUI 10 bold')
b2.grid(row=2, column=2)
b3 = Button(window, text="4A, 4B, 4C, 5A, 5B, 5C, 5D", width=25, command=lambda: hesap(2588), font='SegoeUI 10 bold')
b3.grid(row=2, column=3)
b4 = Button(window, text="Yapı sınıfını bilmiyorsanız\n buraya tıklayın.",
 width=20, command=lambda: yapi_siniflari_print(), font='SegoeUI 10 bold')
b4.grid(row=0, column=2)


window.mainloop()
