#!/usr/bin/env python
"""Render docs/CONTRIBUTIONS.md's content as a paper-style PDF with figures.

Layout: A4, Times body with Helvetica labels, figures as full-width plates
with numbered captions. Greek letters go through the Symbol font (the built-in
Type1 fonts have no Greek glyphs; Unicode kappa/gamma would render as boxes).

    ./.venv/bin/python experiments/make_contributions_pdf.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable,
    Image,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

_SUP = "/System/Library/Fonts/Supplemental"
pdfmetrics.registerFont(TTFont("TNR", f"{_SUP}/Times New Roman.ttf"))
pdfmetrics.registerFont(TTFont("TNR-Bold", f"{_SUP}/Times New Roman Bold.ttf"))
pdfmetrics.registerFont(TTFont("TNR-Italic", f"{_SUP}/Times New Roman Italic.ttf"))
pdfmetrics.registerFont(TTFont("TNR-BoldItalic", f"{_SUP}/Times New Roman Bold Italic.ttf"))
pdfmetrics.registerFont(TTFont("Ari", f"{_SUP}/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Ari-Bold", f"{_SUP}/Arial Bold.ttf"))
registerFontFamily("TNR", normal="TNR", bold="TNR-Bold", italic="TNR-Italic", boldItalic="TNR-BoldItalic")
registerFontFamily("Ari", normal="Ari", bold="Ari-Bold", italic="Ari", boldItalic="Ari-Bold")

ROOT = Path(__file__).resolve().parents[1]
FIGDIR = ROOT / "results" / "figures"
OUT = ROOT / "docs" / "TACT-contributions.pdf"

INK = colors.HexColor("#1E2228")
MUTED = colors.HexColor("#5F6672")
POS = colors.HexColor("#B33A26")
NEG = colors.HexColor("#2A6F97")
RULE = colors.HexColor("#C9C4B8")
CHIP = colors.HexColor("#F2EFE8")

# Unicode Greek works because the registered TrueType fonts carry the glyphs
# (the built-in Type1 fonts do not -- with those, these render as black boxes).
KAPPA = "\u03ba"
GAMMA = "\u03b3"
RHO = "\u03c1\u0304"
PHI = "\u03c6"

S = dict(
    eyebrow=ParagraphStyle(
        "eyebrow", fontName="Ari", fontSize=7.4, leading=10,
        textColor=MUTED, spaceAfter=4, upperCase=True,
    ),
    title=ParagraphStyle(
        "title", fontName="TNR-Bold", fontSize=19.5, leading=23.5,
        textColor=INK, spaceAfter=6,
    ),
    subtitle=ParagraphStyle(
        "subtitle", fontName="TNR-Italic", fontSize=10.6, leading=14,
        textColor=MUTED, spaceAfter=10,
    ),
    h2=ParagraphStyle(
        "h2", fontName="Ari-Bold", fontSize=8.6, leading=11,
        textColor=MUTED, spaceBefore=16, spaceAfter=7,
    ),
    body=ParagraphStyle(
        "body", fontName="TNR", fontSize=10.3, leading=14.6,
        textColor=INK, alignment=TA_LEFT, spaceAfter=8,
    ),
    contrib_head=ParagraphStyle(
        "chead", fontName="TNR-Bold", fontSize=11.4, leading=14.5,
        textColor=INK, spaceAfter=3,
    ),
    caption=ParagraphStyle(
        "caption", fontName="TNR", fontSize=8.8, leading=12,
        textColor=MUTED, spaceBefore=4, spaceAfter=2,
    ),
    statnum=ParagraphStyle(
        "statnum", fontName="Ari-Bold", fontSize=12.5, leading=14.5, textColor=INK
    ),
    statlbl=ParagraphStyle(
        "statlbl", fontName="Ari", fontSize=7.0, leading=9.2, textColor=MUTED
    ),
    foot=ParagraphStyle(
        "foot", fontName="TNR", fontSize=8.8, leading=12.4,
        textColor=MUTED, spaceAfter=5,
    ),
)


def fig(path: Path, width_cm: float) -> Image:
    with PILImage.open(path) as im:
        w, h = im.size
    width = width_cm * cm
    return Image(str(path), width=width, height=width * h / w)


def caption(num: int, title: str, text: str) -> Paragraph:
    return Paragraph(
        f'<font color="#1E2228"><b>Figure {num} — {title}</b></font> {text}', S["caption"]
    )


def contrib(tag: str, title: str, body: str) -> Table:
    cell_tag = Paragraph(
        f'<font face="Ari-Bold" color="#B33A26" size="11">{tag}</font>', S["body"]
    )
    inner = [Paragraph(title, S["contrib_head"]), Paragraph(body, S["body"])]
    t = Table([[cell_tag, inner]], colWidths=[1.35 * cm, None])
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (0, 0), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 4),
                ("LEFTPADDING", (1, 0), (1, 0), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return t


def stats_row() -> Table:
    cells = []
    for num, lbl in [
        ("1.000 <font size='8' color='#5F6672'>vs 0.807 floor</font>",
         f"label-free accuracy on an anti-correlated channel ({KAPPA} = −0.6); every published protocol sits at the floor"),
        ("1.000 <font size='8' color='#5F6672'>vs 0.965 oracle</font>",
         "rank invariance beats the entire raw-value weight family under monotone compression"),
        ("0.940 <font size='8' color='#5F6672'>+79 / −0</font>",
         "label-free per-group voting vs the 0.808 floor; zero losses to SC over 600 paired items"),
        ("4 / 4",
         "pre-registered falsifiers survived, incl. the published CISC-devT protocol and a dev-picked signed grid"),
    ]:
        cells.append([Paragraph(num, S["statnum"]), Paragraph(lbl, S["statlbl"])])
    t = Table([cells], colWidths=[4.3 * cm] * 4, hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CHIP),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("LINEAFTER", (0, 0), (-2, -1), 0.75, colors.white),
            ]
        )
    )
    return t


def falsifier_table() -> Table:
    rows = [
        ["ID", "Falsifier (pre-registered)", "Outcome"],
        ["F1", f"TACT-dev below the best fixed-{GAMMA} CISC at {KAPPA} = +0.6", "survived — 1.000 vs 1.000"],
        ["F2", "Either variant significantly below SC anywhere on the sweep",
         f"survived — bit-identical to SC at {KAPPA} = 0"],
        ["F3", "Label-free variant fails to beat the binary ECE gate on sweep average", "survived — 0.954 vs 0.811"],
        ["F4", "CISC-devT or the dev signed grid matches TACT everywhere",
         "survived — distortion and echo cells are unreachable by grids"],
    ]
    data = [[Paragraph(f"<font face='Ari' size='7.6' color='#5F6672'><b>{c}</b></font>", S["body"])
             if r == 0 else Paragraph(c, ParagraphStyle("cell", parent=S["body"], fontSize=9.2, leading=12, spaceAfter=0))
             for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=[1.1 * cm, 9.6 * cm, 6.6 * cm], hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEBELOW", (0, 0), (-1, 0), 0.8, RULE),
                ("LINEBELOW", (0, 1), (-1, -1), 0.4, RULE),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return t


def build() -> None:
    doc = SimpleDocTemplate(
        str(OUT), pagesize=A4,
        leftMargin=2.1 * cm, rightMargin=2.1 * cm, topMargin=1.9 * cm, bottomMargin=1.9 * cm,
        title="TACT: Trust-Anchored Confidence Tempering — Contributions",
        author="vito1317",
        subject="Signed, label-free confidence tempering for self-consistency voting",
    )
    story = []
    story.append(Paragraph("DRAFT · CONTRIBUTIONS SECTION · SYNTHETIC-ORACLE EVIDENCE", S["eyebrow"]))
    story.append(Paragraph("TACT: Trust-Anchored Confidence Tempering for Self-Consistency Voting", S["title"]))
    story.append(Paragraph(
        "Signed, analytically-derived, optionally label-free trust in a frozen LLM's confidence channel "
        "— with exact self-consistency anchors and a pre-registered falsification protocol.",
        S["subtitle"],
    ))
    story.append(stats_row())
    story.append(Spacer(1, 10))

    story.append(Paragraph("PROBLEM", S["h2"]))
    story.append(Paragraph(
        "Confidence-weighted self-consistency (CISC and its successors) extracts large gains from a frozen "
        "LLM's self-reported confidence — until the channel is miscalibrated in <i>direction</i>. Every "
        "published weighting scheme is structurally monotone <b>increasing</b> in confidence, so an "
        f'<font color="#2A6F97"><b>anti-correlated</b></font> channel poisons the vote rather than informing '
        "it. Binary dev-set gates (e.g. on ECE) survive by discarding the channel entirely, wasting genuinely "
        "discriminative signal. No published method can <i>estimate the sign</i> of the confidence–correctness "
        "association, and none can do so without labels.",
        S["body"],
    ))

    story.append(Paragraph("CONTRIBUTIONS", S["h2"]))
    story.append(contrib(
        "C1", "Signed, analytically-tempered confidence weighting",
        f"We replace CISC's fixed exponent with a derived one: {GAMMA} = clip(L(shrink(D, SE))), where D is the "
        "pooled van Elteren Somers' D = 2·WQD − 1 of the channel — a pure within-item rank statistic, invariant "
        "to every strictly monotone distortion of the confidence scale — shrink is positive-part James–Stein "
        "with a significance floor, and L is the Bayes-discriminant link with a mixture-variance correction. "
        "The map carries exact anchors: inside the dead zone the vote is <b>bit-identical to plain "
        "self-consistency</b> (a shared code path — no paired test can distinguish them), and with the "
        "log-value feature map the family reproduces CISC-power exactly. Voting with "
        f"w<sub>i</sub> = exp({GAMMA}·{PHI}<sub>i</sub>) on standardized within-item rank scores makes the whole "
        "method rank-invariant: under monotone compression it beats the <i>oracle over the entire raw-value "
        "weight family</i> (1.000 vs 0.965; Fig. 2).",
    ))
    story.append(contrib(
        "C2", "Label-free estimation of the signed channel reliability",
        "The crowdsourcing lineage (Dawid–Skene; spectral meta-learners) estimates reliability from "
        "cross-annotator covariance; a single exchangeable confidence channel offers none. We estimate signed "
        "discrimination from <i>agreement pseudo-labels</i> (dedup-weighted plurality per item) and prove a "
        f"class-conditional-noise attenuation identity E[D<sub>g</sub>] = (1 − 2{RHO})·D<sub>true</sub>: the "
        "estimate can only <i>under</i>-trust, never mis-sign, whenever the pair-weighted plurality-error rate "
        "stays below ½. A split-half agreement inversion de-attenuates conservatively, and sign-aware alarms "
        "return the method to plain SC when identifiability is threatened. On the coupling sweep the label-free "
        "variant matches the 200-label variant nearly point-for-point — including full recovery of "
        f'<font color="#2A6F97"><b>negative</b></font> channels ({KAPPA} = −0.6: <b>1.000 label-free</b> vs the '
        "0.807 floor of every published protocol; Fig. 1). The honest boundary is stated: under a confident "
        "verbatim echo the sign is information-theoretically ambiguous; the alarms detect the verbatim case and "
        "refuse, and ~50 labels (sign only) restore full operation.",
    ))
    story.append(contrib(
        "C3", "An impossibility result for per-item adaptation — and the covariate-structured escape",
        f"When the per-item coupling {KAPPA}<sub>q</sub> is i.i.d. with no observable covariate, per-item "
        "label-free adaptation is closed: (i) a <i>self-reinforcement identity</i> — any monotone map from an "
        "item's own agreement statistic to an exponent reweights toward the plurality on both branches, "
        "collapsing to SC (97.5% agreement; residual flips net-harmful); (ii) a <i>winner's curse</i> — on "
        "exactly the plurality-wrong items where a flip could win, the observable sign opposes the truth 96% of "
        f"the time; (iii) <i>two-world unidentifiability</i> — {{{KAPPA}&gt;0, minority correct}} and "
        f"{{{KAPPA}&lt;0, plurality correct}} induce identical observable laws. The per-item oracle (0.983) is "
        "therefore unreachable, and TACT's dead zone degrades to <i>exactly</i> SC there (zero discordant "
        "pairs; Fig. 3, right). When heterogeneity is instead indexed by an observable covariate — "
        "domain-dependent calibration, the realistic case — the same estimator run per group recovers each "
        "group's signed coupling (label-free: {+2.0, 0.0, −2.0}) and cracks the floor that provably binds every "
        "global policy: <b>0.940 label-free vs the 0.808 floor</b>, within 0.007 of the per-item oracle, with "
        "zero losses to SC (+79/−0, p = 3.3×10<super>−24</super>; Fig. 3, left).",
    ))
    story.append(contrib(
        "C4", "A pre-registered falsification protocol with the strongest baselines included",
        "Four falsifiers were fixed before implementation — including the two designed to kill the method: the "
        "<i>published</i> dev-calibrated protocol (CISC-devT, whose tuned temperature already interpolates "
        "SC↔CISC) and a trivial dev-picked signed exponent grid. All four survived, and the honest margins are "
        "reported: against the signed grid the net advantage concentrates in exactly three cells — monotone "
        "distortion (+0.035), confident echo (+0.035), and label-free operation, which no grid can perform. As "
        "a matched pair of honest outcomes, the same protocol applied to our preceding system (RLEV-VoI, "
        "redundancy-discounted voting) <i>fired</i> four of five falsifiers; that system is reported as a "
        "negative result whose post-mortem motivated this work.",
    ))

    story.append(Paragraph("FIGURES", S["h2"]))
    story.append(KeepTogether([
        fig(FIGDIR / "tact_sweep.png", 15.2),
        caption(1, "The confidence-usage frontier.",
                "Published protocols (CISC-devT, the ECE gate) sit at the self-consistency floor across the "
                "entire negative half-axis; TACT-dev and the fully label-free TACT-LF track the oracle over the "
                f"whole sweep, including signed recovery at {KAPPA} &lt; 0. 400 paired items per cell, K = 15."),
    ]))
    story.append(Spacer(1, 8))
    story.append(KeepTogether([
        fig(FIGDIR / "tact_adversarial.png", 16.4),
        caption(2, "Adversarial regimes.",
                "Dotted line: the oracle over raw-value weights. Rank invariance beats that entire family under "
                "monotone compression (1.000 vs 0.965). In the confident-echo cell the labeled variant counters "
                f"the poison with a negative exponent ({GAMMA} = −1.20; 0.585 vs SC 0.200) while the label-free "
                "variant alarms and refuses — its conditional guarantee working as stated."),
    ]))
    story.append(Spacer(1, 8))
    story.append(KeepTogether([
        fig(FIGDIR / "group_eval.png", 16.4),
        caption(3, "Structured vs i.i.d. heterogeneity.",
                "Left: with an observable covariate, per-group TACT (label-free, 0.940) approaches the per-item "
                "oracle (0.947) from a floor of 0.808 with zero losses to SC. Right: the provably-closed i.i.d. "
                "cell — every legitimate method sits at the floor and TACT degrades to exactly SC; the naive "
                "self-referential method (negative control) lands slightly below it."),
    ]))
    story.append(Spacer(1, 8))
    story.append(KeepTogether([
        fig(FIGDIR / "kappa_sweep.png", 14.4),
        caption(4, "The pre-measured problem statement.",
                "Baseline headroom mapped <i>before</i> TACT existed: a trivial sign-corrected AUC gate nearly "
                "saturates the homogeneous sweep, isolating the only cells where a new method could win — "
                "monotone distortion, heterogeneity, small dev sets, and label-free operation. TACT's claims "
                "live exactly there."),
    ]))

    story.append(Paragraph("FALSIFIERS", S["h2"]))
    story.append(falsifier_table())

    story.append(Spacer(1, 14))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Evidence status.</b> All quantitative claims are on a synthetic-oracle harness (paired trace pools, "
        "McNemar tests, 400–600 items per cell) whose adversarial regimes lie outside the estimator's working "
        "model; mechanism-recovery and accuracy claims are reported separately to limit circularity. Validation "
        "on real LLM traces is the remaining step; the cached-trace runner is committed "
        "(experiments/run_real_api.py).",
        S["foot"],
    ))
    story.append(Paragraph(
        "Repository: vito1317/adaptive-reasoning-consensus (private) · spec docs/SPEC-TACT.md · full report "
        "docs/REPORT-TACT.md · 76 tests. Every number traceable to results/*.json; figures reproducible from "
        "the committed scripts.",
        S["foot"],
    ))

    doc.build(story)
    print(f"wrote {OUT} ({OUT.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    build()
