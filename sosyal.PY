import tkinter as tk
from tkinter import messagebox, ttk

class AntikDunyaArsivi:
    def __init__(self, root):
        self.root = root
        self.root.title("Antik Dünya Arşivi - Bilim ve Tarih Modu")
        self.root.geometry("800x900")
        self.root.configure(bg="#1a1a1d") 

        self.verileri_hazirla()
        self.arayuz_olustur()

    def verileri_hazirla(self):
        self.medeniyetler = {
            # --- ANADOLU ---
            "Hititler": {
                "kat": "Anadolu", "renk": "#950740",
                "detay": (
                    "SİYASİ YAPI: Bin Tanrılı İl. Pankuş Meclisi ve Tavananna (Kraliçe) yönetimi.\n\n"
                    "HUKUK: Kadeş Antlaşması ve Anal yıllıklar (Tarafsız tarih yazıcılığı).\n\n"
                    "ASKERİ: Savaş arabaları ve demir silah teknolojisi.\n\n"
                    "MİMARİ: UNESCO Dünya Mirası listesindeki başkent Hattuşaş and Yazılıkaya Açık Hava Tapınağı.\n\n"
                    "KÜLTÜR VE SANAT: Güneş Kursu simgesi, geyik ve boğa figürlü törensel içki kapları (Aslanlı Kapı).\n\n"
                    "DİNSEL TOLERANS: Fethettikleri her bölgenin tanrılarını kendi panteonlarına ekleyerek isyanları önlemişlerdir.\n\n"
                    "TOPLUMSAL YAPI: Kadınların mirastan pay alabildiği ve boşanma hakkına sahip olduğu gelişmiş medeni kanunlar.\n\n"
                    "COĞRAFİ ETKİ: Kızılırmak yayı (Kapadokya bölgesi) merkezli kurulup Suriye sınırlarına kadar genişleyen imparatorluk."
                )
            },
            "Frigler": {
                "kat": "Anadolu", "renk": "#4e4e50",
                "detay": (
                    "EKONOMİ: Tarım koruma yasaları (Saban kırmanın cezası ölüm). Tapates halıları.\n\n"
                    "EFSANE: Kral Midas, Eşek Kulaklar miti ve Gordion Düğümü.\n\n"
                    "MİMARİ: Kaya mezarları, anıtsal dini cepheler (Midas Anıtı) ve Tümülüsler (Yığma mezarlar).\n\n"
                    "EL SANATLARI: 'Fibula' adı verilen tarihin ilk çengelli iğneleri ve mobilyacılıkta kullanılan geçme tekniği.\n\n"
                    "MÜZİK VE KÜLTÜR: Flüt (Flauto) ve simbal gibi müzik aletlerinin icadı; Batı müziğini etkileyen Frig modu.\n\n"
                    "DİNSEL YAPI: Bereket ve doğa tanrıçası Kibele (Magna Mater) merkezli güçlü ana tanrıça kültü.\n\n"
                    "COĞRAFİ ETKİ: Sakarya Nehri havzası merkezli (Gordion/Ankara) kurulup Batı ve Orta Anadolu'ya yayılan egemenlik.\n\n"
                    "YAZI VE DİL: Hint-Avrupa dil ailesine mensup, henüz tamamen çözülememiş kendilerine özgü alfabetik yazı sistemi.\n\n"
                    "KAYNAK VE ARKEOLOJİ: Ankara yakınlarındaki Büyük Tümülüs (Midas Mezarı) içinden çıkarılan dünyanın en eski ahşap mobilya kalıntıları.\n\n"
                    "YIKILIŞ SÜRECİ: Kafkaslar üzerinden gelen göçebe Kimmer akınları sonucu başkent Gordion'un yağmalanmasıyla siyasi güçlerini kaybetmeleri."
                )
            },
            "Lidyalılar": {
                "kat": "Anadolu", "renk": "#c3073f",
                "detay": (
                    "EKONOMİ: Parayı icat eden medeniyet. Kral Yolu ticareti.\n\n"
                    "ORDU: Paralı askerlik sistemi (Yıkılışlarının temel sebebi).\n\n"
                    "BAŞKENT: Sard şehri ticaretin kalbiydi.\n\n"
                    "METALURJİ VE MADENCİLİK: Salihli yakınlarındaki Sart Çayı (Paktolos) yatağından çıkarılan elektrum (altın-gümüş alaşımı) madenini dünyada ilk kez saf altına dönüştürmeyi başarmışlardır.\n\n"
                    "KÜLTÜR VE KAST SİSTEMİ: Mezopotamya kültüründen etkilenmişlerdir. Toplum; soylular, tüccarlar, zanaatkarlar ve köleler olarak sınıflara ayrılmıştır.\n\n"
                    "MİMARİ VE ÖLÜ KÜLTÜ: Friglerden etkilenerek Tümülüs (yığma mezar) mimarisini geliştirmişlerdir. Başkent Sard yakınlarındaki Bintepeler bölgesi, Anadolu'nun en büyük tümülüs alanıdır.\n\n"
                    "DİNSEL SENKRETİZM: Anadolu kökenli Kibele kültüne inanmakla birlikte, zamanla Antik Yunan tanrıları Artemis, Apollo ve Zeus'u da benimsemişlerdir.\n\n"
                    "EFSANELER: Kral Karun (Kroisos) dönemindeki muazzam zenginlikleri, günümüzde 'Karun kadar zengin' deyimiyle dilimize yerleşmiştir.\n\n"
                    "YAZI VE DİL: Hint-Avrupa dil ailesine ait, kendilerine özgü Lidya alfabesini kullanmışlardır; bu yazı sistemi henüz tamamen çözülememiştir.\n\n"
                    "YIKILIŞ SÜRECİ: Pers İmparatoru Büyük Kiros'un M.Ö. 546 yılında Sard şehrini kuşatıp ele geçirmesiyle bağımsızlıklarını kaybetmişlerdir."
                )
            },
            "Urartular": {
                "kat": "Anadolu", "renk": "#6f2232",
                "detay": (
                    "MÜHENDİSLİK: Şamran Kanalı ve devasa su barajları. Yapılan su kanalları günümüzde bile hala işlevselliğini korumaktadır.\n\n"
                    "MADENCİLİK: Demir ve bronz işleme sanatı. 'Madenin Ustaları' olarak bilinirler; ürettikleri metal eşyaları Antik Yunanistan'a kadar ihraç etmişlerdir.\n\n"
                    "MİMARİ VE COĞRAFYA: Başkentleri Tuşpa (Van) merkezli kurulmuştur. Sarp kayalıklar üzerine inşa ettikleri kaleler ve devasa taş bloklardan oluşan surlar savunma dehalarını gösterir.\n\n"
                    "İNANIŞ VE YAŞAM: Oda mezarlar ve ölümden sonra yaşam inancı (Ahiret inancı). Ölülerini değerli eşyalarıyla birlikte gömerlerdi.\n\n"
                    "TARIM: Doğu Anadolu'nun zorlu coğrafyasında hayvancılık ve dağ yamaçlarında teraslama yöntemiyle bağcılık yapmışlardır.\n\n"
                    "YAZI VE DİL: Hem Asurlardan aldıkları çivi yazısını hem de kendi hiyeroglif (resim) yazılarını kullanmışlardır.\n\n"
                    "DİN VE SAVAŞ: En büyük tanrıları savaş tanrısı Haldi'dir. Krallar, seferleri ve zaferleri Haldi adına kayda geçirirdi.\n\n"
                    "YIKILIŞ: İskit ve Med akınları sonucunda zayıflayarak M.Ö. 6. yüzyılda tamamen tarih sahnesinden çekilmişlerdir."
                )
            },
            "İyonlar": {
                "kat": "Anadolu", "renk": "#2e1114",
                "detay": (
                    "BİLİM VE FELSEFE: Özgür düşünce ortamı sayesinde bilimsel düşüncenin temelleri burada atıldı.\n\n"
                    "DEV İSİMLER:\n"
                    "• TALES: Matematiğin ve felsefenin babası. İlk kez bir doğa olayını (güneş tutulması) önceden hesapladı.\n"
                    "• HEREDOT: 'Tarihin Babası' olarak bilinir; olayları hikayeleştirerek kayıt altına aldı.\n"
                    "• HİPOKRAT: Tıbbın kurucusudur; hastalıkların fiziksel nedenleri olduğunu savundu.\n"
                    "• PİSAGOR: Sayıların babası; kendi adıyla anılan ünlü geometri teoremini geliştirdi.\n\n"
                    "MİMARİ: Artemis Tapınağı (Dünyanın 7 Harikası'ndan biri).\n"
                    "YÖNETİM: Şehir devletleri (Polis) ve kolonicilik."
                )
            },
            # --- MEZOPOTAMYA ---
                       "Sümerler": {
                "kat": "Mezopotamya", "renk": "#4e4e50",
                "detay": (
                    "YAZI: Çivi yazısını bularak tarihi çağları (M.Ö. 3200) başlatan ilk medeniyettir.\n\n"
                    "BİLİM: Tekerleğin icadı, Ay yılı esaslı ilk takvim ve 60'lık (seksajisimal) sayı sistemi.\n\n"
                    "YAPI: Ziggurat adı verilen çok işlevli (tapınak, tahıl ambarı, okul ve rasathane) devasa kule tapınaklar.\n\n"
                    "HUKUK SİSTEMİ: Tarihin ilk yazılı kanunları olan 'Urkagina Kanunları'. Bu yasalarla ilk kez özel mülkiyet ve vatandaş hakları korunmuştur.\n\n"
                    "SİYASİ YAPI: Merkezi bir krallık yerine Ur, Uruk, Lagaş, Kiş gibi 'Site' adı verilen bağımsız şehir devletleri şeklinde yönetilmişlerdir.\n\n"
                    "YÖNETİM VE TEOKRASİ: Şehirlerin başında 'Patesi' veya 'Ensi' adı verilen rahip-krallar bulunurdu; en yüksek dini ve siyasi otorite onlardaydı.\n\n"
                    "EDEBİYAT VE MİTOLOJİ: Dünya edebiyat tarihinin ilk yazılı eserleri olan Gılgamış Destanı, Tufan Hikayesi ve Yaratılış Destanı'nın ilk nüshaları.\n\n"
                    "MATEMATİK VE GEOMETRİ: Dört işlemi bulmuşlar, daireyi 360 dereceye bölmüşler, yüzey ve hacim ölçüm hesaplamalarını başlatmışlardır.\n\n"
                    "TOPLUMSAL YAŞAM VE SINIFLAR: Halk; hürler, yarı hürler ve köleler olarak ayrılmış, tarım işçiliği ve zanaatkarlık ekonominin temelini oluşturmuştur.\n\n"
                    "YIKILIŞ SÜRECİ: Şehir devletlerinin kendi aralarındaki bitmek bilmeyen savaşlar nedeniyle zayıflayarak M.Ö. 2350'de Akadlar tarafından istila edilip yıkılmaları."
                )
            },

                        "Babiller": {
                "kat": "Mezopotamya", "renk": "#950740",
                "detay": (
                    "HUKUK: Hammurabi Kanunları (Kısasa kısas esasına dayalı ilk mutlak krallık yasaları).\n\n"
                    "MİMARİ: Babil'in Asma Bahçeleri (Dünyanın 7 Harikası'ndan biri) ve tanrı Marduk adına yapılan Babil Kulesi.\n\n"
                    "ASTRONOMİ: Burçların, yıldız haritalarının ve ay-güneş tutulması döngülerinin (Saros serisi) temeli.\n\n"
                    "SİYASİ YAPI: Gücünü ordudan alan dünyadaki ilk 'Mutlak Monarşi' ve merkezi devlet yönetim sistemi.\n\n"
                    "MATEMATİK VE GEOMETRİ: 60'lık sayı sistemini (Gelişmiş seksajisimal sistem) kullanarak bir saati 60 dakikaya, daireyi 360 dereceye bölmüşlerdir.\n\n"
                    "ŞEHİRCİLİK VE SANAT: Mavi sırlı tuğlalarla inşa edilen, üzerinde aslan ve boğa kabartmaları bulunan ikonik İştar Kapısı.\n\n"
                    "DİNSEL YAŞAM: Panteonun merkezinde yer alan baş tanrı Marduk kültü ve onun adına düzenlenen yeni yıl (Akitu) festivalleri.\n\n"
                    "EDEBİYAT: Sümerlerden devralıp genişlettikleri Gılgamış Destanı ve yaratılış miti olan Enuma Eliş tabletleri.\n\n"
                    "COĞRAFİ ETKİ: Fırat Nehri kıyısında (Bugünkü Irak/Bağdat yakınları) kurulup tüm Mezopotamya ve Suriye'ye yayılan imparatorluk sınırları.\n\n"
                    "YIKILIŞ SÜRECİ: M.Ö. 539 yılında Pers İmparatoru Büyük Kiros'un (Cyrus) Babil şehrini fethetmesiyle devletin tamamen ortadan kalkması."
                )
            },

                      "Asurlar": {
                "kat": "Mezopotamya", "renk": "#c3073f",
                "detay": (
                    "TİCARET: Anadolu'ya yazıyı getiren kavim (Kültepe/Kaniş). Karum adı verilen ticaret merkezleri.\n\n"
                    "KÜLTÜR: Dünyanın ilk kütüphanesi (Ninova Kütüphanesi - Binlerce çivi yazılı tablet).\n\n"
                    "ORDU: İlk süvari birlikleri, profesyonel daimi ordu ve demir silahlı kuşatma kuleleri.\n\n"
                    "SİYASİ YAPI VE EMPERYALİZM: Tarihin ilk büyük 'Merkezi İmparatorluk' modelini kurmuşlar, eyalet sistemini ve gelişmiş istihbarat/posta ağını geliştirmişlerdir.\n\n"
                    "HUKUK SİSTEMİ: Mezopotamya tarihinin en sert ve acımasız ceza kanunları. Yağma, sürgün ve işkence askeri bir devlet politikası olarak uygulanmıştır.\n\n"
                    "MİMARİ VE KABARTMA SANATI: Başkent Ninova ve Nemrud'daki devasa saraylar; saray duvarlarını süsleyen ve kralların aslan avlarını betimleyen yüksek nitelikli taş kabartmalar.\n\n"
                    "MİTOLOJİK KORUYUCULAR: Saray kapılarını koruması amacıyla inşa edilen 'Lamassu' adı verilen insan başlı, kanatlı boğa/aslan heykelleri.\n\n"
                    "EKONOMİK COĞRAFYA: Dicle Nehri kıyısında (Kuzey Irak / Musul) kurulup basiretli tüccarları sayesinde Mezopotamya ile Anadolu arasında köprü oluşturmuşlardır.\n\n"
                    "DİNSEL MERKEZ: Devletin adını da aldığı baş tanrı Aşur kültü. Krallar kendilerini tanrı Aşur'un dünyadaki temsilcisi ve rahipleri olarak görürdü.\n\n"
                    "YIKILIŞ SÜRECİ: Savaşçı politikalarının yarattığı nefrete karşı birleşen Babiller ve Medlerin ortak ittifakı sonucu M.Ö. 612 yılında Ninova'nın yakılmasıyla tarih sahnesinden çekilmişlerdir."
                )
            },

            # --- DÜNYA ---
            "Mısır": {
                "kat": "Dünya", "renk": "#6f2232",
                "detay": "BİLİM: Güneş takvimi, Tıp ve Mumyalama teknikleri.\nMİMARİ: Piramitler ve Hiyeroglif yazısı.\nYÖNETİM: Firavun adı verilen tanrı-krallar."
            },
            "Antik Yunan": {
                "kat": "Dünya", "renk": "#950740",
                "detay": "DEMOKRASİ: Halk meclisleri ve ilk demokrasi denemeleri.\nKÜLTÜR: Felsefe (Aristo, Platon) ve Olimpiyat oyunları.\nYÖNETİM: Şehir devletleri ve güçlü mitoloji."
            },
            "Roma İmparatorluğu": {
                "kat": "Dünya", "renk": "#c3073f",
                "detay": "HUKUK: 12 Levha Kanunları.\nMÜHENDİSLİK: Beton, su kemerleri ve binlerce kilometrelik Roma yolları.\nDİL: Latin alfabesi ve modern takvim sistemi."
            },
            "Antik Çin": {
                "kat": "Dünya", "renk": "#1a1a1d",
                "detay": "İCATLAR: Kağıt, matbaa, barut ve pusula.\nTİCARET: İpek Yolu ve dünya ticareti.\nMİMARİ: Çin Seddi."
            },
            "İnkalar": {
                "kat": "Dünya", "renk": "#4e4e50",
                "detay": "ADAPTASYON: Dağ tepelerinde taş şehirler (Machu Picchu).\nKAYIT: Quipu (Düğümlü iplerle veri tutma).\nTARIM: Teraslama yöntemi."
            },
            "Kartacalılar": {
                "kat": "Dünya", "renk": "#950740",
                "detay": "DENİZCİLİK: Akdeniz'in en güçlü donanması.\nASKERİ: Hannibal Barca'nın filleriyle Alpleri aşması.\nSON: Roma ile yapılan Pön Savaşları sonucu yıkılış."
            }
        }

    def detay_penceresi(self, isim):
        pencere = tk.Toplevel(self.root)
        pencere.title(f"Arşiv Kaydı: {isim}")
        pencere.geometry("600x600")
        pencere.configure(bg="#1a1a1d")

        v = self.medeniyetler[isim]
        tk.Frame(pencere, bg=v['renk'], height=15).pack(fill="x")
        tk.Label(pencere, text=isim.upper(), font=("Impact", 24), bg="#1a1a1d", fg="#ffffff").pack(pady=20)
        
        container = tk.Frame(pencere, bg="#1a1a1d")
        container.pack(fill="both", expand=True, padx=30, pady=10)
        
        txt = tk.Text(container, wrap="word", font=("Segoe UI", 12), bg="#222", fg="#ddd", 
                      padx=20, pady=20, bd=0)
        txt.insert("1.0", v['detay'])
        txt.configure(state="disabled")
        txt.pack(fill="both", expand=True)
        
        tk.Button(pencere, text="KAPAT", command=pencere.destroy, bg="#c3073f", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5).pack(pady=20)

    def arayuz_olustur(self):
        canvas = tk.Canvas(self.root, bg="#1a1a1d", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#1a1a1d")

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=760)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        tk.Label(scroll_frame, text="ANTİK DÜNYA ANSİKLOPEDİSİ", font=("Impact", 32), bg="#1a1a1d", fg="#c3073f").pack(pady=40)

        kategoriler = {
            "ANADOLU GÜÇLERİ": "Anadolu",
            "MEZOPOTAMYA MERKEZİ": "Mezopotamya",
            "KÜRESEL İMPARATORLUKLAR": "Dünya"
        }

        for baslik, anahtar in kategoriler.items():
            frame = tk.LabelFrame(scroll_frame, text=f" {baslik} ", font=("Arial", 14, "bold"), 
                                  bg="#1a1a1d", fg="#ffffff", padx=20, pady=20)
            frame.pack(fill="x", padx=60, pady=15)

            filtreli = [n for n, v in self.medeniyetler.items() if v['kat'] == anahtar]
            
            for medeniyet_ismi in filtreli:
                renk = self.medeniyetler[medeniyet_ismi]['renk']
                btn = tk.Button(
                    frame, 
                    text=medeniyet_ismi, 
                    command=lambda m=medeniyet_ismi: self.detay_penceresi(m),
                    bg=renk, 
                    fg="white", 
                    font=("Segoe UI", 11, "bold"),
                    activebackground="#ffffff",
                    activeforeground=renk,
                    cursor="hand2",
                    bd=0,
                    pady=8
                )
                btn.pack(fill="x", pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = AntikDunyaArsivi(root)
    root.mainloop()
