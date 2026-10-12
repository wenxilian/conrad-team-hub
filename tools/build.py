"""严格构建双平台；仅打包静态文件，不包含内部资料。"""
from pathlib import Path
import subprocess,sys,zipfile,json,hashlib
from datetime import datetime,timezone,timedelta
r=Path(__file__).resolve().parents[1]
for c in ['mkdocs.github.yml','mkdocs.aliyun.yml']:
 subprocess.run([sys.executable,'-m','mkdocs','build','--strict','-f',c],cwd=r,check=True)
try:
 source_commit=subprocess.check_output(['git','-c','safe.directory='+r.as_posix(),'rev-parse','HEAD'],cwd=r,stderr=subprocess.DEVNULL,text=True).strip()
except (subprocess.CalledProcessError,FileNotFoundError):
 source_commit='unknown'
now=datetime.now(timezone(timedelta(hours=8)))
p=r/'dist'/('conrad-team-hub-aliyun-'+now.strftime('%Y%m%d-%H%M%S')+'.zip')
with zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED) as z:
 for f in (r/'dist/aliyun').rglob('*'):
  if f.is_file():z.write(f,f.relative_to(r/'dist/aliyun').as_posix())
(r/'dist/build-manifest.json').write_text(json.dumps({'built_at':now.isoformat(),'archive':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_commit':source_commit,'publication':'local review only; not published'},indent=2),encoding='utf-8')
print(p)
