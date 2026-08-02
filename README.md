# adaptive-reasoning-consensus

凍結 LLM 的**推理期（inference-time）共識演算法**研究倉庫。七個設計、五個基質、
兩個領域的完整紀錄——包含一個存活的演算法、六個死亡的設計，以及一條把它們
全部解釋掉的結構性邊界。

```bash
python3.12 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
./.venv/bin/python -m pytest -q          # 102 tests
```

---

## 一分鐘導覽

| 你想看什麼 | 去哪裡 |
|:--|:--|
| **論文**（IEEE 格式，11 頁） | [paper/tact.pdf](paper/tact.pdf) · [tact.tex](paper/tact.tex) · [tact.docx](paper/tact.docx) |
| **投稿版：TMLR**（雙盲，17 頁） | [tact_tmlr.pdf](paper/tact_tmlr.pdf)（匿名） · [tact_tmlr_preprint.pdf](paper/tact_tmlr_preprint.pdf)（具名） |
| **投稿版：JMLR**（單盲，22 頁） | [tact_jmlr.pdf](paper/tact_jmlr.pdf) · [build_jmlr.py](paper/build_jmlr.py) |
| **論文中文版** | [paper/tact_zh.pdf](paper/tact_zh.pdf) · [.docx](paper/tact_zh.docx) · [.md](paper/tact_zh.md) |
| **公式參數逐項詳解**（中文） | [paper/tact_parameters_zh.pdf](paper/tact_parameters_zh.pdf) · [.docx](paper/tact_parameters_zh.docx) · [.md](paper/tact_parameters_zh.md) |
| **演算法的一行式** | [src/rlev_voi/formula.py](src/rlev_voi/formula.py) |
| **架構：偽碼 ↔ 模組對照** | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| **所有死亡設計與死因** | [docs/GRAVEYARD.md](docs/GRAVEYARD.md) ← 新想法動工前先讀這份 |
| **薄窗結果**（本專案最強的發現） | [docs/REPORT-G1.md](docs/REPORT-G1.md) + GRAVEYARD 的「計畫級綜合」 |

---

## 核心結果

### 存活的演算法：TACT

信心通道的**帶符號**可靠度估計。整條方法收成一個式子：

$$\hat a_q=\arg\max_A \sum_{i:\,a_{q,i}=A}\exp\big(\gamma\,\varphi_{q,i}\big),
\qquad \gamma=z\sqrt{2+z^{2}},\qquad z=\Phi^{-1}(\widehat{\mathrm{AUC}})$$

全式**沒有任何調校常數**。指數 $\gamma$ 由資料導出：訊號不足時恰為 0，
此時投票**位元等同** Self-Consistency。

- 規格：[docs/SPEC-TACT.md](docs/SPEC-TACT.md)　實作：[src/rlev_voi/tact.py](src/rlev_voi/tact.py)、[tempering.py](src/rlev_voi/tempering.py)、[discrimination.py](src/rlev_voi/discrimination.py)
- 一行式與等價性證明：[formula.py](src/rlev_voi/formula.py) + [tests/test_formula.py](tests/test_formula.py)
- 合成結果（四項證偽全過）：[docs/REPORT-TACT.md](docs/REPORT-TACT.md)
- 真實資料結果：[docs/REPORT-TACT-HARD.md](docs/REPORT-TACT-HARD.md)

### 薄窗（結構性邊界）

跨**兩個領域、五個基質**的量測：任何無標籤聚合方法能作用的分層
——多數決錯 **且** 正解在池內——只佔題目的 2.5–7.5%，
且**難度上升不會讓它變寬**（題目直接從「飽和」跳到「正解不可達」）。

| 領域 | 基質 | 窗口 |
|:--|:--|--:|
| 無標籤 QA | GSM8K/CSQA、MATH-L5、AIME/AMC | 2.5–4% |
| 程式碼（可執行真值） | HumanEval+/MBPP+（公開表格重算） | 3.56% |
| 程式碼（可執行真值） | LeetCode Med/Hard（**本專案直接量測**） | 7.5% |

這條邊界解釋了六個設計為什麼會死，也說明 TACT 的**棄權設計**（$\gamma=0$）
在此 régime 下不是保守，而是唯一正確的行為。

---

## 七個設計的下場

| # | 設計 | 結果 | 死因 | 文件 |
|:--|:--|:--|:--|:--|
| 1 | **RLEV-VoI** 冗餘折扣 + VoI 停止 | 負面（實作後） | dedup-SC 同預算全面支配 | [REPORT.md](docs/REPORT.md) |
| 2 | **TACT** 帶符號信心可靠度 | **存活** | — | [REPORT-TACT.md](docs/REPORT-TACT.md) |
| 3 | **ISC** 用驗證器當儀器錨定 | 負面（實作後） | 儀器只貢獻 14%；同/異模型驗證在決定性分層皆失效 | [REPORT-ISC.md](docs/REPORT-ISC.md)、[FINDING](docs/FINDING-instrument-validity.md) |
| 4 | **FIB** frame 不變性誤差下界 | 放棄（實作前） | 被 NIPS 2004 逐字搶發；被 sharp 平凡界支配 | [GRAVEYARD §3](docs/GRAVEYARD.md) |
| 5 | **RLSC** e-process 眾數認證 | 放棄（實作前） | 10 個月內被兩篇獨立論文搶發；lead rule 支配 | [GRAVEYARD §4](docs/GRAVEYARD.md) |
| 6 | **DEC** 分歧處付費的認證 | 放棄（實作前） | 零件全是前例；fixed-n McNemar 檢定力雙倍 | [GRAVEYARD §5](docs/GRAVEYARD.md) |
| 7 | **KAPPA-P** 突變錨定測試可靠度 | 放棄（G1 閘門） | 窗口 7.5% < 閘門 15%；能力牆無法用預算打開 | [SPEC](docs/SPEC-KAPPA-P.md)、[REPORT-G1](docs/REPORT-G1.md)、[STATUS](docs/KAPPA-STATUS.md) |

外加 pool-coverage 方向的六個候選全滅（[GRAVEYARD §6](docs/GRAVEYARD.md)）。
**四個設計在寫程式前就被殺**，各省一個實作週期——這是本專案的標準閘門流程。

---

## 重現實驗

不需要 API key（合成 / 已快取軌跡）：

```bash
./.venv/bin/python experiments/run_tact_eval.py        # TACT headline（合成）
./.venv/bin/python experiments/run_isc_eval.py         # ISC 證偽 + 儀器品質曲線
./.venv/bin/python experiments/run_tact_hard_eval.py   # TACT 真實資料 H1–H5
./.venv/bin/python experiments/run_g1_window.py        # 程式碼領域窗口閘門
./.venv/bin/python experiments/run_g1_deepening.py     # 能力牆確認
./.venv/bin/python experiments/verify_kappa_kill.py    # KAPPA 死因獨立重現
./.venv/bin/python experiments/rlsc_pilot.py           # RLSC 三項 pilot
./.venv/bin/python experiments/make_figures.py         # 所有圖表
```

需要 API key：

```bash
export ANTHROPIC_API_KEY=...
./.venv/bin/python experiments/run_real_api.py --data data/items.jsonl --items 100 --k-max 40
```

---

## 程式碼地圖

```
src/rlev_voi/
  formula.py        ★ TACT 的一行式（閉式，等價性有測試）
  tact.py             TACT 投票、TACT-dev / LF / semi-LF / group
  tempering.py        收縮 + 貝氏判別連結 → 指數 γ
  discrimination.py   vdW 分數、Somers' D、van Elteren 合併
  math_grade.py       LaTeX 答案等價（分桶用正規化、評分用 sympy）
  sandbox.py        ★ 受限子行程執行 LLM 生成的程式碼
  isc.py              ISC（負面結果，保留供引用）
  weights.py          有效權重 n_eff = Σw（Kish 是錯的，見 REPORT）
  posterior.py        Dirichlet 後驗、眾數機率、VoI
  baselines.py        SC / dedup-SC / CISC / ASC / ESC / RASC-lite
  kernel.py           dup / sem 雙通道相似度
  consensus.py        DDWC + never-worse-than-SC 護欄
  algorithm.py        RLEV-VoI 主迴圈
  simulate.py         合成軌跡（僅健全性檢查）
  evaluate.py         frontier、McNemar、Holm、ECE
  backends.py         Anthropic / OpenAI 後端 + 軌跡快取
tests/               102 個測試，含強制單元測試 T1–T6
```

---

## 資料與結果

- [data/](data/) — 題目集（MATH-500 hard、AIME/AMC/HMMT、LeetCode Med/Hard）與快取軌跡
- [results/](results/) — 所有實驗的 JSON 輸出，每個都能由上面的腳本重現
- [results/figures/](results/figures/) — 論文圖表

---

## 方法論（可攜的部分）

本專案真正想推薦給別人的三件事：

1. **決定性分層協定**——只在「多數決已經錯」的題目上評估。SC 之上的方法只能在
   此改變答案，整體指標會被基準飽和度稀釋。三次獨立印證（[REPORT-ISC §13](docs/REPORT-ISC.md)）。
2. **審查先於實作**——兩段式閘門（多域文獻掃 + 多面向對抗攻擊 + 綜合裁決）。
   四個設計因此在零實作成本下被殺。
3. **harness 先用基準自己驗證**——LeetCode 實驗中第一版沙箱因 macOS 拒絕
   `RLIMIT_AS` 而 100% 誤判失敗；先跑 180 題參考解（178 通過）才發現。
   任何用執行評分的研究都該先報這個數字。

完整教訓清單見 [GRAVEYARD 的「橫貫教訓」](docs/GRAVEYARD.md)。

---

## 文件索引

**規格（動工前寫的）**
[SPEC.md](docs/SPEC.md) · [SPEC-TACT.md](docs/SPEC-TACT.md) · [SPEC-TACT-HARD.md](docs/SPEC-TACT-HARD.md) · [SPEC-ISC.md](docs/SPEC-ISC.md) · [SPEC-KAPPA-P.md](docs/SPEC-KAPPA-P.md)

**報告（實驗後寫的）**
[REPORT.md](docs/REPORT.md) · [REPORT-TACT.md](docs/REPORT-TACT.md) · [REPORT-TACT-HARD.md](docs/REPORT-TACT-HARD.md) · [REPORT-ISC.md](docs/REPORT-ISC.md) · [REPORT-G1.md](docs/REPORT-G1.md)

**其他**
[GRAVEYARD.md](docs/GRAVEYARD.md)（死亡紀錄 + 不可能地圖）·
[ALGORITHM.md](docs/ALGORITHM.md)（中文設計推導）·
[CONTRIBUTIONS.md](docs/CONTRIBUTIONS.md) ·
[FINDING-instrument-validity.md](docs/FINDING-instrument-validity.md) ·
[PROPOSAL-NEXT-PROGRAM.md](docs/PROPOSAL-NEXT-PROGRAM.md) ·
[KAPPA-STATUS.md](docs/KAPPA-STATUS.md)

---

作者：柯瑋宸（vito1317）
