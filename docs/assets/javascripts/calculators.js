/* 全部参数为教学模拟。输入、结果和复位共用一套计算函数。 */
(function(){
const models={
saas:{fields:[['n','付费用户数 (人)',300,100,2000,10],['p','月费 (美元)',10,5,30,1],['v','单位月变动成本 (美元)',2,1,10,1]],calc:x=>({revenue:12*x.n*x.p,contribution:12*x.n*(x.p-x.v)})},
hardware:{fields:[['p','售价 (美元/台)',150,50,300,10],['v','单位变动成本 (美元/台)',90,10,200,10],['f','固定成本 (美元)',12000,0,30000,1000],['q','销量 (台)',300,0,600,10]],calc:x=>({revenue:x.p*x.q,cost:x.f+x.v*x.q,profit:(x.p-x.v)*x.q-x.f,breakEven:x.p>x.v?Math.ceil(x.f/(x.p-x.v)):null})},
household:{fields:[['p','购买安装价 (元)',600,100,2000,50],['s','年度净节约 (元/年)',240,20,600,20],['t','使用寿命 (年)',5,1,10,1]],calc:x=>({payback:x.p/x.s,net:x.t*x.s-x.p})}
};window.ConradModels=models;
const f=x=>Number(x).toLocaleString('zh-CN',{maximumFractionDigits:2});
function chart(a,b,la,lb,unit){
const all=a.concat(b),xm=Math.max(1,...all.map(p=>p[0])),yn=Math.min(0,...all.map(p=>p[1])),ym=Math.max(1,...all.map(p=>p[1]));
const px=x=>65+x/xm*440,py=y=>200-(y-yn)/(ym-yn)*160,line=p=>p.map(v=>px(v[0])+','+py(v[1])).join(' ');
return '<svg viewBox="0 0 560 255" role="img" aria-label="'+la+'与'+lb+'，'+unit+'"><line x1="65" x2="505" y1="'+py(0)+'" y2="'+py(0)+'" stroke="#94a3b8"/><line x1="65" x2="65" y1="40" y2="200" stroke="#94a3b8"/><polyline fill="none" stroke="#1d4ed8" stroke-width="3" points="'+line(a)+'"/><polyline fill="none" stroke="#b45309" stroke-width="3" stroke-dasharray="7 4" points="'+line(b)+'"/><g font-size="12" fill="#334155"><text x="2" y="35">'+f(ym)+'</text><text x="2" y="205">'+f(yn)+'</text><text x="65" y="220">0</text><text x="480" y="220">'+f(xm)+'</text><text x="65" y="243" fill="#1d4ed8">'+la+'</text><text x="315" y="243" fill="#b45309">'+lb+'</text></g></svg>';
}
function init(){document.querySelectorAll('.calculator').forEach((r,idx)=>{
if(r.dataset.ready)return;r.dataset.ready='true';const k=r.dataset.model,m=models[k];if(!m)return;
r.innerHTML='<p><strong>教学模拟</strong>：输入参数不代表实际经营。</p>'+m.fields.map(([key,l,v,min,max,step])=>'<label for="c-'+idx+'-'+key+'">'+l+'：<output data-for="'+key+'">'+v+'</output><input id="c-'+idx+'-'+key+'" data-key="'+key+'" type="range" min="'+min+'" max="'+max+'" step="'+step+'" value="'+v+'"></label>').join('')+'<div class="result" aria-live="polite"></div><div class="chart"></div><button type="button">恢复初值</button>';
const update=()=>{
const x={};r.querySelectorAll('input').forEach(i=>{x[i.dataset.key]=Number(i.value);r.querySelector('[data-for="'+i.dataset.key+'"]').textContent=f(Number(i.value));});
const y=m.calc(x),out=r.querySelector('.result'),c=r.querySelector('.chart');
if(k==='saas'){out.innerHTML='年收入：'+f(y.revenue)+' 美元<br>年边际贡献：'+f(y.contribution)+' 美元 (未扣固定费用)';c.innerHTML=chart([[0,0],[x.n,y.revenue]],[[0,0],[x.n,y.contribution]],'年收入','年边际贡献','横轴用户数；纵轴美元')+'<p class="chart-caption">横轴：用户数；纵轴：年度美元金额。</p>';}
else if(k==='hardware'){out.innerHTML='收入：'+f(y.revenue)+' 美元；总成本：'+f(y.cost)+' 美元<br>简化利润：'+f(y.profit)+' 美元<br>'+(y.breakEven===null?'售价不高于单位变动成本：不存在正销量盈亏平衡点。':'盈亏平衡所需销量：'+f(y.breakEven)+' 台');c.innerHTML=chart([[0,0],[600,x.p*600]],[[0,x.f],[600,x.f+x.v*600]],'收入','总成本','横轴销量台；纵轴美元')+'<p class="chart-caption">横轴：销量 (台)；纵轴：美元。</p>';}
else{const status=y.payback<x.t?'回收期早于寿命期':y.payback===x.t?'寿命期末刚好回收初始投入':'寿命期内未能回收初始投入';out.innerHTML='静态回收期：'+f(y.payback)+' 年<br>寿命期简单净节约：'+f(y.net)+' 元<br>'+status;c.innerHTML=chart([[0,0],[x.t,x.t*x.s]],[[0,x.p],[x.t,x.p]],'累计节约','初始支出','横轴年；纵轴元')+'<p class="chart-caption">横轴：年；纵轴：元。差额示意，未贴现、未计残值及额外维修。</p>';}
};r.addEventListener('input',update);r.querySelector('button').addEventListener('click',()=>{m.fields.forEach(([key,l,v])=>r.querySelector('[data-key="'+key+'"]').value=v);update();});update();
});}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
