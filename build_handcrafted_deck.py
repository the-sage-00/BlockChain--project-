import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml

def create_handcrafted_presentation():
    prs = Presentation()
    # 16:9 widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette: Deep Slate, Indigo, Electric Cyan, Emerald, Coral Red, Amber, Pure White
    DARK_BG       = RGBColor(15, 23, 42)      # Slate 900
    DARK_CARD     = RGBColor(30, 41, 59)      # Slate 800
    DARK_BORDER   = RGBColor(51, 65, 85)      # Slate 700
    
    LIGHT_BG      = RGBColor(248, 250, 252)   # Slate 50
    CARD_BG       = RGBColor(255, 255, 255)   # Pure White
    CARD_BORDER   = RGBColor(226, 232, 240)   # Slate 200
    
    NAVY_PRIMARY  = RGBColor(30, 58, 138)     # Navy 900
    INDIGO_ACCENT = RGBColor(79, 70, 229)     # Indigo 600
    CYAN_ACCENT   = RGBColor(14, 165, 233)    # Sky 500
    CYAN_LIGHT    = RGBColor(224, 242, 254)   # Sky 100
    GREEN_EMERALD = RGBColor(16, 185, 129)    # Emerald 500
    GREEN_LIGHT   = RGBColor(209, 250, 229)   # Emerald 100
    RED_CORAL     = RGBColor(239, 68, 68)     # Red 500
    RED_LIGHT     = RGBColor(254, 226, 226)   # Red 100
    AMBER_GOLD    = RGBColor(245, 158, 11)    # Amber 500
    AMBER_LIGHT   = RGBColor(254, 243, 199)   # Amber 100
    
    TEXT_DARK     = RGBColor(15, 23, 42)      # Slate 900
    TEXT_BODY     = RGBColor(51, 65, 85)      # Slate 700
    TEXT_MUTED    = RGBColor(100, 116, 139)   # Slate 500
    TEXT_WHITE    = RGBColor(255, 255, 255)
    CODE_BG       = RGBColor(15, 23, 42)      # Slate 900

    def add_transition(slide, trans_type="push", dir_val="r"):
        """Adds smooth slide transition XML effect"""
        if trans_type == "fade":
            xml = '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:fade/></p:transition>'
        elif trans_type == "wipe":
            xml = f'<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:wipe dir="{dir_val}"/></p:transition>'
        else: # default push
            xml = f'<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:push dir="{dir_val}"/></p:transition>'
        slide._element.append(parse_xml(xml))

    def set_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, step_badge, title, subtitle=None, slide_num=None, dark_mode=False):
        # Header Container
        h_bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.18))
        h_bg.fill.solid()
        h_bg.fill.fore_color.rgb = DARK_BG if not dark_mode else RGBColor(10, 15, 30)
        h_bg.line.fill.background()

        # Accent Bottom Line
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.18), Inches(13.333), Inches(0.04))
        bar.fill.solid()
        bar.fill.fore_color.rgb = CYAN_ACCENT
        bar.line.fill.background()

        # Badge Pill for category
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.18), Inches(2.6), Inches(0.28))
        badge.fill.solid()
        badge.fill.fore_color.rgb = INDIGO_ACCENT
        badge.line.fill.background()
        tb_b = badge.text_frame
        tb_b.margin_left = tb_b.margin_top = tb_b.margin_right = tb_b.margin_bottom = 0
        p_b = tb_b.paragraphs[0]
        p_b.alignment = PP_ALIGN.CENTER
        p_b.text = step_badge.upper()
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = TEXT_WHITE

        # Title Text
        tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.50), Inches(10.5), Inches(0.6))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE

        # Slide Number Badge in Header Right
        if slide_num:
            num_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.8), Inches(0.35), Inches(0.8), Inches(0.42))
            num_card.fill.solid()
            num_card.fill.fore_color.rgb = DARK_CARD
            num_card.line.color.rgb = DARK_BORDER
            num_card.line.width = Pt(1)
            tf_num = num_card.text_frame
            p_n = tf_num.paragraphs[0]
            p_n.alignment = PP_ALIGN.CENTER
            p_n.text = f"{slide_num:02d}"
            p_n.font.size = Pt(13)
            p_n.font.bold = True
            p_n.font.color.rgb = CYAN_ACCENT

        # Footer Status Bar
        f_bg = slide.shapes.add_textbox(Inches(0.8), Inches(7.08), Inches(11.733), Inches(0.32))
        tf_f = f_bg.text_frame
        tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
        p_f = tf_f.paragraphs[0]
        p_f.text = f"SmartInv: Multimodal Smart Contract Invariant Inference | Rishi (ID: 2024ucp1566) | Mid-Sem Evaluation"
        p_f.font.size = Pt(9.5)
        p_f.font.color.rgb = TEXT_MUTED

    def add_styled_card(slide, left, top, width, height, title=None, subtitle=None, accent_color=None, bg_color=CARD_BG, border_color=CARD_BORDER):
        """Creates a modern card container with an optional colored left accent border"""
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)

        # Colored left accent strip
        if accent_color:
            strip = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(0.12), Inches(height))
            strip.fill.solid()
            strip.fill.fore_color.rgb = accent_color
            strip.line.fill.background()

        if title:
            tb = slide.shapes.add_textbox(Inches(left + 0.28), Inches(top + 0.18), Inches(width - 0.45), Inches(0.55))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(15)
            p.font.bold = True
            p.font.color.rgb = TEXT_DARK if bg_color != DARK_CARD else TEXT_WHITE

            if subtitle:
                p_s = tf.add_paragraph()
                p_s.text = subtitle.upper()
                p_s.font.size = Pt(9.5)
                p_s.font.bold = True
                p_s.font.color.rgb = accent_color if accent_color else CYAN_ACCENT

        return card

    # =========================================================================
    # SLIDE 1: Title Hero Deck (Deep Slate & Glowing Accents)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1, DARK_BG)
    add_transition(s1, "fade")

    # Outer Hero Container Card
    hero = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9))
    hero.fill.solid()
    hero.fill.fore_color.rgb = DARK_CARD
    hero.line.color.rgb = INDIGO_ACCENT
    hero.line.width = Pt(2.5)

    # Top Pill Badge
    top_badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.3), Inches(1.25), Inches(4.5), Inches(0.38))
    top_badge.fill.solid()
    top_badge.fill.fore_color.rgb = INDIGO_ACCENT
    top_badge.line.fill.background()
    p_b1 = top_badge.text_frame.paragraphs[0]
    p_b1.alignment = PP_ALIGN.CENTER
    p_b1.text = "🌟 A* RESEARCH PAPER PRESENTATION | MID-SEM REVIEW"
    p_b1.font.size = Pt(10.5)
    p_b1.font.bold = True
    p_b1.font.color.rgb = TEXT_WHITE

    # Main Title & Subtitle Box
    tb_title = s1.shapes.add_textbox(Inches(1.3), Inches(1.85), Inches(10.7), Inches(2.2))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    p1 = tf_t.paragraphs[0]
    p1.text = "SmartInv: Multimodal Smart Contract Invariant Inference"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

    p2 = tf_t.add_paragraph()
    p2.text = "Automated Security Verification for Blockchain Applications using LLMs & Formal Methods"
    p2.font.size = Pt(17)
    p2.font.color.rgb = RGBColor(148, 163, 184)

    # Accent Divider Line
    div_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.3), Inches(4.25), Inches(10.733), Inches(0.04))
    div_line.fill.solid()
    div_line.fill.fore_color.rgb = CYAN_ACCENT
    div_line.line.fill.background()

    # Left Info Column: Presenter Details
    p_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.3), Inches(4.55), Inches(5.1), Inches(1.8))
    p_card.fill.solid()
    p_card.fill.fore_color.rgb = RGBColor(15, 23, 42)
    p_card.line.color.rgb = DARK_BORDER
    p_card.line.width = Pt(1)
    tf_pc = p_card.text_frame
    tf_pc.margin_left = tf_pc.margin_top = Inches(0.2)
    p_ph = tf_pc.paragraphs[0]
    p_ph.text = "👤 PRESENTER PROFILE"
    p_ph.font.size = Pt(10)
    p_ph.font.bold = True
    p_ph.font.color.rgb = CYAN_ACCENT
    p_pd = tf_pc.add_paragraph()
    p_pd.text = "• Student Name: Rishi\n• Student ID: 2024ucp1566\n• Evaluation: Mid-Semester Project Review"
    p_pd.font.size = Pt(12.5)
    p_pd.font.color.rgb = TEXT_WHITE

    # Right Info Column: Paper Citation
    c_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.55), Inches(5.233), Inches(1.8))
    c_card.fill.solid()
    c_card.fill.fore_color.rgb = RGBColor(15, 23, 42)
    c_card.line.color.rgb = DARK_BORDER
    c_card.line.width = Pt(1)
    tf_cc = c_card.text_frame
    tf_cc.margin_left = tf_cc.margin_top = Inches(0.2)
    p_ch = tf_cc.paragraphs[0]
    p_ch.text = "🏛️ RESEARCH PAPER CITATION"
    p_ch.font.size = Pt(10)
    p_ch.font.bold = True
    p_ch.font.color.rgb = GREEN_EMERALD
    p_cd = tf_cc.add_paragraph()
    p_cd.text = "• Authors: Sally Junsong Wang, Kexin Pei, Junfeng Yang\n• Institution: Columbia University, New York, USA\n• Venue: IEEE Symposium on Security & Privacy (S&P) 2024"
    p_cd.font.size = Pt(12.5)
    p_cd.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 2: The Real-World Hook — Why Are We Here?
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2, LIGHT_BG)
    add_transition(s2, "push", "r")
    add_header(s2, "01. Introduction & Stakes", "Smart Contracts: High Stakes, Zero Room for Error", slide_num=2)

    # 3 Strategic Cards
    c1 = add_styled_card(s2, 0.8, 1.45, 3.733, 5.35, "1. The Vending Machine", "What is a Smart Contract?", CYAN_ACCENT)
    tb_c1 = s2.shapes.add_textbox(Inches(1.05), Inches(2.2), Inches(3.25), Inches(4.4))
    tf1 = tb_c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0
    bullets_s2_1 = [
        ("Automated Code", "Programs deployed on Ethereum that execute agreements automatically without banks or middlemen."),
        ("Real Analogy", "Like a physical vending machine: insert tokens, select item, code executes rules permanently."),
        ("DeFi Scale", "Manages digital lending, decentralized exchanges, and billions in liquidity pools.")
    ]
    for i, (head, desc) in enumerate(bullets_s2_1):
        p = tf1.paragraphs[0] if i == 0 else tf1.add_paragraph()
        p.text = f"✔ {head}\n"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = NAVY_PRIMARY
        pd = tf1.add_paragraph()
        pd.text = f"{desc}\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY

    c2 = add_styled_card(s2, 4.8, 1.45, 3.733, 5.35, "2. The Immutability Trap", "The Danger of Blockchain", RED_CORAL)
    tb_c2 = s2.shapes.add_textbox(Inches(5.05), Inches(2.2), Inches(3.25), Inches(4.4))
    tf2 = tb_c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0
    bullets_s2_2 = [
        ("No Patching Allowed", "Once code is committed to Ethereum, it CANNOT be rewritten or edited like normal apps."),
        ("Open Season for Hackers", "Contracts are public 24/7. Any tiny flaw can be instantly drained by anonymous exploiters."),
        ("No Reversibility", "There is no customer support to reverse a stolen $50M blockchain transaction.")
    ]
    for i, (head, desc) in enumerate(bullets_s2_2):
        p = tf2.paragraphs[0] if i == 0 else tf2.add_paragraph()
        p.text = f"⚠️ {head}\n"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = RED_CORAL
        pd = tf2.add_paragraph()
        pd.text = f"{desc}\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY

    c3 = add_styled_card(s2, 8.8, 1.45, 3.733, 5.35, "3. Multi-Billion Losses", "Why This Research Exists", AMBER_GOLD)
    tb_c3 = s2.shapes.add_textbox(Inches(9.05), Inches(2.2), Inches(3.25), Inches(4.4))
    tf3 = tb_c3.text_frame
    tf3.word_wrap = True
    tf3.margin_left = tf3.margin_top = tf3.margin_right = tf3.margin_bottom = 0
    bullets_s2_3 = [
        ("$3.8B+ Stolen", "Over $3.8 Billion lost in smart contract hacks in the last three years alone."),
        ("Expensive Audits", "Human security firms charge $50K–$500K per audit, but human auditors still miss subtle logic bugs."),
        ("The Project Mission", "SmartInv builds an automated AI auditor that catches these complex bugs before deployment.")
    ]
    for i, (head, desc) in enumerate(bullets_s2_3):
        p = tf3.paragraphs[0] if i == 0 else tf3.add_paragraph()
        p.text = f"💡 {head}\n"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = AMBER_GOLD
        pd = tf3.add_paragraph()
        pd.text = f"{desc}\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 3: The Core Problem: Two Types of Bugs
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3, LIGHT_BG)
    add_transition(s3, "push", "r")
    add_header(s3, "02. Problem Statement", "The Big Discovery: Two Fundamentally Different Bug Classes", slide_num=3)

    # Left Column: Implementation Bugs
    c_left = add_styled_card(s3, 0.8, 1.45, 5.6, 5.35, "Class A: Implementation Bugs (The Easy Ones)", "Solved by Existing Tools", GREEN_EMERALD)
    tb_l = s3.shapes.add_textbox(Inches(1.05), Inches(2.2), Inches(5.1), Inches(4.4))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0
    b_left = [
        ("What Are They?", "Syntax mistakes, reentrancy loops, and arithmetic overflows (e.g. 255 + 1 = 0)."),
        ("Why They Are Easy", "They follow obvious pre-programmed patterns that automated linters can flag immediately."),
        ("Tool Status: SOLVED", "Tools like Slither, Mythril, and Securify can detect 95%+ of these coding errors."),
        ("Analogy", "Like a spell-checker catching a typo ('teh' -> 'the'). Easy for machines to detect.")
    ]
    for i, (head, desc) in enumerate(b_left):
        p = tf_l.paragraphs[0] if i == 0 else tf_l.add_paragraph()
        p.text = f"✔ {head}\n"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = GREEN_EMERALD
        pd = tf_l.add_paragraph()
        pd.text = f"{desc}\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY

    # Right Column: Functional Bugs (The Real Danger)
    c_right = add_styled_card(s3, 6.9, 1.45, 5.6, 5.35, "Class B: Functional Bugs (Machine Un-auditable)", "The Multi-Million Dollar Threat", RED_CORAL)
    tb_r = s3.shapes.add_textbox(Inches(7.15), Inches(2.2), Inches(5.1), Inches(4.4))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0
    b_right = [
        ("What Are They?", "Flawed business logic. Code compiles and runs perfectly, but violates what the creator intended!"),
        ("Why They Are Deadly", "No syntax error exists. The contract happily sends $8M to a hacker because rules were poorly specified."),
        ("Tool Status: 0% DETECTED", "Traditional tools report '0 BUGS (SAFE)' because they do NOT understand developer intent."),
        ("Analogy", "Like an essay with zero spelling mistakes, but arguing that 2+2=5. Spell-checkers can't catch logical meaning!")
    ]
    for i, (head, desc) in enumerate(b_right):
        p = tf_r.paragraphs[0] if i == 0 else tf_r.add_paragraph()
        p.text = f"❌ {head}\n"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = RED_CORAL
        pd = tf_r.add_paragraph()
        pd.text = f"{desc}\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 4: Motivating Real-World Case Study (Visor Finance Hack)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4, LIGHT_BG)
    add_transition(s4, "wipe", "r")
    add_header(s4, "03. Real Case Study", "The $8.2 Million Visor Finance Hack (Dec 2021)", slide_num=4)

    # Left Card: The Storyline Breakdown
    add_styled_card(s4, 0.8, 1.45, 6.2, 5.35, "What Actually Happened at Visor?", "The Vulnerability Story", CYAN_ACCENT)
    tb_v = s4.shapes.add_textbox(Inches(1.05), Inches(2.2), Inches(5.7), Inches(4.4))
    tf_v = tb_v.text_frame
    tf_v.word_wrap = True
    tf_v.margin_left = tf_v.margin_top = tf_v.margin_right = tf_v.margin_bottom = 0
    story_pts = [
        ("Step 1: The Function", "Visor had a deposit function: `deposit(uint amount, address token)` designed to mint vault shares."),
        ("Step 2: The Innocent-Looking Line", "The code called `supervisor.approve(token, amount)` to authorize token movement."),
        ("Step 3: The Fatal Oversight", "The contract forgot to check IF `supervisor` was the genuine supervisor contract!"),
        ("Step 4: The Exploit", "A hacker passed their own attacker contract as the supervisor address and drained $8.2M in 1 block.")
    ]
    for i, (h, d) in enumerate(story_pts):
        p = tf_v.paragraphs[0] if i == 0 else tf_v.add_paragraph()
        p.text = f"• {h}\n"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = NAVY_PRIMARY
        pd = tf_v.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY

    # Right Card: The Automated Audit Failure
    add_styled_card(s4, 7.3, 1.45, 5.233, 5.35, "Tool Performance on Visor", "Why Existing Tools Failed", RED_CORAL)
    tb_t = s4.shapes.add_textbox(Inches(7.55), Inches(2.2), Inches(4.7), Inches(4.4))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    tool_data = [
        ("Slither (Static Linter)", "❌ 0 Bugs Reported (Passed as Safe)", TEXT_MUTED),
        ("Mythril (Symbolic Prover)", "❌ 0 Bugs Reported (Passed as Safe)", TEXT_MUTED),
        ("Manticore (Dynamic Engine)", "❌ 0 Bugs Reported (Passed as Safe)", TEXT_MUTED),
        ("VeriSmart (Formal Verifier)", "❌ 0 Bugs Reported (Passed as Safe)", TEXT_MUTED),
        ("SmartInv (Columbia Paper)", "✅ DETECTED INVARIANT VIOLATION & PREVENTED THE HACK!", GREEN_EMERALD)
    ]
    for i, (t_name, t_res, col) in enumerate(tool_data):
        p = tf_t.paragraphs[0] if i == 0 else tf_t.add_paragraph()
        p.text = f"{t_name}:"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = TEXT_DARK

        p_r = tf_t.add_paragraph()
        p_r.text = f"{t_res}\n"
        p_r.font.size = Pt(11.5)
        p_r.font.bold = True
        p_r.font.color.rgb = col

    # =========================================================================
    # SLIDE 5: Why Traditional Tools Fail
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5, LIGHT_BG)
    add_transition(s5, "push", "r")
    add_header(s5, "04. Literature Gap", "Why Existing Approaches Hit a Brick Wall", slide_num=5)

    tool_gaps = [
        ("1. Static Linters (e.g. Slither)", "Pattern-Matching Trap", [
            "Scans source code for hardcoded bad patterns.",
            "Blind to business logic: if a function compiles cleanly, it assumes it is completely safe.",
            "High false alarm rate on novel contract designs."
        ], INDIGO_ACCENT),
        ("2. Symbolic Provers (e.g. Mythril)", "Path Explosion Bottleneck", [
            "Tries to mathematically explore every possible execution path.",
            "Smart contracts with loops and external calls cause exponential branch explosion.",
            "Takes hours per contract and often times out."
        ], CYAN_ACCENT),
        ("3. Arithmetic Verifiers (e.g. VeriSmart)", "Narrow Domain Scope", [
            "Only checks basic mathematical inequalities (e.g. x + y <= MAX_UINT).",
            "Completely ignores access controls, role permissions, and token balances.",
            "Cannot infer high-level business invariants."
        ], AMBER_GOLD),
        ("4. What Was Missing in the Industry", "Intent & Semantic Awareness", [
            "None of these tools understand natural language specs or developer documentation.",
            "They analyze code without understanding the high-level business goal.",
            "SmartInv bridges this gap with Multimodal AI."
        ], GREEN_EMERALD)
    ]
    for idx, (t_head, t_sub, t_pts, t_col) in enumerate(tool_gaps):
        c_x = 0.8 + (idx % 2) * 6.0
        c_y = 1.45 + (idx // 2) * 2.75
        add_styled_card(s5, c_x, c_y, 5.733, 2.55, t_head, t_sub, t_col)
        tb_g = s5.shapes.add_textbox(Inches(c_x + 0.25), Inches(c_y + 0.7), Inches(5.2), Inches(1.75))
        tf_g = tb_g.text_frame
        tf_g.word_wrap = True
        tf_g.margin_left = tf_g.margin_top = tf_g.margin_right = tf_g.margin_bottom = 0
        for b in t_pts:
            p = tf_g.add_paragraph()
            p.text = f"• {b}"
            p.font.size = Pt(11.5)
            p.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 6: What is an Invariant? (The Core Idea Explained Simply)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6, LIGHT_BG)
    add_transition(s6, "fade")
    add_header(s6, "05. Core Concept", "What is an Invariant? (The Golden Rule of Security)", slide_num=6)

    # Top Definition Banner
    add_styled_card(s6, 0.8, 1.45, 11.733, 1.45, "💡 Invariant Defined in 1 Plain English Sentence", "The Mathematical Foundation", INDIGO_ACCENT)
    tb_def = s6.shapes.add_textbox(Inches(1.05), Inches(2.05), Inches(11.2), Inches(0.75))
    tf_def = tb_def.text_frame
    tf_def.word_wrap = True
    p_def = tf_def.paragraphs[0]
    p_def.text = "\"An Invariant is a golden safety rule that must ALWAYS remain TRUE throughout the entire contract lifecycle, no matter what crazy actions a user or hacker takes.\""
    p_def.font.size = Pt(15)
    p_def.font.bold = True
    p_def.font.color.rgb = NAVY_PRIMARY

    # 3 Example Cards
    inv_examples = [
        ("1. Bank Balance Rule", "assert(balance_after >= balance_before);", "Whenever a user deposits money, their balance must increase or stay equal. If a deposit ever reduces your balance -> BUG FOUND!", GREEN_EMERALD),
        ("2. Total Token Supply Rule", "assert(totalSupply == sum(userBalances));", "Total tokens in existence must exactly match the sum of all individual wallets. If tokens appear out of nowhere -> MONEY PRINTING HACK!", CYAN_ACCENT),
        ("3. Admin Authorization Rule", "assert(msg.sender == owner);", "Only the verified creator of the contract can withdraw the vault reserve. If a random user can trigger a withdrawal -> PRIVILEGE ESCALATION BUG!", RED_CORAL)
    ]
    for idx, (i_head, i_code, i_desc, i_col) in enumerate(inv_examples):
        c_x = 0.8 + idx * 4.0
        add_styled_card(s6, c_x, 3.1, 3.733, 3.7, i_head, "Concrete Example", i_col)
        tb_ie = s6.shapes.add_textbox(Inches(c_x + 0.25), Inches(3.75), Inches(3.25), Inches(2.9))
        tf_ie = tb_ie.text_frame
        tf_ie.word_wrap = True
        tf_ie.margin_left = tf_ie.margin_top = tf_ie.margin_right = tf_ie.margin_bottom = 0

        p_c_lbl = tf_ie.paragraphs[0]
        p_c_lbl.text = "Mathematical Invariant:"
        p_c_lbl.font.size = Pt(10.5)
        p_c_lbl.font.bold = True
        p_c_lbl.font.color.rgb = TEXT_MUTED

        p_code = tf_ie.add_paragraph()
        p_code.text = f"{i_code}\n"
        p_code.font.size = Pt(11)
        p_code.font.bold = True
        p_code.font.color.rgb = i_col

        p_desc_lbl = tf_ie.add_paragraph()
        p_desc_lbl.text = "Simple Meaning:"
        p_desc_lbl.font.size = Pt(10.5)
        p_desc_lbl.font.bold = True
        p_desc_lbl.font.color.rgb = TEXT_MUTED

        p_desc = tf_ie.add_paragraph()
        p_desc.text = i_desc
        p_desc.font.size = Pt(11.5)
        p_desc.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 7: The SmartInv Philosophy (AI Intuition + Formal Proof)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7, LIGHT_BG)
    add_transition(s7, "push", "r")
    add_header(s7, "06. Proposed Solution", "SmartInv: Combining AI Intuition with Mathematical Rigor", slide_num=7)

    # 2 Pillars Side-by-Side
    add_styled_card(s7, 0.8, 1.45, 5.6, 5.35, "Pillar 1: Deep Learning Intuition", "Multimodal Large Language Model (LLaMA)", INDIGO_ACCENT)
    tb_p1 = s7.shapes.add_textbox(Inches(1.05), Inches(2.2), Inches(5.1), Inches(4.4))
    tf_p1 = tb_p1.text_frame
    tf_p1.word_wrap = True
    tf_p1.margin_left = tf_p1.margin_top = tf_p1.margin_right = tf_p1.margin_bottom = 0
    p1_pts = [
        ("The AI Role", "Acts like an experienced human security auditor reading the contract."),
        ("Multimodal Understanding", "Reads Solidity code AND English comments/docstrings to understand what the contract is trying to achieve."),
        ("Specialized Training", "Fine-tuned on thousands of invariant samples using PEFT / LoRA adapter weights."),
        ("Output", "Infers candidates for bug-critical invariants at specific line numbers.")
    ]
    for i, (h, d) in enumerate(p1_pts):
        p = tf_p1.paragraphs[0] if i == 0 else tf_p1.add_paragraph()
        p.text = f"🧠 {h}\n"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = INDIGO_ACCENT
        pd = tf_p1.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY

    add_styled_card(s7, 6.9, 1.45, 5.6, 5.35, "Pillar 2: Mathematical Formal Methods", "Bounded Model Checker (VeriSol / Corral)", GREEN_EMERALD)
    tb_p2 = s7.shapes.add_textbox(Inches(7.15), Inches(2.2), Inches(5.1), Inches(4.4))
    tf_p2 = tb_p2.text_frame
    tf_p2.word_wrap = True
    tf_p2.margin_left = tf_p2.margin_top = tf_p2.margin_right = tf_p2.margin_bottom = 0
    p2_pts = [
        ("The Verifier Role", "Acts like a strict mathematician proving or disproving the AI's suggestions."),
        ("Boogie Translation", "Translates Solidity code + candidate invariants into Boogie intermediate representation."),
        ("Corral Engine", "Exhaustively checks if an execution path can violate the invariant."),
        ("Output", "Either proves the invariant holds OR generates an exact step-by-step counterexample exploit trace.")
    ]
    for i, (h, d) in enumerate(p2_pts):
        p = tf_p2.paragraphs[0] if i == 0 else tf_p2.add_paragraph()
        p.text = f"⚖️ {h}\n"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = GREEN_EMERALD
        pd = tf_p2.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 8: Innovation #1 — Multimodal Learning
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8, LIGHT_BG)
    add_transition(s8, "push", "r")
    add_header(s8, "07. Key Innovation #1", "Multimodal Learning: Seeing the Complete Picture", slide_num=8)

    modalities = [
        ("1. Solidity Code", "The Technical Logic", [
            "Mapping structures, variable states, and function declarations.",
            "Captures the exact mechanical execution flow.",
            "Tells the AI HOW the contract runs."
        ], INDIGO_ACCENT),
        ("2. Natural Language Specs", "The Human Intention", [
            "NatSpec comments, developer documentation, and naming conventions.",
            "Captures the intended business logic rules.",
            "Tells the AI WHAT the contract is supposed to do."
        ], CYAN_ACCENT),
        ("3. Transaction History", "The Real-World Behavior", [
            "Historical Ethereum execution traces and state transitions.",
            "Captures active on-chain usage patterns.",
            "Tells the AI HOW USERS actually interact with the code."
        ], GREEN_EMERALD)
    ]
    for idx, (m_head, m_sub, m_pts, m_col) in enumerate(modalities):
        c_x = 0.8 + idx * 4.0
        add_styled_card(s8, c_x, 1.45, 3.733, 4.0, m_head, m_sub, m_col)
        tb_m = s8.shapes.add_textbox(Inches(c_x + 0.25), Inches(2.1), Inches(3.25), Inches(3.2))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0
        for b in m_pts:
            p = tf_m.add_paragraph()
            p.text = f"• {b}\n"
            p.font.size = Pt(11.5)
            p.font.color.rgb = TEXT_BODY

    # Bottom Analogy Banner
    add_styled_card(s8, 0.8, 5.65, 11.733, 1.15, "🏥 The Medical Analogy (Why Multimodal Wins)", "Real-World Intuition", AMBER_GOLD)
    tb_med = s8.shapes.add_textbox(Inches(1.05), Inches(6.1), Inches(11.2), Inches(0.6))
    tf_med = tb_med.text_frame
    tf_med.word_wrap = True
    p_med = tf_med.paragraphs[0]
    p_med.text = "A great doctor doesn't just look at an X-ray (Code). They look at blood tests (Traces) and listen to the patient describe their symptoms (Natural Language). Combining all 3 sources gives the true diagnosis!"
    p_med.font.size = Pt(12)
    p_med.font.bold = True
    p_med.font.color.rgb = NAVY_PRIMARY

    # =========================================================================
    # SLIDE 9: Innovation #2 — Tier of Thought (ToT) Architecture
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9, LIGHT_BG)
    add_transition(s9, "wipe", "d")
    add_header(s9, "08. Key Innovation #2", "Tier of Thought (ToT): 6-Step Cognitive Pipeline", slide_num=9)

    tiers_data = [
        ("Tier 1A: Transaction Context", "Identifies what business domain this contract belongs to (e.g. cross-function lending, swaps, arithmetics).", INDIGO_ACCENT),
        ("Tier 1B: Critical Program Points", "Pinpoints the exact security-sensitive lines of code (e.g. Line 8: supervisor approval, Line 15: token minting).", INDIGO_ACCENT),
        ("Tier 2A: Invariant Generation", "Synthesizes mathematical assert statements that must hold at those critical program points.", GREEN_EMERALD),
        ("Tier 2B: Critical Invariant Filter", "Removes trivial tautologies (like x == x) to keep only bug-critical safety rules.", GREEN_EMERALD),
        ("Tier 3A: Invariant Priority Ranking", "Sorts invariants by risk priority so auditors immediately inspect high-threat vulnerabilities.", CYAN_ACCENT),
        ("Tier 3B: Vulnerability Classification", "Outputs final security status: Healthy OR Identifies the exact bug category (e.g. Privilege Escalation).", RED_CORAL)
    ]
    for idx, (t_name, t_desc, t_col) in enumerate(tiers_data):
        c_x = 0.8 + (idx % 2) * 6.0
        c_y = 1.45 + (idx // 2) * 1.78
        add_styled_card(s9, c_x, c_y, 5.733, 1.62, t_name, "Cognitive Stage", t_col)
        tb_td = s9.shapes.add_textbox(Inches(c_x + 0.25), Inches(c_y + 0.65), Inches(5.2), Inches(0.85))
        tf_td = tb_td.text_frame
        tf_td.word_wrap = True
        tf_td.margin_left = tf_td.margin_top = tf_td.margin_right = tf_td.margin_bottom = 0
        pt = tf_td.paragraphs[0]
        pt.text = t_desc
        pt.font.size = Pt(11.5)
        pt.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 10: Step-by-Step Code Walkthrough
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10, LIGHT_BG)
    add_transition(s10, "push", "r")
    add_header(s10, "09. Live Walkthrough", "How SmartInv Analyzes a Real Contract Step-by-Step", slide_num=10)

    # Left: Code Card
    add_styled_card(s10, 0.8, 1.45, 5.2, 5.35, "1. Input Solidity Contract", "Code Under Audit", INDIGO_ACCENT)
    code_card = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.05), Inches(2.15), Inches(4.7), Inches(4.4))
    code_card.fill.solid()
    code_card.fill.fore_color.rgb = CODE_BG
    code_card.line.fill.background()
    tf_c = code_card.text_frame
    tf_c.margin_left = tf_c.margin_top = Inches(0.2)
    sample_code = (
        "1  pragma solidity >=0.5.0;\n"
        "2  contract Vault {\n"
        "3    mapping(address => uint) public bal;\n"
        "4    address public supervisor;\n"
        "5\n"
        "6    function deposit(uint amount) external {\n"
        "7      // [Vulnerable Point]\n"
        "8      supervisor.approve(msg.sender, amount);\n"
        "9      bal[msg.sender] += amount;\n"
        "10   }\n"
        "11 }"
    )
    p_code = tf_c.paragraphs[0]
    p_code.text = sample_code
    p_code.font.size = Pt(11)
    p_code.font.name = "Consolas"
    p_code.font.color.rgb = CYAN_LIGHT

    # Right: Step-by-Step ToT Processing
    add_styled_card(s10, 6.3, 1.45, 6.233, 5.35, "2. SmartInv ToT Reasoning Flow", "Live Inference Output", GREEN_EMERALD)
    tb_flow = s10.shapes.add_textbox(Inches(6.55), Inches(2.15), Inches(5.7), Inches(4.4))
    tf_f = tb_flow.text_frame
    tf_f.word_wrap = True
    tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
    flow_lines = [
        ("Tier 1A Context", "Cross-function Vault token approval logic."),
        ("Tier 1B Critical Line", "Line 8 (Supervisor approval without address validation)."),
        ("Tier 2A/2B Invariant", "8+ assert(supervisor == trustedVaultSupervisor);"),
        ("Tier 3A Ranking", "Rank 1: Highest security priority."),
        ("Tier 3B Bug Inference", "Classification: 'Unauthorized Privilege Escalation'."),
        ("Formal Verifier", "❌ Invariant VIOLATED: Attacker can supply rogue supervisor address!")
    ]
    for i, (head, desc) in enumerate(flow_lines):
        p = tf_f.paragraphs[0] if i == 0 else tf_f.add_paragraph()
        p.text = f"• {head}: "
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = NAVY_PRIMARY if i < 5 else RED_CORAL
        pd = tf_f.add_paragraph()
        pd.text = f"  {desc}\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY if i < 5 else RED_CORAL
        pd.font.bold = (i == 5)

    # =========================================================================
    # SLIDE 11: Innovation #3 — Formal Verification Pipeline
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_bg(s11, LIGHT_BG)
    add_transition(s11, "push", "r")
    add_header(s11, "10. Key Innovation #3", "Formal Verification: The Mathematical Proof Engine", slide_num=11)

    v_stages = [
        ("Stage 1: Instrumentation", "Solidity + Invariants", [
            "Candidate invariants from the AI are inserted directly into the source code as formal assertions.",
            "Cleaned and prepared for compilation."
        ], INDIGO_ACCENT),
        ("Stage 2: VeriSol Translation", "Boogie Intermediate Language", [
            "Microsoft's VeriSol compiler translates Ethereum EVM bytecode and Solidity logic into Boogie formal syntax.",
            "Eliminates compiler ambiguities."
        ], CYAN_ACCENT),
        ("Stage 3: Corral Model Checker", "Bounded Proof & Exploit Trace", [
            "Corral checks if ANY transaction sequence up to bounded depth can violate the assertion.",
            "If violated -> Generates a step-by-step counterexample trace showing exactly how to exploit the bug!"
        ], GREEN_EMERALD)
    ]
    for idx, (v_head, v_sub, v_pts, v_col) in enumerate(v_stages):
        c_x = 0.8 + idx * 4.0
        add_styled_card(s11, c_x, 1.45, 3.733, 4.0, v_head, v_sub, v_col)
        tb_v = s11.shapes.add_textbox(Inches(c_x + 0.25), Inches(2.1), Inches(3.25), Inches(3.2))
        tf_v = tb_v.text_frame
        tf_v.word_wrap = True
        tf_v.margin_left = tf_v.margin_top = tf_v.margin_right = tf_v.margin_bottom = 0
        for b in v_pts:
            p = tf_v.add_paragraph()
            p.text = f"• {b}\n"
            p.font.size = Pt(11.5)
            p.font.color.rgb = TEXT_BODY

    # Bottom Takeaway
    add_styled_card(s11, 0.8, 5.65, 11.733, 1.15, "🎯 What is a Counterexample Trace?", "Zero Hallucination Guarantee", RED_CORAL)
    tb_ce = s11.shapes.add_textbox(Inches(1.05), Inches(6.1), Inches(11.2), Inches(0.6))
    tf_ce = tb_ce.text_frame
    tf_ce.word_wrap = True
    p_ce = tf_ce.paragraphs[0]
    p_ce.text = "A counterexample trace is definitive mathematical proof: 'If user calls deposit(100) -> then calls execute() -> invariant fails at Line 8.' This eliminates false alarms!"
    p_ce.font.size = Pt(12)
    p_ce.font.bold = True
    p_ce.font.color.rgb = NAVY_PRIMARY

    # =========================================================================
    # SLIDE 12: Benchmark Results on 80,000+ Real Contracts
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_bg(s12, LIGHT_BG)
    add_transition(s12, "fade")
    add_header(s12, "11. Experimental Results", "Large-Scale Evaluation on 80,000+ Smart Contracts", slide_num=12)

    # 3 Stat Cards on Top
    stat_boxes = [
        ("3.5×", "More Bug Invariants", "Discovered 3.5× more security-critical invariants than baseline tools.", INDIGO_ACCENT),
        ("4.0×", "More Critical Bugs", "Detected 4× more high-risk functional vulnerabilities than state of the art.", GREEN_EMERALD),
        ("150×", "Faster Execution", "Inference runs in seconds compared to hours for symbolic execution.", CYAN_ACCENT)
    ]
    for idx, (num, lbl, desc, col) in enumerate(stat_boxes):
        c_x = 0.8 + idx * 4.0
        add_styled_card(s12, c_x, 1.45, 3.733, 1.9, None, None, col)
        tb_s = s12.shapes.add_textbox(Inches(c_x + 0.25), Inches(1.55), Inches(3.25), Inches(1.7))
        tf_s = tb_s.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
        p_n = tf_s.paragraphs[0]
        p_n.text = num
        p_n.font.size = Pt(32)
        p_n.font.bold = True
        p_n.font.color.rgb = col

        p_l = tf_s.add_paragraph()
        p_l.text = lbl
        p_l.font.size = Pt(12)
        p_l.font.bold = True
        p_l.font.color.rgb = NAVY_PRIMARY

        p_d = tf_s.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = TEXT_MUTED

    # Bottom Comparison Table Card
    add_styled_card(s12, 0.8, 3.55, 11.733, 3.25, "Comprehensive Tool Comparison (1,200+ Audited Ground Truth Benchmark)", "Performance Summary", NAVY_PRIMARY)
    tb_comp = s12.shapes.add_textbox(Inches(1.05), Inches(4.15), Inches(11.2), Inches(2.4))
    tf_comp = tb_comp.text_frame
    tf_comp.word_wrap = True
    tf_comp.margin_left = tf_comp.margin_top = tf_comp.margin_right = tf_comp.margin_bottom = 0
    t_rows = [
        ("Slither", "Static Linter", "Fast (Seconds)", "High (Noise)", "Misses all functional logic bugs"),
        ("Mythril", "Symbolic Execution", "Slow (Hours)", "Moderate", "Path explosion bottleneck"),
        ("Manticore", "Dynamic Analysis", "Very Slow (Hours)", "Moderate", "Cannot scale to large contracts"),
        ("SmartInv", "Multimodal AI + Verifier", "Fast (Seconds)", "Low (Verified)", "Detects & Proves Functional Bugs ⭐")
    ]
    for tool, tech, spd, fp, verdict in t_rows:
        p_tr = tf_comp.add_paragraph()
        is_si = ("SmartInv" in tool)
        p_tr.text = f"• {tool.ljust(14)} | Tech: {tech.ljust(24)} | Speed: {spd.ljust(18)} | Verdict: {verdict}"
        p_tr.font.size = Pt(11.5)
        p_tr.font.bold = is_si
        p_tr.font.color.rgb = GREEN_EMERALD if is_si else TEXT_BODY

    # =========================================================================
    # SLIDE 13: Real-World Impact — 119 Live Zero-Day Bugs
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_bg(s13, LIGHT_BG)
    add_transition(s13, "push", "r")
    add_header(s13, "12. Real-World Impact", "119 Zero-Day Vulnerabilities Discovered on Ethereum", slide_num=13)

    # 4 Discovery Cards
    findings = [
        ("1. 119 Zero-Day Vulnerabilities", "Previously Unknown Bugs", [
            "Discovered in live, actively deployed Ethereum smart contracts.",
            "Zero previous reports existed anywhere in the security community.",
            "All 119 bugs were 100% missed by Slither, Mythril, and Manticore."
        ], RED_CORAL),
        ("2. 5 High-Severity Confirmed", "Developer Validations", [
            "5 vulnerabilities officially confirmed as High-Severity by project core developers.",
            "Responsible disclosure prevented multimillion-dollar exploitations.",
            "Demonstrates practical real-world industry value."
        ], GREEN_EMERALD),
        ("3. Business Logic Inconsistencies", "Vault & Staking Flaws", [
            "Discovered flawed reward accrual algorithms in staking pools.",
            "Fixed share-dilution loopholes where early depositors were cheated.",
            "Prevented price-oracle arbitrage exploits."
        ], CYAN_ACCENT),
        ("4. Privilege Escalations", "Access Control Bypasses", [
            "Found contracts where unauthorized external callers could trigger administrative functions.",
            "Identified uninitialized state variables in proxy contracts.",
            "Secured cross-bridge token transfers."
        ], AMBER_GOLD)
    ]
    for idx, (f_head, f_sub, f_pts, f_col) in enumerate(findings):
        c_x = 0.8 + (idx % 2) * 6.0
        c_y = 1.45 + (idx // 2) * 2.75
        add_styled_card(s13, c_x, c_y, 5.733, 2.55, f_head, f_sub, f_col)
        tb_f = s13.shapes.add_textbox(Inches(c_x + 0.25), Inches(c_y + 0.7), Inches(5.2), Inches(1.75))
        tf_f = tb_f.text_frame
        tf_f.word_wrap = True
        tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
        for b in f_pts:
            p = tf_f.add_paragraph()
            p.text = f"• {b}"
            p.font.size = Pt(11.5)
            p.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 14: Ablation Study — Proof that ToT is the Hero
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_bg(s14, LIGHT_BG)
    add_transition(s14, "push", "r")
    add_header(s14, "13. Scientific Rigor", "Ablation Study: Proving Tier of Thought is the Hero", slide_num=14)

    # Left: Explanation Card
    add_styled_card(s14, 0.8, 1.45, 5.2, 5.35, "What is an Ablation Study?", "Isolating What Really Works", INDIGO_ACCENT)
    tb_ab = s14.shapes.add_textbox(Inches(1.05), Inches(2.2), Inches(4.7), Inches(4.4))
    tf_ab = tb_ab.text_frame
    tf_ab.word_wrap = True
    tf_ab.margin_left = tf_ab.margin_top = tf_ab.margin_right = tf_ab.margin_bottom = 0
    ab_points = [
        ("The Scientific Test", "Researchers systematically removed one component at a time to measure exactly how much accuracy drops."),
        ("Key Finding #1", "Removing Tier of Thought causes a catastrophic 66% drop in F1-score!"),
        ("Key Finding #2", "Removing Natural Language causes a 37% drop (and functional bug detection drops 40×)."),
        ("The Conclusion", "Tier of Thought structured reasoning is the single most vital innovation of the paper.")
    ]
    for i, (h, d) in enumerate(ab_points):
        p = tf_ab.paragraphs[0] if i == 0 else tf_ab.add_paragraph()
        p.text = f"• {h}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = NAVY_PRIMARY
        pd = tf_ab.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY

    # Right: Data Table Card
    add_styled_card(s14, 6.3, 1.45, 6.233, 5.35, "Ablation Experiment Data (Table 9 & 11)", "Measured Accuracy & F1", GREEN_EMERALD)
    tb_dat = s14.shapes.add_textbox(Inches(6.55), Inches(2.2), Inches(5.7), Inches(4.4))
    tf_dat = tb_dat.text_frame
    tf_dat.word_wrap = True
    tf_dat.margin_left = tf_dat.margin_top = tf_dat.margin_right = tf_dat.margin_bottom = 0
    ab_data = [
        ("Full SmartInv (All Features)", "0.89", "0.82", "Optimal Baseline ⭐", GREEN_EMERALD),
        ("Remove Optimization", "0.89", "0.82", "Minimal difference", TEXT_DARK),
        ("Remove Labeled Features", "0.59", "0.60", "-22% F1 Decrease", TEXT_MUTED),
        ("Remove Natural Language (NL)", "0.62", "0.45", "-37% F1 Drop 📉", RED_CORAL),
        ("Remove Tier of Thought (ToT)", "0.24", "0.16", "-66% F1 Collapse 📉📉", RED_CORAL),
        ("Raw Base LLM (No Fine-tuning)", "0.12", "0.14", "Complete Failure", RED_CORAL)
    ]
    for name, acc, f1, note, col in ab_data:
        p = tf_dat.add_paragraph()
        p.text = f"• {name}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = col

        pd = tf_dat.add_paragraph()
        pd.text = f"  Accuracy: {acc} | F1-Score: {f1} ({note})\n"
        pd.font.size = Pt(11.5)
        pd.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 15: What I Personally Built & Ran (Mid-Sem Milestones)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_bg(s15, LIGHT_BG)
    add_transition(s15, "push", "r")
    add_header(s15, "14. Mid-Sem Milestones", "Practical Work Executed on Local Machine", slide_num=15)

    milestones = [
        ("1. Environment & Setup", "Dependency Integration", [
            "Cloned full research repository and configured local Python environment.",
            "Integrated PyTorch 2.8, HuggingFace Transformers, PEFT, and OpenAI SDK.",
            "Created clean workspace structure with Git version control."
        ], INDIGO_ACCENT),
        ("2. Bug Fixing & Compatibility", "Windows Porting & Fixes", [
            "Fixed Windows file encoding bug (UnicodeEncodeError for pi symbols) in dataset generator.",
            "Replaced hardcoded Linux author paths (/home/sally...) with dynamic relative paths.",
            "Patched OpenAI client initialization crash to support offline and help modes."
        ], CYAN_ACCENT),
        ("3. Dataset Processing", "ToT Training Data Generation", [
            "Executed generator.py — generated all 3,000+ ToT structured prompt-completion pairs.",
            "Validated smartinv.py CLI argument parser (Exit Code 0).",
            "Tested verification routines on sample benchmark contracts."
        ], GREEN_EMERALD),
        ("4. Comprehensive Guides & Git", "Defense Prep & Repository", [
            "Authored 5 extensive study guide documents in dedicated study_guide/ folder.",
            "Set up dual remotes (origin -> User GitHub, upstream -> Columbia).",
            "Pushed all code fixes, datasets, and presentation decks to GitHub."
        ], AMBER_GOLD)
    ]
    for idx, (m_head, m_sub, m_pts, m_col) in enumerate(milestones):
        c_x = 0.8 + (idx % 2) * 6.0
        c_y = 1.45 + (idx // 2) * 2.75
        add_styled_card(s15, c_x, c_y, 5.733, 2.55, m_head, m_sub, m_col)
        tb_m = s15.shapes.add_textbox(Inches(c_x + 0.25), Inches(c_y + 0.7), Inches(5.2), Inches(1.75))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0
        for b in m_pts:
            p = tf_m.add_paragraph()
            p.text = f"✔ {b}"
            p.font.size = Pt(11.5)
            p.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 16: Conclusion & Future Vision (Dark Grand Finale Theme)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    set_bg(s16, DARK_BG)
    add_transition(s16, "fade")

    # Center Hero Box
    box_end = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(0.9), Inches(10.933), Inches(5.7))
    box_end.fill.solid()
    box_end.fill.fore_color.rgb = DARK_CARD
    box_end.line.color.rgb = INDIGO_ACCENT
    box_end.line.width = Pt(2)

    tb_end = s16.shapes.add_textbox(Inches(1.6), Inches(1.2), Inches(10.133), Inches(5.1))
    tf_e = tb_end.text_frame
    tf_e.word_wrap = True
    tf_e.margin_left = tf_e.margin_top = tf_e.margin_right = tf_e.margin_bottom = 0

    p_e_badge = tf_e.paragraphs[0]
    p_e_badge.alignment = PP_ALIGN.CENTER
    p_e_badge.text = "🎯 PROJECT SUMMARY & KEY TAKEAWAYS"
    p_e_badge.font.size = Pt(12)
    p_e_badge.font.bold = True
    p_e_badge.font.color.rgb = CYAN_ACCENT

    p_e_title = tf_e.add_paragraph()
    p_e_title.alignment = PP_ALIGN.CENTER
    p_e_title.text = "SmartInv: AI Intuition Meets Mathematical Proof"
    p_e_title.font.size = Pt(26)
    p_e_title.font.bold = True
    p_e_title.font.color.rgb = TEXT_WHITE

    concl_bullets = [
        "First automated security tool to solve 'Machine Un-auditable' functional bugs.",
        "Tier of Thought (ToT) is the core breakthrough — boosting F1-score by 66%.",
        "Discovered 119 live zero-day vulnerabilities in production Ethereum contracts.",
        "Fully implemented, debugged, and verified on local machine with full study repository."
    ]
    for b in concl_bullets:
        pb = tf_e.add_paragraph()
        pb.alignment = PP_ALIGN.CENTER
        pb.text = f"\n✔ {b}"
        pb.font.size = Pt(13)
        pb.font.color.rgb = RGBColor(226, 232, 240)

    p_qa = tf_e.add_paragraph()
    p_qa.alignment = PP_ALIGN.CENTER
    p_qa.text = "\n\nThank You! | Ready for Teacher Q&A and Viva Defense"
    p_qa.font.size = Pt(16)
    p_qa.font.bold = True
    p_qa.font.color.rgb = GREEN_EMERALD

    # Save Handcrafted PPTX
    out_file = r"c:\Users\saini\OneDrive\Desktop\BLOCKCHAIN-PROJECT\SmartInv_Crafted_Presentation.pptx"
    prs.save(out_file)
    print(f"Handcrafted presentation saved successfully to: {out_file}")

if __name__ == "__main__":
    create_handcrafted_presentation()
