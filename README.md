# ImageConverter

## 概要と背景

最近、`.webp`という拡張子の画像ファイルに出会うことが増えてきました。

どこで出会うかというと、アングラなネットを徘徊する**青年男性**なら分かるかと思います。

ちなみにラオス(.la)のドメインを採用しているサイトです。
[.la - Wikipedia](https://ja.wikipedia.org/wiki/.la)

と、読者が十分にドン引きしたと思いますので、さっさと本題に入ります。

## 「やりたいこと」と「ソリューション」

- 特定のフォルダ配下すべての`.webp`を変換したい。
  - `os.glob`で再帰的に検索する。
- (大抵)連番で保存されているので、ファイル名は変えたくない。
  - 拡張子が変われば重複判定にならない。
- 何を変換したのかログファイルを出力したい。
  - 実装する。
- 対象のディレクトリで簡単実行したい。
  - `__file__`から`os.glob`キーを作成する。
- Pythonの環境のないマシンでも実行したい。
  - `Pyinstaller`を活用する。

# 更新履歴

- プライベートリポジトリをPublicに変更