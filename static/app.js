// 検索結果の追加取得には fetch() を使用。初期HTMLには記事li要素が含まれない。
const query = new URLSearchParams(window.location.search).get('search_term') || '';
const PAGE_SIZE = 10;
let offset = 0;
let loading = false;
const list = document.getElementById('bulletinStream');
const panel = document.getElementById('feedActions');
const button = panel.querySelector('button[data-role="append-news"]');
const input = document.getElementById('queryInput');
input.value = query;
if (query) document.getElementById('pageTitle').textContent = `「${query}」の検索結果`;
function makeArticle(a) {
  const wrapper = document.createElement('div');
  wrapper.className = 'bulletin-entry';
  const article = document.createElement('article');
  article.className = 'dispatch-card';
  const link = document.createElement('a');
  link.className = 'story-link';
  link.href = `/article/${a.id}`;
  const box = document.createElement('div'); box.className = 'story-text';
  const category = document.createElement('span'); category.className = 'category'; category.textContent = a.category;
  const h = document.createElement('h3'); h.className = 'story-title'; h.textContent = a.title;
  const summary = document.createElement('p'); summary.className = 'story-summary'; summary.textContent = a.summary;
  const meta = document.createElement('p'); meta.className = 'meta'; meta.textContent = `${a.source}　${a.time}`;
  box.append(category,h,summary,meta);
  const thumb = document.createElement('img'); thumb.className = 'story-thumb'; thumb.alt = `${a.category}のイメージ画像`; thumb.loading = 'lazy';
  const illustration = ({'食と科学':'food', 'テクノロジー':'tech', '農業':'agri', '地域':'city', '教育':'study', '経済':'economy'})[a.category] || 'tech';
  thumb.src = `/static/images/${illustration}.jpg`;
  link.append(box,thumb); article.append(link); wrapper.append(article);
  return wrapper;
}
async function loadMore() {
  if (loading) return;
  loading = true; button.disabled = true;
  const label = button.querySelector('.button-caption'); label.textContent = '読み込み中…';
  try {
    const res = await fetch(`/api/articles?search_term=${encodeURIComponent(query)}&offset=${offset}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    for (const item of data.items) list.appendChild(makeArticle(item));
    offset = data.next_offset;
    document.getElementById('resultText').textContent = `該当記事 ${data.total} 件 — 10件ずつ追加表示します。`;
    document.getElementById('shownCount').textContent = `${offset} / ${data.total} 件`;
    panel.hidden = !data.has_more;
    document.getElementById('finished').hidden = data.has_more || offset === 0;
    if (data.total===0) {list.innerHTML = '<div class="no-results">該当する記事がありません。別のキーワードを試してください。</div>';panel.hidden=true;}
  } catch (e) {console.error(e);label.textContent='通信エラー：再試行';}
  finally {loading = false;button.disabled = false;if(label.textContent==='読み込み中…')label.textContent='もっと見る';}
}
button.addEventListener('click',loadMore);
loadMore();
