# 下一個計畫：便宜外部真值下的驗證通道可靠度（已定向，未動工）

完整調查與三個候選：`results/external_truth_survey.json`（proposal 欄位含全文）。

## 已定位的缺口（三個 lens 交叉證實）

生成測試的驗證通道有自己的雙世界問題,而現有方法全部有同一個盲點：
- **ACES** (arXiv:2604.03922) 用 LOO-AUC 估計測試判別力 δ_j,但權重
  `max(0, LOO-AUC − 1/2)` **在零截斷**——LOO-AUC 0.2 的測試（強反相關 =
  翻轉符號後強訊息）與純雜訊同權。**沒有任何已定位工作給測試判決負權重。**
- 在決定性分層上 ACES 的參考排名被反轉,會系統性歸零恰好能救援的測試
  ——而**沒有人報告決定性分層的條件量**（我協定的直接遷移點）。
- 無 per-problem 可靠度估計,只有全域平均（Assumption 4）。

## 首選候選：KAPPA（Kill-Anchored Per-verdict Precision Assignment）

用 AST 語意突變體（~20/代表解,零標籤零 LLM 呼叫）估計每
(測試, 候選叢集) 的局部 kill rate κ_lj → 逐判決似然比 LLR,
**完全不參照計票**,打破 ACES 的循環。可表達「繞錯誤叢集緊、繞正確
叢集鬆」的測試形狀——標量權重無法表達。TACT 帶符號可靠度 +
決定性分層協定的直接移植。

## 動工前必經（六連殺紀律）

1. 完整文獻掃（KAPPA 對 STING/mutation-testing 線、VeRPO、B4 的 delta 需逐篇驗證）
2. 對抗審查（機制、經濟學、基線——尤其「mutant 分布 ≈ 鄰近錯誤程式分布」
   這個中心假設的檢驗設計）
3. 預註冊證偽器後才收資料（HumanEval+/MBPP+/LiveCodeBench,凍結模型）
