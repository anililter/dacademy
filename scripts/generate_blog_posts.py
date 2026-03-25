#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 40 blog post HTML files and update blog.html with new cards."""

import os

BLOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'blog')
POSTS = [
    # Boks (1-10)
    ("golge-boksu", "Gölge Boksu: Neden Her Antrenmanın Kalbidir?", "Boks & Teknik",
     "Gölge boksu tekniği, koordinasyon ve kondisyon için neden vazgeçilmez? Nasıl çalışılır?", "photo-1549719386-74dfcbf7dbed",
     "Gölge boksu, rakipsiz çalışarak yumruk tekniği, ayak hareketi ve gardı bir arada geliştirdiğiniz temel antrenmandır. Her antrenmanın başında veya ısınma sonrası 3–5 tur gölge boksu yapmak, hem zihinsel hem fiziksel hazırlık sağlar. Aynada veya videoda kendinizi izleyerek açılarınızı ve toparlanmayı düzeltebilirsiniz. d.academy’de bire bir çalışmada antrenör bu hareketi adım adım şekillendirir.",
     [("Neden Gölge Boksu?", "Rakip olmadan tekniğe odaklanırsınız; hata yapma lüksünüz vardır. Kombinasyonlar, mesafe ve tempo gölge boksuyla içselleştirilir."), ("Nasıl Çalışılır?", "Gardı koruyarak jab, cross, hook ve ayak kaymalarını birleştirin. Tur süreleri 2–3 dakika, dinlenme 1 dakika olabilir. Nefes ve rahatlık öncelikli olsun.")]),
    ("bandaj-sarma", "Bandaj Sarma Sanatı: Elleri Sakatlıktan Korumanın Püf Noktaları", "Boks & Teknik",
     "Boks bandajı nasıl sarılır? Parmak, bilek ve el eklemlerini koruma rehberi.", "photo-1599058917212-d750089bc07e",
     "Bandaj sarma, yumruk atarken el ve bileği destekleyerek kırık ve burkulma riskini azaltır. Doğru sarma tekniği öğrenmek her boksör için zorunludur.",
     [("Neden Bandaj?", "El kemikleri ve bilek eklemi tekrarlayan darbelere maruz kalır. Bandaj bu yükü dağıtır ve eklemi sabitler."), ("Temel Sarma", "Parmak araları ve bilek çevresi sıkıca sarılmalı; avuç içi ve parmak uçları açık kalmalı. 3–4 m bandaj çoğu el için yeterlidir.")]),
    ("kum-torbasi", "Kum Torbası Antrenmanı: Sadece Vurmak Yetmez, Nasıl Çalışmalısın?", "Boks & Teknik",
     "Kum torbası antrenmanı: güç, tempo ve kombinasyon. Doğru çalışma yöntemleri.", "photo-1549719386-74dfcbf7dbed",
     "Kum torbası güç ve dayanıklılık geliştirir; ancak rastgele vurmak yerine turlar, kombinasyonlar ve mesafe çalışması yapmak gerekir.",
     [("Turlar ve Süre", "2–3 dakikalık turlar, 1 dakika dinlenme. Ağır vuruş turları, hız turları ve kombinasyon turları ayrı planlanabilir."), ("Teknik Öncelik", "Gardı koruyun, vuruştan sonra toparlanın. Torbaya çok yaklaşmadan mesafe hissini koruyun. Antrenör eşliğinde hata düzeltmesi çok değerlidir.")]),
    ("eskiv-defans", "Eskiv ve Defans: Yumruklardan Kaçmanın 5 Temel Yolu", "Boks & Teknik",
     "Boks defansı: slipping, block, parry, roll ve step. Yumruklardan kaçma teknikleri.", "photo-1551698618-1dfe5d97d256",
     "Eskiv (slipping), blok, parry, roll ve adım atma; rakibin yumruğundan kaçmanın veya savuşturmanın temel yollarıdır. Her biri farklı açı ve mesafede kullanılır.",
     [("Slipping (Kayma)", "Başı hafif yana veya geriye kaydırarak yumruğu ıskalattırmak. Boyun ve omuz esnekliği gerekir."), ("Block ve Parry", "Blok yumruğu el veya dirsekle kapatmak; parry ise yumruğun yönünü hafifçe saptırmaktır. İkisi de gardı bozmadan yapılmalı.")]),
    ("ip-atlama", "İp Atlamanın İncelikleri: Boksörler Neden Saatlerce İp Atlar?", "Boks & Teknik",
     "İp atlama boksçularda ayak hızı, koordinasyon ve kondisyon. Nasıl başlanır?", "photo-1571019613454-1cb2f99b2d8b",
     "İp atlama, ayak çevikliği, ritim ve kardiyovasküler dayanıklılık için boks antrenmanının temelidir. Düzenli çalışma bacakları hafif ve hazır tutar.",
     [("Faydaları", "Ayak hızı, denge ve koordinasyon artar. Kalp atımı yükselir, antrenman öncesi ısınma veya sonrası soğuma olarak kullanılabilir."), ("Temel Teknik", "Bileklerden döndürün, zıplama yüksekliği az olsun. Tek ayak, çift ayak ve alternatif varyasyonlarla süreyi kademeli artırın.")]),
    ("kontra-atak", "Kontra Atak Rehberi: Rakibi Beklemediği Anda Yakalamak", "Boks & Teknik",
     "Boks kontra atak: rakibin açığını görme ve anında karşılık verme.", "photo-1549719386-74dfcbf7dbed",
     "Kontra atak, rakibin vuruşundan hemen sonra veya açık verdiği anı kullanarak karşı yumruk atmaktır. Savunma ve saldırı aynı anda düşünülür.",
     [("Zamanlama", "Rakip yumruk atarken veya toparlanırken açık verir. Slip veya block sonrası hemen karşı vuruş (cross veya hook) devreye girer."), ("Antrenman", "Partner veya antrenörle kontra atak drill’leri yapılır. Önce yavaş tempo, sonra hız artırılır. Refleks ve karar hızı gelişir.")]),
    ("mesafe-kontrolu", "Mesafe Kontrolü: Ringde Alanı Nasıl Yönetirsin?", "Boks & Teknik",
     "Boksta mesafe kontrolü: uzak, orta ve yakın mesafe. Alan yönetimi ve footwork.", "photo-1599058917212-d750089bc07e",
     "Ringde kim alanı kontrol ederse genelde üstün olur. Uzak, orta ve yakın mesafe farklı teknik ve taktik gerektirir; ayaklar ve jab bu kontrolü sağlar.",
     [("Uzak Mesafe", "Jab ve uzun vuruşlarla rakibi uzak tutun. İleri-geri adımlarla mesafeyi siz belirleyin."), ("Orta ve Yakın", "Orta mesafede cross ve hook devreye girer; yakın mesafede klinç veya kısa hook. Her mesafede gard ve denge korunmalı.")]),
    ("kilinc-teknikleri", "Klinç (Clinch) Teknikleri: Yakın Dövüşte Kontrolü Ele Al", "Boks & Teknik",
     "Boks klinç: yakın mesafede tutunma, yönlendirme ve ayrılma. Temel klinç teknikleri.", "photo-1551698618-1dfe5d97d256",
     "Klinç, rakiple yakın temasta kolları kilitleyerek hem dinlenme hem kontrol sağlar. Doğru kullanımda hakem ayrılmadan önce nefes toplar ve pozisyon alırsınız.",
     [("Neden Klinç?", "Yorulduğunuzda veya rakibin kombinasyonlarına kapıldığınızda klinç ile tempo düşer. Ayrıca rakibi köşeye veya ipe doğru yönlendirebilirsiniz."), ("Temel Kurallar", "Kolları rakibin kollarının üstünde tutun; başınız rakibin omzuna yakın, çene içeride. Yumruk atarken serbest kalacak şekilde ayrılın.")]),
    ("boyun-egzersizleri", "Boksörler İçin Boyun Egzersizleri: Darbe Direncini Artırmak", "Boks & Teknik",
     "Boyun güçlendirme boks: darbe emilimi ve sakatlık önleme. Güvenli boyun egzersizleri.", "photo-1571019614242-c5c5dee9f50b",
     "Güçlü boyun kasları, kafanın ani hareketini ve sarsıntıyı azaltarak sakatlık riskini düşürür. Ağırlık veya direnç bandı ile kontrollü çalışma yapılmalıdır.",
     [("Neden Önemli?", "Darbe geldiğinde boyun ne kadar stabilse beyin sarsıntısı o kadar azalır. Boyun kasları bu stabiliteyi sağlar."), ("Örnek Hareketler", "Boyun fleksiyon/ekstansiyon (öne-arkaya), yan eğmeler ve izometrik basınç. Ağırlık çok hafif başlanır; antrenör eşliğinde ilerlenir.")]),
    ("mac-oncesi-psikoloji", "Maç Öncesi Psikoloji: Ring Korkusunu Nasıl Yenersin?", "Boks & Teknik",
     "Maç öncesi stres ve ring korkusu. Nefes, odaklanma ve hazırlık ipuçları.", "photo-1549719386-74dfcbf7dbed",
     "Ringe çıkmadan önce heyecan ve korku normaldir. Nefes teknikleri, rutinler ve zihinsel prova bu duyguyu yönetmenize yardım eder.",
     [("Nefes ve Rutin", "Derin nefes alıp yavaşça vermek kalp atımını düşürür. Aynı ısınma ve giyinme sırası her maçta tekrarlanırsa zihin rahatlar."), ("Zihinsel Prova", "Ringde rakip karşınızda ne yapacağınızı gözünüzde canlandırın. İlk jab, defans ve kontra atak senaryoları zihinsel antrenman olur.")]),
    # Antrenman (11-20)
    ("hiit-antrenmanlari", "HIIT Antrenmanları: Kısa Sürede Maksimum Yağ Yakımı", "Antrenman Bilimi",
     "HIIT nedir, nasıl yapılır? Yüksek yoğunluklu interval antrenman rehberi.", "photo-1517836357463-d25dfeac3438",
     "HIIT (yüksek yoğunluklu interval antrenman), kısa süreli yoğun çalışma ve dinlenme aralıklarıyla hem yağ yakımını hem kondisyonu artırır. 20–30 dakika bile etkili olabilir.",
     [("HIIT Nasıl Çalışır?", "Yoğun fazda kalp atımı ve metabolizma zirveye çıkar; dinlenme fazında toparlanırsınız. EPOC (antrenman sonrası kalori harcaması) artar."), ("Örnek Yapı", "30 saniye sprint veya burpee, 30 saniye yürüme; 8–10 tekrar. Isınma ve soğuma mutlaka ekleyin. Kronik rahatsızlığı olanlar doktora danışmalı.")]),
    ("bolgesel-zayiflama", "Bölgesel Zayıflama Yalanı: Neden Sadece Göbekten Kilo Veremezsin?", "Antrenman Bilimi",
     "Spot reduction neden işe yaramaz? Yağ kaybı vücutta nasıl dağılır?", "photo-1571019614242-c5c5dee9f50b",
     "Bilim, belirli bir bölgeden (örneğin sadece göbek) yağ yakımının mümkün olmadığını gösteriyor. Yağ kaybı genelde tüm vücutta, genetik ve hormonlara göre dağılır.",
     [("Spot Reduction Nedir?", "Sadece o bölgeye yönelik hareket yaparak oradan yağ eritmek anlamına gelir. Maalesef vücut yağı bölgesel olarak seçerek yakmaz."), ("Ne Yapmalı?", "Kalori açığı + kuvvet antrenmanı + sabır. Göbek bölgesi çoğu kişide en geç incilen yer olabilir; süreklilik önemli.")]),
    ("plateau-donemi", "Plateau (Duraklama) Dönemi: Gelişimin Durduğunda Ne Yapmalısın?", "Antrenman Bilimi",
     "Antrenmanda plateau neden olur? Ağırlık ve performans takılı kaldığında çözümler.", "photo-1534438327276-14e5300c3a48",
     "Plateau, ilerlemenin geçici olarak durduğu dönemdir. Yükü, hacmi veya türü değiştirmek, beslenme ve uykuyu gözden geçirmek genelde çözüm sağlar.",
     [("Neden Takılırız?", "Vücut aynı uyarana alışır; ayrıca uyku, beslenme veya aşırı antrenman da ilerlemeyi durdurabilir."), ("Çözümler", "Progresyonu artırın (ağırlık, tekrar, set). Programı değiştirin (split, full body, yeni hareketler). Deload haftası ve yeterli uyku deneyin.")]),
    ("evde-ekipmansiz", "Evde Ekipmansız Antrenman: Kendi Vücut Ağırlığınla Sınırları Zorla", "Antrenman Bilimi",
     "Ekipmansız ev antrenmanı: push-up, squat, plank ve daha fazlası. Program örnekleri.", "photo-1541534741688-6078c6bfb5c5",
     "Vücut ağırlığı antrenmanı, ekipman olmadan kuvvet ve kondisyon geliştirmenizi sağlar. Doğru progresyonla evde ciddi ilerleme kaydedilir.",
     [("Temel Hareketler", "Push-up, squat, lunge, plank, mountain climber, burpee. Zorlaştırmak için tek bacak/kol, yavaş tempo veya pause kullanın."), ("Program", "Haftada 3–4 gün, 30–45 dakika. Isınma ve soğuma unutulmamalı. Bire bir online veya yüz yüze plan için antrenör desteği alabilirsiniz.")]),
    ("esneklik", "Esnekliğin Önemi: Kas Sertliği ile Nasıl Başa Çıkılır?", "Antrenman Bilimi",
     "Esneklik ve mobilite antrenmanı. Germe, foam roll ve hareket açıklığı.", "photo-1544367567-0f2fcb009e0b",
     "Esneklik ve mobilite, hem sakatlık riskini azaltır hem de hareket kalitesini artırır. Antrenman öncesi dinamik, sonrası statik germe mantıklıdır.",
     [("Neden Önemli?", "Sert kaslar hareketi kısıtlar ve ağrıya yol açabilir. Özellikle kalça, bel ve omuz bölgesi masa başı çalışanlarda sıkıdır."), ("Ne Yapmalı?", "Isınmada dinamik germe (leg swing, arm circle). Soğumada 20–30 saniye statik germe. Foam roll kasları yumuşatmak için eklenebilir.")]),
    ("full-body-split", "Full Body vs. Split: Hangi Program Senin İçin Daha Uygun?", "Antrenman Bilimi",
     "Full body ve split program farkı. Haftalık antrenman sıklığına göre seçim.", "photo-1517836357463-d25dfeac3438",
     "Full body her günde tüm vücudu çalıştırır; split (upper/lower veya push/pull/legs) ise günlere bölünmüş grupları hedefler. Hedef ve haftalık gün sayısına göre seçim yapılır.",
     [("Full Body", "Haftada 3 gün ideal. Her seansta bileşik hareketlerle tüm vücut uyarılır. Yeni başlayanlar ve zamanı kısıtlı olanlar için uygundur."), ("Split", "Haftada 4–5 gün antrenman yapanlar için. Her kas grubuna daha fazla hacim ve toparlanma süresi verilir. İleri seviye için mantıklıdır.")]),
    ("core-gucu", "Core Bölgesinin Gücü: Karın Kasından Fazlası Neden Gerekli?", "Antrenman Bilimi",
     "Core antrenmanı: karın, bel ve kalça stabilitesi. Plank, dead bug ve daha fazlası.", "photo-1517836357463-d25dfeac3438",
     "Core sadece karın değil; bel, kalça ve pelvisi de kapsar. Güç ve stabilite, hem günlük hareketlerde hem spor performansında kritiktir.",
     [("Core Neyi Kapsar?", "Rectus abdominis, obliques, transversus abdominis, bel kasları ve kalça stabilizatörleri. Hepsi birlikte gövdeyi sabit tutar."), ("Temel Çalışmalar", "Plank, dead bug, bird dog, pallof press. Ağırlık kaldırırken (squat, deadlift) core zaten devreye girer; ek izole çalışma dengeyi artırır.")]),
    ("sakatliktan-korunma", "Sakatlıktan Korunma: Isınma ve Soğuma Hareketlerinin Altın Kuralları", "Antrenman Bilimi",
     "Isınma ve soğuma neden şart? Sakatlık önleme rehberi.", "photo-1571019614242-c5c5dee9f50b",
     "Isınma kas ve eklemleri hazırlar; soğuma nabzı düşürür ve esnekliği korur. İkisi de sakatlık riskini azaltır ve toparlanmayı hızlandırır.",
     [("Isınma", "5–10 dakika hafif kardiyo (koşu, kürek) + dinamik germe. Yapacağınız hareketlere benzer hareketler (squat, lunge) ekleyin."), ("Soğuma", "5–10 dakika hafif yürüyüş veya pedal + statik germe. Nabız yavaşça düşer, kaslar uzar.")]),
    ("yas-aldikca-spor", "Yaş Aldıkça Spor: 30'lu ve 40'lı Yaşlarda Antrenman Nasıl Değişmeli?", "Antrenman Bilimi",
     "30 ve 40'lı yaşlarda antrenman: toparlanma, mobilite ve kuvvet koruma.", "photo-1534438327276-14e5300c3a48",
     "Yaş ilerledikçe toparlanma süresi uzar, mobilite ve hormonlar değişir. Antrenman yoğunluğu ve sıklığı buna göre ayarlanmalı; kuvvet ve hareket kalitesi ön planda tutulmalıdır.",
     [("Ne Değişir?", "Toparlanma yavaşlar, sakatlık riski artar. Testosteron ve büyüme hormonu düşebilir. Esneklik ve ısınma daha da önem kazanır."), ("Öneriler", "Isınma ve soğumayı atlamayın. Haftada 2–3 kuvvet, 1–2 kardiyo/mobilite yeterli olabilir. Uyku ve beslenme kritiktir. Bire bir antrenörle kişiye özel plan alın.")]),
    ("postur-bozukluklari", "Postür (Duruş) Bozuklukları: Masa Başı Çalışanlar İçin Düzeltici Egzersizler", "Antrenman Bilimi",
     "Kambur, öne eğik baş, omuz düşüklüğü. Düzeltici egzersiz ve mobilite.", "photo-1544367567-0f2fcb009e0b",
     "Masa başı çalışma öne eğik postür, kambur ve omuz ağrısına yol açar. Germe ve güçlendirme ile denge kurulabilir.",
     [("Yaygın Sorunlar", "Baş öne, omuzlar içe, göğüs kafesi kapalı. Bel ve kalça fleksörleri kısa, sırt ve kalça ekstansörleri zayıf olabilir."), ("Çözümler", "Göğüs ve kalça fleksörü germe; sırt (row, face pull) ve core güçlendirme. Monitör göz hizasında, sandalye ve masa ergonomisi düzeltilmeli.")]),
    # Beslenme (21-30)
    ("protein-tozu", "Protein Tozları: Gerçekten İhtiyacın Var mı?", "Beslenme & Takviyeler",
     "Protein tozu ne zaman gerekli? Günlük protein ihtiyacı ve besinlerle karşılama.", "photo-1546069901-ba9599a7e63c",
     "Protein tozu bir zorunluluk değildir; günlük proteini yemeklerle alamıyorsanız veya pratiklik istiyorsanız takviye kullanılabilir. Önce besinlerle hedefi tutturmaya çalışın.",
     [("Kimler Kullanabilir?", "Yoğun antrenman yapan, ihtiyacı yüksek (1,6–2 g/kg) olan ve öğünlerde yeterli protein alamayanlar. Vejetaryen/veganlar da sıklıkla kullanır."), ("Nasıl Kullanılır?", "Antrenman sonrası veya öğün arası. Süt/su ile karıştırılır. Kalori ve makro hedefinize göre porsiyon ayarlayın; aşırı tüketmek gereksizdir.")]),
    ("kreatin-rehberi", "Kreatin Rehberi: Güç ve Performans Artışı İçin Nasıl Kullanılır?", "Beslenme & Takviyeler",
     "Kreatin nedir, dozu ve yükleme. Bilimsel olarak kanıtlanmış takviye.", "photo-1593095948071-474c5cc2989d",
     "Kreatin, kısa süreli yüksek yoğunluklu performansı ve kuvveti artıran, iyi çalışılmış bir takviyedir. Günde 3–5 g yeterlidir; yükleme isteğe bağlıdır.",
     [("Ne İşe Yarar?", "Kas hücresinde fosfokreatin depolarını doldurur; ATP yenilenmesi hızlanır. Setler arası toparlanma ve tekrar sayısı artabilir."), ("Kullanım", "Günde 3–5 g monohidrat. Yükleme (5 g x 4, 5–7 gün) isteğe bağlı. Su tutulumu yapabilir; böbrek hastalığı varsa doktora danışın.")]),
    ("pre-workout-beslenme", "Antrenman Öncesi (Pre-Workout) Beslenme: Enerji Patlaması İçin Ne Yemeli?", "Beslenme & Takviyeler",
     "Antrenman öncesi yemek: zamanlama, karbonhidrat ve protein. Pre-workout önerileri.", "photo-1546069901-ba9599a7e63c",
     "Antrenmandan 1–2 saat önce karbonhidrat + hafif protein enerji ve performansı destekler. Çok yakın yersen mide rahatsızlığı olabilir.",
     [("Zamanlama", "Büyük öğün 2–3 saat, atıştırmalık 30–60 dakika önce. Yağ ve lifi az tutun; karbonhidrat öncelikli olsun."), ("Örnekler", "Muz + fıstık ezmesi, yulaf + süt, tost + yumurta. Kahve veya çay isteğe bağlı; kafein performansı artırabilir.")]),
    ("aralikli-oruc", "Aralıklı Oruç (Intermittent Fasting): Kimler Yapmalı, Kimler Uzak Durmalı?", "Beslenme & Takviyeler",
     "IF nedir? 16/8 ve diğer protokoller. Kilo verme ve sağlık.", "photo-1512621776951-a57141f2eefd",
     "Aralıklı oruç, yeme penceresi dışında kalori almayı içerir. Bazıları için kilo kontrolü ve pratiklik sağlar; bazıları için uygun değildir.",
     [("Kimler Yapabilir?", "Sağlıklı yetişkinler, kalori ve makroları takip edebilenler. Hamile/emziren, yeme bozukluğu geçmişi olan veya diyabetliler dikkatli olmalı veya uzak durmalı."), ("Örnek 16/8", "8 saat yeme penceresi (örn. 12:00–20:00), 16 saat açlık. İçinde öğünler normal kalori ve protein hedefine göre planlanır.")]),
    ("cheat-meal", "Cheat Meal Mantığı: Diyeti Bozmadan Kaçamak Yapmanın Yolları", "Beslenme & Takviyeler",
     "Cheat meal ne zaman ve nasıl? Planlı kaçamak ve psikolojik rahatlama.", "photo-1546069901-ba9599a7e63c",
     "Planlı bir kaçamak öğün, diyette sürdürülebilirliği artırabilir. Kontrolsüz tüketim ise ilerlemeyi yavaşlatır; sıklık ve porsiyon önemli.",
     [("Ne Zaman?", "Haftada bir veya iki haftada bir; hedefe ve psikolojik ihtiyaca göre. Aşırı kısıtlayıcı diyetlerde bazen gerekli olur."), ("Nasıl Kontrol?", "Tek öğün sınırlı tutun; günü 'cheat gün' yapmayın. Sonrasında su ve normal öğünlere dönün. Suçluluk hissetmeyin; planlıdır.")]),
    ("su-tuketimi", "Su Tüketimi ve Performans: Kasların %70'i Suysa, Sen Neden Az İçiyorsun?", "Beslenme & Takviyeler",
     "Günlük su ihtiyacı, antrenmanda sıvı tüketimi ve performans.", "photo-1548839140-29a749e1cf4d",
     "Yeterli su, performans, toparlanma ve genel sağlık için şarttır. Susuzluk hissi geciktiği için düzenli içmek alışkanlık haline getirilmelidir.",
     [("Ne Kadar?", "Genel kılavuz 2–3 litre/gün; antrenman ve terleme artırır. İdrar rengi açık sarı olmalı."), ("Antrenmanda", "Öncesi 1–2 bardak; antrenman sırasında küçük yudumlar. Uzun ve yoğun antrenmanda elektrolit (sodyum) da gerekebilir.")]),
    ("gece-yemek", "Gece Yemek Yemek: Kilo Aldırır mı Yoksa Mit mi?", "Beslenme & Takviyeler",
     "Gece yemek yemek kilo aldırır mı? Kalori ve zamanlama bilimi.", "photo-1490818387583-1baba5e638af",
     "Kilo alımı veya verme, toplam kalori ve makrolara bağlıdır; saat kaçta yediğiniz tek başına belirleyici değildir. Gece atıştırması aşırı kalori ekliyorsa kilo artar.",
     [("Bilim Ne Diyor?", "Metabolizma gece çok düşmez; kalori aynı kalori sayılır. Ancak geç saatte yemek uyku kalitesini bozabilir veya reflü yapabilir."), ("Pratik", "Açsanız hafif bir atıştırmalık yiyin; günlük kaloriyi aşmayın. Uykuya 1–2 saat kala ağır yemekten kaçının.")]),
    ("kalori-sayma", "Kalori Sayma Rehberi: Makrolarını (Protein, Karbonhidrat, Yağ) Nasıl Hesaplarsın?", "Beslenme & Takviyeler",
     "Kalori ve makro hesaplama. Günlük ihtiyaç ve uygulama ipuçları.", "photo-1512621776951-a57141f2eefd",
     "Hedef kiloya göre kalori ve makro (protein, karbonhidrat, yağ) hesaplamak, ilerlemeyi ölçülebilir kılar. Uygulama veya basit hesaplarla yapılabilir.",
     [("Kalori", "Bazal metabolizma + aktivite = toplam harcama. Kilo vermek için açık, almak için fazla verin. Haftalık tartı takibi ile ayarlayın."), ("Makrolar", "Protein önce (1,6–2 g/kg); kalan kalori karbonhidrat ve yağa bölünür. Uygulama (MyFitnessPal vb.) ile takip kolaylaşır.")]),
    ("dogal-yag-yakici", "Doğal Yağ Yakıcı Besinler: Mutfağındaki Gizli Kahramanlar", "Beslenme & Takviyeler",
     "Protein, lif ve termik etkisi yüksek besinler. Yağ kaybına destek gıdalar.", "photo-1512621776951-a57141f2eefd",
     "Hiçbir besin tek başına yağ yaktırmaz; ancak protein, lif ve bazı baharatlar tokluk ve metabolizmayı destekleyerek diyete yardımcı olur.",
     [("Protein ve Lif", "Protein termik etkisi yüksektir; tokluk sağlar. Sebze ve tam tahıllar lifle doygunluk verir, kalori yoğunluğu düşüktür."), ("Baharat ve Çay", "Acı biber (kapsaisin) ve yeşil çay hafif metabolik etki gösterir. Asıl belirleyici toplam kalori ve antrenmandır.")]),
    ("vegan-sporcu", "Vegan Sporcu Beslenmesi: Bitkisel Kaynaklarla Kas Yapmak Mümkün mü?", "Beslenme & Takviyeler",
     "Vegan beslenme ve kas geliştirme. Protein kaynakları ve B12, demir.", "photo-1512621776951-a57141f2eefd",
     "Bitkisel beslenme ile kas yapmak mümkündür. Yeterli kalori, protein (baklagiller, tofu, seitan, tam tahıllar) ve B12, demir, D vitamini takibi gerekir.",
     [("Protein", "Mercimek, nohut, fasulye, tofu, tempeh, seitan, kinoa. Çeşitlilik ile tüm amino asitler alınır. Kilogram başına 1,6–2 g hedef aynı kalır."), ("Dikkat Edilecekler", "B12 takviyesi önerilir. Demir (ıspanak, mercimek) C vitamini ile alınmalı. D vitamini güneş veya takviye.")]),
    # Motivasyon (31-40)
    ("disiplin-motivasyon", "Disiplin mi Motivasyon mu?: Motivasyon Bittiğinde Seni Ne Ayakta Tutar?", "Motivasyon & Yaşam",
     "Disiplin ve alışkanlık. Motivasyon dalgalı; disiplin sürdürür.", "photo-1571019613454-1cb2f99b2d8b",
     "Motivasyon gelir gider; disiplin ve rutin ise antrenmanı ve beslenmeyi zor günlerde de sürdürür. Küçük adımlar ve net hedefler disiplini güçlendirir.",
     [("Motivasyon vs Disiplin", "Motivasyon duygusal bir itici güçtür; disiplin ise 'hissetmesen de yapmak'tır. Uzun vadede disiplin kazandırır."), ("Nasıl Gelişir?", "Küçük, ölçülebilir hedefler koyun. Antrenmanı aynı saatlere sabitleyin. Kaçırdığınızda suçluluk yerine ertesi gün devam edin.")]),
    ("uyku-toparlanma", "Uyku ve Toparlanma (Recovery): Kasların Antrenmanda Değil, Uykuda Büyür", "Motivasyon & Yaşam",
     "Uyku kalitesi ve süresi. Kas onarımı ve performans.", "photo-1541783245831-57d6fb0926d3",
     "Kas dokusu antrenmanda uyarılır; büyüme ve adaptasyon uyku ve beslenme ile tamamlanır. 7–9 saat kaliteli uyku toparlanmanın temelidir.",
     [("Neden Uyku?", "Büyüme hormonu ve protein sentezi uykuda artar. Yetersiz uyku kortizolu yükseltir, performansı ve iyileşmeyi düşürür."), ("Pratik", "Aynı saatte yatın-kalkın. Yatak odası karanlık ve serin olsun. Kafeini öğleden sonra sınırlayın; ekranı yatmadan önce kapatın.")]),
    ("erken-kalkma", "Erken Kalkmanın Gücü: Sabah Antrenmanları Neden Daha Verimli?", "Motivasyon & Yaşam",
     "Sabah antrenmanı avantajları. Enerji, tutarlılık ve günlük plan.", "photo-1571019614242-c5c5dee9f50b",
     "Sabah antrenmanı, günün koşuşturmasından önce tamamlanır; tutarlılık artar. Isınma ile vücut uyanır ve performans yükselir.",
     [("Avantajlar", "Gün içi işler antrenmanı erteletmez. Sabah kortizol yüksektir; bazıları için kuvvet ve odak iyidir. Boş salon da artıdır."), ("Nasıl Alışılır?", "Yatmadan 1 saat önce ekranı bırakın; aynı saatte yatın. Alarmı uzakta tutun. İlk haftalar kısa antrenmanla başlayın.")]),
    ("spor-ayakkabisi", "Spor Ayakkabısı Seçimi: Yanlış Ayakkabı Nasıl Sakatlığa Yol Açar?", "Motivasyon & Yaşam",
     "Koşu ve antrenman ayakkabısı. Taban, destek ve aktiviteye uygunluk.", "photo-1542291026-7eec264c27ff",
     "Yanlış ayakkabı diz, ayak bileği ve bel ağrısına neden olabilir. Aktiviteye (koşu, ağırlık, cross training) uygun seçim önemlidir.",
     [("Ne Seçmeli?", "Koşu için koşu ayakkabısı; ağırlık için düz taban veya minimal drop. Cross training için dengeli destek. Ayak numarası ve genişliği doğru olsun."), ("Ne Zaman Değişmeli?", "500–800 km koşu veya 6–12 ayda bir. Taban aşınması ve destek kaybı sakatlık riskini artırır.")]),
    ("sosyal-hayat-spor", "Sosyal Hayat ve Spor Dengesi: Arkadaşlarınla Dışarıdayken Diyeti Korumak", "Motivasyon & Yaşam",
     "Sosyal ortamda beslenme. Restoran seçimi ve alkol.", "photo-1529156069898-49953e39b3ac",
     "Sosyal hayat ve diyet bir arada yürüyebilir. Önceden plan, menüden akıllı seçim ve alkol tüketimini sınırlama dengeyi korur.",
     [("Planlama", "Menüyü önceden inceleyin; protein ve sebze ağırlıklı seçin. Aç gittiğinizde aşırı yeme riski artar; hafif atıştırın."), ("Alkol", "Kalorisi yüksektir; toplam kaloriye ekleyin. Birkaç içkiden sonra irade zayıflar; limit koyun veya alkolsüz tercih edin.")]),
    ("gelisim-takip", "Gelişimi Takip Etmek: Neden Tartıdaki Rakam Her Şey Demek Değildir?", "Motivasyon & Yaşam",
     "İlerleme ölçümü: tartı, ölçü, fotoğraf, performans.", "photo-1517836357463-d25dfeac3438",
     "Kilo tek başına yanıltıcı olabilir; kas artarken yağ azalınca tartı sabit kalabilir. Ölçü, fotoğraf ve antrenman performansı daha iyi gösterge sunar.",
     [("Neden Tartı Yetmez?", "Su, sindirim ve kas/yağ değişimi tartıyı günlük oynatır. Haftalık ortalama ve trend daha anlamlıdır."), ("Ne Takip Edilmeli?", "Bel, kalça, göğüs ölçüsü; aynı ışıkta aylık fotoğraf; ağırlık kaldırma veya koşu süresi. Bu veriler motivasyonu ve doğru yönü gösterir.")]),
    ("muzik-performans", "Müzik ve Performans: Antrenman Modunu Yükselten Çalma Listeleri", "Motivasyon & Yaşam",
     "Müziğin antrenman üzerine etkisi. Tempo ve motivasyon.", "photo-1511671782779-c97d3d27a1d4",
     "Müzik, algılanan eforu düşürür ve motivasyonu artırır. Tempo yüksek olduğunda kardiyo ve ağırlık antrenmanında performans artabilir.",
     [("Bilim", "Çalışmalar, müzikle çalışanların daha uzun süre dayandığını ve daha iyi hissettiğini gösteriyor. Özellikle tempolu parçalar ritim sağlar."), ("Pratik", "Isınmada orta tempo; ana setlerde yüksek BPM. Kulaklık güvenliği (trafik, salon) unutulmamalı.")]),
    ("meditasyon-odaklanma", "Meditasyon ve Odaklanma: Sporcular İçin Zihinsel Antrenman", "Motivasyon & Yaşam",
     "Nefes ve odaklanma. Maç ve antrenman öncesi zihin hazırlığı.", "photo-1506126613408-eca07ce68773",
     "Meditasyon ve nefes çalışması, odaklanmayı ve stres yönetimini geliştirir. Sporcular maç veya zor antrenman öncesi zihinsel hazırlık yapabilir.",
     [("Faydalar", "Dikkat artar, kaygı azalır. Nefes kontrolü (özellikle yüksek eforda) performansı destekler."), ("Nasıl Başlanır?", "5–10 dakika sessiz oturma, nefese odaklanma. Uygulama (Headspace, Calm) veya antrenör eşliğinde nefes drill’leri kullanılabilir.")]),
    ("overtraining", "Overtraining (Aşırı Antrenman): Vücudun 'Dur' Dediğini Nasıl Anlarsın?", "Motivasyon & Yaşam",
     "Aşırı antrenman belirtileri. Toparlanma ve deload.", "photo-1571019614242-c5c5dee9f50b",
     "Aşırı antrenman, toparlanmadan sürekli yüklenmekten kaynaklanır. Performans düşer, yorgunluk ve uyku bozukluğu artar. Dinlenme ve deload şarttır.",
     [("Belirtiler", "Kronik yorgunluk, uyku bozulması, antrenman performansında düşüş, sık hastalanma, sinirlilik. Nabız dinlenme halinde yüksekse dikkat."), ("Çözüm", "1 hafta deload (hacim/yük düşük) veya tam dinlenme. Uyku ve beslenmeyi gözden geçirin. Sonra kademeli artış.")]),
    ("spora-yeni-baslayanlar", "Spora Yeni Başlayanlara Tavsiyeler: İlk 3 Ayı Kazasız Atlatma Rehberi", "Motivasyon & Yaşam",
     "Yeni başlayanlar için antrenman ve beslenme. Adım adım ilerleme.", "photo-1517836357463-d25dfeac3438",
     "İlk 3 ayda tutarlılık, teknik ve hafif progresyon önceliklidir. Aşırı yüklenme ve sakatlıktan kaçınarak alışkanlık oluşturun.",
     [("Temel Kurallar", "Haftada 3 antrenman yeterli. Temel hareketleri öğrenin (squat, hinge, push, pull). Her hafta biraz daha ağır veya tekrar artırın."), ("Beslenme ve Uyku", "Yeterli protein ve kalori; aşırı kısıtlama yapmayın. Uyku 7–8 saat. Bire bir antrenör ilk aylarda çok değerli olur.")]),
]

NAV = """  <header class="header scrolled">
    <div class="container header-inner">
      <a href="../index.html" class="logo">
        <img src="../assets/logo.png" alt="d.academy" class="logo-img" />
      </a>
      <nav class="nav">
        <a href="../index.html">Anasayfa</a>
        <a href="../index.html#hakkimizda">Hakkımızda</a>
        <a href="../index.html#egitim">Eğitimler</a>
        <a href="../index.html#neden">Neden Biz</a>
        <a href="../index.html#nasil">Süreç</a>
        <a href="../index.html#indirim">Fırsat</a>
        <a href="../blog.html">Blog</a>
        <a href="../iletisim.html">İletişim</a>
      </nav>
      <button class="menu-btn" aria-label="Menü" id="menuBtn">
        <span></span><span></span><span></span>
      </button>
    </div>
    <nav class="nav-mobile" id="navMobile" aria-hidden="true">
      <a href="../index.html">Anasayfa</a>
      <a href="../index.html#hakkimizda">Hakkımızda</a>
      <a href="../index.html#egitim">Eğitimler</a>
      <a href="../index.html#neden">Neden Biz</a>
      <a href="../index.html#nasil">Süreç</a>
      <a href="../index.html#indirim">Fırsat</a>
      <a href="../blog.html">Blog</a>
      <a href="../iletisim.html">İletişim</a>
    </nav>
  </header>"""

FOOTER = """  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-block">
        <h4 class="footer-title">Hızlı Erişim</h4>
        <ul class="footer-links">
          <li><a href="../index.html">Ana sayfa</a></li>
          <li><a href="../index.html#hakkimizda">Hakkımızda</a></li>
          <li><a href="../index.html#egitim">Eğitimler</a></li>
          <li><a href="../blog.html">Blog</a></li>
          <li><a href="../iletisim.html">İletişim</a></li>
        </ul>
      </div>
      <div class="footer-block">
        <h4 class="footer-title">Eğitimler</h4>
        <ul class="footer-links">
          <li><a href="../index.html#egitim">Fitness</a></li>
          <li><a href="../index.html#egitim">Dövüş Sporları</a></li>
          <li><a href="../index.html#egitim">Reformer Pilates</a></li>
          <li><a href="../index.html#egitim">Yüzme</a></li>
        </ul>
      </div>
      <div class="footer-block">
        <h4 class="footer-title">İletişim</h4>
        <ul class="footer-contact">
          <li><a href="tel:+905330140534">+90 533 014 05 34</a></li>
          <li><a href="https://www.google.com/maps/search/?api=1&query=İstiklal,+Piyalepaşa+Blv.+1+30+D:2,+34440+Beyoğlu+İstanbul" target="_blank" rel="noopener">İstiklal, Piyalepaşa Blv. 1 30 D:2, Beyoğlu/İstanbul</a></li>
          <li><a href="https://www.instagram.com/d.academytr/" target="_blank" rel="noopener">Instagram</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p class="footer-brand">d.academy</p>
      <p class="footer-copy">© 2025 d.academy. Tüm hakları saklıdır.</p>
    </div>
  </footer>

  <div class="fixed-contact" aria-label="Hızlı iletişim">
    <a href="tel:+905330140534" class="fixed-btn fixed-phone" aria-label="Telefonla ara" title="Telefon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    </a>
    <a href="https://wa.me/905330140534" class="fixed-btn fixed-whatsapp" aria-label="WhatsApp" title="WhatsApp" target="_blank" rel="noopener">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    </a>
  </div>

  <script>
    (function () {
      var menuBtn = document.getElementById('menuBtn');
      var navMobile = document.getElementById('navMobile');
      if (menuBtn && navMobile) {
        menuBtn.addEventListener('click', function () {
          var open = navMobile.getAttribute('aria-hidden') !== 'true';
          navMobile.setAttribute('aria-hidden', open);
          menuBtn.classList.toggle('open', !open);
        });
        navMobile.querySelectorAll('a').forEach(function (a) {
          a.addEventListener('click', function () {
            navMobile.setAttribute('aria-hidden', 'true');
            menuBtn.classList.remove('open');
          });
        });
      }
    })();
  </script>
</body>
</html>"""

def build_body(slug, title, meta, lead, sections):
    h2_block = ""
    for h2_title, h2_text in sections:
        h2_block += f"""
        <h2>{h2_title}</h2>
        <p>{h2_text}</p>"""
    return f"""      <div class="container blog-post-body">
        <p class="blog-post-lead">{lead}</p>
{h2_block}
        <p>Kişiye özel program ve antrenman için <a href="../iletisim.html">bizimle iletişime geçebilirsiniz</a>.</p>
      </div>"""

def main():
    os.makedirs(BLOG_DIR, exist_ok=True)
    base = "https://images.unsplash.com"
    for slug, title, meta, desc, img_id, lead, sections in POSTS:
        img_url = f"{base}/{img_id}?auto=format&fit=crop&w=1200&q=80"
        body = build_body(slug, title, meta, lead, sections)
        html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | d.academy Blog</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="https://dacademy.com.tr/blog/{slug}.html" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
{NAV}
  <main class="blog-post-page">
    <article class="blog-post">
      <div class="blog-post-hero">
        <img src="{img_url}" alt="{title}" class="blog-post-hero-img" />
        <div class="container blog-post-hero-inner">
          <a href="../blog.html" class="blog-post-back">← Blog</a>
          <h1 class="blog-post-title">{title}</h1>
          <p class="blog-post-meta">{meta}</p>
        </div>
      </div>
{body}
    </article>
  </main>
{FOOTER}"""
        path = os.path.join(BLOG_DIR, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Wrote", path)
    print("Done. 40 posts created.")

def update_blog_html():
    blog_path = os.path.join(os.path.dirname(__file__), '..', 'blog.html')
    with open(blog_path, 'r', encoding='utf-8') as f:
        content = f.read()
    cards_html = []
    for slug, title, meta, desc, img_id, lead, sections in POSTS:
        short_title = title.split(':')[0].strip() if ':' in title else title
        card = f"""          <article class="blog-card">
            <a href="blog/{slug}.html" class="blog-card-link">
              <div class="blog-card-img" style="--img: url('https://images.unsplash.com/{img_id}?auto=format&fit=crop&w=600&q=80')"></div>
              <div class="blog-card-content">
                <h2 class="blog-card-title">{short_title}</h2>
                <p class="blog-card-desc">{desc}</p>
              </div>
            </a>
          </article>"""
        cards_html.append(card)
    insert = '\n'.join(cards_html)
    old = """          </article>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">"""
    new = """          </article>
""" + insert + """
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">"""
    if old not in content:
        # Try without extra newline
        old2 = """          </article>
        </div>
      </div>
    </section>
  </main>

  <footer"""
        new2 = """          </article>
""" + insert + """
        </div>
      </div>
    </section>
  </main>

  <footer"""
        content = content.replace(old2, new2, 1)
    else:
        content = content.replace(old, new, 1)
    with open(blog_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated blog.html with 40 new cards.")

if __name__ == "__main__":
    main()
    update_blog_html()
