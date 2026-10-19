#!/usr/bin/env python3
"""Offline smoke checks for site metadata, links, translations and the original CV."""
import hashlib,json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.refs=[];self.lang=None;self.h1=0;self.canonical=[];self.alternates=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if tag=='h1':self.h1+=1
  if a.get('id'):self.ids.append(a['id'])
  if tag in ('a','link','script','img') and (a.get('href') or a.get('src')):self.refs.append(a.get('href') or a['src'])
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if tag=='link' and a.get('rel')=='alternate':self.alternates.append(a.get('hreflang'))
for filename,lang in [('index.html','en'),('ru/index.html','ru')]:
 file=ROOT/filename;text=file.read_text(encoding='utf-8');p=Page();p.feed(text)
 assert p.lang==lang and p.h1==1
 assert len(p.ids)==len(set(p.ids))
 assert len(p.canonical)==1 and set(p.alternates)=={'en','ru','x-default'}
 assert 'Vladimir Latypov' in text and 'Владимир Латыпов' in text
 assert 'mailto:donrumata03@gmail.com' in text and 'tel:+79995163856' in text
 assert 'https://t.me/donRumata03' in text and 'https://amdm.ru/users/donRumata03/songs/' in text
 assert 'https://www.linkedin.com/in/don-rumata-558842353/' in text
 assert ('Дисклеймер:' in text)==(lang=='ru')
 assert 'Делиться тем, что изучаю' not in text
 start=text.index('<script type="application/ld+json">')+len('<script type="application/ld+json">')
 json.loads(text[start:text.index('</script>',start)])
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  if not u.path:
   assert u.fragment in p.ids,ref
   continue
  target=ROOT/u.path.lstrip('/') if u.path.startswith('/') else file.parent/unquote(u.path)
  if target.is_dir():target=target/'index.html'
  assert target.exists(),f'{filename}: missing {ref}'
 print('PASS',filename,'languages, metadata, local links and contacts')
cv=(ROOT/'assets/vladimir-latypov-cv.pdf').read_bytes()
assert cv.startswith(b'%PDF-')
assert hashlib.sha256(cv).hexdigest()=='5b262974b89a5f2b39d031314cd2c8242c3123e8cc52d3e03690e7673ffd3205'
ET.parse(ROOT/'sitemap.xml')
print('PASS sitemap and byte-identical original CV')
