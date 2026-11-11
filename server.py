"""Local news crawler lab — Python standard library only.
Run: python server.py
Open: http://127.0.0.1:8000/
"""
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import json
import mimetypes
import html

BASE = Path(__file__).resolve().parent
ARTICLES = json.loads((BASE / 'articles.json').read_text(encoding='utf-8'))
PAGE_SIZE = 10

def matched(q):
    q = q.strip().casefold()
    if not q:
        return ARTICLES
    return [a for a in ARTICLES if q in (' '.join([a['title'],a['summary'],a['category']]+a['keywords'])).casefold()]

class Handler(BaseHTTPRequestHandler):
    def send(self, body, code=200, content_type='text/html; charset=utf-8'):
        if isinstance(body,str): body=body.encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type',content_type)
        self.send_header('Content-Length',str(len(body)))
        self.send_header('Cache-Control','no-store')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url=urlparse(self.path)
        params=parse_qs(url.query)
        q=params.get('search_term',[''])[0]
        if url.path in ('/','/search'):
            template=(BASE/'static/index.html').read_text(encoding='utf-8')
            self.send(template)
        elif url.path=='/api/articles':
            try: offset=max(0,int(params.get('offset',['0'])[0]))
            except ValueError: offset=0
            matches=matched(q)
            chunk=matches[offset:offset+PAGE_SIZE]
            body=json.dumps({'items':chunk,'total':len(matches),'next_offset':offset+len(chunk),'has_more':offset+len(chunk)<len(matches)},ensure_ascii=False)
            self.send(body,content_type='application/json; charset=utf-8')
        elif url.path.startswith('/article/'):
            try: ident=int(url.path.split('/')[-1])
            except ValueError: ident=-1
            a=next((a for a in ARTICLES if a['id']==ident),None)
            if a is None:
                self.send('記事がありません',404);return
            illustration = {'食と科学':'food','テクノロジー':'tech','農業':'agri','地域':'city','教育':'study','経済':'economy'}.get(a['category'],'tech')
            safe = {k: html.escape(str(v),quote=True) for k,v in a.items()}
            body = f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet" href="/static/style.css"><title>{safe['title']}</title></head><body><header class="site-header"><div class="header-inner container"><a class="logo" href="/">NEWS <em>LAB</em><small>ニュース演習</small></a></div></header><nav class="nav"><div class="nav-inner container"><a href="/">トップ</a><a href="/search?search_term=AI">AI・テクノロジー</a></div></nav><main class="detail"><a href="/">← ニュース一覧へ</a><p><span class="category">{safe['category']}</span></p><h1>{safe['title']}</h1><p class="meta">{safe['source']}　{safe['time']}</p><img class="detail-visual" src="/static/images/{illustration}.jpg" alt="教材用イメージ画像"><p class="lead">{safe['summary']}</p><p>本ページはスクレイピング演習向けの架空記事です。実際の出来事を伝えるものではありません。</p></main></body></html>''' 
            self.send(body)
        elif url.path.startswith('/static/'):
            path=(BASE/url.path.lstrip('/')).resolve()
            if path.is_file() and BASE in path.parents:
                ctype=mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
                if ctype.startswith('text/') or ctype in ('application/javascript','application/json'): ctype+='; charset=utf-8'
                self.send(path.read_bytes(),content_type=ctype)
            else:self.send('Not Found',404)
        else:self.send('Not Found',404)

if __name__=='__main__':
    server=ThreadingHTTPServer(('127.0.0.1',8000),Handler)
    print('演習サイト: http://127.0.0.1:8000/')
    print('終了: Ctrl+C')
    try:server.serve_forever()
    except KeyboardInterrupt:print('\n終了しました')
    finally:server.server_close()
