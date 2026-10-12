/* 本地公式渲染，错误保持可见用于验收。 */
(function(){
function renderMath(){
if(!window.katex)return;
document.querySelectorAll('.arithmatex').forEach(function(el){
if(el.dataset.rendered)return;
let s=el.textContent.trim();const d=s.startsWith('\\[')||s.startsWith('$$');
if(s.startsWith('\\(')||s.startsWith('\\[')||s.startsWith('$$'))s=s.slice(2,-2);else if(s.startsWith('$'))s=s.slice(1,-1);
try{window.katex.render(s,el,{displayMode:d,throwOnError:true,strict:'warn'});el.dataset.rendered='true';}
catch(e){el.classList.add('math-error');el.title=e.message;}
});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',renderMath);else renderMath();
})();
