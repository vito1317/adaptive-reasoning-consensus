# adaptive-reasoning-consensus

推理期（inference-time）LLM 共識演算法的研究倉庫。兩個階段：

| 階段 | 方法 | 結果 | 報告 |
|---|---|---|---|
| 1 | **RLEV-VoI** — 冗餘折扣投票 + VoI 停止 | **負面結果**：簡單去重基線全面勝出；有效機制被定位在逐字重複偵測 | [REPORT.md](docs/REPORT.md) |
| 2 | **TACT** — 信心穩健加權（有符號、可無標籤） | **正面結果**：四項證偽條件全數存活；無標籤變體零標籤辨識通道正負號 | [REPORT-TACT.md](docs/REPORT-TACT.md) |

階段 2 直接誕生於階段 1 的屍檢：CISC 類方法在信心校準崩壞時毀滅（R5: 0.062），
二元 ECE 閘門倖存但拋棄了有效訊號——TACT 用「排名統計量 → JS 收縮 → Bayes 判別連結」
的解析管線給出連續、有符號、可完全無標籤的信任調節。規格見 [SPEC-TACT.md](docs/SPEC-TACT.md)。

```bash
./.venv/bin/python -m pytest tests/ -q                  # 69 tests
./.venv/bin/python experiments/run_kappa_sweep.py       # 基線 frontier（問題陳述）
./.venv/bin/python experiments/run_tact_eval.py         # TACT headline 實驗
```

---

# RLEV-VoI — 冗餘折扣共識 + 資訊價值自適應停止

> ### 實測結論：負面結果
>
> 診斷的問題是真的。在逐字回音情境下 Self-Consistency 會崩潰到接近隨機（0.320），而且**越取樣越差**（K=1 時 0.403 是它的峰值）。本方法確實能修復（0.880，p≈7e-68）。
>
> **但一個簡單得多的基準線贏了。** 單純的 n-gram 近重複去重 + 信心加權 + 穩定度停止（RASC-lite），在每一個情境都以明顯差距支配 RLEV-VoI——R1 準確率更高且成本只有 1/4，R4 同樣準確度只花 1/5 成本。
>
> 消融把有效機制精確定位在**逐字重複偵測**（與增益相關 +0.935），而非反相似度加權、設計效應修正或 VoI。SPEC 預先登記的五項證偽條件觸發了四項半。完整數據與歸因見 **[docs/REPORT.md](docs/REPORT.md)**。
>
> 實務建議：若你的推理系統受回音之苦，先做最簡單的去重。本研究找不到證據支持更複雜的做法。

針對**凍結 LLM** 的推理期（inference-time）演算法。改良 Self-Consistency 的兩個核心問題：

1. **回音式重複投票**：SC 把每條推理鏈當成獨立一票，但取樣出來的鏈是相關的。一個熱門但錯誤的推理模板可以靠複製自己贏得多數決。
2. **固定 K 浪費算力**：簡單題抽 40 條是浪費，難題抽 5 條又不夠。

## 核心構想

**DDWC（冗餘折扣加權共識）** — 用相似度質量的倒數當作「有效權重」：

```
s_i = Σ_j S_ij        (相似度質量，S_ii = 1)
w_i = 1 / s_i          (有效權重，落在 [1/K, 1])
N_a^eff = Σ_{i:a_i=a} w_i        (答案 a 的有效票數)
n_eff   = Σ_i w_i = tr(D⁻¹S)     (總有效票數，落在 [1, K])
```

m 條近乎相同的鏈，總權重會收斂到 **1 票**而不是 m 票：

```
N_g^eff = m / (1 + (m-1)ρ)   →  1   當 ρ→1（完全回音）
                             →  m   當 ρ→0（真正獨立）
```

**VoI-Stop** — 對有效票數維護 Dirichlet 後驗 `α_a = α₀ + N_a^eff`，每抽一條鏈就評估「領先者是真眾數」的機率與每 token 的邊際資訊價值，不划算就停。

> **關鍵修正**：早期版本用 Kish 離散度比 `(Σw)²/Σw²` 當有效樣本數——這是錯的。K 份完全相同的複本權重是均勻的，Kish 會回報 **K**（完全相反）。正確的是權重和 `Σw_i`。這個錯誤由紅隊審查抓出，並固化成單元測試 T2/T3。

## 誠實的新穎性定位

這**不是**全新的統計量。它是既有元件的組合：

- `w_i = 1/Σ_j S_ij` 是 Goldberg–Richardson fitness sharing／逆密度加權，也是 ridge leverage 的廉價 O(K²) 代理。
- 用有效樣本數修正計數是 **Rao–Scott 設計效應修正**（1981/1984），複雜抽樣統計的四十年老方法。
- Dirichlet「領先穩定就停」**就是** Adaptive-Consistency（Aggarwal 2023）的準則。
- VoI/成本停止是教科書的 EVSI-per-cost（Raiffa & Schlaifer 1961）。

真正的貢獻只有三項，且都需要實證支撐：把估計量**修對**、dup-vs-sem 通道拆解當安全閥、以及一個非循環的公平評測協定。完整定位見 [docs/SPEC.md](docs/SPEC.md) §2。

## 專案結構

```
src/rlev_voi/
  config.py      凍結預設參數（spec §6）
  kernel.py      相似度核：dup（逐字重複）/ sem（語意）雙通道分解
  weights.py     有效權重與有效計數 ← 核心修正在這
  posterior.py   Dirichlet 後驗、P_stable、VoI
  consensus.py   DDWC 共識 + never-worse-than-SC 護欄
  algorithm.py   主串流迴圈（SAFE / AGGRESSIVE 兩種停止）
  baselines.py   SC / ASC / CISC / dedup-SC / ESC / SPRT / RASC-lite
  simulate.py    合成軌跡產生器（僅供健全性檢查，非效果證據）
  evaluate.py    frontier、配對統計、McNemar、Holm、ECE
  backends.py    真實 LLM 後端（Anthropic / OpenAI），含軌跡快取
tests/
  test_units.py       強制測試 T1–T6 + Kish 反向測試
  test_properties.py  架構保證（SAFE 停止序、後驗不吃信心、置換不變性）
  test_components.py  核函數數值、護欄邊際、VoI、成本模型
experiments/           frontier / boundary / real-API / 繪圖
docs/SPEC.md           完整英文規格、新穎性定位、證偽條件、紅隊修正紀錄
docs/ALGORITHM.md      中文版設計動機與數學推導
docs/REPORT.md         實驗結果、發現與缺陷修正紀錄
```

## 執行

```bash
python3.12 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
```

強制單元測試（演算法極限行為的解析驗證）：

```bash
./.venv/bin/python -m pytest tests/ -q
```

合成實驗（**不需要 API key**）：

```bash
./.venv/bin/python experiments/run_frontier.py --items 400 --out results/frontier.json
./.venv/bin/python experiments/run_boundary.py --items 150 --out results/boundary.json
./.venv/bin/python experiments/make_figures.py
```

真實 LLM 實驗（**需要 API key**，這才是 spec 認定的 headline 證據）：

```bash
export ANTHROPIC_API_KEY=...
./.venv/bin/python experiments/run_real_api.py --data data/items.jsonl --items 100 --k-max 40
```

## 合成實驗能證明什麼、不能證明什麼

| 能 | 不能 |
|---|---|
| 實作正確性（T1–T6 解析極限） | 在真實 LLM 軌跡上有效 |
| ρ=0 精確歸約成 SC、S=I 精確歸約成 ASC | 相似度—正確性混淆在實務上可控 |
| 護欄在逐字回音下確實觸發 | 逐字回音在真實取樣中真的會發生 |
| 消融歸因（哪個元件在做事） | 對 RASC/ASC 的 frontier 支配 |
| **適用邊界**：權重何時塌陷成均勻 | — |

合成資料的生成過程**正好就是** DDWC 假設的區塊叢集結構，所以在 R2/R4 上贏是資料生成方式的產物，不是證據。見 SPEC.md §8.a。
