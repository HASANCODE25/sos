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
                "detay": "SİYASİ YAPI: Bin Tanrılı İl. Pankuş Meclisi ve Tavananna (Kraliçe) yönetimi.\nHUKUK: Kadeş Antlaşması ve Anal yıllıklar (Tarafsız tarih yazıcılığı).\nASKERİ: Savaş arabaları ve demir silah teknolojisi."
            },
            "Frigler": {
                "kat": "Anadolu", "renk": "#4e4e50",
                "detay": "EKONOMİ: Tarım koruma yasaları (Saban kırmanın cezası ölüm). Tapates halıları.\nEFSANE: Kral Midas ve Gordion Düğümü.\nMİMARİ: Kaya mezarları ve Tümülüsler."
            },
            "Lidyalılar": {
                "kat": "Anadolu", "renk": "#c3073f",
                "detay": "EKONOMİ: Parayı icat eden medeniyet. Kral Yolu ticareti.\nORDU: Paralı askerlik sistemi (Yıkılışlarının temel sebebi).\nBAŞKENT: Sard şehri ticaretin kalbiydi."
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
                "detay": "YAZI: Çivi yazısını bularak tarihi başlattılar.\nBİLİM: Tekerlek, Ay takvimi ve 60'lık sayı sistemi.\nYAPI: Zigguratlar (Tapınak, okul ve gözlemevi)."
            },
            "Babiller": {
                "kat": "Mezopotamya", "renk": "#950740",
                "detay": "HUKUK: Hammurabi Kanunları (Kısasa kısas).\nMİMARİ: Babil'in Asma Bahçeleri ve Babil Kulesi.\nASTRONOMİ: Burçların ve yıldız haritalarının temeli."
            },
            "Asurlar": {
                "kat": "Mezopotamya", "renk": "#c3073f",
                "detay": "TİCARET: Anadolu'ya yazıyı getiren kavim (Kültepe/Kaniş).\nKÜLTÜR: Dünyanın ilk kütüphanesi (Ninova).\nORDU: İlk süvari birlikleri ve profesyonel ordu."
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
