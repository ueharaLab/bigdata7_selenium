NEWS LAB 第3版（ビジュアル強化版）

【起動】
1. ZIPを解凍し、local_news_xpath_lab_v3 フォルダに移動します。
2. python server.py
3. http://127.0.0.1:8000/ を開きます。

【Selenium演習】
別ターミナルで python ensyu_mottomiru_answer_v2.py
AIで検索：最初の10件＋「もっと見る」5回×10件＝計60件

【第2版からの改良】
・記事ごとの写真風サムネイル（オリジナルSVGイラスト）、トップの特集カード、ランキング、カテゴリーバー。
・画像は static/images 内に保存。外部ネットワーク接続不要。
・XPath演習の対象となる検索 input[name="search_term"]、記事 section[data-zone="bulletins"] > div.bulletin-entry > article、
  ボタン footer#feedActions > div > button > strong は第2版から変更していません。
・変更したHTMLはデザインに関する部分だけです。

【注意】
・使用画像は写真ではなくオリジナルの写真風イラストです。写真そのものを複製した素材ではありません。
・架空ニュースです。実在メディアのロゴ、記事、写真の複製はありません。
・旧サーバーが起動中なら Ctrl+C で止めてから新しく起動してください。

【第4版の変更】
ニュースポータル型のレイアウトに変更し、トップ記事写真・ニュース一覧写真・ランキング写真を追加しました。
写真はオフライン表示可能なローカル同梱素材で、scikit-image配布のサンプル画像を使用しています。
XPath（検索 search_term、記事 section[data-zone="bulletins"]、ボタン footer#feedActions）は第2版と同じです。
もし古い画面が表示される場合は、古い server.py を Ctrl+C で終了し、第4版フォルダ内で python server.py を実行してください。
