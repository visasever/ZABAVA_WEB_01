from pathlib import Path
import re,base64
src=Path('prototype');dst=Path('prototype-v2')
s=(src/'index.html').read_text(encoding='utf-8')
s=s.replace('Забава — місце, де живе «вау!»','Забава — свято на повну!')
s=s.replace('ДИЗАЙН-КОНЦЕПЦІЯ 01','ДРОГОБИЧ · ТЦ «СІЛЬ», 2 ПОВЕРХ').replace('Ціни з наданого каталогу · актуальність уточнюйте','Ваш наступний привід бути разом ♥')
s=s.replace('<a href="#services">Послуги й ціни</a>','<a href="#gallery">Галерея</a><a href="#services">Послуги й ціни</a>')
start=s.index('<section class="hero">');end=s.index('<section id="fun">')
s=s[:start]+'''<section class="hero"><div class="hero-photo"><img src="assets/party-hero.png" alt="Концептуальна ілюстрація дитячого свята" fetchpriority="high"></div><div class="hero-shade"></div><div class="hero-copy"><span class="hero-tag">МАЛЕНЬКІ ГОСТІ. ВЕЛИКІ ЕМОЦІЇ.</span><h1>Свято<br>на <em>повну!</em><span class="hero-spark" aria-hidden="true">✳</span></h1><p>Дні народження, які хочеться повторити.<br>Пригоди, про які ще довго розповідають.</p><div class="actions"><a class="button" href="#packages">Знайти своє свято <span>↗</span></a><a class="play-button" href="#gallery"><span>▷</span> Пориньте в атмосферу</a></div><div class="hero-bottom"><span>01 / ДНІ НАРОДЖЕННЯ</span><a href="#fun">Ще більше пригод ↓</a></div></div><span class="photo-note">Концептуальне зображення · не фото центру</span><div class="floating-note"><span>♥</span><b>Їм — пригоди.<br>Вам — щасливі спогади.</b></div></section><div class="ticker" aria-hidden="true"><div class="ticker-track">ГРАЙ ✳ СВЯТКУЙ ✳ МРІЙ ✳ ЗАБАВЛЯЙСЯ ✳ ГРАЙ ✳ СВЯТКУЙ ✳ МРІЙ ✳ ЗАБАВЛЯЙСЯ ✳ </div></div><section class="intro reveal"><span class="eyebrow">ЦЕ ВСЕ — ЗАБАВА</span><h2>Дитинство не чекає.<br><span>Наповнюймо його пригодами.</span></h2><p>Збирайте друзів, обирайте улюблених героїв і створюйте свій особливий день. А ми допоможемо з програмою.</p></section>'''+s[end:]
s=s.replace('<div class="symbol">✳</div>','<div class="card-art art-party"><span>✳</span><b>HAPPY<br>DAY!</b><i>♥</i></div>').replace('<div class="symbol">◎</div>','<div class="card-art art-quest"><span>◎</span><b>MISSION<br>WOW!</b><i>↗</i></div>').replace('<div class="symbol">◒</div>','<div class="card-art art-make"><span>◒</span><b>MAKE<br>MAGIC!</b><i>✦</i></div>')
s=s.replace('<a class="text-link" href="assets/catalog.pdf" target="_blank" rel="noopener">Повний каталог PDF ↗</a>','<a class="text-link" href="tel:+380962233033">Допомогти з вибором? ↗</a>')
s=s.replace('<a href="assets/catalog.pdf">Каталог послуг</a>','<a href="#services">Послуги та ціни</a>').replace('<a href="design-notes.html">Про дизайн-концепцію ↗</a>','<a href="#gallery">Атмосфера свята ↗</a>')
gallery='''<section id="gallery" class="gallery reveal"><div class="section-top"><div><div class="eyebrow">НЕХАЙ ЦЕ БУДЕ ВАШ НАСТУПНИЙ СПОГАД</div><h2>У кадрі — <em>радість.</em></h2></div><p>Натисніть на картинку,<br>щоб роздивитися ближче.</p></div><div class="gallery-grid"><button class="gallery-item gallery-main" data-image="assets/party-hero.png" data-caption="Свято на повну! Концептуальне зображення, створене ШІ; не фото центру."><img src="assets/party-hero.png" alt="Діти святкують день народження — концептуальна ілюстрація" loading="lazy"><span>День, який запам’ятається <b>↗</b></span></button><button class="gallery-item gallery-brand" data-image="assets/mascot.png" data-caption="Фірмовий персонаж «Забави» з брендбуку."><img src="assets/mascot.png" alt="Фірмовий персонаж Забави" loading="lazy"><span>Знайомтеся: настрій «Забава» <b>↗</b></span><i aria-hidden="true">✳</i></button></div><p class="fine">Зображення свята — концептуальна візуалізація. Перед запуском тут з’являться справжні фото центру та заходів.</p></section><section class="steps reveal"><div class="section-top"><div><div class="eyebrow">ВІД ІДЕЇ ДО «З ДНЕМ НАРОДЖЕННЯ!»</div><h2>Ваше свято.<br>Три прості кроки.</h2></div><a class="button" href="tel:+380962233033">Поговорімо про свято ↗</a></div><div class="steps-grid"><article><span>01</span><h3>Оберіть пригоду</h3><p>Пакет, герой чи квест — почніть із того, що любить дитина.</p></article><article><span>02</span><h3>Обговорімо деталі</h3><p>Зателефонуйте: узгодимо дату, кількість гостей, програму та бюджет.</p></article><article><span>03</span><h3>Святкуйте разом</h3><p>Збирайте друзів і приходьте за новими спільними спогадами.</p></article></div></section>'''
s=s.replace('<section class="faq">',gallery+'<section class="faq reveal">')
s=s.replace('Прототип · 2026','Дизайн-концепція 02 · 2026')
s=s.replace('</main>','</main><dialog id="lightbox" aria-labelledby="lightbox-caption"><button class="lightbox-close" aria-label="Закрити зображення">×</button><img id="lightbox-image" alt=""><p id="lightbox-caption"></p></dialog><button id="motion-toggle" class="motion-toggle" aria-pressed="false" aria-label="Призупинити декоративні анімації">Ⅱ Анімація</button>')
(dst/'index.html').write_text(s,encoding='utf-8')
css=(src/'style.css').read_text(encoding='utf-8')+'\n'+(dst/'refresh.css').read_text(encoding='utf-8')
# Normalize every CSS color to brand RGB values or neutral black/white.
brand={'000000','ffffff','26cad3','b1e3e3','ff3a1e','f8ea47','675dc6','ff8189'}
remap={'0058bb':'675dc6','202321':'000000','153c39':'000000','fffaf1':'ffffff','fffefa':'ffffff','e6f1ec':'b1e3e3','f1f3ed':'b1e3e3','f6f2eb':'ffffff','f0f2eb':'ffffff','ecf0e6':'ffffff','eaf0e6':'b1e3e3','fff9d4':'f8ea47','f9e96d':'f8ea47','f7ee91':'f8ea47','ecf4d2':'ffffff','ffd2d5':'ff8189','ff969f':'ff8189','e45d73':'ff8189','ff6678':'ff8189','a82841':'000000','8b5723':'000000','164d47':'26cad3','25645d':'000000','00969f':'000000','00858d':'000000','51bfc2':'26cad3','80bcbc':'26cad3'}
def brand_color(match):
 value=match.group()[1:].lower()
 if len(value) in (3,4):value=''.join(c*2 for c in value)
 rgb,alpha=value[:6],value[6:]
 if rgb in brand:return '#'+rgb+alpha
 return '#'+remap.get(rgb,'000000' if sum(int(rgb[i:i+2],16) for i in (0,2,4))<520 else 'ffffff')+alpha
css=re.sub(r'#[0-9a-fA-F]{3,8}\b',brand_color,css)
css+='\n'+(dst/'brand.css').read_text(encoding='utf-8')
(dst/'style.css').write_text(css,encoding='utf-8')
js=(src/'app.js').read_text(encoding='utf-8')+'\n'+(dst/'motion.js').read_text(encoding='utf-8')
(dst/'app.js').write_text(js,encoding='utf-8')
if (dst/'assets/party-hero.png').exists():
 single=s.replace('<link rel="stylesheet" href="style.css">','<style>'+css+'</style>').replace('<script src="app.js"></script>','<script>'+js+'</script>')
 for name in ['logo.png','mascot.png','party-hero.png']:
  single=single.replace('assets/'+name,'data:image/png;base64,'+base64.b64encode((dst/'assets'/name).read_bytes()).decode())
 (dst/'zabava-v2-full.html').write_text(single,encoding='utf-8')
assert '.pdf' not in s.lower()
print('Variant 2 built; no PDF links')
