/* 三情景利润图：从原参数计算，保留亏损与零点。 */
(function(){
function init(){document.querySelectorAll('[data-scenario-chart]').forEach(root=>{
 const rows=[{name:'保守',p:180,q:100,v:140,f:20000},{name:'基准',p:200,q:200,v:120,f:20000},{name:'乐观',p:220,q:300,v:110,f:20000}];
 rows.forEach(x=>x.profit=(x.p-x.v)*x.q-x.f);
 root.innerHTML='<p>教学模拟 · 左：亏损；右：盈利 · 纵向零线在中间</p>'+rows.map(x=>'<div class="scenario-row"><span>'+x.name+'</span><div class="scenario-track" aria-hidden="true"><div class="scenario-bar" style="width:'+Math.abs(x.profit)/16000*48+'%;'+(x.profit<0?'right:50%;background:#b45309':'left:50%;background:#1d4ed8')+'"></div></div><span>'+x.profit.toLocaleString('zh-CN')+' 元</span></div>').join('')+'<label>查看输入情景：<select><option value="0">保守</option><option value="1">基准</option><option value="2">乐观</option></select></label><p class="scenario-note" aria-live="polite"></p>';
 const select=root.querySelector('select'),note=root.querySelector('.scenario-note');
 const update=()=>{const x=rows[Number(select.value)];note.textContent='单价 '+x.p+' 元；销量 '+x.q+' 件；单位变动成本 '+x.v+' 元；固定成本 '+x.f+' 元；利润 '+x.profit+' 元。';};
 select.addEventListener('change',update);update();
});}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
