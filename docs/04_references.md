# 出典

根拠の種類を3つに分ける。

- **確認（要旨）** … 検索で存在を確かめ、要旨か紹介ページまで読んだ。本文は通読していない
- **確認（実機）** … 自分で動かして確かめた
- **記憶** … Claude の知識（2026年6月までの記憶）で、確かめていない。**使う前に検索で確かめる**

## 検索で存在を確認したもの

| 文献 | 用途 | 状態 |
|---|---|---|
| SimPy "AI Coders Are Among Us"（arXiv 2404.16333） | トークン節約：Python と可逆に変換し最大34.7%減 | 確認（要旨） |
| Wu・Anderson・Guha "Tokenmaxxing"（Northeastern） | 慣れない言語でエージェントが Python に戻る。言語ごとのトークン量 | 確認（要旨）。言語ごとの数値と順位は未確認 |
| Ronacher "A Language For Agents"（2026-02） | AI に書きやすい言語設計の経験則 | 確認。計測ではなく本人の経験と推論 |
| CangjieBench（arXiv 2603.14501） | 資料の少ない言語の評価。制約付き生成が精度と費用の釣り合いで最良 | 確認（要旨） |
| CodeRise（ACL 2026 Findings） | 自己デバッグを重ねる段階的な学習 | 確認（要旨） |
| FSE 2026 のサーベイ（低資源・領域特化言語のコード生成） | 全体像 | 確認（題名・概要） |
| Kilgarriff 1997 "I don't believe in word senses"（arXiv cmp-lg/9712006） | 語義は離散的でない | 確認（要旨） |
| Kilgarriff 1992 Polysemy（Sussex CSRP 261） | 多義は自然な種類ではない | 確認（紹介） |
| Navigli 2009 "Word Sense Disambiguation: A Survey"（ACM Computing Surveys 41(2)） | 語義曖昧性解消の総説 | 確認（存在） |
| OntoNotes / Palmer ら | 注釈者一致率90%以上で語義を統合 | 確認（紹介ページ） |
| Computational Linguistics Journal の多義性の総説 | 同音異義・多義・曖昧さの区別 | 確認（題名のみ） |
| Temerko ら CoNLL 2025 | 規則的多義と言語モデルの驚き度 | 確認（要旨） |
| Kugler 2025（arXiv 2511.21334） | 語義を埋め込みのクラスタで定義 | 確認（要旨） |

## 実機で確かめたもの

| 内容 | 状態 |
|---|---|
| Dafny 4.11.0 で、`Max`・`Withdraw` 等の検証と、性質を抜いた版の判定（[01_discussion.md](01_discussion.md) 5） | 確認（実機）。Dafny の導入先は会話用の一時フォルダで、このリポジトリには無い |
| 注：Dafny の zip を展開すると z3 の実行権が落ちる（`chmod +x z3/bin/*` が要った） | 確認（実機） |

## 記憶のみ（未確認）

| 分野 | 内容 |
|---|---|
| 検証・抽象化 | CEGAR（Clarke ら、2000）、SLAM、BLAST、遅延抽象化（Henzinger ら、2002）、CEGIS（Solar-Lezama）、抽象解釈（Cousot）、漸進的型付け（Siek と Taha）、漸進的検証（Bader・Aldrich・Tanter 2018、Gradual C0）、Liquid Types、Wirth の段階的精緻化、Event-B と Rodin、形式概念分析（Ganter・Wille） |
| 検査 | Knight と Leveson（1986）、translation validation、Alive2、Spolsky「漏れる抽象化の法則」、Eiffel の契約による設計 |
| 型と機械語 | TIL、GHC Core、型付きアセンブラ（TAL、Morrisett ら 1999）、CompCert、CakeML、seL4 の C から機械語への translation validation（Sewell・Myreen・Klein 2013）、Vale・HACL\*・Low\*・KaRaMeL、Bedrock、Jasmin、Sail（ISA 仕様） |
| 安全な終点 | Cyclone、CHERI、WebAssembly |
| 非機能 | 安全なコンパイル（Abate ら "Journey Beyond Full Abstraction"）、ハイパー性質（Clarkson・Schneider）、定数時間を保存する CompCert 拡張（Barthe ら、POPL 2020）、WCET（aiT）、型による資源解析（RAML） |
| 言語学 | Pustejovsky "The Generative Lexicon"（1995）、Wierzbicka の NSM、Cruse "Lexical Semantics"（1986）、Wüster と ISO 704 |
| その他 | Meta の LLM Compiler（2024）、EnerJ、`Uncertain<T>`、Koka、Unison、Lean 4 が C 経由でバイナリを作ること、各言語の機能（[03_evaluation.md](03_evaluation.md) の評価はすべてこの区分） |

次に調べる優先順は [05_open_questions.md](05_open_questions.md)。
