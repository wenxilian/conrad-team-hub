"""检查双平台静态产物的本地链接、锚点、资源和隐私边界。"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,sys
r=Path(__file__).resolve().parents[1]
class Scan(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.refs=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if d.get('id'):self.ids.add(d['id'])
  for a in ['href','src']:
   if d.get(a):self.refs.append((tag,a,d[a]))
def validate(directory):
 scans={}
 for p in directory.rglob('*.html'):
  s=Scan();s.feed(p.read_text(encoding='utf-8'));scans[p.resolve()]=s
 broken=[];anchors=[];external_assets=[]
 for p,s in scans.items():
  for tag,a,url in s.refs:
   u=urlsplit(url)
   if u.scheme or u.netloc:
    if a=='src' or tag=='script' or (tag=='link' and u.path.endswith('.css')):external_assets.append([str(p.relative_to(directory)),url])
    continue
   if not u.path:target=p
   elif u.path.startswith('/'):
    prefix='/conrad-team-hub/' if directory.name=='conrad-team-hub' else '/'
    if not u.path.startswith(prefix):
     broken.append([str(p.relative_to(directory)),url,'wrong deployment prefix']);continue
    target=(directory/unquote(u.path[len(prefix):])).resolve()
   else:target=(p.parent/unquote(u.path)).resolve()
   if target.is_dir():target=target/'index.html'
   if not target.exists():broken.append([str(p.relative_to(directory)),url,'not found'])
   elif u.fragment and target.suffix=='.html' and unquote(u.fragment) not in scans.get(target,Scan()).ids:
    anchors.append([str(p.relative_to(directory)),url])
 # CSS 字体引用也逐个核查。
 for p in directory.rglob('*.css'):
  for url in re.findall(r'url\(([^)]+)\)',p.read_text(encoding='utf-8')):
   url=url.strip(' "\'');u=urlsplit(url)
   if u.scheme or u.netloc:continue
   if not (p.parent/unquote(u.path)).exists():broken.append([str(p.relative_to(directory)),url,'CSS asset missing'])
 return {'html_pages':len(scans),'broken_links':broken,'missing_anchors':anchors,'external_runtime_assets':external_assets}
out={}
for name in ['github/conrad-team-hub','aliyun']:
 d=(r/'dist'/name).resolve()
 if not d.exists():raise SystemExit('请先运行 tools/build.py')
 out[name]=validate(d)
findings=[]
patterns=[r'[A-Z]:\\',r'Administrator',r'与当前团队研究范围',r'随着项目实际面向',r'两位专业家长',r'gh[pousr]_[A-Za-z0-9]{20,}',r'AKIA[A-Z0-9]{16}']
for p in (r/'docs').rglob('*.md'):
 if 'vendor' in p.parts:continue
 t=p.read_text(encoding='utf-8')
 for x in patterns:
  if re.search(x,t):findings.append({'file':p.relative_to(r).as_posix(),'pattern':x})
out['sensitive_pattern_findings']=findings
out['content_pages']=len([p for p in (r/'docs').rglob('*.md') if 'assets' not in p.parts])
out['financial_recalculation']={'saas_revenue':12*300*10,'saas_contribution':12*300*(10-2),'hardware_break_even':12000/(150-90),'hardware_profit':(150-90)*300-12000,'household_payback':600/240,'household_net':5*240-600,'bom_total':60+2*25+40+30+30+20,'scenario_profits':[(180-140)*100-20000,(200-120)*200-20000,(220-110)*300-20000]}
(r/'logs').mkdir(exist_ok=True)
(r/'logs/static-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
failed=bool(findings) or any(v['broken_links'] or v['missing_anchors'] or v['external_runtime_assets'] for k,v in out.items() if k in ['github/conrad-team-hub','aliyun'])
print(json.dumps({'passed':not failed,'profiles':{k:{'html_pages':v['html_pages'],'broken_links':len(v['broken_links']),'missing_anchors':len(v['missing_anchors']),'external_runtime_assets':len(v['external_runtime_assets'])} for k,v in out.items() if k in ['github/conrad-team-hub','aliyun']},'sensitive_findings':findings},ensure_ascii=False))
sys.exit(1 if failed else 0)
