// Native dialog provides keyboard focus containment and Escape support.
const lightbox=document.querySelector('#lightbox');let opener;
document.querySelectorAll('[data-image]').forEach(button=>button.addEventListener('click',()=>{opener=button;const image=document.querySelector('#lightbox-image');image.src=button.dataset.image;image.alt=button.dataset.caption;document.querySelector('#lightbox-caption').textContent=button.dataset.caption;lightbox.showModal();document.body.style.overflow='hidden'}));
document.querySelector('.lightbox-close').onclick=()=>lightbox.close();
lightbox.addEventListener('click',event=>{if(event.target===lightbox){const rect=lightbox.getBoundingClientRect();if(event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom)lightbox.close()}});
lightbox.addEventListener('close',()=>{document.body.style.overflow='';opener?.focus()});
document.querySelectorAll('#fun,#packages,#services,.faq,.visit').forEach(section=>section.classList.add('reveal'));
if('IntersectionObserver' in window){document.body.classList.add('js-motion');const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.08});document.querySelectorAll('.reveal').forEach(section=>observer.observe(section))}
document.querySelector('#motion-toggle').addEventListener('click',event=>{const paused=document.body.classList.toggle('motion-paused');event.currentTarget.setAttribute('aria-pressed',paused);event.currentTarget.setAttribute('aria-label',paused?'Увімкнути декоративні анімації':'Призупинити декоративні анімації');event.currentTarget.textContent=paused?'▷ Анімація':'Ⅱ Анімація'});
