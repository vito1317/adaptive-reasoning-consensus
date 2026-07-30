# TACT：面向大型語言模型自我一致性投票的信任錨定信心調節

**柯瑋宸（Wei-Chen Ko, vito1317）— 獨立研究者**

*草稿——證據來自合成 oracle 實驗；真實軌跡驗證待完成*

## 摘要

信心加權自我一致性（CISC 及其後繼方法）能從凍結大型語言模型的自我回報信心中萃取可觀的增益——直到信心通道在**方向**上失準為止。所有已發表的加權方案在結構上都是信心的單調遞增函數，因此一條反相關的通道會毒化投票而非提供資訊；而二元 dev-set 閘門雖能倖存，卻是靠整批丟棄真正具辨別力的訊號。本文提出 **TACT**（Trust-Anchored Confidence Tempering，信任錨定信心調節），將固定的信心指數替換為由通道的**帶符號題內辨別度**推導而得的指數：以混合 van Elteren Somers' $D$ 排名統計量（配題內叢集標準誤）為基礎，經正部 James–Stein 收縮與 Bayes 判別連結映射。此映射帶有精確錨點——收縮死區內的投票與純自我一致性**位元級相同**，而對數值特徵映射可精確重現 CISC-power。無標籤變體從一致性偽標籤估計帶符號可靠度，並證明了一個衰減恆等式：只要多數決錯誤率低於二分之一，符號估計必然一致；輔以保守的去衰減與識別性邊界上的回音警報。在配對軌跡池的合成 oracle 實驗中，無標籤變體恢復了將所有已發表協定釘死在多數決地板上的反相關通道（$\kappa=-0.6$：$1.000$ 對 $0.807$）；排名不變性在單調信心壓縮下勝過整個原始值權重家族的 oracle（$1.000$ 對 $0.965$）；逐群組擴展突破了異質性地板且對自我一致性零配對損失（$0.940$ 對 $0.808$；$+79/-0$，$p=3.3\times10^{-24}$）。本文進一步證明在 i.i.d. 潛在耦合下逐題無標籤自適應是不可能的，並預先登記了四項證偽準則——包括以已發表的 dev 校準 CISC 協定作為指定殺手基線——方法全數存活。

**關鍵詞——** 大型語言模型、自我一致性、信心校準、加權投票、無標籤估計、排名統計量

## 一、引言

自我一致性（Self-Consistency, SC）[1] 透過取樣 $K$ 條思維鏈軌跡並回傳多數答案，提升凍結大型語言模型（LLM）的推理準確率。由於每條軌跡還可以回報一個信心分數——口頭表述的 [6][7]、由 token 對數機率導出的、或以 $P(\text{True})$ 形式引出的 [5]——一個自然的改良是以信心加權投票。信心引導自我一致性（CISC）[2] 證明了這種做法能以一小部分取樣預算恢復純 SC 的準確率，並提出題內辨別度（Within-Question Discrimination, WQD）指標，主張讓信心訊號對投票有用的性質是**辨別力**而非校準度。

這項改良帶有一個就作者所知尚無已發表方法處理的結構性脆弱點。所有現存的加權方案——CISC 的 softmax 權重、可靠度感知偽計數 [11]、暖啟動門檻過濾 [12]——都是信心的單調**遞增**函數。信任決策只剩「上調權重的幅度多大」；通道可能與正確性**反相關**這件事根本無法表示。然而方向性失準並不罕見：強化微調已知會扭曲口頭信心，分布位移可以反轉一個在域內原本有效的訊號；在本文的實驗裡，一條簡單的反相關通道（$\kappa=-0.6$；第三節）把信心加權基線從近乎完美打到遠低於多數決地板——而同一份證據，只要讀對符號，就是一個完美的訊號。防禦性的替代方案——校準誤差過高時關閉通道的二元 dev-set 閘門——雖能在反轉下倖存，卻整批丟棄辨別性訊號：一條系統性低估自信但排名完美的通道，會因為與投票效用無關的理由而未通過 ECE 閘門 [2][8]。

本文把問題歸結為估計一個純量：信心通道的**帶符號**題內辨別度，並將它——連同不確定性——映射為投票指數。本文貢獻如下：

**C1：帶符號、解析調節的信心加權。** TACT 以權重 $w_i=\exp(\gamma\,\varphi_i)$ 投票，其中 $\varphi_i$ 是軌跡 $i$ 題內信心中位秩的標準化 van der Waerden 分數，而 $\gamma$ 是**推導**而非網格搜尋所得：混合 van Elteren Somers' $D$ 統計量（等於 $2\cdot\mathrm{WQD}-1$）配精確 tie 校正零假設變異數與題內叢集 jackknife 標準誤，經帶顯著性下限的正部 James–Stein 收縮，再通過帶混合變異數校正的 Bayes 判別連結。此構造帶有精確錨點：收縮死區內的投票與純 SC **位元級相同**（共用程式碼路徑），而對數值特徵映射精確重現 CISC-power（第四節）。由於 $\varphi$ 只透過題內排名依賴信心，整個方法對信心尺度的一切嚴格單調失真不變；在單調壓縮下它勝過整個原始值權重家族的 oracle（$1.000$ 對 $0.965$）。

**C2：帶符號通道可靠度的無標籤估計。** 群眾外包一脈從跨標註者共變異估計可靠度 [13][16]；來自單一模型的單一可交換信心通道並無此結構。本文從**一致性偽標籤**（每題去重加權多數決）估計帶符號辨別度，並證明類別條件雜訊衰減恆等式 $\mathbb{E}[\widehat{D}_g]=(1-2\bar{\rho})\,D$：只要成對加權多數決錯誤率 $\bar{\rho}$ 低於 $1/2$，無標籤估計只會**低估**信任、絕不會弄錯符號。split-half 一致性反演做保守的去衰減，符號感知警報在識別性受威脅時讓方法退回純 SC。在耦合掃描上，無標籤變體與 200 標籤變體幾乎逐點吻合，包括負通道的完整恢復（第八節）。

**C3：一個不可能性結果及其結構化出路。** 當逐題耦合 i.i.d. 且無可觀測協變量時，本文證明逐題無標籤自適應是封閉的：任何對題目自身一致性統計量的單調使用都塌縮為多數決增強；在恰好可以靠翻轉獲勝的多數決錯誤題目上，可觀測符號 $96\%$ 的時間與真值相反；且 $\{\kappa>0,\text{少數方正確}\}$ 與 $\{\kappa<0,\text{多數方正確}\}$ 兩個假設誘導出完全相同的可觀測分布。當異質性改由可觀測協變量索引（域相關校準）時，同一估計器按群組執行即可恢復各群組的帶符號耦合，以對 SC 零配對損失逼近逐題 oracle（第六節）。

**C4：預先登記的證偽協定。** 四項證偽準則在實作前即已固定，包括兩個以殺死本方法為目的而設計的基線：**已發表的** dev 校準 CISC 協定（其調參溫度本身就是 SC$\leftrightarrow$CISC 的內插）與平凡的 dev 選取帶符號指數網格。四項全數存活，且誠實邊際如實報告：對帶符號網格的淨優勢恰好集中在三格——單調失真、自信回音、以及網格根本無法執行的無標籤運作。

## 二、相關工作

**信心加權自我一致性。** SC [1] 把取樣軌跡當作 i.i.d. 票。CISC [2] 以在標籤分割上調參的溫度做 softmax 信心加權，其 WQD 指標提出了同樣驅動本文的「辨別力對校準度」論點；排名校準一脈 [8] 獨立得到相同結論。加權變體 [9][10] 與提早停止家族 [3][4] 改良預算；可靠度感知偽計數 [11] 與暖啟動門檻過濾 [12] 做線上調整，但都只重新縮放正向信任。這些方法沒有一個能表示、更遑論估計負的信心—正確性關聯。因此本文的 dev 校準變體必須誠實定位：CISC 的調參溫度已經是 dev 校準的 SC$\leftrightarrow$CISC 內插，TACT-dev 的新穎性在於符號、排名不變性與解析（免網格）映射，而非 dev 校準本身。

**無標籤可靠度估計。** 從一致性估計工作者可靠度是經典問題 [13][14][15]；頻譜元學習器 [16] 與近期 LLM 集成工作 [17][18] 利用**多個**預測器之間的共變異。本文的設定不同：單一模型的單一可交換通道、逐題投票結構、以及一致性代理在相關錯誤下的已知失效——本文以量化的衰減恆等式、保守去衰減與警報應對，而非提出無條件的主張。

**收縮與排名統計量。** 估計器組裝了經典零件：分層排名統計量 [19]、James–Stein 正部估計器 [20]、有效樣本數修正 [21][22]、normal-scores 判別分析。本文主張的是組裝方式及其錨點，而非零件本身。

**誠實的姊妹結果。** 作者本人的前一個系統（RLEV-VoI，冗餘折扣投票配資訊價值停止）在相同的證偽紀律下評估並**未能存活**——一個簡單的去重基線全面支配了它——已作為負面結果報告。其屍檢分離出了本文研究的信心兩難。

## 三、問題設定

### 3.1 記號

題目 $q=1,\dots,Q$；題 $q$ 有 $m_q$ 條取樣軌跡。軌跡 $(q,i)$ 產生離散答案 $a_{q,i}$ 與信心 $c_{q,i}\in(0,1)$；正確性 $y_{q,i}=\mathbf{1}[a_{q,i}=a_q^\ast]$ 在測試時不可觀測。純 SC 回傳 $\arg\max_A n_q(A)$，其中 $n_q(A)$ 是答案 $A$ 的票數。CISC-power 以固定 $\gamma>0$ 用 $c_{q,i}^{\,\gamma}$ 加權。

### 3.2 信心兩難

本文的合成 oracle 逐題從帶潛在正確答案的叢集混合分布取樣軌跡，並按下式生成信心：

$$c_{q,i}=\operatorname{clip}\!\big(\tfrac12+\kappa\,(y_{q,i}-\tfrac12)+\varepsilon_{q,i},\,0.01,\,0.99\big)$$

其中雜訊 $\varepsilon\sim\mathcal{N}(0,0.1^2)$、耦合 $\kappa\in[-0.6,0.6]$。圖 1 描繪了在本方法存在**之前**量測的基線版圖：無條件加權（CISC，$\gamma=1$）在 $\kappa<0$ 崩潰；ECE 閘門在校準良好的對角線之外從不開啟；dev 標籤上的符號校正 AUC 閘門幾乎吃滿同質掃描。這次預先量測固定了新方法可以正當主張獲勝的格子——信心尺度的單調失真、協變量異質性、小 dev set、無標籤運作——而評測恰好只對這些格子負責。

![圖 1——預先量測的問題陳述：固定 $K=15$ 下各基線信心策略的準確率隨真實耦合 $\kappa$ 的變化。平凡的符號校正 AUC 閘門（綠）幾乎吃滿同質掃描；任何新方法的空間（陰影）集中在中段，以及圖外的失真、異質性與無標籤格。](figs/kappa_sweep.png)

## 四、TACT

### 4.1 投票家族

在題 $q$ 內，令 $R_{q,i}$ 為 $c_{q,i}$ 的中位秩（並列取平均），且

$$\varphi_{q,i}=\frac{v_{q,i}-\bar v_q}{\sigma_q},\qquad v_{q,i}=\Phi^{-1}\!\Big(\frac{R_{q,i}}{m_q+1}\Big)$$

其中 $\sigma_q$ 是 $v$ 在題內的**實現**標準差（無並列時 $m=4$ 的值是 $0.62$、$m=40$ 是 $0.95$；使用閉式解會在不同預算下悄悄重新縮放 $\gamma$），且若 $\sigma_q\le 10^{-8}$ 則 $\varphi\equiv 0$（全並列的信心以純 SC 投票）。投票為

$$\hat a_q=\arg\max_A \sum_{i:\,a_{q,i}=A}\exp\big(\gamma\,\varphi_{q,i}\big)$$

當 $\gamma=0$ 時，實作**直接呼叫 SC 常式本身**，使零信任錨點是位元級精確而非僅分布相等。由於 $\varphi$ 只透過題內排名依賴 $c$，信心尺度的一切嚴格單調失真都不改變投票結果。

### 4.2 可靠度統計量

對具 $n^1_q$ 個正標籤與 $n^0_q$ 個負標籤的題 $q$（dev 用 $y$；無標籤用第五節的偽標籤），中位秩上的 Mann–Whitney 統計量給出

$$D_q = 2\,\mathrm{AUC}_q-1,\qquad \mathrm{AUC}_q=\frac{U_q}{n^1_q n^0_q}$$

即 CISC 記號中的 $2\cdot\mathrm{WQD}_q-1$。以 van Elteren 成對計數權重 $N_q=n^1_q n^0_q$ 混合 [19]：

$$\widehat{D}=\frac{\sum_q N_q D_q}{\sum_q N_q}$$

在題內可交換性零假設下，$U_q$ 有精確 tie 校正變異數 $n^1_qn^0_q(m_q+1)/12\cdot[1-\sum_t(t^3-t)/(m_q^3-m_q)]$，得零假設標準誤 $\mathrm{SE}_0$；題間異質性由閉式的刪一題 jackknife $\mathrm{SE}_J$ 捕捉。取保守的

$$\mathrm{SE}=\max\big(\mathrm{SE}_0,\ \mathrm{SE}_J,\ \tfrac{1}{2\sqrt{N}}\big),\qquad r=\widehat{D}/\mathrm{SE}$$

由於 $D$ 是成對泛函，$\mathbb{E}[\widehat{D}]$ 不依賴 $m_q$：在 $m=40$ 估計的指數可直接遷移到 $m=8$ 的部署。

### 4.3 調節映射

**收縮。** 帶顯著性下限 $\nu$ 的正部 James–Stein：

$$\tilde D=\operatorname{sign}(\widehat{D})\,\max\!\big(0,\ |\widehat{D}|-\nu^2\mathrm{SE}^2/|\widehat{D}|\big)$$

死區為 $\{|r|\le\nu\}$；$\nu_{\mathrm{dev}}=1.28$、$\nu_{\mathrm{LF}}=2.33$。取 $\nu=1$ 時，上式恰是 $\mathcal{N}(0,\tau^2)$ 先驗配插入式 $\hat\tau^2=\max(0,\widehat{D}^2-\mathrm{SE}^2)$ 的經驗 Bayes 後驗均值 [20]。此映射是奇函數、連續、絕不超過 $|\widehat{D}|$、對 $\widehat{D}$ 單調、對 $\mathrm{SE}$ 反單調。

**連結。** 設題內 $\varphi\,|\,y\sim\mathcal{N}(\mu_y,s^2)$ 且**混合分布**標準化為單位變異數——這正是 4.1 節的標準化所強制——故 $s^2=1/(1+\bar p(1-\bar p)u^2)$，其中 $u=\sqrt2\,\Phi^{-1}\!\big(\tfrac{1+\tilde D}{2}\big)$，$\bar p$ 為正確軌跡的基礎率。則 Bayes 最適的逐軌跡對數權重係數為

$$\gamma^\ast=\frac{u}{s}=u\sqrt{1+\bar p(1-\bar p)\,u^2}$$

上限 $\gamma_{\max}$（dev 為 $4$、無標籤為 $2$）。未校正的連結 $\gamma=u$ 在 $D=0.9$ 時對強通道低估權重達約 $50\%$。

### 4.4 錨點性質

**命題 1（精確 SC 歸約）。** $\gamma=0$ 時，投票在每個軌跡池上作為函數等於純 SC，包括平手處理。在 $D=0$ 下，$P(\gamma=0)\to 2\Phi(\nu)-1$（dev 為 $80\%$、無標籤為 $98\%$），且 $\gamma$ 在死區邊界連續，因此偽陽性只施加一個無窮小的指數。

**命題 2（精確 CISC 歸約）。** 取特徵映射 $\varphi^{\log}_{q,i}=\log c_{q,i}-\overline{\log c_q}$，權重等於 $\kappa_q\,c_{q,i}^{\,\gamma}$（$\kappa_q>0$ 為逐題常數）；故 argmax、平手與正規化投票份額在每個池上都與 CISC-power$(\gamma)$ 一致。

**命題 3（正則性）。** 複合映射 $g(\widehat{D},\mathrm{SE})$ 連續、奇、對 $\widehat{D}$ 非遞減、幅度對 $\mathrm{SE}$ 非遞增，且 $g(D,0^+)=\gamma^\ast(D)$。

證明皆為初等，並由釋出程式碼中的單元測試釘住（76 項測試；置換驗證的零假設變異數、收縮式的 EB 恆等式、連結推導各有數值測試）。

## 五、無標籤估計

### 5.1 管線

（i）**去重**：在字面相似度通道上以 $0.95$ 做單鏈結重複分群；每條軌跡在多數決判定與成對加權中取權重 $1/|\text{群}|$。（ii）**偽標籤**：$g_{q,i}=\mathbf{1}[a_{q,i}=M_q]$，$M_q$ 為去重加權多數。（iii）**margin 閘門**：保留去重加權 margin 前 $60\%$ 的題目。（iv）以 $\mathrm{lab}=g$ 計算 4.2 節統計量，得 $(\widehat{D}_g,\mathrm{SE}_g,r_g)$。

### 5.2 符號一致性及其邊界

**命題 4（衰減恆等式）。** 令 $\bar\rho$ 為題目多數決錯誤的成對加權機率。若多數決錯誤事件在給定 $y$ 下與 $\varphi$ 獨立（類別條件雜訊），則 $\mathbb{E}[\widehat{D}_g]=(1-2\bar\rho)\,D$。特別地，只要 $\bar\rho<1/2$ 就有 $\operatorname{sign}\mathbb{E}[\widehat{D}_g]=\operatorname{sign} D$：無標籤估計只會低估信任，絕不會弄錯符號。

此恆等式恰在翻轉由信心**造成**時失效——自信回音。彼時 $\{$多數對、$D<0\}$ 與 $\{$多數錯於自信回音、$D>0\}$ 下的可觀測分布完全相同（[16] 的雙根歧義在單通道情形的重述），因此任何無標籤保證必然是條件的；本文如實陳述而非粉飾。

### 5.3 去衰減與警報

對 $R=20$ 次隨機對半分割的一致率 $\alpha$，在具 $k$ 個有效錯誤選項（逆 Simpson）的單硬幣模型下 $\alpha=p^2+(1-p)^2/k$，反解得 $p=[1+\sqrt{1-(k+1)(1-k\alpha)}]/(k+1)$；將 $\widehat{D}_g$ 除以 $2p-1$ 的**上** $95\%$ 自助法界（下限 $0.2$），只可能低估膨脹。四個警報強制 $\gamma=0$：重複塌縮（Kish 比中位數 $<0.5$）、符號感知 margin 去耦、split-half 二次式的根歧義、有效題數不足。margin 去耦警報必須以估計的信任方向為條件：符號天真的版本（「多數方平均 $\varphi$ 最高」）會在每一條良性反相關通道上誤觸發——這是作者實際踩到、診斷並修復的缺陷，且已由釋出測試釘住。最後在**原始** $z$ 上做顯著性閘門（命題 4 保證其符號無偏），在去衰減值上做調節。半無標籤模式僅從約 50 個 dev 標籤取符號、將其送入管線並僅停用代理符號警報；以可忽略的標註成本買到對上述歧義的免疫。

## 六、異質性：不可能性與出路

### 6.1 i.i.d. 耦合下逐題自適應是封閉的

設 $\kappa_q\stackrel{\text{iid}}{\sim}\mathcal{N}(0,0.6^2)$ 且無可觀測協變量。

**命題 5（自我增強）。** 任何 $h$ 單調遞增且奇的逐題規則 $\gamma_q=h(\widehat{D}^g_q)$ 在兩個分支上都增強多數決：$\widehat{D}^g_q>0$ 時上調自信軌跡權重，而它們與多數一致；$\widehat{D}^g_q<0$ 時上調不自信軌跡權重，而那又是多數方。實證上此類規則與 SC 在 $97.5\%$ 的題目上一致，殘餘翻轉為淨傷害（每 400 題翻對 1 題、翻錯 9 題）。

**命題 6（贏家詛咒）。** 在 $|D_q|>0.3$ 的多數決錯誤題目——恰好是翻轉可以獲勝的題目——上，一致性統計量的符號只有 $4\%$ 的時間與真符號一致。

**命題 7（兩世界不可辨識）。** 對任何觀測 $(a,c)$，世界 $\{\kappa>0,\ \text{少數方正確}\}$ 與 $\{\kappa<0,\ \text{多數方正確}\}$ 誘導相同的可觀測分布（構造性地，對兩種真值計算的 $D$ 滿足 $D^{w_1}=-D^{w_2}$）。任何無標籤方法都無法區分。

因此逐題 oracle（本實驗中 $0.983$）不可達，誠實的行為是退回全域估計——而 TACT 的死區**精確地**做到了這一點：在 i.i.d. 格中每個變體都回傳位元級 SC（零不一致配對）。

### 6.2 TACT-group

真實異質性通常由可觀測協變量索引（領域、題型）。當 $\kappa$ 由群組標籤索引時，按群組執行估計器可讓每個群組都落在第四、五節的作業範圍內；dev 少於 30 題（或無標籤少於 60 題）的群組退回全域估計——由命題 5–7，這不是妥協而是唯一站得住的預設。

## 七、實驗設定

**實驗架構。** 叢集混合 oracle 逐題生成至多 $K_{\max}=20$ 條快取軌跡（答案、信心、兩個相似度通道）；所有方法重放相同的池（配對比較、精確 McNemar 檢定）。投票預算 $K=15$；掃描每格 400 題、群組研究 600 題；dev 分割 200（主要）與 50（小 dev）。

**情境。** $\kappa$ 掃描 $\{-0.6,\dots,+0.6\}$；三種嚴格單調信心失真（向 $0.5$ 壓縮、過度自信 sigmoid、四次冪）——構造上保排名，辨別力完好而校準度全毀；i.i.d. 異質性（$\kappa_q\sim\mathcal{N}(0,0.6^2)$）；協變量結構異質性（三群組 $+0.6/0/-0.6$）；自信回音毒化（錯誤叢集以信心 $0.95$ 逐字回音）。

**基線。** SC；CISC-power（$\gamma\in\{0.25,\dots,4\}$）；**CISC-devT**——已發表的 dev 校準協定（dev 上選取的正向網格）；二元 ECE 閘門；**SignGrid-dev**——最強平凡基線（dev 上選取的帶符號指數網格）；以及作為上包絡的帶符號固定指數測試集 oracle。群組研究另加天真自我參照逐題法作為陰性對照，與逐題連結 oracle 作為天花板。

**預先登記的證偽準則。** F1：$\kappa=+0.6$ 時 TACT-dev 顯著低於最佳固定 $\gamma$ 的 CISC。F2：任一變體在掃描任一處顯著低於 SC。F3：無標籤變體未能在掃描平均上勝過 ECE 閘門。F4：CISC-devT 或 SignGrid-dev 在所有格（含失真、異質性、小 dev 格）追平 TACT-dev。

**表 1：耦合掃描（$K=15$ 準確率；每格 400 配對題；dev $n=200$）。已發表協定在整個負半軸貼在 SC 地板上。**

| $\kappa$ | SC | ECE | devT | SignGrid | **TACT-dev** | **TACT-LF** | oracle |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $-0.6$ | .807 | .807 | .807 | 1.000 | **1.000** | **1.000** | 1.000 |
| $-0.4$ | .797 | .797 | .797 | 1.000 | **1.000** | **1.000** | 1.000 |
| $-0.2$ | .835 | .835 | .835 | .993 | .978 | .978 | .993 |
| $-0.1$ | .762 | .762 | .762 | .892 | .880 | .885 | .892 |
| $0.0$ | .835 | .835 | .835 | .835 | .835 | .835 | .835 |
| $+0.1$ | .795 | .795 | .917 | .917 | .902 | .902 | .917 |
| $+0.2$ | .845 | .845 | .993 | .993 | .988 | .988 | .993 |
| $+0.4$ | .838 | .838 | 1.000 | 1.000 | **1.000** | **1.000** | 1.000 |
| $+0.6$ | .782 | .782 | 1.000 | 1.000 | **1.000** | **1.000** | 1.000 |

![圖 2——信心使用 frontier 上的主結果。TACT-dev 與完全無標籤的 TACT-LF 全程追蹤帶符號 oracle；CISC-devT 與 ECE 閘門在所有 $\kappa<0$ 貼在 SC 地板上。](figs/tact_sweep.png)

## 八、結果

### 8.1 帶符號恢復：有標籤與無標籤

表 1 與圖 2 給出掃描結果。三個觀察。第一，已發表協定在 $\kappa<0$ 從未離開地板：CISC-devT 的網格只有正向，ECE 閘門從不開啟（掃描中 dev ECE 介於 $0.10$–$0.80$，而極端處訊號的辨別力是完美的）。第二，無標籤變體與 200 標籤變體幾乎逐點吻合——在 $\kappa=-0.6$ 原始一致性統計量為 $\widehat{D}_g=-0.81$、$z=-17.6$，CCN 恆等式的符號保證如預測般成立，零標籤達到 $1.000$。第三，$\kappa=0$ 時死區精確回傳 $\gamma=0$，對 SC 的配對準確率差恆為零——「不劣於」被「完全相同」取代。

**表 2：對抗情境（$K=15$ 準確率）。「oracle」是原始值權重策略的測試集最佳；排名不變性在壓縮下勝過整個該家族。**

| 情境 | SC | devT | SignGrid | **TACT-dev** | **TACT-LF** |
|---|---:|---:|---:|---:|---:|
| 單調壓縮 | .795 | .965 | .965 | **1.000** | **1.000** |
| 單調過度自信 | .795 | 1.000 | 1.000 | 1.000 | 1.000 |
| 單調四次冪 | .795 | 1.000 | 1.000 | 1.000 | 1.000 |
| 異質（i.i.d.） | .810 | .810 | .810 | .810 | .810 |
| 自信回音 | .200 | .200 | .550 | **.585** | .200* |

*警報觸發，方法拒絕離開 SC——命題 4 的條件保證按其陳述運作。

### 8.2 原始值失效處的排名不變性

在單調壓縮下（表 2、圖 3），所有信心擠在 $0.5$ 附近，任何 $c^{\gamma}$ 家族的權重都近乎均勻：即使原始值策略的 **oracle** 也只到 $0.965$。TACT 的排名分數不受失真影響，兩個變體皆達 $1.000$。在自信回音下，dev 標籤揭露反轉（高信心 $\Rightarrow$ 錯誤），TACT-dev 以 $\gamma=-1.20$ 反制，是全場最佳（$0.585$；SC 地板的三倍）；無標籤時重複塌縮警報觸發、方法正確拒絕——由命題 7，任何無標籤方法在此對符號的判斷都不可能勝過擲硬幣，假裝可以才是真正的失敗。

![圖 3——對抗情境。虛線：原始值權重的 oracle。左組長條：排名不變性在壓縮下勝過整個該家族；右側：有標籤變體反制自信回音，無標籤變體警報並拒絕。](figs/tact_adversarial.png)

### 8.3 異質性

表 3 與圖 4 給出群組研究。在協變量結構格中，逐群組 TACT 恢復各群組的帶符號耦合——dev $\{+4.0,0.0,-4.0\}$、無標籤 $\{+2.0,0.0,-2.0\}$，$\kappa=0$ 群組被正確死區化——並突破了可證明束縛所有全域策略的地板：無標籤變體達 $0.940$，距逐題連結 oracle 僅 $0.007$，對 SC 在 600 題上**零**配對損失（$+79/-0$，$p=3.3\times10^{-24}$）。在 i.i.d. 格中，所有正當方法都以零不一致配對貼在地板上，天真自我參照對照略低於地板——命題 5–7 的實證面貌。有一個如實報告而非調參求得的觀察：無標籤變體在群組格中優於 dev 變體（$0.940$ 對 $0.923$），因為其較低的指數上限（$2$ 對 $4$）在 $|D|\approx1$ 時正則化得更好；上限穩健性留作消融。

**表 3：異質性研究（600 配對題；$K=15$）。**

| 方法 | 群組結構 | i.i.d. |
|---|---:|---:|
| SC（地板） | .808 | .827 |
| TACT 全域（dev） | .808 | .827 |
| TACT-group（dev） | .923 | .827 |
| **TACT-group（無標籤）** | **.940** | .827 |
| 天真逐題（陰性對照） | .803 | .820 |
| 逐題連結 oracle（天花板） | .947 | .983 |

![圖 4——結構化對 i.i.d. 異質性。左：有可觀測協變量時，逐群組 TACT（無標籤）從 0.808 地板逼近逐題 oracle 且對 SC 零損失。右：可證明封閉的 i.i.d. 格——所有正當方法貼地板，陰性對照略低於地板。](figs/group_eval.png)

### 8.4 小 dev set 與證偽準則

dev $n=50$ 時結論不變（$|\kappa|=0.6$ 仍 $1.000$；$-0.2$ 仍 $0.978$）：SE 感知的收縮平滑退化而非災難性失效。四項證偽準則全數存活：F1（$1.000$ 對 $1.000$）、F2（$\kappa=0$ 位元級相同；他處從未顯著低於 SC）、F3（掃描平均 $0.954$ 對 $0.811$）、F4（失真與回音格是兩個網格基線都到不了的）。對 SignGrid-dev 的誠實邊際在同質掃描上很窄——中段 TACT 甚至落後 $0.005$–$0.015$，這是收縮的刻意代價——淨優勢恰好集中在預先登記之處：失真（$+0.035$）、回音（$+0.035$）、以及網格無法執行的無標籤運作。

## 九、討論與限制

**證據顯示了什麼、沒顯示什麼。** 所有量化主張都在合成 oracle 上，其信心模型在同質格中正是估計器所測的耦合。本文以三種設計限制循環性：對抗情境（失真、異質性、回音）落在估計器的工作模型之外；機制恢復主張（$\widehat{D}$ 是否追蹤 $\kappa$？）與準確率主張分開報告；且預先量測的基線版圖（圖 1）在方法存在前就固定了可獲勝的格子。真實 LLM 軌跡的驗證是剩餘的步驟；快取軌跡執行器已提交，且預測是可證偽的：若真實信心通道從不出現方向性失準或協變量結構，TACT 的死區應使其在那裡與 CISC-devT 操作上無法區分。

**標籤充足時邊際很窄。** 當標籤充裕且信心尺度可信時，dev 選取的帶符號網格能吃到大部分價值；TACT 的價值主張立足於無標籤情境、失真的尺度、小 dev set，以及其錨點的精確性。

**條件性的無標籤保證。** 命題 4 需要去重後 $\bar\rho<1/2$，且自信回音的歧義是根本性的（命題 7）；警報只能偵測逐字情形，改寫式回音會逃過——半無標籤模式是約 50 個標籤的誠實修法。

**每群組一個全域指數。** 群組內 TACT 只出一個指數；群組內的逐題變異依命題 5–7 不可利用，除非存在更多協變量。

## 十、結論

TACT 把「該信任這個模型的信心多少？」變成一個被量測的、帶符號的、不確定性感知的量，兩端有精確退路——證據缺席時是純自我一致性、證據滿格時是 CISC——並證明長期在此方法家族中無法表示的「符號」可以在陳述並測試過的條件下零標籤恢復。隨附的不可能性結果劃出任何未來逐題方法必須尊重的邊界；而這套已經殺死過作者自己一個系統的證偽協定，或許是更可攜的貢獻。

## 參考文獻

[1] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang, A. Chowdhery, and D. Zhou, "Self-consistency improves chain of thought reasoning in language models," in *Proc. ICLR*, 2023.

[2] A. Taubenfeld *et al.*, "Confidence improves self-consistency in LLMs," in *Findings of ACL*, 2025, arXiv:2502.06233.

[3] A. M. Aggarwal, A. Madaan, Y. Yang, and Mausam, "Let's sample step by step: Adaptive-consistency for efficient reasoning and coding with LLMs," in *Proc. EMNLP*, 2023.

[4] Y. Li *et al.*, "Escape sky-high cost: Early-stopping self-consistency for multi-step reasoning," in *Proc. ICLR*, 2024.

[5] S. Kadavath *et al.*, "Language models (mostly) know what they know," arXiv:2207.05221, 2022.

[6] K. Tian *et al.*, "Just ask for calibration: Strategies for eliciting calibrated confidence scores from language models fine-tuned with human feedback," in *Proc. EMNLP*, 2023.

[7] M. Xiong *et al.*, "Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs," in *Proc. ICLR*, 2024.

[8] X. Huang *et al.*, "Uncertainty in language models: Assessment through rank-calibration," arXiv:2404.03163, 2024.

[9] Y. Li *et al.*, "Making language models better reasoners with step-aware verifier," in *Proc. ACL*, 2023.

[10] Z. Kang *et al.*, "Scalable best-of-N selection for large language models via self-certainty," arXiv:2502.18581, 2025.

[11] J. Kim *et al.*, "Reliability-aware adaptive self-consistency," arXiv:2601.02970, 2026.

[12] Y. Fu *et al.*, "Deep think with confidence," arXiv:2508.15260, 2025.

[13] A. P. Dawid and A. M. Skene, "Maximum likelihood estimation of observer error-rates using the EM algorithm," *J. Roy. Statist. Soc. C*, vol. 28, no. 1, pp. 20–28, 1979.

[14] J. Whitehill *et al.*, "Whose vote should count more: Optimal integration of labels from labelers of unknown expertise," in *Proc. NeurIPS*, 2009.

[15] D. R. Karger, S. Oh, and D. Shah, "Iterative learning for reliable crowdsourcing systems," in *Proc. NeurIPS*, 2011.

[16] F. Parisi, F. Strino, B. Nadler, and Y. Kluger, "Ranking and combining multiple predictors without labeled data," *Proc. Natl. Acad. Sci.*, vol. 111, no. 4, pp. 1253–1258, 2014.

[17] Anonymous, "FUSE: Label-free reliability estimation for ensembles of LLM verifiers," arXiv:2604.18547, 2026.

[18] Anonymous, "Beyond majority voting: Unsupervised reliability weighting of multiple LLMs," arXiv:2510.01499, 2025.

[19] P. van Elteren, "On the combination of independent two sample tests of Wilcoxon," *Bull. Int. Statist. Inst.*, vol. 37, pp. 351–361, 1960.

[20] W. James and C. Stein, "Estimation with quadratic loss," in *Proc. 4th Berkeley Symp. Math. Statist. Prob.*, 1961, pp. 361–379.

[21] L. Kish, *Survey Sampling*. New York, NY, USA: Wiley, 1965.

[22] J. N. K. Rao and A. J. Scott, "The analysis of categorical data from complex sample surveys," *J. Amer. Statist. Assoc.*, vol. 76, no. 374, pp. 221–230, 1981.

[23] L. Kuhn, Y. Gal, and S. Farquhar, "Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation," in *Proc. ICLR*, 2023.

[24] G. Wan *et al.*, "Reasoning-aware self-consistency: Leveraging reasoning paths for efficient LLM sampling," arXiv:2408.17017, 2024.
