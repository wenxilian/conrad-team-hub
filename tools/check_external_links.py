"""仅检查公开外链可访问性，不把HTTP成功当作事实核实。"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,re,csv,json
r=Path(__file__).resolve().parents[1]
urls=set()
for p in (r/'docs').rglob('*.md'):
 if 'vendor' in p.parts:continue
 for u in re.findall(r'https?://[^\s<>\)]+',p.read_text(encoding='utf-8')):
  urls.add(u.rstrip('。，；.'))
def get(u):
 try:
  resp=requests.get(u,timeout=(6,12),stream=True,allow_redirects=True)
  row={'url':u,'retrieved_date':'2026-10-12','http_status':resp.status_code,'final_url':resp.url,'status':'reachable' if resp.status_code<400 else 'unavailable','note':'URL accessibility only; not claim validation'};resp.close();return row
 except Exception as e:return {'url':u,'retrieved_date':'2026-10-12','http_status':'unknown','final_url':'unknown','status':'access-failed','note':type(e).__name__}
with ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(get,sorted(urls)))
(r/'logs').mkdir(exist_ok=True)
with (r/'logs/external-links.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['url','retrieved_date','http_status','final_url','status','note']);w.writeheader();w.writerows(rows)
print(json.dumps({'total':len(rows),'reachable':sum(x['status']=='reachable' for x in rows),'unconfirmed':[x for x in rows if x['status']!='reachable']},ensure_ascii=False))
