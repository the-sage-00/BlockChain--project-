import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml

def create_ultimate_candy_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Premium Color Palette (Candy & Clean Tech)
    MIDNIGHT_DARK = RGBColor(11, 15, 25)       # Ultra-deep dark blue
    NAVY_CARD     = RGBColor(23, 32, 54)       # Deep slate card
    NAVY_BORDER   = RGBColor(45, 60, 95)       # Card border
    
    LIGHT_BG      = RGBColor(248, 250, 254)    # Soft icy white background
    WHITE_CARD    = RGBColor(255, 255, 255)    # Pure card
    BORDER_LIGHT  = RGBColor(226, 232, 245)    # Clean subtle border
    
    INDIGO_VIBRANT= RGBColor(79, 70, 229)      # Electric Indigo (Primary accent)
    INDIGO_SOFT   = RGBColor(238, 242, 255)    # Indigo pill background
    
    CYAN_ELECTRIC = RGBColor(14, 165, 233)     # Sky Cyan
    CYAN_SOFT     = RGBColor(224, 242, 254)    # Cyan pill background
    
    EMERALD_GREEN = RGBColor(16, 185, 129)     # Emerald Green (Success)
    EMERALD_SOFT  = RGBColor(209, 250, 229)    # Emerald pill background
    
    CORAL_ROSE    = RGBColor(244, 63, 94)      # Coral Rose (Warning / Danger)
    CORAL_SOFT    = RGBColor(255, 228, 230)    # Coral pill background
    
    AMBER_GOLD    = RGBColor(245, 158, 11)     # Warm Gold
    AMBER_SOFT    = RGBColor(254, 243, 199)    # Gold pill background
    
    PURPLE_CANDY  = RGBColor(168, 85, 247)     # Candy Purple
    PURPLE_SOFT   = RGBColor(243, 232, 255)    # Purple pill background
    
    TEXT_HEADING  = RGBColor(15, 23, 42)       # Slate 900
    TEXT_BODY     = RGBColor(51, 65, 85)       # Slate 700
    TEXT_MUTED    = RGBColor(100, 116, 139)    # Slate 500
    TEXT_WHITE    = RGBColor(255, 255, 255)

    def add_transition(slide, trans_type="push", dir_val="r"):
        if trans_type == "fade":
            xml = '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:fade/></p:transition>'
        elif trans_type == "wipe":
            xml = f'<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:wipe dir="{dir_val}"/></p:transition>'
        else:
            xml = f'<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:push dir="{dir_val}"/></p:transition>'
        slide._element.append(parse_xml(xml))

    def set_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, module_tag, title, subtitle=None, slide_num=None, dark=False):
        # Header Top Container
        h_bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.18))
        h_bg.fill.solid()
        h_bg.fill.fore_color.rgb = MIDNIGHT_DARK if not dark else RGBColor(8, 12, 22)
        h_bg.line.fill.background()

        # Gradient-like Accent Line
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.18), Inches(13.333), Inches(0.04))
        bar.fill.solid()
        bar.fill.fore_color.rgb = CYAN_ELECTRIC
        bar.line.fill.background()

        # Category Pill Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.18), Inches(2.8), Inches(0.28))
        badge.fill.solid()
        badge.fill.fore_color.rgb = INDIGO_VIBRANT
        badge.line.fill.background()
        p_b = badge.text_frame.paragraphs[0]
        p_b.alignment = PP_ALIGN.CENTER
        p_b.text = module_tag.upper()
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = TEXT_WHITE

        # Slide Main Title
        tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.50), Inches(10.5), Inches(0.6))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE

        # Slide Counter Pill on Right
        if slide_num:
            num_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.6), Inches(0.35), Inches(1.0), Inches(0.42))
            num_pill.fill.solid()
            num_pill.fill.fore_color.rgb = NAVY_CARD
            num_pill.line.color.rgb = NAVY_BORDER
            num_pill.line.width = Pt(1)
            p_n = num_pill.text_frame.paragraphs[0]
            p_n.alignment = PP_ALIGN.CENTER
            p_n.text = f"{slide_num:02d} / 16"
            p_n.font.size = Pt(11.5)
            p_n.font.bold = True
            p_n.font.color.rgb = CYAN_ELECTRIC

        # Footer Status Bar
        f_tb = slide.shapes.add_textbox(Inches(0.8), Inches(7.08), Inches(11.733), Inches(0.32))
        tf_f = f_tb.text_frame
        tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
        p_f = tf_f.paragraphs[0]
        p_f.text = "SmartInv: Multimodal Smart Contract Invariant Inference | Rishi (ID: 2024ucp1566) | Mid-Sem Evaluation"
        p_f.font.size = Pt(9.5)
        p_f.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title=None, subtitle=None, pill_text=None, accent_color=None, bg_color=WHITE_CARD, border_color=BORDER_LIGHT):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)

        # Left Accent Strip
        if accent_color:
            strip = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(0.12), Inches(height))
            strip.fill.solid()
            strip.fill.fore_color.rgb = accent_color
            strip.line.fill.background()

        if pill_text:
            pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left + 0.28), Inches(top + 0.18), Inches(len(pill_text)*0.11 + 0.4), Inches(0.26))
            pill.fill.solid()
            pill.fill.fore_color.rgb = accent_color if accent_color else INDIGO_VIBRANT
            pill.line.fill.background()
            p_pl = pill.text_frame.paragraphs[0]
            p_pl.alignment = PP_ALIGN.CENTER
            p_pl.text = pill_text.upper()
            p_pl.font.size = Pt(8.5)
            p_pl.font.bold = True
            p_pl.font.color.rgb = TEXT_WHITE

        if title:
            top_offset = 0.50 if pill_text else 0.18
            tb = slide.shapes.add_textbox(Inches(left + 0.28), Inches(top + top_offset), Inches(width - 0.5), Inches(0.5))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = TEXT_HEADING if bg_color != NAVY_CARD else TEXT_WHITE

            if subtitle:
                p_s = tf.add_paragraph()
                p_s.text = subtitle
                p_s.font.size = Pt(10)
                p_s.font.bold = True
                p_s.font.color.rgb = accent_color if accent_color else CYAN_ELECTRIC

        return card

    # =========================================================================
    # SLIDE 1: Hero Welcome Deck (Dark & Glowing Candy Theme)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1, MIDNIGHT_DARK)
    add_transition(s1, "fade")

    # Glowing Backdrop Card
    hero_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9))
    hero_card.fill.solid()
    hero_card.fill.fore_color.rgb = NAVY_CARD
    hero_card.line.color.rgb = INDIGO_VIBRANT
    hero_card.line.width = Pt(2.5)

    # Pill Tag
    hero_pill = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.3), Inches(1.2), Inches(4.6), Inches(0.38))
    hero_pill.fill.solid()
    hero_pill.fill.fore_color.rgb = INDIGO_VIBRANT
    hero_pill.line.fill.background()
    p_hp = hero_pill.text_frame.paragraphs[0]
    p_hp.alignment = PP_ALIGN.CENTER
    p_hp.text = "🌟 A* RESEARCH PAPER PRESENTATION | MID-SEM REVIEW"
    p_hp.font.size = Pt(10.5)
    p_hp.font.bold = True
    p_hp.font.color.rgb = TEXT_WHITE

    # Big Title
    tb_t = s1.shapes.add_textbox(Inches(1.3), Inches(1.75), Inches(10.7), Inches(2.3))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t1 = tf_t.paragraphs[0]
    p_t1.text = "SmartInv: Smart Contract Invariant Inference"
    p_t1.font.size = Pt(32)
    p_t1.font.bold = True
    p_t1.font.color.rgb = TEXT_WHITE

    p_t2 = tf_t.add_paragraph()
    p_t2.text = "Solving 'Machine Un-auditable' Functional Bugs on Blockchain using LLMs & Formal Verification"
    p_t2.font.size = Pt(16.5)
    p_t2.font.color.rgb = RGBColor(148, 163, 184)

    # Divider
    div = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.3), Inches(4.2), Inches(10.733), Inches(0.04))
    div.fill.solid()
    div.fill.fore_color.rgb = CYAN_ELECTRIC
    div.line.fill.background()

    # Left Box: Student Profile
    s_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.3), Inches(4.5), Inches(5.1), Inches(1.85))
    s_box.fill.solid()
    s_box.fill.fore_color.rgb = MIDNIGHT_DARK
    s_box.line.color.rgb = NAVY_BORDER
    s_box.line.width = Pt(1)
    tf_sb = s_box.text_frame
    tf_sb.margin_left = tf_sb.margin_top = Inches(0.2)
    p_sh = tf_sb.paragraphs[0]
    p_sh.text = "👤 PRESENTER INFORMATION"
    p_sh.font.size = Pt(10)
    p_sh.font.bold = True
    p_sh.font.color.rgb = CYAN_ELECTRIC
    p_sd = tf_sb.add_paragraph()
    p_sd.text = "• Student Name: Rishi\n• Student ID: 2024ucp1566\n• Evaluation: Mid-Semester Project Review"
    p_sd.font.size = Pt(12.5)
    p_sd.font.color.rgb = TEXT_WHITE

    # Right Box: Paper Citation
    p_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.5), Inches(5.233), Inches(1.85))
    p_box.fill.solid()
    p_box.fill.fore_color.rgb = MIDNIGHT_DARK
    p_box.line.color.rgb = NAVY_BORDER
    p_box.line.width = Pt(1)
    tf_pb = p_box.text_frame
    tf_pb.margin_left = tf_pb.margin_top = Inches(0.2)
    p_ph = tf_pb.paragraphs[0]
    p_ph.text = "🏛️ PAPER CITATION"
    p_ph.font.size = Pt(10)
    p_ph.font.bold = True
    p_ph.font.color.rgb = EMERALD_GREEN
    p_pd = tf_pb.add_paragraph()
    p_pd.text = "• Authors: Sally Junsong Wang, Kexin Pei, Junfeng Yang\n• Institution: Columbia University, New York, USA\n• Venue: IEEE Symposium on Security & Privacy (S&P) 2024"
    p_pd.font.size = Pt(12.5)
    p_pd.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 2: The Real-World Hook — Why Are We Here?
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2, LIGHT_BG)
    add_transition(s2, "push", "r")
    add_header(s2, "01. Introduction & Context", "Why Smart Contract Security is a Multi-Billion Dollar Crisis", slide_num=2)

    # 3 Story Cards
    c1 = add_card(s2, 0.8, 1.45, 3.733, 5.35, "1. What is a Smart Contract?", "The Vending Machine Analogy", "BASIC CONCEPT", CYAN_ELECTRIC)
    tb1 = s2.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(3.25), Inches(4.2))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0
    bullets_s2_1 = [
        ("Self-Executing Programs", "Smart contracts are programs running on Ethereum that execute agreements automatically without banks or middlemen."),
        ("The Vending Machine", "Put in tokens, select an option, and the code dispenses the output according to strict pre-coded rules."),
        ("DeFi Scale", "Today, smart contracts safeguard hundreds of billions in digital loans, exchanges, and vaults.")
    ]
    for i, (h, d) in enumerate(bullets_s2_1):
        p = tf1.paragraphs[0] if i == 0 else tf1.add_paragraph()
        p.text = f"✔ {h}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = INDIGO_VIBRANT
        pd = tf1.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_BODY

    c2 = add_card(s2, 4.8, 1.45, 3.733, 5.35, "2. The Immutability Trap", "Why Blockchain is Different", "THE CORE RISK", CORAL_ROSE)
    tb2 = s2.shapes.add_textbox(Inches(5.05), Inches(2.4), Inches(3.25), Inches(4.2))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0
    bullets_s2_2 = [
        ("No Edit Button Allowed", "Once code is committed to the blockchain, it CANNOT be modified, patched, or updated like normal software."),
        ("Open 24/7 to the World", "Anyone in the world can inspect the code. If a tiny flaw exists, hackers will find it and drain the funds."),
        ("Irreversible Loss", "There is no undo button on blockchain. Once money is transferred to a hacker, it is gone forever.")
    ]
    for i, (h, d) in enumerate(bullets_s2_2):
        p = tf2.paragraphs[0] if i == 0 else tf2.add_paragraph()
        p.text = f"⚠️ {h}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = CORAL_ROSE
        pd = tf2.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_BODY

    c3 = add_card(s2, 8.8, 1.45, 3.733, 5.35, "3. Multi-Billion Losses", "Why Human Audits Fail", "INDUSTRY PROBLEM", AMBER_GOLD)
    tb3 = s2.shapes.add_textbox(Inches(9.05), Inches(2.4), Inches(3.25), Inches(4.2))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    tf3.margin_left = tf3.margin_top = tf3.margin_right = tf3.margin_bottom = 0
    bullets_s2_3 = [
        ("$3.8B+ Stolen", "Over $3.8 Billion lost to smart contract exploits in recent years across top DeFi protocols."),
        ("Crazy Expensive Audits", "Companies pay $50,000 to $500,000+ for human security reviews, yet humans still miss subtle bugs."),
        ("The Project Goal", "SmartInv builds an AI-powered automated auditor that catches deep functional bugs before release.")
    ]
    for i, (h, d) in enumerate(bullets_s2_3):
        p = tf3.paragraphs[0] if i == 0 else tf3.add_paragraph()
        p.text = f"💡 {h}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = AMBER_GOLD
        pd = tf3.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 3: The Big Discovery: Two Fundamentally Different Bug Classes
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3, LIGHT_BG)
    add_transition(s3, "push", "r")
    add_header(s3, "02. The Core Problem", "Implementation Bugs vs. Machine Un-auditable Functional Bugs", slide_num=3)

    # Left: Implementation Bugs
    c_l = add_card(s3, 0.8, 1.45, 5.6, 5.35, "Type 1: Implementation Bugs", "The Easy Syntax Errors", "SOLVED BY TOOLS", EMERALD_GREEN)
    tbl = s3.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.1), Inches(4.2))
    tfl = tbl.text_frame
    tfl.word_wrap = True
    tfl.margin_left = tfl.margin_top = tfl.margin_right = tfl.margin_bottom = 0
    pts_l = [
        ("What Are They?", "Low-level coding mistakes like integer overflow (255+1=0) or reentrancy loops (calling withdraw before updating balance)."),
        ("Why They Are Easy", "They follow predictable syntax patterns that linters can match line-by-line."),
        ("Tool Status: SOLVED", "Tools like Slither, Mythril, and Securify catch over 95% of these straightforward syntax bugs."),
        ("The Spell-Checker Analogy", "Like a spell-checker highlighting 'teh' -> 'the'. Simple pattern matching solves it.")
    ]
    for i, (h, d) in enumerate(pts_l):
        p = tfl.paragraphs[0] if i == 0 else tfl.add_paragraph()
        p.text = f"✔ {h}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = EMERALD_GREEN
        pd = tfl.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_BODY

    # Right: Functional Bugs
    c_r = add_card(s3, 6.9, 1.45, 5.6, 5.35, "Type 2: Functional Bugs", "The Deadly Business Logic Flaws", "MACHINE UN-AUDITABLE", CORAL_ROSE)
    tbr = s3.shapes.add_textbox(Inches(7.15), Inches(2.4), Inches(5.1), Inches(4.2))
    tfr = tbr.text_frame
    tfr.word_wrap = True
    tfr.margin_left = tfr.margin_top = tfr.margin_right = tfr.margin_bottom = 0
    pts_r = [
        ("What Are They?", "Business logic flaws. Code compiles cleanly and runs with zero crashes, but violates what the developer intended!"),
        ("Why They Are Deadly", "The contract happily transfers $8M to a random user because rules were misconfigured."),
        ("Tool Status: 0% DETECTED", "Traditional tools report '0 BUGS (SAFE)' because they do NOT understand developer intent."),
        ("The Essay Analogy", "Like an essay with perfect grammar arguing that 2+2=5. Spell-checkers can't detect flawed meaning!")
    ]
    for i, (h, d) in enumerate(pts_r):
        p = tfr.paragraphs[0] if i == 0 else tfr.add_paragraph()
        p.text = f"❌ {h}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = CORAL_ROSE
        pd = tfr.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 4: Case Study: The $8.2M Visor Finance Hack
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4, LIGHT_BG)
    add_transition(s4, "wipe", "r")
    add_header(s4, "03. Real Case Study", "The $8.2 Million Visor Finance Hack (Dec 2021)", slide_num=4)

    # Left: Story Card
    add_card(s4, 0.8, 1.45, 6.2, 5.35, "The Story Behind the Exploit", "A Single Missing Address Check", "INCIDENT REPORT", CYAN_ELECTRIC)
    tb_v = s4.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.7), Inches(4.2))
    tf_v = tb_v.text_frame
    tf_v.word_wrap = True
    tf_v.margin_left = tf_v.margin_top = tf_v.margin_right = tf_v.margin_bottom = 0
    v_story = [
        ("The Intended Logic", "Visor had a deposit function: `deposit(uint amount, address token)` designed to mint vault shares for users."),
        ("The Innocent-Looking Line", "The code called `supervisor.approve(token, amount)` to authorize token movement between contracts."),
        ("The Fatal Bug", "The contract forgot to check IF `supervisor` was the genuine supervisor contract or a fake address!"),
        ("The $8.2M Drain", "A hacker passed their own attacker contract as the supervisor. The vault approved unlimited tokens, draining $8.2M in 1 transaction.")
    ]
    for i, (h, d) in enumerate(v_story):
        p = tf_v.paragraphs[0] if i == 0 else tf_v.add_paragraph()
        p.text = f"• {h}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = INDIGO_VIBRANT
        pd = tf_v.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_BODY

    # Right: Tool Comparison Card
    add_card(s4, 7.3, 1.45, 5.233, 5.35, "How Existing Tools Reacted", "The Failure of Traditional Auditing", "AUDIT VERDICT", CORAL_ROSE)
    tb_tr = s4.shapes.add_textbox(Inches(7.55), Inches(2.4), Inches(4.7), Inches(4.2))
    tf_tr = tb_tr.text_frame
    tf_tr.word_wrap = True
    tf_tr.margin_left = tf_tr.margin_top = tf_tr.margin_right = tf_tr.margin_bottom = 0
    tool_verdicts = [
        ("Slither (Static Analysis)", "❌ Reported: 0 Bugs (Passed as Safe)", TEXT_MUTED),
        ("Mythril (Symbolic Execution)", "❌ Reported: 0 Bugs (Passed as Safe)", TEXT_MUTED),
        ("Manticore (Dynamic Engine)", "❌ Reported: 0 Bugs (Passed as Safe)", TEXT_MUTED),
        ("VeriSmart (Arithmetic Verifier)", "❌ Reported: 0 Bugs (Passed as Safe)", TEXT_MUTED),
        ("SmartInv (Columbia Paper)", "✅ INFERRED INVARIANT VIOLATION & PREVENTED THE HACK!", EMERALD_GREEN)
    ]
    for i, (name, verdict, col) in enumerate(tool_verdicts):
        p = tf_tr.paragraphs[0] if i == 0 else tf_tr.add_paragraph()
        p.text = f"{name}:"
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_HEADING

        pv = tf_tr.add_paragraph()
        pv.text = f"{verdict}\n"
        pv.font.size = Pt(11)
        pv.font.bold = True
        pv.font.color.rgb = col

    # =========================================================================
    # SLIDE 5: Why Traditional Tools Hit a Brick Wall
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5, LIGHT_BG)
    add_transition(s5, "push", "r")
    add_header(s5, "04. Literature Analysis", "Why Existing Security Tools Fail Against Logic Flaws", slide_num=5)

    tool_quad = [
        ("1. Static Analysis (e.g. Slither)", "The Pattern-Matching Trap", "STATIC LINTERS", [
            "Scans source code for predefined bad coding patterns.",
            "Completely blind to business logic: if code compiles cleanly, it assumes it is 100% safe.",
            "High false positive noise on complex protocols."
        ], INDIGO_VIBRANT),
        ("2. Symbolic Execution (e.g. Mythril)", "The Path Explosion Bottleneck", "SYMBOLIC PROVERS", [
            "Tries to mathematically explore every possible execution branch.",
            "Smart contracts with loops and external calls explode into millions of paths.",
            "Takes hours per contract and often times out with no answer."
        ], CYAN_ELECTRIC),
        ("3. Arithmetic Verifiers (e.g. VeriSmart)", "Narrow Domain Scope", "FORMAL VERIFIERS", [
            "Only checks basic arithmetic bounds (e.g. x + y <= MAX_INT).",
            "Cannot reason about user roles, admin permissions, or balance consistency.",
            "Fails to infer high-level business rules."
        ], AMBER_GOLD),
        ("4. The Fundamental Missing Link", "Intent & Semantic Awareness", "THE AI SOLUTION", [
            "Traditional tools do not read English comments, documentation, or specifications.",
            "They analyze syntax without understanding the developer's goal.",
            "SmartInv bridges this gap with Multimodal AI."
        ], EMERALD_GREEN)
    ]
    for idx, (head, sub, tag, pts, col) in enumerate(tool_quad):
        c_x = 0.8 + (idx % 2) * 6.0
        c_y = 1.45 + (idx // 2) * 2.75
        add_card(s5, c_x, c_y, 5.733, 2.55, head, sub, tag, col)
        tb_q = s5.shapes.add_textbox(Inches(c_x + 0.25), Inches(c_y + 0.85), Inches(5.2), Inches(1.6))
        tf_q = tb_q.text_frame
        tf_q.word_wrap = True
        tf_q.margin_left = tf_q.margin_top = tf_q.margin_right = tf_q.margin_bottom = 0
        for b in pts:
            p = tf_q.add_paragraph()
            p.text = f"• {b}"
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 6: What is an Invariant? (The Core Idea Explained Simply)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6, LIGHT_BG)
    add_transition(s6, "fade")
    add_header(s6, "05. Core Concept", "What is an Invariant? (The Golden Rule of Smart Contract Security)", slide_num=6)

    # Top Definition Card
    add_card(s6, 0.8, 1.45, 11.733, 1.45, "Invariant Defined in 1 Plain English Sentence", "The Mathematical Anchor", "DEFINITION", INDIGO_VIBRANT)
    tb_d = s6.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(11.2), Inches(0.65))
    tf_d = tb_d.text_frame
    tf_d.word_wrap = True
    p_d = tf_d.paragraphs[0]
    p_d.text = "\"An Invariant is a golden safety rule that must ALWAYS remain TRUE throughout the entire contract lifecycle, no matter what crazy transactions a hacker executes.\""
    p_d.font.size = Pt(14)
    p_d.font.bold = True
    p_d.font.color.rgb = NAVY_CARD

    # 3 Example Cards
    inv_trio = [
        ("1. Bank Balance Rule", "assert(balance_after >= balance_before);", "When a user deposits funds, their account balance must never decrease. If a deposit reduces your balance -> MAJOR BUG FOUND!", EMERALD_GREEN),
        ("2. Token Supply Rule", "assert(totalSupply == sum(userBalances));", "Total tokens in circulation must strictly equal the sum of all individual wallets. If tokens appear out of thin air -> MONEY PRINTING EXPLOIT!", CYAN_ELECTRIC),
        ("3. Admin Permission Rule", "assert(msg.sender == owner);", "Only the verified creator of the contract can withdraw vault reserves. If a random user triggers a withdrawal -> PRIVILEGE ESCALATION BUG!", CORAL_ROSE)
    ]
    for idx, (head, code, desc, col) in enumerate(inv_trio):
        c_x = 0.8 + idx * 4.0
        add_card(s6, c_x, 3.1, 3.733, 3.7, head, "Practical Invariant Example", "SAFETY RULE", col)
        tb_i = s6.shapes.add_textbox(Inches(c_x + 0.25), Inches(3.9), Inches(3.25), Inches(2.7))
        tf_i = tb_i.text_frame
        tf_i.word_wrap = True
        tf_i.margin_left = tf_i.margin_top = tf_i.margin_right = tf_i.margin_bottom = 0

        p_lbl = tf_i.paragraphs[0]
        p_lbl.text = "Mathematical Invariant:"
        p_lbl.font.size = Pt(10)
        p_lbl.font.bold = True
        p_lbl.font.color.rgb = TEXT_MUTED

        p_c = tf_i.add_paragraph()
        p_c.text = f"{code}\n"
        p_c.font.size = Pt(10.5)
        p_c.font.bold = True
        p_c.font.color.rgb = col

        p_dl = tf_i.add_paragraph()
        p_dl.text = "Simple Meaning:"
        p_dl.font.size = Pt(10)
        p_dl.font.bold = True
        p_dl.font.color.rgb = TEXT_MUTED

        p_desc = tf_i.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 7: The SmartInv Philosophy (AI Intuition + Formal Proof)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7, LIGHT_BG)
    add_transition(s7, "push", "r")
    add_header(s7, "06. Proposed Architecture", "SmartInv: AI Intuition Meets Mathematical Formal Proof", slide_num=7)

    # Pillar 1
    add_card(s7, 0.8, 1.45, 5.6, 5.35, "Pillar 1: Deep Learning Intuition", "Fine-Tuned LLaMA Foundation Model", "COGNITIVE STAGE", INDIGO_VIBRANT)
    tb_p1 = s7.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.1), Inches(4.2))
    tf_p1 = tb_p1.text_frame
    tf_p1.word_wrap = True
    tf_p1.margin_left = tf_p1.margin_top = tf_p1.margin_right = tf_p1.margin_bottom = 0
    p1_pts = [
        ("The AI Role", "Acts like an experienced human security auditor reading the contract."),
        ("Multimodal Understanding", "Reads Solidity code AND English comments/docstrings to grasp developer intent."),
        ("Fine-Tuned Specialization", "Trained on thousands of invariant samples using PEFT / LoRA adapter layers."),
        ("Output", "Infers candidates for bug-critical invariants at specific line numbers in seconds.")
    ]
    for i, (h, d) in enumerate(p1_pts):
        p = tf_p1.paragraphs[0] if i == 0 else tf_p1.add_paragraph()
        p.text = f"🧠 {h}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = INDIGO_VIBRANT
        pd = tf_p1.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_BODY

    # Pillar 2
    add_card(s7, 6.9, 1.45, 5.6, 5.35, "Pillar 2: Mathematical Formal Methods", "Bounded Model Checker (VeriSol & Corral)", "VERIFICATION STAGE", EMERALD_GREEN)
    tb_p2 = s7.shapes.add_textbox(Inches(7.15), Inches(2.4), Inches(5.1), Inches(4.2))
    tf_p2 = tb_p2.text_frame
    tf_p2.word_wrap = True
    tf_p2.margin_left = tf_p2.margin_top = tf_p2.margin_right = tf_p2.margin_bottom = 0
    p2_pts = [
        ("The Verifier Role", "Acts like a strict mathematician proving or disproving the AI's candidate invariants."),
        ("Boogie Intermediate Form", "Translates Solidity + Invariants into Boogie formal verification language."),
        ("Corral Solver Engine", "Exhaustively checks if ANY transaction sequence can violate the invariant."),
        ("Output", "Either proves safety OR outputs a step-by-step counterexample exploit trace.")
    ]
    for i, (h, d) in enumerate(p2_pts):
        p = tf_p2.paragraphs[0] if i == 0 else tf_p2.add_paragraph()
        p.text = f"⚖️ {h}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = EMERALD_GREEN
        pd = tf_p2.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 8: Key Innovation #1 — Multimodal Learning
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8, LIGHT_BG)
    add_transition(s8, "push", "r")
    add_header(s8, "07. Key Innovation #1", "Multimodal Learning: Seeing the Complete Picture", slide_num=8)

    trio_modal = [
        ("1. Solidity Source Code", "The Technical Logic", "SYNTAX", [
            "Mappings, state variables, and execution pathways.",
            "Tells the AI HOW the code actually runs.",
            "Captures technical mechanics."
        ], INDIGO_VIBRANT),
        ("2. Natural Language Specs", "The Human Intention", "SEMANTICS", [
            "NatSpec comments, documentation, and parameter descriptions.",
            "Tells the AI WHAT the code is supposed to achieve.",
            "Captures developer business intent."
        ], CYAN_ELECTRIC),
        ("3. Transaction History", "The Real-World Behavior", "BEHAVIOR", [
            "Historical Ethereum execution traces and balances.",
            "Tells the AI HOW USERS actually interact with the contract.",
            "Captures runtime context."
        ], EMERALD_GREEN)
    ]
    for idx, (head, sub, tag, pts, col) in enumerate(trio_modal):
        c_x = 0.8 + idx * 4.0
        add_card(s8, c_x, 1.45, 3.733, 4.0, head, sub, tag, col)
        tb_m = s8.shapes.add_textbox(Inches(c_x + 0.25), Inches(2.3), Inches(3.25), Inches(3.0))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0
        for b in pts:
            p = tf_m.add_paragraph()
            p.text = f"• {b}\n"
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_BODY

    # Bottom Analogy Card
    add_card(s8, 0.8, 5.65, 11.733, 1.15, "🏥 The Doctor Analogy (Why Multimodal Learning Wins)", "Real-Life Intuition", "ANALOGY", AMBER_GOLD)
    tb_doc = s8.shapes.add_textbox(Inches(1.05), Inches(6.15), Inches(11.2), Inches(0.55))
    tf_doc = tb_doc.text_frame
    tf_doc.word_wrap = True
    p_doc = tf_doc.paragraphs[0]
    p_doc.text = "A great doctor doesn't just look at an X-Ray (Code). They check blood tests (Traces) and listen to what the patient describes (Natural Language). Combining all 3 sources reveals the true diagnosis!"
    p_doc.font.size = Pt(11.5)
    p_doc.font.bold = True
    p_doc.font.color.rgb = NAVY_CARD

    # =========================================================================
    # SLIDE 9: Key Innovation #2 — Tier of Thought (ToT)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9, LIGHT_BG)
    add_transition(s9, "wipe", "d")
    add_header(s9, "08. Key Innovation #2", "Tier of Thought (ToT): 6-Step Structured AI Reasoning", slide_num=9)

    tot_steps = [
        ("Tier 1A: Transaction Context", "Identifies what business domain this contract belongs to (e.g. cross-function lending, swaps, arithmetics).", "TIER 1A", INDIGO_VIBRANT),
        ("Tier 1B: Critical Program Points", "Pinpoints the exact security-sensitive lines of code (e.g. Line 8: supervisor approval, Line 15: token minting).", "TIER 1B", INDIGO_VIBRANT),
        ("Tier 2A: Invariant Generation", "Synthesizes mathematical assert statements that must hold at those critical program points.", "TIER 2A", EMERALD_GREEN),
        ("Tier 2B: Critical Invariant Filter", "Removes trivial tautologies (like x == x) to keep only bug-critical safety rules.", "TIER 2B", EMERALD_GREEN),
        ("Tier 3A: Invariant Priority Ranking", "Sorts invariants by risk priority so auditors immediately inspect high-threat vulnerabilities.", "TIER 3A", CYAN_ELECTRIC),
        ("Tier 3B: Vulnerability Classification", "Outputs final security status: Healthy OR Identifies the exact bug category (e.g. Privilege Escalation).", "TIER 3B", CORAL_ROSE)
    ]
    for idx, (head, desc, tag, col) in enumerate(tot_steps):
        c_x = 0.8 + (idx % 2) * 6.0
        c_y = 1.45 + (idx // 2) * 1.78
        add_card(s9, c_x, c_y, 5.733, 1.62, head, "Cognitive Step", tag, col)
        tb_t = s9.shapes.add_textbox(Inches(c_x + 0.25), Inches(c_y + 0.82), Inches(5.2), Inches(0.7))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p = tf_t.paragraphs[0]
        p.text = desc
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 10: Live Step-by-Step Code Walkthrough
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10, LIGHT_BG)
    add_transition(s10, "push", "r")
    add_header(s10, "09. Live Walkthrough", "How SmartInv Analyzes a Vulnerable Contract Step-by-Step", slide_num=10)

    # Left: Code Snippet Card
    add_card(s10, 0.8, 1.45, 5.2, 5.35, "1. Input Solidity Contract", "Code Under Audit", "SOLIDITY", INDIGO_VIBRANT)
    code_bg = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.05), Inches(2.2), Inches(4.7), Inches(4.35))
    code_bg.fill.solid()
    code_bg.fill.fore_color.rgb = MIDNIGHT_DARK
    code_bg.line.fill.background()
    tf_c = code_bg.text_frame
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
    p_code.font.color.rgb = CYAN_SOFT

    # Right: ToT Progression Card
    add_card(s10, 6.3, 1.45, 6.233, 5.35, "2. SmartInv ToT Reasoning Flow", "Live Inference Output", "AI INFERENCE", EMERALD_GREEN)
    tb_fl = s10.shapes.add_textbox(Inches(6.55), Inches(2.3), Inches(5.7), Inches(4.2))
    tf_fl = tb_fl.text_frame
    tf_fl.word_wrap = True
    tf_fl.margin_left = tf_fl.margin_top = tf_fl.margin_right = tf_fl.margin_bottom = 0
    flow_steps = [
        ("Tier 1A Context", "Cross-function Vault token approval logic."),
        ("Tier 1B Critical Line", "Line 8 (Supervisor approval without address validation)."),
        ("Tier 2A/2B Invariant", "8+ assert(supervisor == trustedVaultSupervisor);"),
        ("Tier 3A Ranking", "Rank 1: Highest security priority."),
        ("Tier 3B Bug Inference", "Classification: 'Unauthorized Privilege Escalation'."),
        ("Formal Verifier", "❌ Invariant VIOLATED: Attacker can supply rogue supervisor address!")
    ]
    for i, (h, d) in enumerate(flow_steps):
        p = tf_fl.paragraphs[0] if i == 0 else tf_fl.add_paragraph()
        p.text = f"• {h}: "
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = INDIGO_VIBRANT if i < 5 else CORAL_ROSE
        pd = tf_fl.add_paragraph()
        pd.text = f"  {d}\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_BODY if i < 5 else CORAL_ROSE
        pd.font.bold = (i == 5)

    # =========================================================================
    # SLIDE 11: Key Innovation #3 — Formal Verification Pipeline
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_bg(s11, LIGHT_BG)
    add_transition(s11, "push", "r")
    add_header(s11, "10. Key Innovation #3", "Formal Verification: The Mathematical Proof Engine", slide_num=11)

    stages = [
        ("Stage 1: Instrumentation", "Solidity + Invariants", "STAGE 1", [
            "Inferred invariants from AI are inserted as formal `assert()` statements at critical lines.",
            "Prepared and cleaned for verification."
        ], INDIGO_VIBRANT),
        ("Stage 2: VeriSol Translation", "Boogie Intermediate Form", "STAGE 2", [
            "Microsoft VeriSol translates EVM bytecode and Solidity logic into Boogie formal IR.",
            "Eliminates compiler ambiguities."
        ], CYAN_ELECTRIC),
        ("Stage 3: Corral Solver", "Bounded Model Checker", "STAGE 3", [
            "Corral proves if ANY transaction sequence can violate the invariant rule.",
            "If violated -> Generates an exact counterexample exploit trace!"
        ], EMERALD_GREEN)
    ]
    for idx, (head, sub, tag, pts, col) in enumerate(stages):
        c_x = 0.8 + idx * 4.0
        add_card(s11, c_x, 1.45, 3.733, 4.0, head, sub, tag, col)
        tb_s = s11.shapes.add_textbox(Inches(c_x + 0.25), Inches(2.3), Inches(3.25), Inches(3.0))
        tf_s = tb_s.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
        for b in pts:
            p = tf_s.add_paragraph()
            p.text = f"• {b}\n"
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_BODY

    # Bottom Proof Card
    add_card(s11, 0.8, 5.65, 11.733, 1.15, "🎯 What is a Counterexample Trace?", "Zero Hallucination Guarantee", "PROOF", CORAL_ROSE)
    tb_p = s11.shapes.add_textbox(Inches(1.05), Inches(6.15), Inches(11.2), Inches(0.55))
    tf_p = tb_p.text_frame
    tf_p.word_wrap = True
    p_p = tf_p.paragraphs[0]
    p_p.text = "A counterexample trace is mathematically definitive proof: 'If user calls deposit(100) -> then calls execute() -> invariant fails at Line 8.' This eliminates false alarms!"
    p_p.font.size = Pt(11.5)
    p_p.font.bold = True
    p_p.font.color.rgb = NAVY_CARD

    # =========================================================================
    # SLIDE 12: Benchmark Results on 80,000+ Real Contracts
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_bg(s12, LIGHT_BG)
    add_transition(s12, "fade")
    add_header(s12, "11. Experimental Results", "Large-Scale Evaluation on 80,000+ Smart Contracts", slide_num=12)

    # 3 Big Stat Cards
    stat_boxes = [
        ("3.5×", "More Invariants", "Discovered 3.5× more security-critical invariants than previous tools.", "BENCHMARK", INDIGO_VIBRANT),
        ("4.0×", "More Critical Bugs", "Detected 4× more high-risk functional vulnerabilities than baselines.", "DETECTION", EMERALD_GREEN),
        ("150×", "Faster Speed", "Inference runs in seconds compared to hours for symbolic execution.", "EFFICIENCY", CYAN_ELECTRIC)
    ]
    for idx, (num, lbl, desc, tag, col) in enumerate(stat_boxes):
        c_x = 0.8 + idx * 4.0
        add_card(s12, c_x, 1.45, 3.733, 1.9, None, None, tag, col)
        tb_sb = s12.shapes.add_textbox(Inches(c_x + 0.25), Inches(1.85), Inches(3.25), Inches(1.4))
        tf_sb = tb_sb.text_frame
        tf_sb.word_wrap = True
        tf_sb.margin_left = tf_sb.margin_top = tf_sb.margin_right = tf_sb.margin_bottom = 0
        p_n = tf_sb.paragraphs[0]
        p_n.text = num
        p_n.font.size = Pt(28)
        p_n.font.bold = True
        p_n.font.color.rgb = col

        p_l = tf_sb.add_paragraph()
        p_l.text = f"{lbl} — {desc}"
        p_l.font.size = Pt(10.5)
        p_l.font.color.rgb = TEXT_BODY

    # Comparison Grid Card
    add_card(s12, 0.8, 3.55, 11.733, 3.25, "Comprehensive Tool Comparison (1,200+ Audited Ground Truth Benchmark)", "Performance Summary", "COMPARISON", NAVY_CARD)
    tb_tbl = s12.shapes.add_textbox(Inches(1.05), Inches(4.25), Inches(11.2), Inches(2.3))
    tf_tbl = tb_tbl.text_frame
    tf_tbl.word_wrap = True
    tf_tbl.margin_left = tf_tbl.margin_top = tf_tbl.margin_right = tf_tbl.margin_bottom = 0
    comp_rows = [
        ("Slither", "Static Linter", "Fast (Seconds)", "High (Noise)", "Misses all functional logic bugs"),
        ("Mythril", "Symbolic Execution", "Slow (Hours)", "Moderate", "Path explosion bottleneck"),
        ("Manticore", "Dynamic Analysis", "Very Slow (Hours)", "Moderate", "Cannot scale to large contracts"),
        ("SmartInv", "Multimodal AI + Verifier", "Fast (Seconds)", "Low (Verified)", "Detects & Proves Functional Bugs ⭐")
    ]
    for tool, tech, spd, fp, verdict in comp_rows:
        p_r = tf_tbl.add_paragraph()
        is_si = ("SmartInv" in tool)
        p_r.text = f"• {tool.ljust(14)} | Tech: {tech.ljust(24)} | Speed: {spd.ljust(18)} | Verdict: {verdict}"
        p_r.font.size = Pt(11)
        p_r.font.bold = is_si
        p_r.font.color.rgb = EMERALD_GREEN if is_si else TEXT_BODY

    # =========================================================================
    # SLIDE 13: Real-World Impact — 119 Live Zero-Day Bugs
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_bg(s13, LIGHT_BG)
    add_transition(s13, "push", "r")
    add_header(s13, "12. Real-World Impact", "119 Zero-Day Vulnerabilities Discovered on Ethereum", slide_num=13)

    quad_findings = [
        ("1. 119 Zero-Day Bugs", "Previously Unknown Exploits", "DISCOVERY", [
            "Discovered in live, deployed Ethereum mainnet contracts.",
            "Zero previous public knowledge or audit reports existed.",
            "All 119 bugs were 100% missed by traditional tools."
        ], CORAL_ROSE),
        ("2. 5 High-Severity Confirmed", "Developer Validations", "CONFIRMED", [
            "5 critical vulnerabilities officially confirmed by project core teams.",
            "Responsible disclosure prevented potential millions in exploit losses.",
            "Demonstrates practical real-world industry impact."
        ], EMERALD_GREEN),
        ("3. Business Logic Flaws", "Vault & Staking Issues", "LOGIC BUGS", [
            "Discovered flawed reward calculation algorithms in staking pools.",
            "Fixed share-dilution loopholes where early depositors were cheated.",
            "Prevented price-oracle arbitrage exploits."
        ], CYAN_ELECTRIC),
        ("4. Privilege Escalations", "Access Control Bypasses", "SECURITY", [
            "Found contracts where unauthorized external callers triggered admin functions.",
            "Identified uninitialized state variables in proxy contracts.",
            "Secured cross-bridge token transfers."
        ], AMBER_GOLD)
    ]
    for idx, (head, sub, tag, pts, col) in enumerate(quad_findings):
        c_x = 0.8 + (idx % 2) * 6.0
        c_y = 1.45 + (idx // 2) * 2.75
        add_card(s13, c_x, c_y, 5.733, 2.55, head, sub, tag, col)
        tb_f = s13.shapes.add_textbox(Inches(c_x + 0.25), Inches(c_y + 0.85), Inches(5.2), Inches(1.6))
        tf_f = tb_f.text_frame
        tf_f.word_wrap = True
        tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
        for b in pts:
            p = tf_f.add_paragraph()
            p.text = f"• {b}"
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 14: Ablation Study — Proof that ToT is the Hero
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_bg(s14, LIGHT_BG)
    add_transition(s14, "push", "r")
    add_header(s14, "13. Scientific Rigor", "Ablation Study: Proving Tier of Thought is the Hero", slide_num=14)

    # Left Card
    add_card(s14, 0.8, 1.45, 5.2, 5.35, "What is an Ablation Study?", "Isolating What Really Works", "METHODOLOGY", INDIGO_VIBRANT)
    tb_ab = s14.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(4.7), Inches(4.2))
    tf_ab = tb_ab.text_frame
    tf_ab.word_wrap = True
    tf_ab.margin_left = tf_ab.margin_top = tf_ab.margin_right = tf_ab.margin_bottom = 0
    ab_pts = [
        ("The Scientific Test", "Researchers systematically removed one component at a time to measure exactly how much accuracy drops."),
        ("Key Finding #1", "Removing Tier of Thought causes a catastrophic 66% drop in F1-score!"),
        ("Key Finding #2", "Removing Natural Language causes a 37% drop (and functional bug detection drops 40×)."),
        ("The Conclusion", "Tier of Thought structured reasoning is the single most vital innovation of the paper.")
    ]
    for i, (h, d) in enumerate(ab_pts):
        p = tf_ab.paragraphs[0] if i == 0 else tf_ab.add_paragraph()
        p.text = f"• {h}\n"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = INDIGO_VIBRANT
        pd = tf_ab.add_paragraph()
        pd.text = f"{d}\n"
        pd.font.size = Pt(11)
        pd.font.color.rgb = TEXT_BODY

    # Right Card
    add_card(s14, 6.3, 1.45, 6.233, 5.35, "Ablation Experiment Data (Table 9 & 11)", "Measured Accuracy & F1", "RESULTS", EMERALD_GREEN)
    tb_dt = s14.shapes.add_textbox(Inches(6.55), Inches(2.4), Inches(5.7), Inches(4.2))
    tf_dt = tb_dt.text_frame
    tf_dt.word_wrap = True
    tf_dt.margin_left = tf_dt.margin_top = tf_dt.margin_right = tf_dt.margin_bottom = 0
    ab_data = [
        ("Full SmartInv (All Features)", "0.89", "0.82", "Optimal Baseline ⭐", EMERALD_GREEN),
        ("Remove Optimization", "0.89", "0.82", "Minimal difference", TEXT_HEADING),
        ("Remove Labeled Features", "0.59", "0.60", "-22% F1 Decrease", TEXT_MUTED),
        ("Remove Natural Language (NL)", "0.62", "0.45", "-37% F1 Drop 📉", CORAL_ROSE),
        ("Remove Tier of Thought (ToT)", "0.24", "0.16", "-66% F1 Collapse 📉📉", CORAL_ROSE),
        ("Raw Base LLM (No Fine-tuning)", "0.12", "0.14", "Complete Failure", CORAL_ROSE)
    ]
    for name, acc, f1, note, col in ab_data:
        p = tf_dt.add_paragraph()
        p.text = f"• {name}"
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = col

        pd = tf_dt.add_paragraph()
        pd.text = f"  Accuracy: {acc} | F1-Score: {f1} ({note})\n"
        pd.font.size = Pt(10.5)
        pd.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 15: What I Personally Built & Ran (Mid-Sem Milestones)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_bg(s15, LIGHT_BG)
    add_transition(s15, "push", "r")
    add_header(s15, "14. Mid-Sem Milestones", "Practical Work Executed on Local Machine", slide_num=15)

    my_milestones = [
        ("1. Environment & Setup", "Dependency Integration", "SETUP", [
            "Cloned full research repository and configured local Python environment.",
            "Integrated PyTorch 2.8, HuggingFace Transformers, PEFT, and OpenAI SDK.",
            "Created clean workspace structure with Git version control."
        ], INDIGO_VIBRANT),
        ("2. Bug Fixing & Compatibility", "Windows Porting & Fixes", "DEBUGGING", [
            "Fixed Windows file encoding bug (UnicodeEncodeError for pi symbols) in dataset generator.",
            "Replaced hardcoded Linux author paths (/home/sally...) with dynamic relative paths.",
            "Patched OpenAI client initialization crash to support offline and help modes."
        ], CYAN_ELECTRIC),
        ("3. Dataset Processing", "ToT Training Data Generation", "EXECUTION", [
            "Executed generator.py — generated all 3,000+ ToT structured prompt-completion pairs.",
            "Validated smartinv.py CLI argument parser (Exit Code 0).",
            "Tested verification routines on sample benchmark contracts."
        ], EMERALD_GREEN),
        ("4. Comprehensive Guides & Git", "Defense Prep & Repository", "DELIVERABLES", [
            "Authored 5 extensive study guide documents in dedicated study_guide/ folder.",
            "Set up dual remotes (origin -> User GitHub, upstream -> Columbia).",
            "Pushed all code fixes, datasets, and presentation decks to GitHub."
        ], AMBER_GOLD)
    ]
    for idx, (head, sub, tag, pts, col) in enumerate(my_milestones):
        c_x = 0.8 + (idx % 2) * 6.0
        c_y = 1.45 + (idx // 2) * 2.75
        add_card(s15, c_x, c_y, 5.733, 2.55, head, sub, tag, col)
        tb_m = s15.shapes.add_textbox(Inches(c_x + 0.25), Inches(c_y + 0.85), Inches(5.2), Inches(1.6))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0
        for b in pts:
            p = tf_m.add_paragraph()
            p.text = f"✔ {b}"
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 16: Conclusion & Future Vision (Dark Grand Finale Theme)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    set_bg(s16, MIDNIGHT_DARK)
    add_transition(s16, "fade")

    # Center Hero Card
    box_e = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(0.9), Inches(10.933), Inches(5.7))
    box_e.fill.solid()
    box_e.fill.fore_color.rgb = NAVY_CARD
    box_e.line.color.rgb = INDIGO_VIBRANT
    box_e.line.width = Pt(2)

    tb_e = s16.shapes.add_textbox(Inches(1.6), Inches(1.2), Inches(10.133), Inches(5.1))
    tf_e = tb_e.text_frame
    tf_e.word_wrap = True
    tf_e.margin_left = tf_e.margin_top = tf_e.margin_right = tf_e.margin_bottom = 0

    p_eb = tf_e.paragraphs[0]
    p_eb.alignment = PP_ALIGN.CENTER
    p_eb.text = "🎯 PROJECT SUMMARY & KEY TAKEAWAYS"
    p_eb.font.size = Pt(12)
    p_eb.font.bold = True
    p_eb.font.color.rgb = CYAN_ELECTRIC

    p_et = tf_e.add_paragraph()
    p_et.alignment = PP_ALIGN.CENTER
    p_et.text = "SmartInv: AI Intuition Meets Mathematical Proof"
    p_et.font.size = Pt(26)
    p_et.font.bold = True
    p_et.font.color.rgb = TEXT_WHITE

    concl_items = [
        "First automated security tool to solve 'Machine Un-auditable' functional bugs.",
        "Tier of Thought (ToT) is the core breakthrough — boosting F1-score by 66%.",
        "Discovered 119 live zero-day vulnerabilities in production Ethereum contracts.",
        "Fully implemented, debugged, and verified on local machine with full study repository."
    ]
    for b in concl_items:
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
    p_qa.font.color.rgb = EMERALD_GREEN

    # Save Ultimate Deck
    out_file = r"c:\Users\saini\OneDrive\Desktop\BLOCKCHAIN-PROJECT\SmartInv_Ultimate_Candy_Deck.pptx"
    prs.save(out_file)
    print(f"Ultimate Candy presentation saved successfully to: {out_file}")

if __name__ == "__main__":
    create_ultimate_candy_deck()
