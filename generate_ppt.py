import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    PRIMARY_DARK = RGBColor(15, 23, 42)      # Slate 900
    PRIMARY_BLUE = RGBColor(30, 58, 138)     # Navy Blue
    ACCENT_BLUE = RGBColor(37, 99, 235)      # Royal Blue
    ACCENT_CYAN = RGBColor(14, 165, 233)     # Cyan
    ACCENT_GREEN = RGBColor(16, 185, 129)    # Emerald Green
    ACCENT_RED = RGBColor(239, 68, 68)       # Coral Red
    BG_LIGHT = RGBColor(248, 250, 252)       # Slate 50
    CARD_BG = RGBColor(255, 255, 255)        # Pure White
    CARD_BORDER = RGBColor(226, 232, 240)    # Slate 200
    TEXT_MAIN = RGBColor(30, 41, 59)         # Slate 800
    TEXT_MUTED = RGBColor(100, 116, 139)     # Slate 500
    WHITE = RGBColor(255, 255, 255)

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, category, title, subtitle=None):
        # Top banner background
        header_bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        header_bg.fill.solid()
        header_bg.fill.fore_color.rgb = PRIMARY_DARK
        header_bg.line.fill.background()

        # Accent bar on bottom of header
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.15), Inches(13.333), Inches(0.05))
        bar.fill.solid()
        bar.fill.fore_color.rgb = ACCENT_BLUE
        bar.line.fill.background()

        # Text in header
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.7), Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = category.upper()
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_CYAN

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(22)
        p2.font.bold = True
        p2.font.color.rgb = WHITE

        # Footer
        footer_tb = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.7), Inches(0.35))
        ftf = footer_tb.text_frame
        ftf.word_wrap = True
        fp = ftf.paragraphs[0]
        fp.text = "SmartInv: Multimodal Learning for Smart Contract Invariant Inference | Rishi (2024ucp1566) | Mid-Sem Evaluation"
        fp.font.size = Pt(9.5)
        fp.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title=None, bg_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)

        if title:
            tb = slide.shapes.add_textbox(Inches(left + 0.25), Inches(top + 0.2), Inches(width - 0.5), Inches(0.5))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(16)
            p.font.bold = True
            p.font.color.rgb = PRIMARY_DARK

        return card

    # ==========================================
    # SLIDE 1: Title Slide (Dark Theme)
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1, PRIMARY_DARK)

    # Decorative accent card
    card_glow = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(11.733), Inches(5.5))
    card_glow.fill.solid()
    card_glow.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card_glow.line.color.rgb = ACCENT_BLUE
    card_glow.line.width = Pt(2)

    # Header Tag
    tb_tag = slide1.shapes.add_textbox(Inches(1.3), Inches(1.4), Inches(10), Inches(0.5))
    p_tag = tb_tag.text_frame.paragraphs[0]
    p_tag.text = "🌟 A* RESEARCH PAPER PRESENTATION | IEEE S&P 2024"
    p_tag.font.size = Pt(13)
    p_tag.font.bold = True
    p_tag.font.color.rgb = ACCENT_CYAN

    # Title & Subtitle
    tb_title = slide1.shapes.add_textbox(Inches(1.3), Inches(2.0), Inches(10.7), Inches(2.2))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    p_t1 = tf_title.paragraphs[0]
    p_t1.text = "SmartInv: Multimodal Invariant Inference"
    p_t1.font.size = Pt(36)
    p_t1.font.bold = True
    p_t1.font.color.rgb = WHITE

    p_t2 = tf_title.add_paragraph()
    p_t2.text = "Automated Security Verification for Smart Contracts using LLMs & Formal Methods"
    p_t2.font.size = Pt(18)
    p_t2.font.color.rgb = RGBColor(148, 163, 184)

    # Divider
    div = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.3), Inches(4.3), Inches(10.7), Inches(0.04))
    div.fill.solid()
    div.fill.fore_color.rgb = ACCENT_BLUE
    div.line.fill.background()

    # Meta Info Boxes
    meta_box1 = slide1.shapes.add_textbox(Inches(1.3), Inches(4.6), Inches(5.0), Inches(1.5))
    tf_m1 = meta_box1.text_frame
    p_m1 = tf_m1.paragraphs[0]
    p_m1.text = "PRESENTER INFORMATION"
    p_m1.font.size = Pt(11)
    p_m1.font.bold = True
    p_m1.font.color.rgb = ACCENT_CYAN

    p_m2 = tf_m1.add_paragraph()
    p_m2.text = "Name: Rishi\nStudent ID: 2024ucp1566\nEvaluation: Mid-Semester Project Review"
    p_m2.font.size = Pt(14)
    p_m2.font.color.rgb = WHITE

    meta_box2 = slide1.shapes.add_textbox(Inches(6.8), Inches(4.6), Inches(5.2), Inches(1.5))
    tf_m2 = meta_box2.text_frame
    p_m3 = tf_m2.paragraphs[0]
    p_m3.text = "ORIGINAL RESEARCH CITATION"
    p_m3.font.size = Pt(11)
    p_m3.font.bold = True
    p_m3.font.color.rgb = ACCENT_CYAN

    p_m4 = tf_m2.add_paragraph()
    p_m4.text = "Columbia University (New York, USA)\nAuthors: Sally Junsong Wang, Kexin Pei, Junfeng Yang\nConference: IEEE Symposium on Security & Privacy 2024"
    p_m4.font.size = Pt(13)
    p_m4.font.color.rgb = RGBColor(203, 213, 225)

    # ==========================================
    # SLIDE 2: What are Smart Contracts & The Stakes
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2, BG_LIGHT)
    add_header(slide2, "Background & Context", "Why Smart Contract Security is Critical")

    # Card 1: What is a Smart Contract?
    add_card(slide2, 0.8, 1.45, 5.6, 5.3, "📜 What is a Smart Contract?")
    tb = slide2.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(5.1), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    bullets1 = [
        ("Self-Executing Code", "Programs stored directly on the Ethereum blockchain that run automatically without middlemen."),
        ("The Vending Machine Analogy", "Put in money, choose an option, rules execute automatically and cannot be altered."),
        ("DeFi (Decentralized Finance)", "Powering digital banking, lending, token swaps, and multi-billion-dollar liquidity pools."),
        ("No Do-Overs", "Unlike normal software, blockchain transactions are PERMANENT and IRREVERSIBLE.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets1):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_BLUE
        
        # Add description part
        p_desc = tf.add_paragraph()
        p_desc.text = f"  {b_desc}\n"
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_MAIN

    # Card 2: The Critical Danger
    add_card(slide2, 6.9, 1.45, 5.6, 5.3, "⚠️ The Multi-Billion Dollar Threat")
    tb2 = slide2.shapes.add_textbox(Inches(7.15), Inches(2.15), Inches(5.1), Inches(4.3))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    bullets2 = [
        ("Immutability Trap", "Once deployed, code CANNOT be patched. If there is a bug, anyone in the world can exploit it 24/7."),
        ("Astronomical Losses", "Over $3.8 Billion stolen in DeFi smart contract exploits in recent years alone."),
        ("High Audit Costs", "Human security audits cost $50,000 to $500,000+ per contract, yet human auditors still miss subtle logic bugs."),
        ("The Core Need", "An automated, intelligent system that can find complex logical vulnerabilities before hackers do.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets2):
        p = tf2.paragraphs[0] if i == 0 else tf2.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_RED
        
        p_desc = tf2.add_paragraph()
        p_desc.text = f"  {b_desc}\n"
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 3: Two Types of Bugs - The Core Problem
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3, BG_LIGHT)
    add_header(slide3, "The Problem Statement", "Implementation Bugs vs. Machine Un-auditable Bugs")

    # Column 1: Implementation Bugs
    add_card(slide3, 0.8, 1.45, 5.6, 5.3, "🟢 Type 1: Implementation Bugs (Easy)")
    tb = slide3.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(5.1), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    items1 = [
        ("What they are", "Low-level coding mistakes, syntax errors, or well-known vulnerability patterns."),
        ("Classic Examples", "Reentrancy attacks (e.g. DAO Hack), Integer Overflow / Underflow, Unchecked return values."),
        ("Detection Status", "SOLVED by existing automated tools (Slither, Mythril, Securify)."),
        ("Why tools can catch them", "Tools look for predefined syntax patterns (e.g., 'call before state update').")
    ]
    for i, (b_title, b_desc) in enumerate(items1):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"✔ {b_title}: "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p_d = tf.add_paragraph()
        p_d.text = f"  {b_desc}\n"
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MAIN

    # Column 2: Functional Bugs (Machine Un-auditable)
    add_card(slide3, 6.9, 1.45, 5.6, 5.3, "🔴 Type 2: Functional Bugs (The Real Threat)", bg_color=CARD_BG, border_color=ACCENT_RED)
    tb2 = slide3.shapes.add_textbox(Inches(7.15), Inches(2.15), Inches(5.1), Inches(4.3))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    items2 = [
        ("What they are", "Business logic flaws. Code compiles and runs perfectly, but behaves against developer intention!"),
        ("Classic Examples", "Price manipulation, unauthorized privilege escalation, flawed reward distribution, broken invariant rules."),
        ("Detection Status", "COMPLETELY MISSED by traditional tools (0% caught). Called 'Machine Un-auditable'."),
        ("The Core Dilemma", "Traditional tools don't know what the contract is SUPPOSED to do!")
    ]
    for i, (b_title, b_desc) in enumerate(items2):
        p = tf2.paragraphs[0] if i == 0 else tf2.add_paragraph()
        p.text = f"❌ {b_title}: "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_RED
        p_d = tf2.add_paragraph()
        p_d.text = f"  {b_desc}\n"
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 4: Case Study - Visor Finance Hack
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4, BG_LIGHT)
    add_header(slide4, "Real-World Motivating Example", "The $8.2M Visor Finance Hack (Why Existing Tools Failed)")

    # Left Card: The Exploit
    add_card(slide4, 0.8, 1.45, 6.0, 5.3, "💥 What Happened in Visor Finance?")
    tb = slide4.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(5.5), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    v_points = [
        ("The Contract Function", "`deposit(uint amount, address token)` allowed users to deposit funds into a vault."),
        ("The Subtle Flaw", "The contract forwarded a call to `supervisor.approve()`, but NEVER verified if `supervisor` was the genuine contract!"),
        ("The Attack", "An attacker passed a fake malicious supervisor address. The contract approved unlimited tokens to the attacker."),
        ("The Result", "$8,200,000 was drained in a single transaction in December 2021.")
    ]
    for i, (b_title, b_desc) in enumerate(v_points):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_BLUE
        p_d = tf.add_paragraph()
        p_d.text = f"  {b_desc}\n"
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MAIN

    # Right Card: The Tool Comparison
    add_card(slide4, 7.1, 1.45, 5.4, 5.3, "🔍 Tool Performance on Visor")
    tb2 = slide4.shapes.add_textbox(Inches(7.35), Inches(2.15), Inches(4.9), Inches(4.3))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    tools = [
        ("Slither (Static Analysis)", "❌ Reported: 0 Bugs (Safe)", TEXT_MUTED),
        ("Mythril (Symbolic Execution)", "❌ Reported: 0 Bugs (Safe)", TEXT_MUTED),
        ("Manticore (Dynamic Analysis)", "❌ Reported: 0 Bugs (Safe)", TEXT_MUTED),
        ("VeriSmart (Formal Verifier)", "❌ Reported: 0 Bugs (Safe)", TEXT_MUTED),
        ("SmartInv (Proposed Paper)", "✅ DETECTED BUG & PROVED IT!", ACCENT_GREEN)
    ]
    for i, (t_name, t_res, col) in enumerate(tools):
        p = tf2.paragraphs[0] if i == 0 else tf2.add_paragraph()
        p.text = f"{t_name}:"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_DARK

        p_res = tf2.add_paragraph()
        p_res.text = f"  {t_res}\n"
        p_res.font.size = Pt(13)
        p_res.font.bold = True
        p_res.font.color.rgb = col

    # ==========================================
    # SLIDE 5: What is an Invariant?
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5, BG_LIGHT)
    add_header(slide5, "Core Concept", "What is an Invariant? (The Mathematical Key)")

    # Card 1: Plain English Definition
    add_card(slide5, 0.8, 1.45, 11.733, 1.6, "💡 Invariant Defined in 1 Sentence")
    tb = slide5.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(11.2), Inches(0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "\"An invariant is a safety condition or business rule that must ALWAYS remain TRUE throughout the entire program execution, no matter what actions a user or hacker takes.\""
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    # 3 Example Cards
    cards_data = [
        ("1. Balance Invariant", "assert(balance_after >= balance_before)", "After depositing funds, a user's vault balance must never decrease.", ACCENT_BLUE),
        ("2. Token Supply Invariant", "assert(totalSupply == sum(all_balances))", "The total minted currency must strictly equal the sum of all individual user wallets.", ACCENT_GREEN),
        ("3. Authorization Invariant", "assert(msg.sender == owner)", "Critical admin functions (like draining reserves) must only execute for authorized creators.", ACCENT_RED)
    ]
    for idx, (c_title, c_code, c_desc, c_col) in enumerate(cards_data):
        left_pos = 0.8 + idx * 4.0
        add_card(slide5, left_pos, 3.25, 3.733, 3.5, c_title, border_color=c_col)
        tb_c = slide5.shapes.add_textbox(Inches(left_pos + 0.2), Inches(3.9), Inches(3.333), Inches(2.6))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p1 = tf_c.paragraphs[0]
        p1.text = "Mathematical Rule:"
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_MUTED

        p2 = tf_c.add_paragraph()
        p2.text = c_code
        p2.font.size = Pt(11.5)
        p2.font.bold = True
        p2.font.color.rgb = c_col

        p3 = tf_c.add_paragraph()
        p3.text = f"\nMeaning:\n{c_desc}"
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 6: SmartInv Overview & 3 Key Ideas
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6, BG_LIGHT)
    add_header(slide6, "The SmartInv Solution", "How SmartInv Solves Machine Un-auditable Bugs")

    ideas = [
        ("1. Multimodal Learning", "Combines 3 Sources of Information", [
            "Source Code (Solidity logic)",
            "Natural Language (Docstrings, comments & specs)",
            "Transaction Traces (Execution history)",
            "Like a doctor using X-rays + blood tests + patient symptoms together."
        ], ACCENT_BLUE),
        ("2. Tier of Thought (ToT)", "6-Step Structured AI Reasoning", [
            "Upgrades standard prompt engineering.",
            "Deconstructs expert auditing into 6 distinct cognitive steps.",
            "Each tier answers a specialized question fed to the next tier.",
            "Prevents AI hallucinations."
        ], ACCENT_GREEN),
        ("3. Formal Verification", "Mathematical Proof with VeriSol", [
            "Translates inferred invariants into Boogie formal logic.",
            "Corral model checker searches for violation paths.",
            "Produces concrete counterexample execution traces.",
            "Zero false confidence — 100% mathematically verified."
        ], ACCENT_CYAN)
    ]

    for idx, (i_title, i_sub, i_bullets, i_col) in enumerate(ideas):
        left_pos = 0.8 + idx * 4.0
        add_card(slide6, left_pos, 1.45, 3.733, 5.3, i_title, border_color=i_col)
        tb_i = slide6.shapes.add_textbox(Inches(left_pos + 0.25), Inches(2.1), Inches(3.233), Inches(4.4))
        tf_i = tb_i.text_frame
        tf_i.word_wrap = True

        p_sub = tf_i.paragraphs[0]
        p_sub.text = i_sub.upper()
        p_sub.font.size = Pt(10.5)
        p_sub.font.bold = True
        p_sub.font.color.rgb = i_col

        for b in i_bullets:
            p_b = tf_i.add_paragraph()
            p_b.text = f"\n• {b}"
            p_b.font.size = Pt(12)
            p_b.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 7: The 3-Phase Pipeline Architecture
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7, BG_LIGHT)
    add_header(slide7, "System Architecture", "The End-to-End SmartInv Pipeline")

    phases = [
        ("PHASE 1: TRAINING", "Teaching the AI Invariant Patterns", [
            "Collected 80,000+ real Ethereum smart contracts.",
            "Expert manual labeling of 2,000+ invariant samples.",
            "Formatted into 3,000+ Tier of Thought (ToT) question-answer pairs.",
            "Fine-tuned LLaMA-7B using PEFT / LoRA adapter weights."
        ], PRIMARY_BLUE),
        ("PHASE 2: INFERENCE", "Tier of Thought Invariant Generation", [
            "Takes ANY unseen smart contract (.sol file).",
            "Passes through 6 cognitive tiers (Context -> Program Points -> Invariants -> Ranking -> Vulnerability).",
            "Synthesizes bug-critical invariants at specific lines.",
            "Operates in seconds per contract."
        ], ACCENT_BLUE),
        ("PHASE 3: VERIFICATION", "Mathematical Counterexample Proof", [
            "Instruments inferred invariants into contract.",
            "VeriSol compiles contract into Boogie IR language.",
            "Corral Bounded Model Checker proves or disproves invariants.",
            "Outputs exact counterexample exploit trace if violated."
        ], ACCENT_GREEN)
    ]

    for idx, (p_title, p_sub, p_bullets, p_col) in enumerate(phases):
        left_pos = 0.8 + idx * 4.0
        add_card(slide7, left_pos, 1.45, 3.733, 5.3, p_title, border_color=p_col)
        tb_p = slide7.shapes.add_textbox(Inches(left_pos + 0.25), Inches(2.15), Inches(3.233), Inches(4.3))
        tf_p = tb_p.text_frame
        tf_p.word_wrap = True

        p_s = tf_p.paragraphs[0]
        p_s.text = p_sub
        p_s.font.size = Pt(11)
        p_s.font.bold = True
        p_s.font.color.rgb = p_col

        for b in p_bullets:
            pb = tf_p.add_paragraph()
            pb.text = f"\n✔ {b}"
            pb.font.size = Pt(12)
            pb.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 8: Deep Dive: Tier of Thought (ToT)
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8, BG_LIGHT)
    add_header(slide8, "Core Innovation", "The 6-Step Tier of Thought (ToT) Pipeline")

    tiers = [
        ("Tier 1A: Transaction Context", "What business domain is this? (e.g., cross-function, token lending, swaps, arithmetics).", ACCENT_BLUE),
        ("Tier 1B: Critical Program Points", "Which exact line numbers handle security-sensitive logic, fund transfers, or state changes?", ACCENT_BLUE),
        ("Tier 2A: Invariant Generation", "Given the critical lines, what mathematical assert statements MUST always hold true?", ACCENT_GREEN),
        ("Tier 2B: Critical Filter", "Filters out trivial rules (like x==x) to retain only bug-preventing invariants.", ACCENT_GREEN),
        ("Tier 3A: Invariant Ranking", "Sorts invariants by security priority so auditors focus on highest-risk conditions first.", ACCENT_CYAN),
        ("Tier 3B: Vulnerability Inference", "Synthesizes bug classification (Healthy vs. Logic Flaw / Privilege Escalation).", ACCENT_RED)
    ]

    for idx, (t_name, t_desc, t_col) in enumerate(tiers):
        col_idx = idx % 2
        row_idx = idx // 2
        left_pos = 0.8 + col_idx * 6.0
        top_pos = 1.45 + row_idx * 1.75

        add_card(slide8, left_pos, top_pos, 5.733, 1.55, t_name, border_color=t_col)
        tb_t = slide8.shapes.add_textbox(Inches(left_pos + 0.25), Inches(top_pos + 0.65), Inches(5.2), Inches(0.8))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        pt = tf_t.paragraphs[0]
        pt.text = t_desc
        pt.font.size = Pt(12.5)
        pt.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 9: Concrete Walkthrough on a Contract
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9, BG_LIGHT)
    add_header(slide9, "Methodology in Action", "Step-by-Step Contract Execution Walkthrough")

    # Left: Contract Code
    add_card(slide9, 0.8, 1.45, 5.2, 5.3, "📄 Input Smart Contract")
    tb_code = slide9.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(4.7), Inches(4.3))
    tf_c = tb_code.text_frame
    tf_c.word_wrap = True
    code_lines = (
        "1  pragma solidity >=0.5.0;\n"
        "2  contract Vault {\n"
        "3    mapping(address => uint) public bal;\n"
        "4    address public supervisor;\n"
        "5\n"
        "6    function deposit(uint amount) external {\n"
        "7      // critical transfer point\n"
        "8      supervisor.approve(msg.sender, amount);\n"
        "9      bal[msg.sender] += amount;\n"
        "10   }\n"
        "11 }"
    )
    p_c = tf_c.paragraphs[0]
    p_c.text = code_lines
    p_c.font.size = Pt(12)
    p_c.font.name = "Courier New"
    p_c.font.color.rgb = PRIMARY_BLUE

    # Right: ToT Execution Flow
    add_card(slide9, 6.3, 1.45, 6.233, 5.3, "⚙️ ToT Reasoning Progression")
    tb_flow = slide9.shapes.add_textbox(Inches(6.55), Inches(2.15), Inches(5.7), Inches(4.3))
    tf_f = tb_flow.text_frame
    tf_f.word_wrap = True
    flow_steps = [
        ("Tier 1A Output", "Context: 'Cross-function token vault approval'"),
        ("Tier 1B Output", "Critical Program Point: Line 8 (Supervisor approval)"),
        ("Tier 2A/2B Output", "Inferred Invariant:\n  8+ assert(supervisor == trustedVaultSupervisor)"),
        ("Tier 3A/3B Output", "High Priority | Bug: 'Unauthorized Privilege Escalation'"),
        ("Verification Result", "❌ Invariant Violated! Attacker can supply fake supervisor.")
    ]
    for i, (f_title, f_desc) in enumerate(flow_steps):
        p = tf_f.paragraphs[0] if i == 0 else tf_f.add_paragraph()
        p.text = f"{f_title}: "
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_DARK

        pd = tf_f.add_paragraph()
        pd.text = f"  {f_desc}\n"
        pd.font.size = Pt(12)
        pd.font.color.rgb = ACCENT_BLUE if i < 4 else ACCENT_RED

    # ==========================================
    # SLIDE 10: Experimental Results & Benchmarks
    # ==========================================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10, BG_LIGHT)
    add_header(slide10, "Experimental Evaluation", "Key Results on 80,000+ Smart Contracts")

    # 3 Stat Cards on Top
    stat_cards = [
        ("3.5×", "More Bug-Critical Invariants", "Compared to previous formal tools", ACCENT_BLUE),
        ("4.0×", "More Critical Bugs Detected", "Specifically functional logic flaws", ACCENT_GREEN),
        ("150×", "Faster Execution Speed", "Seconds vs. hours of symbolic execution", ACCENT_CYAN)
    ]
    for idx, (s_num, s_title, s_desc, s_col) in enumerate(stat_cards):
        left_pos = 0.8 + idx * 4.0
        add_card(slide10, left_pos, 1.45, 3.733, 1.9, border_color=s_col)
        tb_s = slide10.shapes.add_textbox(Inches(left_pos + 0.2), Inches(1.55), Inches(3.333), Inches(1.7))
        tf_s = tb_s.text_frame
        tf_s.word_wrap = True

        p1 = tf_s.paragraphs[0]
        p1.text = s_num
        p1.font.size = Pt(32)
        p1.font.bold = True
        p1.font.color.rgb = s_col

        p2 = tf_s.add_paragraph()
        p2.text = s_title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = PRIMARY_DARK

        p3 = tf_s.add_paragraph()
        p3.text = s_desc
        p3.font.size = Pt(10.5)
        p3.font.color.rgb = TEXT_MUTED

    # Bottom Comparison Summary Card
    add_card(slide10, 0.8, 3.55, 11.733, 3.2, "📊 Tool Comparison Summary (1,200+ Ground-Truth Benchmark)")
    tb_table = slide10.shapes.add_textbox(Inches(1.05), Inches(4.15), Inches(11.2), Inches(2.4))
    tf_t = tb_table.text_frame
    tf_t.word_wrap = True

    table_rows = [
        ("Slither", "Static Analysis", "Fast", "High False Positives", "Misses all functional bugs"),
        ("Mythril", "Symbolic Exec", "Slow (Hours)", "Moderate", "Suffers path explosion"),
        ("Manticore", "Dynamic Analysis", "Very Slow", "Moderate", "Scalability bottleneck"),
        ("SmartInv (Paper)", "Multimodal AI + Verifier", "Fast (Seconds)", "Low (Verified)", "Detects & Proves Functional Bugs ⭐")
    ]
    for tr_tool, tr_type, tr_speed, tr_fp, tr_verdict in table_rows:
        p_row = tf_t.add_paragraph()
        p_row.text = f"• {tr_tool.ljust(18)} | Type: {tr_type.ljust(22)} | Speed: {tr_speed.ljust(14)} | Verdict: {tr_verdict}"
        p_row.font.size = Pt(12)
        p_row.font.color.rgb = ACCENT_GREEN if "SmartInv" in tr_tool else TEXT_MAIN
        p_row.font.bold = "SmartInv" in tr_tool

    # ==========================================
    # SLIDE 11: Real-World Discoveries - 119 Zero-Days
    # ==========================================
    slide11 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide11, BG_LIGHT)
    add_header(slide11, "Real-World Impact", "119 Zero-Day Vulnerabilities Discovered on Ethereum")

    # Left: Big Callout
    add_card(slide11, 0.8, 1.45, 5.6, 5.3, "🛡️ Live Mainnet Findings", border_color=ACCENT_RED)
    tb_l = slide11.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(5.1), Inches(4.3))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    points_z = [
        ("119 Zero-Day Bugs", "SmartInv was run on deployed Ethereum contracts and discovered 119 previously unknown vulnerabilities!"),
        ("5 High-Severity Confirmed", "5 critical vulnerabilities were officially confirmed by project developer teams upon responsible disclosure."),
        ("100% Missed by Others", "Every single one of these 119 bugs was completely missed by Slither, Mythril, and Manticore."),
        ("Real Financial Protection", "Prevented millions in potential exploit losses before malicious hackers could discover them.")
    ]
    for i, (b_title, b_desc) in enumerate(points_z):
        p = tf_l.paragraphs[0] if i == 0 else tf_l.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_RED
        pd = tf_l.add_paragraph()
        pd.text = f"  {b_desc}\n"
        pd.font.size = Pt(12)
        pd.font.color.rgb = TEXT_MAIN

    # Right: Bug Categories Found
    add_card(slide11, 6.9, 1.45, 5.6, 5.3, "📋 Discovered Vulnerability Categories")
    tb_r = slide11.shapes.add_textbox(Inches(7.15), Inches(2.15), Inches(5.1), Inches(4.3))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    cats = [
        ("Business Logic Inconsistencies", "Flawed calculation rules in liquidity vaults and staking contracts."),
        ("Privilege Escalation", "Unauthorized callers triggering state-altering or administrative actions."),
        ("Atomicity & Cross-Call Failures", "External contract calls updating balance without synchronizing global state."),
        ("Price Oracle Manipulation", "Flawed price reporting allowing attackers to borrow assets below fair market value.")
    ]
    for i, (c_title, c_desc) in enumerate(cats):
        p = tf_r.paragraphs[0] if i == 0 else tf_r.add_paragraph()
        p.text = f"✔ {c_title}:"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_BLUE
        pd = tf_r.add_paragraph()
        pd.text = f"  {c_desc}\n"
        pd.font.size = Pt(12)
        pd.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 12: Ablation Study - What Makes It Work?
    # ==========================================
    slide12 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide12, BG_LIGHT)
    add_header(slide12, "Scientific Rigor", "Ablation Study: Proving the Power of ToT")

    # Left: Explanation Card
    add_card(slide12, 0.8, 1.45, 5.4, 5.3, "🔬 What is an Ablation Study?")
    tb_ab = slide12.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(4.9), Inches(4.3))
    tf_ab = tb_ab.text_frame
    tf_ab.word_wrap = True

    ab_text = [
        ("Scientific Goal", "Remove components one by one to scientifically isolate which innovation provides the real performance gain."),
        ("Finding #1: Tier of Thought is King", "Removing ToT causes the F1-Score to collapse by 66% (from 0.82 down to 0.16)."),
        ("Finding #2: Natural Language Matters", "Removing natural language reduces functional bug detection by 40× (F1 drops 37%)."),
        ("Key Conclusion", "The structured cognitive reasoning of ToT is the primary breakthrough of this paper.")
    ]
    for i, (b_title, b_desc) in enumerate(ab_text):
        p = tf_ab.paragraphs[0] if i == 0 else tf_ab.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_BLUE
        pd = tf_ab.add_paragraph()
        pd.text = f"  {b_desc}\n"
        pd.font.size = Pt(12)
        pd.font.color.rgb = TEXT_MAIN

    # Right: Data Table Card
    add_card(slide12, 6.5, 1.45, 6.033, 5.3, "📊 Ablation Results (Table 9 & 11)")
    tb_res = slide12.shapes.add_textbox(Inches(6.75), Inches(2.15), Inches(5.5), Inches(4.3))
    tf_res = tb_res.text_frame
    tf_res.word_wrap = True

    ab_rows = [
        ("Full SmartInv (All Components)", "0.89", "0.82", "Baseline (Best) ⭐", ACCENT_GREEN),
        ("Remove Optimization", "0.89", "0.82", "Minimal change", TEXT_MAIN),
        ("Remove Labeled Features", "0.59", "0.60", "-22% F1 Drop", TEXT_MUTED),
        ("Remove Natural Language (NL)", "0.62", "0.45", "-37% F1 Drop 📉", ACCENT_RED),
        ("Remove Tier of Thought (ToT)", "0.24", "0.16", "-66% F1 Collapse 📉📉", ACCENT_RED),
        ("Baseline LLM (No specialization)", "0.12", "0.14", "Complete failure", ACCENT_RED)
    ]
    for name, acc, f1, note, col in ab_rows:
        p = tf_res.add_paragraph()
        p.text = f"• {name}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = col

        pd = tf_res.add_paragraph()
        pd.text = f"  Accuracy: {acc} | F1-Score: {f1} ({note})\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 13: Local Implementation & Practical Work
    # ==========================================
    slide13 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide13, BG_LIGHT)
    add_header(slide13, "Mid-Semester Progress", "Practical Work Executed on Local Machine")

    milestones = [
        ("1. Environment & Setup", [
            "Cloned full research repository and configured dependencies.",
            "Installed PyTorch 2.8, HuggingFace Transformers, PEFT, and OpenAI SDK.",
            "Created clean workspace structure with Git version tracking."
        ], PRIMARY_BLUE),
        ("2. Bug Fixing & Compatibility", [
            "Fixed Windows file encoding bug (UnicodeEncodeError) in dataset generator.",
            "Replaced hardcoded Linux paths with dynamic relative pathing.",
            "Patched OpenAI client initialization crash for offline and help commands."
        ], ACCENT_BLUE),
        ("3. Dataset Processing & Verification", [
            "Executed generator.py — generated all 3,000+ ToT structured prompt-completion pairs.",
            "Verified smartinv.py CLI execution (Exit Code 0).",
            "Tested standalone and verifier components on sample contracts."
        ], ACCENT_GREEN),
        ("4. Documentation & Repository", [
            "Authored 5 comprehensive study guides in dedicated study_guide/ directory.",
            "Configured Git remotes (origin -> User GitHub, upstream -> Columbia).",
            "Prepared complete presentation defense material."
        ], ACCENT_CYAN)
    ]

    for idx, (m_title, m_bullets, m_col) in enumerate(milestones):
        col_idx = idx % 2
        row_idx = idx // 2
        left_pos = 0.8 + col_idx * 6.0
        top_pos = 1.45 + row_idx * 2.65

        add_card(slide13, left_pos, top_pos, 5.733, 2.45, m_title, border_color=m_col)
        tb_m = slide13.shapes.add_textbox(Inches(left_pos + 0.25), Inches(top_pos + 0.65), Inches(5.2), Inches(1.7))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True

        for b in m_bullets:
            p = tf_m.add_paragraph()
            p.text = f"✔ {b}"
            p.font.size = Pt(11.5)
            p.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 14: Limitations & Future Enhancements
    # ==========================================
    slide14 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide14, BG_LIGHT)
    add_header(slide14, "Critical Analysis", "Limitations & Future Roadmap")

    # Left: Limitations
    add_card(slide14, 0.8, 1.45, 5.6, 5.3, "⚠️ Current System Limitations")
    tb_lim = slide14.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(5.1), Inches(4.3))
    tf_lim = tb_lim.text_frame
    tf_lim.word_wrap = True

    lims = [
        ("LLM Non-Determinism", "Commercial models (like GPT-4 in light mode) can generate varying outputs across runs."),
        ("Heavy Manual Annotation", "Curating initial invariant training sets requires substantial expert human effort."),
        ("Verifier Compiler Bounds", "VeriSol is bound to specific Solidity versions and cannot compile all cutting-edge compiler constructs."),
        ("Human Assistance Still Needed", "SmartInv is designed as an auditor assistant, not a 100% autonomous replacement.")
    ]
    for i, (b_title, b_desc) in enumerate(lims):
        p = tf_lim.paragraphs[0] if i == 0 else tf_lim.add_paragraph()
        p.text = f"• {b_title}: "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_RED
        pd = tf_lim.add_paragraph()
        pd.text = f"  {b_desc}\n"
        pd.font.size = Pt(12)
        pd.font.color.rgb = TEXT_MAIN

    # Right: Future Work
    add_card(slide14, 6.9, 1.45, 5.6, 5.3, "🚀 Future Project Directions")
    tb_fut = slide14.shapes.add_textbox(Inches(7.15), Inches(2.15), Inches(5.1), Inches(4.3))
    tf_fut = tb_fut.text_frame
    tf_fut.word_wrap = True

    futs = [
        ("Modern Foundation Models", "Integrating LLaMA-3, Claude 3.5, and Gemini 1.5 Pro for enhanced contextual reasoning."),
        ("Synthetic Data Generation", "Using automated mutation fuzzing to generate thousands of synthetic invariant datasets automatically."),
        ("Cross-Chain Bridge Verification", "Extending invariant inference to multi-chain communication protocols and bridges."),
        ("IDE Integration", "Building VS Code and Remix IDE plugins for real-time invariant checking during development.")
    ]
    for i, (b_title, b_desc) in enumerate(futs):
        p = tf_fut.paragraphs[0] if i == 0 else tf_fut.add_paragraph()
        p.text = f"✔ {b_title}:"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        pd = tf_fut.add_paragraph()
        pd.text = f"  {b_desc}\n"
        pd.font.size = Pt(12)
        pd.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 15: Conclusion & Q&A (Dark Theme)
    # ==========================================
    slide15 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide15, PRIMARY_DARK)

    # Center summary box
    add_card(slide15, 1.5, 1.0, 10.333, 5.5, bg_color=RGBColor(30, 41, 59), border_color=ACCENT_BLUE)

    tb_end = slide15.shapes.add_textbox(Inches(2.0), Inches(1.4), Inches(9.333), Inches(4.7))
    tf_end = tb_end.text_frame
    tf_end.word_wrap = True

    p_e1 = tf_end.paragraphs[0]
    p_e1.alignment = PP_ALIGN.CENTER
    p_e1.text = "🎯 PROJECT CONCLUSION"
    p_e1.font.size = Pt(14)
    p_e1.font.bold = True
    p_e1.font.color.rgb = ACCENT_CYAN

    p_e2 = tf_end.add_paragraph()
    p_e2.alignment = PP_ALIGN.CENTER
    p_e2.text = "SmartInv: AI Intuition + Mathematical Rigor"
    p_e2.font.size = Pt(28)
    p_e2.font.bold = True
    p_e2.font.color.rgb = WHITE

    summary_bullets = [
        "First automated framework solving 'Machine Un-auditable' functional bugs in smart contracts.",
        "Combines Multimodal LLM Learning with Formal Verification (VeriSol/Corral).",
        "Tier of Thought (ToT) is the core breakthrough — boosting F1-score by 66%.",
        "Discovered 119 live zero-day vulnerabilities in production Ethereum contracts."
    ]
    for b in summary_bullets:
        pb = tf_end.add_paragraph()
        pb.alignment = PP_ALIGN.CENTER
        pb.text = f"\n✔ {b}"
        pb.font.size = Pt(13.5)
        pb.font.color.rgb = RGBColor(226, 232, 240)

    p_qa = tf_end.add_paragraph()
    p_qa.alignment = PP_ALIGN.CENTER
    p_qa.text = "\n\nThank You! | Open for Questions & Discussion"
    p_qa.font.size = Pt(16)
    p_qa.font.bold = True
    p_qa.font.color.rgb = ACCENT_CYAN

    # Save
    output_path = r"c:\Users\saini\OneDrive\Desktop\BLOCKCHAIN-PROJECT\SmartInv_MidSem_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_presentation()
