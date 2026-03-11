#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 8 remaining egitim detail pages (dovus-sporlari through mma)."""

import os

EGITIM_DIR = os.path.join(os.path.dirname(__file__), '..', 'egitim')

PAGES = [
    ("dovus-sporlari", "Dövüş Sporları", "photo-1599058917212-d750089bc07e",
     "Neden Dövüş Sporları?", "Dövüş sporları yalnızca savunma değil; disiplin, kondisyon ve teknik bir arada gelişir. d.academy’de bire bir antrenörle güvenli ortamda tekniğinizi ilerletir, fiziksel ve zihinsel dayanıklılık kazanırsınız.",
     "Boks, kick boks, MMA veya güreş; hedefinize göre program kişiselleştirilir. Tüm dikkat sizin üzerinizde, sakatlık riski minimumda tutulur.",
     [("Teknik Eğitim", "photo-1549719386-74dfcbf7dbed", "Yumruk, tekme ve savunma teknikleri. Doğru form ve güç aktarımı."), ("Kondisyon", "photo-1551698618-1dfe5d97d256", "Dayanıklılık ve çeviklik. Ring ve antrenman için hazırlık."), ("Güvenli Ortam", "photo-1599058917212-d750089bc07e", "Kontrollü sparring ve ekipman. Disiplinli ilerleme.")],
     ["photo-1599058917212-d750089bc07e", "photo-1549719386-74dfcbf7dbed", "photo-1551698618-1dfe5d97d256"],
     "Bire Bir Dövüş Sporlarına Başlayın"),
    ("reformer-pilates", "Reformer Pilates", "photo-1518611012118-696072aa579a",
     "Neden Reformer Pilates?", "Reformer ile esneklik, core gücü ve postür bir arada gelişir. Sakatlık önleme ve rehabilitasyon için ideal. d.academy’de bire bir reformer dersiyle hareket kalitenizi artırırsınız.",
     "Her seviyeye uygun ayarlanabilir direnç; eğitmen tüm dikkati size verir. Bel, kalça ve omuz bölgesi güçlenir, günlük hayat rahatlar.",
     [("Esneklik & Mobilite", "photo-1544367567-0f2fcb009e0b", "Kas uzunluğu ve eklem hareketi. Reformer ile güvenli germe."), ("Core Gücü", "photo-1518611012118-696072aa579a", "Karın, bel ve pelvis stabilitesi. Postür düzeltmesi."), ("Rehabilitasyon", "photo-1544367567-0f2fcb009e0b", "Sakatlık sonrası toparlanma. Düşük impact, yüksek etki.")],
     ["photo-1518611012118-696072aa579a", "photo-1544367567-0f2fcb009e0b", "photo-1571019614242-c5c5dee9f50b"],
     "Bire Bir Reformer Pilatese Başlayın"),
    ("yuzme", "Yüzme", "photo-1530549387789-4c1017266635",
     "Neden Yüzme?", "Başlangıçtan ileri seviyeye yüzme; tekniği doğru öğrenmek hem güvenli hem keyifli yüzmeyi getirir. d.academy’de bire bir yüzme dersiyle nefes, stroke ve dönüşleri geliştirirsiniz.",
     "Çocuk ve yetişkin için uygun program. Havuz güvenliği ve kişiye özel antrenman planı.",
     [("Teknik Gelişim", "photo-1530549387789-4c1017266635", "Serbest, sırt, kurbağalama. Nefes ve vücut pozisyonu."), ("Güven", "photo-1571902943202-507ec2618e8f", "Su güvenliği ve rahat hissetme. Adım adım ilerleme."), ("Kondisyon", "photo-1530549387789-4c1017266635", "Tüm vücut çalışması. Düşük impact kardiyo.")],
     ["photo-1530549387789-4c1017266635", "photo-1571902943202-507ec2618e8f", "photo-1530549387789-4c1017266635"],
     "Bire Bir Yüzme Dersine Başlayın"),
    ("medikal-fitness-pilates", "Medikal Fitness / Pilates", "photo-1544367567-0f2fcb009e0b",
     "Neden Medikal Fitness / Pilates?", "Rehabilitasyon ve sakatlık sonrası iyileşme odaklı program. Fizik tedavi sonrası veya kronik ağrı yönetiminde hareket kalitesini artırmak için bire bir çalışma.",
     "Tıbbi geçmişinize göre kişiselleştirilmiş egzersiz. Düşük impact, güvenli progresyon.",
     [("Rehabilitasyon", "photo-1544367567-0f2fcb009e0b", "Sakatlık sonrası güç ve hareket açıklığı. Doktor önerisi ile uyumlu."), ("Postür & Ağrı", "photo-1518611012118-696072aa579a", "Bel, boyun ve omuz. Masa başı kaynaklı sorunlara yönelik."), ("Kişiye Özel", "photo-1544367567-0f2fcb009e0b", "Hedef ve kısıtlamalara göre tam özelleştirilmiş program.")],
     ["photo-1544367567-0f2fcb009e0b", "photo-1518611012118-696072aa579a", "photo-1571019614242-c5c5dee9f50b"],
     "Medikal Fitness / Pilatese Başlayın"),
    ("kick-boks", "Kick Boks", "photo-1551698618-1dfe5d97d256",
     "Neden Kick Boks?", "Yumruk ve tekneğin bir arada kullanıldığı kick boks; kondisyon, çeviklik ve teknik bir arada. d.academy’de bire bir antrenörle güvenli ortamda ilerleyin.",
     "Kum torbası, gölge boksu ve partner çalışması. Hedefinize göre fitness veya müsabaka yönelimi.",
     [("Yumruk & Teknik", "photo-1549719386-74dfcbf7dbed", "Jab, cross, hook ve tekme kombinasyonları. Doğru form."), ("Kondisyon", "photo-1551698618-1dfe5d97d256", "İnterval ve tur antrenmanı. Yağ yakımı ve dayanıklılık."), ("Savunma", "photo-1599058917212-d750089bc07e", "Blok, slip ve mesafe. Güvenli sparring.")],
     ["photo-1551698618-1dfe5d97d256", "photo-1549719386-74dfcbf7dbed", "photo-1599058917212-d750089bc07e"],
     "Bire Bir Kick Boksa Başlayın"),
    ("boks", "Boks", "photo-1549719386-74dfcbf7dbed",
     "Neden Boks?", "Klasik boks tekniği, ayak çalışması ve ring stratejisi. d.academy’de bire bir boks antrenmanıyla jab, cross, hook ve defansı öğrenin.",
     "Gölge boksu, kum torbası ve teknik drill. İster fitness ister amatör hedef; program size özel.",
     [("Teknik", "photo-1549719386-74dfcbf7dbed", "Yumruk tekniği ve güç aktarımı. Gard ve toparlanma."), ("Ayak Çalışması", "photo-1551698618-1dfe5d97d256", "Footwork ve mesafe kontrolü. Ring hareketi."), ("Kondisyon", "photo-1599058917212-d750089bc07e", "Tur antrenmanı ve dayanıklılık. İp atlama, koşu.")],
     ["photo-1549719386-74dfcbf7dbed", "photo-1551698618-1dfe5d97d256", "photo-1599058917212-d750089bc07e"],
     "Bire Bir Boksa Başlayın"),
    ("gures", "Güreş", "photo-1571019614242-c5c5dee9f50b",
     "Neden Güreş?", "Geleneksel ve serbest güreş teknikleri. Güç, denge ve taktik. d.academy’de bire bir güreş eğitimiyle temel pozisyonlar, atak ve savunmayı geliştirin.",
     "Güvenli minderde çalışma. Yaş ve seviyeye uygun progresyon.",
     [("Teknik", "photo-1571019614242-c5c5dee9f50b", "Duruş, tutuş ve temel hareketler. Serbest ve geleneksel."), ("Güç & Denge", "photo-1517836357463-d25dfeac3438", "Üst vücut ve core. Denge ve pozisyon kontrolü."), ("Taktik", "photo-1599058917212-d750089bc07e", "Atak-savunma geçişleri. Maç simülasyonu.")],
     ["photo-1571019614242-c5c5dee9f50b", "photo-1517836357463-d25dfeac3438", "photo-1599058917212-d750089bc07e"],
     "Bire Bir Güreşe Başlayın"),
    ("mma", "MMA", "photo-1599058917212-d750089bc07e",
     "Neden MMA?", "Karma dövüş sanatları: boks, tekme, güreş ve yer dövüşü. d.academy’de bire bir MMA eğitimiyle ayakta ve yerde tekniği, kondisyonu ve stratejiyi geliştirin.",
     "Güvenli ve kademeli ilerleme. İster fitness ister amatör hedef; tam size özel program.",
     [("Ayakta Dövüş", "photo-1549719386-74dfcbf7dbed", "Boks ve tekme. Mesafe ve kombinasyonlar."), ("Yer Dövüşü", "photo-1571019614242-c5c5dee9f50b", "Güreş, geçiş ve ground game. Güvenli çalışma."), ("Kondisyon", "photo-1551698618-1dfe5d97d256", "MMA’ye özel dayanıklılık ve güç. Tur antrenmanı.")],
     ["photo-1599058917212-d750089bc07e", "photo-1549719386-74dfcbf7dbed", "photo-1571019614242-c5c5dee9f50b"],
     "Bire Bir MMA'ya Başlayın"),
]

NAV_DROPDOWN = '''        <div class="nav-dropdown">
          <a href="../index.html#egitim" class="nav-dropdown-trigger">Eğitimler <span class="nav-arrow">▼</span></a>
          <div class="nav-dropdown-menu">
            <a href="fitness.html">Fitness</a>
            <a href="dovus-sporlari.html">Dövüş Sporları</a>
            <a href="reformer-pilates.html">Reformer Pilates</a>
            <a href="yuzme.html">Yüzme</a>
            <a href="medikal-fitness-pilates.html">Medikal Fitness / Pilates</a>
            <a href="kick-boks.html">Kick Boks</a>
            <a href="boks.html">Boks</a>
            <a href="gures.html">Güreş</a>
            <a href="mma.html">MMA</a>
          </div>
        </div>'''

def build_page(slug, title, hero_img, intro_h, intro_p1, intro_p2, benefits, gallery_imgs, cta_title):
    base = "https://images.unsplash.com"
    hero_url = f"{base}/{hero_img}?auto=format&fit=crop&w=1920&q=85"
    benefits_html = ""
    for b_title, b_img, b_desc in benefits:
        benefits_html += f"""
          <div class="egitim-benefit-card">
            <div class="egitim-benefit-img" style="--img: url('{base}/{b_img}?auto=format&fit=crop&w=600&q=80')"></div>
            <h3>{b_title}</h3>
            <p>{b_desc}</p>
          </div>"""
    gallery_html = ""
    for g in gallery_imgs:
        gallery_html += f"""
          <div class="egitim-gallery-item">
            <img src="{base}/{g}?auto=format&fit=crop&w=600&q=80" alt="" />
          </div>"""
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} – Bire Bir Eğitim | d.academy</title>
  <meta name="description" content="{title} bire bir eğitim. İstanbul d.academy. Ücretsiz detaylı ölçüm ve kişiye özel program." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
  <header class="header scrolled">
    <div class="container header-inner">
      <a href="../index.html" class="logo">
        <img src="../assets/logo.png" alt="d.academy" class="logo-img" />
      </a>
      <nav class="nav">
        <a href="../index.html">Anasayfa</a>
        <a href="../index.html#hakkimizda">Hakkımızda</a>
        {NAV_DROPDOWN}
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
      <a href="fitness.html">Fitness</a>
      <a href="dovus-sporlari.html">Dövüş Sporları</a>
      <a href="reformer-pilates.html">Reformer Pilates</a>
      <a href="yuzme.html">Yüzme</a>
      <a href="medikal-fitness-pilates.html">Medikal Fitness / Pilates</a>
      <a href="kick-boks.html">Kick Boks</a>
      <a href="boks.html">Boks</a>
      <a href="gures.html">Güreş</a>
      <a href="mma.html">MMA</a>
      <a href="../index.html#neden">Neden Biz</a>
      <a href="../index.html#nasil">Süreç</a>
      <a href="../index.html#indirim">Fırsat</a>
      <a href="../blog.html">Blog</a>
      <a href="../iletisim.html">İletişim</a>
    </nav>
  </header>

  <main class="egitim-page">
    <section class="egitim-hero">
      <div class="egitim-hero-bg" style="--img: url('{hero_url}')"></div>
      <div class="egitim-hero-overlay"></div>
      <div class="container egitim-hero-inner">
        <span class="egitim-hero-badge">Eğitimlerimiz</span>
        <h1 class="egitim-hero-title">{title}</h1>
        <p class="egitim-hero-desc">Bire bir antrenör eşliğinde kişiye özel program. Ücretsiz detaylı ölçüm ile başlıyoruz.</p>
      </div>
    </section>

    <section class="egitim-intro">
      <div class="container">
        <div class="egitim-intro-grid">
          <div class="egitim-intro-text">
            <h2>{intro_h}</h2>
            <p>{intro_p1}</p>
            <p>{intro_p2}</p>
          </div>
          <div class="egitim-intro-img">
            <img src="{base}/{hero_img}?auto=format&fit=crop&w=800&q=80" alt="{title} eğitimi" />
          </div>
        </div>
      </div>
    </section>

    <section class="egitim-benefits">
      <div class="container">
        <h2 class="egitim-section-title">Bu Eğitimde Neler Var?</h2>
        <div class="egitim-benefits-grid">{benefits_html}
        </div>
      </div>
    </section>

    <section class="egitim-gallery">
      <div class="container">
        <h2 class="egitim-section-title">Ortamımız</h2>
        <div class="egitim-gallery-grid">{gallery_html}
        </div>
      </div>
    </section>

    <section class="egitim-cta">
      <div class="container">
        <div class="egitim-cta-box">
          <h2>{cta_title}</h2>
          <p>Ücretsiz detaylı ölçüm ve size özel program için hemen iletişime geçin.</p>
          <a href="../iletisim.html" class="btn btn-primary">İletişime Geç</a>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-block">
        <h4 class="footer-title">Hızlı Erişim</h4>
        <ul class="footer-links">
          <li><a href="../index.html">Ana sayfa</a></li>
          <li><a href="../index.html#egitim">Eğitimler</a></li>
          <li><a href="../blog.html">Blog</a></li>
          <li><a href="../iletisim.html">İletişim</a></li>
        </ul>
      </div>
      <div class="footer-block">
        <h4 class="footer-title">Eğitimler</h4>
        <ul class="footer-links">
          <li><a href="fitness.html">Fitness</a></li>
          <li><a href="dovus-sporlari.html">Dövüş Sporları</a></li>
          <li><a href="reformer-pilates.html">Reformer Pilates</a></li>
          <li><a href="yuzme.html">Yüzme</a></li>
        </ul>
      </div>
      <div class="footer-block">
        <h4 class="footer-title">İletişim</h4>
        <ul class="footer-contact">
          <li><a href="tel:+905337336511">+90 533 733 65 11</a></li>
          <li><a href="https://www.google.com/maps/search/?api=1&query=İstiklal,+Piyalepaşa+Blv.+1+30+D:2,+34440+Beyoğlu+İstanbul" target="_blank" rel="noopener">Piyalepaşa Blv. 1 30 D:2, Beyoğlu/İstanbul</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p class="footer-brand">d.academy</p>
      <p class="footer-copy">© 2025 d.academy. Tüm hakları saklıdır.</p>
    </div>
  </footer>

  <div class="fixed-contact" aria-label="Hızlı iletişim">
    <a href="tel:+905337336511" class="fixed-btn fixed-phone" aria-label="Telefonla ara" title="Telefon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    </a>
    <a href="https://wa.me/905337336511" class="fixed-btn fixed-whatsapp" aria-label="WhatsApp" title="WhatsApp" target="_blank" rel="noopener">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    </a>
  </div>

  <script>
    (function () {{
      var menuBtn = document.getElementById('menuBtn');
      var navMobile = document.getElementById('navMobile');
      if (menuBtn && navMobile) {{
        menuBtn.addEventListener('click', function () {{
          var open = navMobile.getAttribute('aria-hidden') !== 'true';
          navMobile.setAttribute('aria-hidden', open);
          menuBtn.classList.toggle('open', !open);
        }});
        navMobile.querySelectorAll('a').forEach(function (a) {{
          a.addEventListener('click', function () {{
            navMobile.setAttribute('aria-hidden', 'true');
            menuBtn.classList.remove('open');
          }});
        }});
      }}
      var dropdown = document.querySelector('.nav-dropdown');
      if (dropdown) {{
        dropdown.addEventListener('mouseenter', function () {{ dropdown.classList.add('open'); }});
        dropdown.addEventListener('mouseleave', function () {{ dropdown.classList.remove('open'); }});
      }}
    }})();
  </script>
</body>
</html>"""

def main():
    os.makedirs(EGITIM_DIR, exist_ok=True)
    for slug, title, hero_img, intro_h, intro_p1, intro_p2, benefits, gallery_imgs, cta_title in PAGES:
        html = build_page(slug, title, hero_img, intro_h, intro_p1, intro_p2, benefits, gallery_imgs, cta_title)
        path = os.path.join(EGITIM_DIR, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Wrote", path)
    print("Done. 8 egitim pages created.")

if __name__ == "__main__":
    main()
