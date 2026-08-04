# 第十二輪 JMLR PDF Re-audit

**目標**：[tact_jmlr.pdf](/Users/vito/development/adaptive-reasoning-consensus/paper/tact_jmlr.pdf)  
**版本**：`bfc9c11`  
**模式**：re-audit（PDF-side；中文）  
**前一輪未關閉根因**：`planted-margin-diagnostics-string-bucketing`

## 結論

**0 條開放 finding。** 前一輪的唯一中等 finding 已完整修正；沒有發現新的可由 PDF、實作或 released artifact 支持的問題。

## 前一輪 finding：FULLY_ADDRESSED

`run_planted_sensitivity.py` 的 `margin_diagnostics()` 現在使用
`rlev_voi.math_grade.build_math_pool`，並以各 substrate 自己的 budget 和
campaign split 計算；不再以原始字串把數學等價答案拆桶。新診斷同時修正了
兩個伴隨缺陷：MATH 曾被錯用本腳本預設 `K=12`，以及 evaluation split 曾依 traces
dict 的順序而非 campaign 的 sorted-gold 順序產生。

對同一個 89 題 MATH L5 evaluation set，現在所有相關 artifact 一致：

| 量 | 結果 |
|---|---:|
| `tact_hard_eval.substrate.decisive_n` | 10 |
| `substrate_health.math_l5_eval.decisive_n` | 10 |
| in-window items | 4 |
| decisive / window 比例 | 11.24% / 4.49% |
| shipped `n_gated`（`β=0.40`） | 13 |
| margin diagnostics `n_gated` | 13 |
| sign-set `z` | +0.8335 |
| evaluation-set contrast `z` | +2.5428 |

這與論文的 10/4、11.2/4.5、13、+0.83、+2.54 全部相符。新增的
`check_paper_numbers.py` 跨 artifact assertion 也會比對 decisive count、gated count
與 evaluation z；目前 **47/47** 個論文數值可回溯，且零個 artifact 矛盾。

## PDF-side 檢視

- 28 頁 JMLR PDF；JMLR 無頁數上限。
- Algorithm 1 與 Algorithm 2 的 rendered page 已目視檢查；文字框都在頁面內，未見裁切或 overfull 顯示。
- 本輪是 PDF-side audit：未將未出現在 PDF 的 LaTeX-only mechanical check 推論為 finding。

## 保留的審稿不確定性

本次的零 finding 代表此前 audit 提出的根因均已修正並驗證；不是對 JMLR 編輯或審稿結果的預測。論文已明示其可作用 stratum 的 2.5--7.5% 邊界；這個定位是否足以構成期刊貢獻，仍是審稿判斷而非機械正確性問題。
