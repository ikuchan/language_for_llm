# 作業の履歴

新しいものを下に。1行ずつ。

- 2026-10-17 リポジトリを開始。これまでの議論（目的の整理、入口・出口・実行の枠、出口の検査、省略の宣言と降下の道、概念の識別、CEGAR の不足4点、型と機械語、非機能要件）を `docs/` にまとめた
- 2026-10-17 要求31項目（`data/requirements.csv`）と、15言語の評価（`data/evaluation.csv`）を作成。得点は `tools/score.py` で再現できる
- 2026-10-17 会話中の誤りを記録：最大値の「常に 1000000 を返す」弱い仕様の抜け道は、通過ではなく拒否だった（`docs/01_discussion.md` 5 で訂正）
- 2026-10-17 Dafny 4.11.0 を会話用の一時フォルダに導入して検証した。このリポジトリには入れていない
- 2026-10-17 複数モデルの使い分けを追加（.claude/agents に Explore/researcher=Haiku、worker=Sonnet。ObsidianMemo の運用設定15の仕組みのみ移植、私的内容は不使用）
- 2026-10-17 出典の記憶区分のうち検証・抽象化の12件を researcher で検索確認し、04_references.md に移した。訂正：Gradual C0 は Bader らの 2018 年論文ではなく DiVincenzo ら（arXiv 2210.02428）
- 2026-10-17 出典の記憶区分のうち型と機械語の13件を researcher で検索確認し、04_references.md に移した。KaRaMeL と Sail の論文は未確認のまま
