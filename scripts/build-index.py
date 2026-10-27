import os,re,json,shutil,subprocess,html
S='_site';shutil.rmtree(S,ignore_errors=True)
shutil.copytree('.',S,ignore=shutil.ignore_patterns('.git','.github','scripts','_site'))
items=[]
for d in os.listdir('.'):
    p=os.path.join(d,'index.html')
    if d.startswith(('.','_')) or not os.path.isfile(p): continue
    t,desc=d,''
    m=re.search(r'<title>(.*?)</title>',open(p,encoding='utf-8',errors='ignore').read(),re.S|re.I)
    if m: t=m.group(1).strip()
    if os.path.isfile(os.path.join(d,'meta.json')):
        j=json.load(open(os.path.join(d,'meta.json'),encoding='utf-8')); t=j.get('title',t); desc=j.get('description','')
    ts=subprocess.run(['git','log','-1','--format=%ct','--',d],capture_output=True,text=True).stdout.strip() or '0'
    items.append((int(ts),d,t,desc))
items.sort(reverse=True)
import datetime
li=''.join(f'<li><a href="{html.escape(d)}/">{html.escape(t)}</a> <code>{html.escape(d)}/</code> <small>{datetime.datetime.fromtimestamp(ts,datetime.timezone(datetime.timedelta(hours=8))):%Y-%m-%d %H:%M}</small>{"<br>"+html.escape(desc) if desc else ""}</li>\n' for ts,d,t,desc in items)
open(f'{S}/index.html','w',encoding='utf-8').write(f'<!doctype html><meta charset="utf-8"><meta name=viewport content="width=device-width"><title>hubgork pages</title><h1>hubgork 预览目录</h1><ul>\n{li}</ul>')
print(len(items),'entries')
