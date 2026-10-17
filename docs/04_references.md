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

## 書誌を検索で確認したもの（2026-10-17、検証・抽象化の12件）

調査は `researcher`（Haiku）で、**検索結果のスニペットと書誌ページまで**。本文は通読していない。8番だけ本体が arXiv のページを開いて確かめた。

| 文献 | 確かめた書誌 | 状態 |
|---|---|---|
| CEGAR | Clarke・Grumberg・Jha・Lu・Veith, CAV 2000, LNCS 1855 | 確認（書誌） |
| SLAM | Ball・Rajamani（SPIN 2001 ほか）。Static Driver Verifier の基盤 | 確認（要旨） |
| BLAST | Henzinger ら "Lazy Abstraction" から派生。SPIN 2003 の紹介論文 | 確認（要旨） |
| 遅延抽象化 | Henzinger・Jhala・Majumdar・Sutre, POPL 2002, pp.58–70 | 確認（書誌） |
| CEGIS | Solar-Lezama の博士論文 2008（UCB/EECS-2008-177）。**CEGIS という用語をここで導入したかは未確認** | 確認（要旨）。用語の初出は未確認 |
| 抽象解釈 | Cousot・Cousot, POPL 1977, pp.238–252 | 確認（書誌） |
| 漸進的型付け | Siek・Taha, Scheme Workshop 2006 | 確認（要旨） |
| 漸進的検証 | Bader・Aldrich・Tanter, "Gradual Program Verification", VMCAI 2018。**訂正：Gradual C0 はこの論文ではなく DiVincenzo ら10名の別の論文**（arXiv 2210.02428、2022年投稿のプレプリント。POPL 2025 採録は researcher の報告のみで未確認） | 確認（要旨）。arXiv は本体が開いた |
| Liquid Types | Rondon・Kawaguchi・Jhala, PLDI 2008, pp.159–169 | 確認（書誌） |
| 段階的精緻化 | Wirth, CACM 14(4), 1971, pp.221–227 | 確認（要旨） |
| Event-B と Rodin | Abrial らの Event-B。Rodin は Abrial ら, STTT 2010。著者リストの細部は未確認 | 確認（要旨） |
| 形式概念分析 | Ganter・Wille, Springer 1999（独語原書 1996） | 確認（書誌） |

## 実機で確かめたもの

| 内容 | 状態 |
|---|---|
| Dafny 4.11.0 で、`Max`・`Withdraw` 等の検証と、性質を抜いた版の判定（[01_discussion.md](01_discussion.md) 5） | 確認（実機）。Dafny の導入先は会話用の一時フォルダで、このリポジトリには無い |
| 注：Dafny の zip を展開すると z3 の実行権が落ちる（`chmod +x z3/bin/*` が要った） | 確認（実機） |

## 記憶のみ（未確認）

| 分野 | 内容 |
|---|---|
| 検査 | Knight と Leveson（1986）、translation validation、Alive2、Spolsky「漏れる抽象化の法則」、Eiffel の契約による設計 |
| 型と機械語 | TIL、GHC Core、型付きアセンブラ（TAL、Morrisett ら 1999）、CompCert、CakeML、seL4 の C から機械語への translation validation（Sewell・Myreen・Klein 2013）、Vale・HACL\*・Low\*・KaRaMeL、Bedrock、Jasmin、Sail（ISA 仕様） |
| 安全な終点 | Cyclone、CHERI、WebAssembly |
| 非機能 | 安全なコンパイル（Abate ら "Journey Beyond Full Abstraction"）、ハイパー性質（Clarkson・Schneider）、定数時間を保存する CompCert 拡張（Barthe ら、POPL 2020）、WCET（aiT）、型による資源解析（RAML） |
| 言語学 | Pustejovsky "The Generative Lexicon"（1995）、Wierzbicka の NSM、Cruse "Lexical Semantics"（1986）、Wüster と ISO 704 |
| その他 | Meta の LLM Compiler（2024）、EnerJ、`Uncertain<T>`、Koka、Unison、Lean 4 が C 経由でバイナリを作ること、各言語の機能（[03_evaluation.md](03_evaluation.md) の評価はすべてこの区分） |

次に調べる優先順は [05_open_questions.md](05_open_questions.md)。
