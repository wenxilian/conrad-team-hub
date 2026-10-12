"""使用已有 Playwright 和浏览器，检查全部正文与两个部署路径；不装浏览器。"""
from pathlib import Path
import json,time
from playwright.sync_api import sync_playwright
r=Path(__file__).resolve().parents[1];out={'pages':[],'errors':[],'bad_responses':[],'external_requests':[]}
pages=json.loads((r/'planning/page-index.json').read_text(encoding='utf-8'))
screens=r/'tmp/browser-qa';screens.mkdir(parents=True,exist_ok=True)
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True)
 c=b.new_context(viewport={'width':1440,'height':1000})
 c.route('**/*',lambda route:route.continue_() if route.request.url.startswith('http://127.0.0.1:') or route.request.url.startswith('data:') else (out['external_requests'].append(route.request.url),route.abort())[-1])
 p=c.new_page()
 p.on('pageerror',lambda e:out['errors'].append(str(e)))
 p.on('response',lambda resp:out['bad_responses'].append({'url':resp.url,'status':resp.status}) if resp.status>=400 else None)
 reps=['index.md','01-overview/rules.md','01-overview/timeline.md','01-overview/submissions.md','02-projects/fireaidss.md','02-projects/aphelion.md','02-projects/beeguard.md','03-engineering/rescuebot.md','04-business/market-research.md','04-business/competition.md','04-business/calculators.md','05-team/mentors.md','06-planning/stage-gates.md','07-resources/templates.md','07-resources/visual-tools.md']
 for base in ['http://127.0.0.1:8001/conrad-team-hub/','http://127.0.0.1:8002/']:
  for src in pages:
   url=base+src.replace('.md','.html')
   p.goto(url,wait_until='networkidle')
   row=p.evaluate("""() => ({title:document.querySelector('h1')?.innerText, math:document.querySelectorAll('.arithmatex').length,math_errors:[...document.querySelectorAll('.math-error')].map(x=>x.title),rendered:document.querySelectorAll('.arithmatex[data-rendered]').length,scroll:document.documentElement.scrollWidth,width:window.innerWidth})""")
   row.update({'page':src,'base':base,'viewport':'desktop'});out['pages'].append(row)
  for src in reps:
   p.set_viewport_size({'width':375,'height':812});p.goto(base+src.replace('.md','.html'),wait_until='networkidle')
   row=p.evaluate("""() => ({title:document.querySelector('h1')?.innerText,math_errors:[...document.querySelectorAll('.math-error')].map(x=>x.title),scroll:document.documentElement.scrollWidth,width:window.innerWidth,tables:document.querySelectorAll('table').length})""")
   row.update({'page':src,'base':base,'viewport':'mobile'});out['pages'].append(row)
   if base.endswith('8002/') and src in ['index.md','04-business/calculators.md','02-projects/aphelion.md']:
    p.screenshot(path=str(screens/(src.split('/')[-1].replace('.md','')+'-mobile.png')),full_page=True)
  p.set_viewport_size({'width':1440,'height':1000})
  p.goto(base+'04-business/calculators.html',wait_until='networkidle')
  result=p.evaluate("""() => ({saas:ConradModels.saas.calc({n:300,p:10,v:2}),hardware:ConradModels.hardware.calc({p:150,v:90,f:12000,q:300}),household:ConradModels.household.calc({p:600,s:240,t:5}),bad_margin:ConradModels.hardware.calc({p:90,v:90,f:12000,q:300})})""")
  assert result['saas']['revenue']==36000 and result['saas']['contribution']==28800
  assert result['hardware']['profit']==6000 and result['hardware']['breakEven']==200
  assert result['household']['payback']==2.5 and result['household']['net']==600
  assert result['bad_margin']['breakEven'] is None
  p.locator('[data-model="household"] input[data-key="p"]').fill('1200')
  p.locator('[data-model="household"] input[data-key="p"]').dispatch_event('input')
  assert '5 年' in p.locator('[data-model="household"] .result').inner_text()
  assert '刚好' in p.locator('[data-model="household"] .result').inner_text()
  p.locator('[data-model="household"] button').click()
  assert '2.5 年' in p.locator('[data-model="household"] .result').inner_text()
  p.locator('[data-model="hardware"] input[data-key="q"]').fill('200')
  p.locator('[data-model="hardware"] input[data-key="q"]').dispatch_event('input')
  assert '简化利润：0 美元' in p.locator('[data-model="hardware"] .result').inner_text()
  p.locator('[data-model="hardware"] button').click()
  out.setdefault('calculator_checks',[]).append({'base':base,'defaults':result,'slider_reset_and_break_even':'passed'})
  p.goto(base+'index.html',wait_until='networkidle')
  p.locator('input.md-search__input').fill('BeeGuard')
  p.wait_for_function("document.querySelector('.md-search-result__list')?.innerText.includes('BeeGuard')",timeout=15000)
  out.setdefault('search_checks',[]).append({'base':base,'query':'BeeGuard','results':p.locator('.md-search-result__list').inner_text()[:500]})
  if base.endswith('8002/'):p.keyboard.press('Escape');p.screenshot(path=str(screens/'home-desktop.png'),full_page=True)
 b.close()
out['failed_pages']=[x for x in out['pages'] if not x['title'] or x.get('math_errors') or x['scroll']>x['width']+2 or (x.get('math',0)!=x.get('rendered',0))]
out['passed']=not(out['failed_pages'] or out['errors'] or out['bad_responses'] or out['external_requests'])
(r/'logs').mkdir(exist_ok=True)
(r/'logs/browser-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='pages'},ensure_ascii=False,indent=2))
raise SystemExit(0 if out['passed'] else 1)
