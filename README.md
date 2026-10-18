# language_for_llm

AI が使うプログラミング言語を、理論として詰め、作るための作業場。出発点の目的は「勉強したい」だったが、この作業場は言語を作るために開かれた。理論を詰めるか、実装に進むかは著者が決める。

## 中心の問い

人間が中身を読まない前提で、自然言語から機械語までを、**何を省いたかを宣言し、粗い概念から細かい概念へ滑らかに降りられる**形でつなげるか。

- 抽象化は情報を捨てる圧縮。捨てたものと、その下へ降りる道を、言語が強制する
- 一つの語は複数の概念を覆う。概念を事例の集合として持ち、粗いままテストが通る間は粗く使い、落ちた領域だけ割る（CEGAR に近いが、そのままでは足りない4点がある）
- 型付きで、機械語まで精度を保つ。C のような未定義動作を終点にしない
- 非機能要件（メモリ安全、定数時間性、費用）も、段を下りて保たれる

## 構成

| 場所 | 内容 |
|---|---|
| [docs/00_scope.md](docs/00_scope.md) | 目的、扱わないもの、著者が示した前提 |
| [docs/01_discussion.md](docs/01_discussion.md) | 議論のまとめ（根拠の種類つき） |
| [docs/02_requirements.md](docs/02_requirements.md) | 言語への要求38項目と重み |
| [docs/03_evaluation.md](docs/03_evaluation.md) | 15言語の評価と得点（単純・重み付き） |
| [docs/04_references.md](docs/04_references.md) | 出典（確認／記憶の区分） |
| [docs/05_open_questions.md](docs/05_open_questions.md) | 未解決の問い |
| [docs/06_core.md](docs/06_core.md) | 核の骨組み（決まったことの表） |
| [docs/07_overview.md](docs/07_overview.md) | この言語は何をするものか（決まった範囲の文章と、未決の表） |
| `data/` | 要求と評価の実体（CSV） |
| `tools/` | 集計（`score.py`）と表の再生成（`build_docs.py`） |
| [LOG.md](LOG.md) | 作業の履歴 |
| [CLAUDE.md](CLAUDE.md) | Claude Code への指示 |

## 現在の到達点

- 38の要求を整理し、15言語を ◎○△× で評価した。重み付きの最高は Lean 4（48%）、ほぼ並んで F\*（48%）、次いで Dafny（42%）。主流言語では Rust（35%）が最高
- 15言語すべてが満たさない項目：落ちた理由の3択の区別、細かさと確からしさの軸、非機能性質の保存の種類の宣言
- **評価は記憶にもとづく。** 裏取りは [docs/05_open_questions.md](docs/05_open_questions.md) の B

## 使い方

```bash
python3 tools/score.py              # 順位表
python3 tools/score.py --lang Lean  # 1言語の失点項目
python3 tools/build_docs.py         # CSV を直したあと、docs の表を作り直す
```
