# KAPPA 審查狀態（進行中，未動工）

## 原始設計（可加式 per-cluster LLR）：已死，作者獨立重現

`experiments/verify_kappa_kill.py` 重現審查者的載重論證：

**重現成立（結構性）**
- 恆等式精確成立（20,000 隨機格點最大誤差 **2.31e-14**）：
  `score_l = Σ_j log(eps_j/kappa_lj) + Σ_{j:pass}[logit(kappa_lj)+logit(1−eps_j)]`
- 推論成立：kappa>eps 時每個通過的測試貢獻恆正（20,000 抽樣 **0 反例**）
  ——失敗永遠不可能成為支持某叢集的證據，旗艦 novelty 不存在
- fragility confound 成立：`score ~ +4.34*tally +13.66*mean_kappa`，R²=0.984
  ——固定 pass row（唯一的行為證據）仍可用突變體脆弱度買分數

**未重現（經驗性，雙方各 n=1）**
- 審查者稱「fragility 與正確性反相關、KAPPA 選錯而多數決選對」；
  在我建構的任務上**相反**（fragility 正相關，兩者都選對）。
  差異原因：我的任務不是決定性案例（正解 18/18 全過）。此爭點**未解**。

## 修復（成對對比）：通過機制攻擊

只對**分歧的**測試累加，兩端都用 kappa：
`LLR(A>B) = Σ_{分歧} ±log[(1−eps_j)·kappa_對手j / ((1−kappa_己方j)·eps_j)]`

作者驗證：
- (a) 行為相同的候選**精確打平**（0/20000 非平手）——confound 結構性消除
- (b) 失敗可以成為支持證據，且由 **kappa 對比**驅動（eps=0.10 觸發 1.64%，
  eps=0.20 觸發 8.09%）——可加式版本 0/162 從未觸發的 novelty 現在真的存在
- (c) 與計票 argmax 分歧 11.7%——不是換皮的多數決

## 文獻掃修正（三個 lens 一致）

- 四個宣稱 delta **三個是錯的**：B4 與 ARBITER 的 log-posterior 已含帶符號
  逐判決貢獻；ACES 權重**是** per-problem（缺口應為 per-cluster）；
  MIST-RL (2603.01409) 已建立「突變資訊改善程式碼選擇」（HumanEval+ +3.05）
- **唯一存活的 novelty：kappa 的第二個索引**（within-problem 的 per-cluster
  可靠度）——三個 lens 獨立確認未被claim
- 強制新基線：mutation-hardened suite + 均勻投票（MIST-RL）
- 前提威脅：arXiv:2606.16999 測量研究稱同算力下無任何事後語意算子勝過
  Best-of-N；ACES Hard region「14 題中無方法通過超過 1 題」——決定性分層
  可能小到沒有檢定力（薄窗在程式碼領域的重演？）

## 待決（攻擊進行中）

三個 lens 攻擊修復後的設計：可尋址窗口大小（決定一切）、同算力經濟學、
基線電池（Dawid-Skene/EM、MIST-RL、ACES-O、oracle 天花板）。
裁決回來後才決定 BUILD / ABANDON。
