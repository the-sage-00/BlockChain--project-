# 📖 Part 5: Teacher Q&A Preparation — Anticipated Questions & Answers

> Practice these Q&As and you'll be ready for **anything** your teacher asks.

---

## 🟢 Basic Understanding Questions

### Q1: "What is SmartInv?"
**Answer:** SmartInv is an automated tool from Columbia University that uses AI (large language models) to find security bugs in smart contracts. Its key innovation is that it can detect "machine un-auditable" bugs — complex functional vulnerabilities that no existing automated tool can find. It was published at IEEE S&P 2024, one of the top-4 security conferences in the world.

---

### Q2: "What problem does it solve?"
**Answer:** Smart contracts on Ethereum handle billions of dollars, and bugs in them lead to massive hacks. Existing tools like Slither and Mythril can only catch simple coding errors like reentrancy or integer overflow. But there's a much more dangerous category of bugs — functional bugs — where the code runs correctly but doesn't match what the developer intended. For example, the Visor Finance hack lost \$8.2 million because of such a bug, and no existing tool detected it. SmartInv solves this by understanding both the code AND the intended behavior.

---

### Q3: "What is an invariant?"
**Answer:** An invariant is a rule or condition that must always be true during a program's execution. For example, in a banking contract: "a user's balance after a deposit should always be greater than or equal to their balance before the deposit." If this rule is ever violated, it means there's a bug. SmartInv automatically figures out what these rules should be for any given contract.

---

### Q4: "What is a smart contract?"
**Answer:** A smart contract is a self-executing program that lives on the blockchain. Once deployed, it runs automatically according to its programmed rules — no human can change or stop it. Think of it like a vending machine: you put in money, press a button, and get exactly what was programmed. Smart contracts are used in DeFi for lending, trading, insurance — all without banks.

---

### Q5: "Why can't we just use existing tools?"
**Answer:** Existing tools like Slither, Mythril, and Manticore only analyze the code itself. They look for known patterns of bugs. But they have no way of knowing what the code is *supposed to do*. It's like having a spell-checker that catches typos but can't tell you if your essay makes sense. SmartInv is different because it reads both the code AND the natural language specifications to understand intent.

---

## 🟡 Methodology Deep-Dive Questions

### Q6: "What is Tier of Thought and how is it different from Chain of Thought?"
**Answer:** Chain of Thought asks the AI to "think step by step" in a single chain. Tier of Thought goes further — it structures the reasoning into 6 specific tiers, where each tier asks a different type of question and the output of one tier becomes the input of the next. 

The tiers are:
1. Understand the transaction context
2. Find critical program points
3. Generate invariants
4. Filter to critical invariants
5. Rank the invariants
6. Detect vulnerabilities

This mimics how a human expert auditor would actually think — first understanding what the contract does, then focusing on critical areas, then checking for violations. The ablation study proves ToT is THE most important component — removing it causes a 66% drop in F1-score.

---

### Q7: "What does 'multimodal' mean in this context?"
**Answer:** Multimodal means using multiple types of information simultaneously. SmartInv uses three modalities:
1. **Source code** — the Solidity smart contract itself
2. **Natural language** — documentation, comments, specifications describing what the contract should do
3. **Transaction history** — how the contract actually behaves on the blockchain

Combining all three gives a much more complete understanding than using code alone. The analogy is a doctor who uses X-rays, blood tests, AND the patient's description together for a better diagnosis.

---

### Q8: "How does the AI model get trained?"
**Answer:** The researchers took LLaMA-7B, a general-purpose AI model from Meta with 7 billion parameters. They manually created a dataset of 2,000+ smart contracts with their correct invariants, formatted into 3,000+ Tier of Thought training samples. They then fine-tuned LLaMA using PEFT/LoRA — a technique that only modifies a small portion of the model's parameters, saving time and GPU memory. After fine-tuning, the model becomes specialized in understanding smart contract invariants.

---

### Q9: "What is PEFT and LoRA?"
**Answer:** PEFT stands for Parameter-Efficient Fine-Tuning. Instead of changing all 7 billion parameters of LLaMA (which would need enormous GPU resources), PEFT only modifies a small fraction. LoRA is a specific PEFT technique — it adds tiny "adapter" layers to the model that learn the new task while keeping the original model frozen. The analogy: instead of rebuilding an entire car engine for racing, you just attach a turbocharger.

---

### Q10: "How does verification work?"
**Answer:** After the AI generates invariants, SmartInv verifies them using formal methods. The contract with invariants is converted to a formal language called Boogie using VeriSol (a Microsoft Research tool). Then a bounded model checker called Corral checks if the invariants hold for all possible executions. If an invariant is violated, Corral produces a counterexample trace — a step-by-step proof of how a hacker could trigger the bug.

---

### Q11: "What is a bounded model checker?"
**Answer:** It's a tool that mathematically proves a program is correct — but only up to a certain number of steps. It explores all possible executions of the contract up to, say, 10 transactions. If no invariant violation is found in those 10 transactions, it's considered safe. It's not infinite proof, but it catches the vast majority of real-world bugs.

---

### Q12: "What are the two modes of SmartInv?"
**Answer:** Heavy mode uses a locally-running fine-tuned LLaMA model. It needs a powerful GPU (A100 or V100) but gives the best results and is free to use. Light mode uses GPT-4 through OpenAI's API. It doesn't need a GPU but costs money per query and gives slightly less deterministic results. Heavy mode is recommended for research, light mode for quick checks.

---

## 🔴 Results & Evaluation Questions

### Q13: "What are the main results?"
**Answer:** SmartInv generated 3.5× more bug-critical invariants, detected 4× more critical bugs, and ran 150× faster than existing tools. It found 119 zero-day vulnerabilities in real-world contracts, 5 of which were confirmed as high-severity by the developers. It achieved an F1-score of 0.82, which is very strong for this domain.

---

### Q14: "How was SmartInv evaluated?"
**Answer:** Five main experiments were conducted:
1. **Motivating examples** — proved it catches real hacks (Visor, TimelockController)
2. **Large-scale experiment** — tested on 80,000+ contracts from Etherscan
3. **Refined analysis** — tested on 1,200+ contracts with known ground truths
4. **Prompting comparison** — compared ToT vs other prompting strategies
5. **Ablation study** — removed components one by one to measure their importance

---

### Q15: "What did the ablation study show?"
**Answer:** The ablation study systematically removed each component of SmartInv and measured the impact. The key findings were:
- Removing ToT caused the biggest drop — 66% decrease in F1
- Removing natural language caused a 37% drop in F1 and 40× reduction in functional bug detection
- Removing labeled features caused a 22% drop
- This proves that ToT is the most critical innovation, followed by multimodal learning

---

### Q16: "What are zero-day vulnerabilities and how many did SmartInv find?"
**Answer:** A zero-day vulnerability is a bug that nobody has ever discovered before — "zero days" since it was found. SmartInv discovered 119 of these in real, deployed smart contracts on Ethereum. Five were confirmed by the actual developers as "high severity." None of these bugs were detected by any existing automated tool.

---

### Q17: "What is precision, recall, and F1?"
**Answer:** 
- Precision: Of all bugs the tool reported, what percentage were real? (Low false alarms = high precision)
- Recall: Of all real bugs that exist, what percentage did the tool find? (Misses few bugs = high recall)
- F1: The harmonic mean — a balance between precision and recall. SmartInv achieved 0.82 F1, meaning it's good at both finding real bugs AND not raising false alarms.

---

## 🟣 Critical Thinking & Limitations Questions

### Q18: "What are the limitations of SmartInv?"
**Answer:** The paper honestly acknowledges several limitations:
1. **Non-deterministic output** — AI models can give different answers each time, making results unstable
2. **No uniform benchmark** — different papers use different test sets, making fair comparison hard
3. **Heavy manual work** — creating the training dataset required extensive human labeling
4. **Ground truth subjectivity** — deciding whether something is a "bug" involves human judgment, which can be wrong
5. **Compiler compatibility** — the VeriSol verifier doesn't support all Solidity versions

---

### Q19: "Can SmartInv replace human auditors?"
**Answer:** No, not entirely. SmartInv is meant to **assist** human auditors, not replace them. It automates the detection of functional bugs that are extremely hard to find manually, but it still requires human oversight for:
- Interpreting results
- Fixing compilation issues in generated invariants
- Validating whether identified bugs are truly exploitable
- Handling contracts that VeriSol can't verify

---

### Q20: "What if the AI generates wrong invariants?"
**Answer:** This is a valid concern. The AI might generate invariants that are too strict (false positives — flagging safe code as buggy) or too loose (false negatives — missing real bugs). SmartInv mitigates this through: (1) the ToT structured reasoning, which improves accuracy, (2) the verification phase, which mathematically checks if violations are real, and (3) the ranking system, which prioritizes high-confidence invariants.

---

### Q21: "Why not just use GPT-4 directly?"
**Answer:** The prompting experiment showed that even GPT-4 with good prompts performs significantly worse than SmartInv's fine-tuned model with ToT. Just asking GPT-4 "find bugs" doesn't work well because it lacks: (1) training on smart-contract-specific invariant data, (2) the structured Tier of Thought reasoning, and (3) the formal verification pipeline. SmartInv's approach of fine-tuning + ToT + verification is fundamentally more effective.

---

### Q22: "Is this approach generalizable beyond smart contracts?"
**Answer:** Yes, potentially. The core ideas — multimodal learning (code + natural language) and Tier of Thought reasoning — could apply to any domain where code needs to match specifications. For example: medical device software, financial trading systems, or autonomous vehicle controllers. However, new training datasets would need to be created for each domain.

---

## 🔵 Comparison Questions

### Q23: "How is SmartInv different from Slither?"
**Answer:** Slither is a static analysis tool that looks for known bad patterns in code (like a spell-checker for smart contracts). SmartInv uses AI to understand the intended behavior and generates custom invariants. Slither is fast and catches simple bugs but misses functional bugs entirely. SmartInv is more powerful but requires more compute resources.

---

### Q24: "How is SmartInv different from GPTScan?"
**Answer:** GPTScan also uses GPT for smart contract analysis, but it uses generic prompting without fine-tuning or structured reasoning. SmartInv's key advantages are: (1) it's fine-tuned specifically on invariant data, (2) it uses the Tier of Thought prompting strategy, and (3) it includes formal verification. GPTScan relies entirely on the base model's knowledge without specialization.

---

## ⚫ Tricky / Advanced Questions

### Q25: "What is the difference between 'implementation bugs' and 'machine un-auditable bugs'?"
**Answer:** Implementation bugs are coding mistakes — the developer wrote technically incorrect code (like a reentrancy vulnerability or integer overflow). These produce wrong outputs even by programming standards. Machine un-auditable bugs are different — the code is technically correct, it compiles and runs fine, but it doesn't match the developer's actual intention. The code "works" but does the wrong thing. Existing tools can catch implementation bugs but miss machine un-auditable bugs entirely.

---

### Q26: "How do you define 'critical program point'?"
**Answer:** A critical program point is a specific line of code where security-relevant operations happen — money transfers, balance updates, access control checks, or state changes. Not every line is equally important. Line 5 might just initialize a variable (not critical), while Line 23 might transfer tokens (very critical). SmartInv identifies which lines matter most and focuses invariant generation on those lines.

---

### Q27: "What is the training data format for ToT?"
**Answer:** Each training sample is a prompt-completion pair. The prompt contains the contract code plus a specific question (like "What are the critical program points?"), and the completion contains the correct answer. For each contract, there are 6 such pairs — one for each tier. So a dataset of 500 contracts produces 3,000 training samples. The format is JSON with "prompt" and "completion" fields.

---

### Q28: "What models were compared and which performed best?"
**Answer:** Seven models were tested: PEFT-LLaMA, Alpaca-LLaMA, Full LLaMA with CoT, GPT-2, T5, OPT-350M, and GPT-4. PEFT-LLaMA with ToT fine-tuning performed best overall for the heavy mode. For light mode (no GPU needed), GPT-4 with ToT prompting was the best choice. All deployed models are publicly available on HuggingFace.

---

### Q29: "What would you improve about this paper?"
**Answer (shows critical thinking):**
1. Create a **standardized benchmark** so future papers can fairly compare against SmartInv
2. Reduce the **manual work** in dataset creation — perhaps use semi-supervised learning
3. Add support for **more Solidity compiler versions** in the verifier
4. Address the **non-deterministic output** problem — maybe use ensemble methods (running the model multiple times and voting)
5. Explore **newer models** like GPT-4-Turbo, Claude, or Gemini which didn't exist when this paper was written

---

### Q30: "Why was this published at S&P and not an AI conference?"
**Answer:** Because the primary contribution is in **security**, not AI. The paper solves a security problem (detecting smart contract vulnerabilities) using AI as a tool. IEEE S&P is a top-4 security conference that focuses on practical security impact. The 119 zero-day vulnerabilities discovered demonstrate significant real-world security impact, which is exactly what S&P values.

---

## 🎤 5-Minute Presentation Script Outline

```
1. HOOK (30 sec)
   → Start with the Visor hack story: "$8.2 million stolen, 
     no tool detected it."

2. PROBLEM (1 min)
   → Smart contracts handle billions → bugs = massive theft
   → Two types of bugs: implementation (easy) vs functional (hard)
   → Existing tools only catch easy bugs

3. SOLUTION (1.5 min)
   → SmartInv: AI + Code + Natural Language + Verification
   → Tier of Thought: 6-step structured reasoning
   → Draw the 3-phase pipeline (Training → Inference → Verification)

4. RESULTS (1 min)
   → 3.5× more invariants, 4× more bugs, 150× faster
   → 119 zero-day vulnerabilities in real contracts
   → Ablation: ToT is the key (66% drop without it)

5. CONCLUSION & LIMITATIONS (1 min)
   → First tool to detect "machine un-auditable" bugs
   → Limitations: non-deterministic, manual datasets
   → Future: standardized benchmarks, newer models
```

---

> [!TIP]
> **Pro tips for your presentation:**
> - If you don't know an answer, say "The paper doesn't specifically address that, but based on the methodology, I think..."
> - Use analogies liberally (vending machine, spell-checker, doctor)
> - Show you read critically by mentioning limitations without being asked
> - The Visor hack example is your strongest weapon — use it whenever possible
