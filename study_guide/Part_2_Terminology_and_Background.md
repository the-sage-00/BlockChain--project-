# 📖 Part 2: Terminology & Background — Every Term You Need to Know

> This guide explains **every important term** used in the SmartInv paper in the simplest possible language. Master these and you can answer any terminology question your teacher asks.

---

## 🔗 Blockchain Basics

### Blockchain
A **digital ledger** (record book) that is shared across thousands of computers worldwide. Once something is written in it, it **cannot be changed or deleted**.

**Analogy:** Think of it as a Google Doc that everyone can read, anyone can add to, but nobody can edit or delete past entries.

### Ethereum
The **most popular blockchain** for running smart contracts. Created by Vitalik Buterin in 2015. While Bitcoin is mainly for sending money, Ethereum is a **general-purpose computer** that runs programs (smart contracts) on the blockchain.

### Solidity
The **programming language** used to write smart contracts on Ethereum. Just like Python is used for data science, and Java is used for Android apps — Solidity is used for blockchain programs.

### Gas
The **fee** you pay to execute operations on Ethereum. Every line of code costs gas. This prevents people from running infinite loops and spamming the network.

### EVM (Ethereum Virtual Machine)
The **engine** that runs smart contracts. Every computer in the Ethereum network has an EVM, and they all execute the same code to reach the same result.

---

## 📜 Smart Contract Concepts

### Smart Contract
A **self-executing program** stored on the blockchain. Once deployed, it runs exactly as programmed — no human intervention needed.

**Analogy:** A vending machine. You put in money, press a button, and get exactly what was programmed. Nobody can change the rules mid-transaction.

### DeFi (Decentralized Finance)
Traditional banking (loans, trading, insurance) **rebuilt on blockchain** using smart contracts. No banks needed — the smart contracts ARE the bank.

**Why it matters for this paper:** DeFi contracts handle billions of dollars. A bug = massive theft.

### Token (ERC-20)
A digital asset created by a smart contract. Think of it as creating your own currency or loyalty points on the blockchain.

### Reentrancy
A famous smart contract bug where a function can be **called again before the first call finishes**.

**Analogy:** You go to an ATM, withdraw \$100, but before the ATM updates your balance, you quickly withdraw another \$100. Your balance only decreases by \$100, but you got \$200. The famous 2016 DAO hack (\$60M stolen) exploited this exact bug.

### Integer Overflow
When a number gets **too big for the computer to store** and wraps around to zero (or a small number).

**Analogy:** A car odometer that shows 999,999 km. Drive one more km, and it resets to 000,000. In smart contracts, this can make a huge balance suddenly become zero.

---

## 🧠 Core SmartInv Concepts

### Invariant
> [!IMPORTANT]
> This is THE most important concept in the entire paper.

An **invariant** is a **rule or condition that must ALWAYS be true** during the execution of a program, no matter what.

**Simple examples:**
| Invariant | Meaning |
|---|---|
| `balance_after >= balance_before` | After a deposit, your balance should never decrease |
| `totalSupply == sum(all_balances)` | Total tokens should always equal the sum of everyone's tokens |
| `only_owner_can_withdraw` | Only the contract owner should be able to take money out |
| `x + 2 == y` (after `y = x + 2`) | If y is computed as x+2, then this must always hold |

**Why invariants matter:**
- If you know the invariants of a contract, you know the **rules it must follow**
- If the code **violates** an invariant → **you found a bug**
- Traditional tools can only check simple invariants (like "no overflow")
- SmartInv can figure out **complex, business-logic invariants** that humans would write

### Program Point
A **specific line or location** in the code where an invariant should hold.

**Example:**
```
Line 5: balance = balance + deposit;   ← Program point!
         // Invariant at line 5: balance should increase by exactly 'deposit'
Line 8: transfer(user, amount);        ← Program point!
         // Invariant at line 8: amount should not exceed balance
```

### Critical Program Point
A **program point that is especially important for security**. Not every line of code is equally important — some lines handle money transfers, access control, or state changes. These are "critical."

### Bug-Critical Invariant
An invariant whose **violation would directly lead to a security vulnerability**. SmartInv focuses on finding these, not just any invariant.

---

## 🤖 AI & Machine Learning Concepts

### Foundation Model / Large Language Model (LLM)
A **massive AI model** trained on huge amounts of text data that can understand and generate human-like text. Examples: GPT-4, LLaMA, T5.

**Analogy:** It's like a very smart student who has read millions of books and can answer questions, write essays, and even understand code.

### Fine-tuning
**Teaching a pre-trained AI model to specialize** in a specific task by training it on a smaller, task-specific dataset.

**Analogy:** A medical student (pre-trained general knowledge) does a residency in cardiology (fine-tuning) to become a heart specialist. The model already knows language — you just teach it to understand smart contract invariants.

### PEFT (Parameter-Efficient Fine-Tuning)
A **shortcut method** for fine-tuning that modifies only a **small portion** of the model's parameters instead of all of them. This saves time, memory, and computing power.

### LoRA (Low-Rank Adaptation)
A specific PEFT technique. Instead of changing the entire AI model, LoRA adds small "adapter" layers that learn the new task. The original model stays frozen.

**Analogy:** Instead of rebuilding an entire car engine for racing, you just attach a turbocharger. The car's original engine stays the same, but it performs better for racing.

### Multimodal Learning
Training an AI model using **multiple types of data** simultaneously:
- **Source code** (programming language)
- **Natural language** (English descriptions, documentation)
- **Transaction history** (how the contract behaves on-chain)

**Analogy:** A doctor diagnosing a patient uses multiple sources — X-rays (images), blood tests (numbers), and the patient's description of symptoms (words). Using all sources together gives a much better diagnosis than using just one.

### Prompt Engineering
Carefully **crafting the question/instruction** you give to an AI model to get better answers.

**Example:**
- Bad prompt: "Find bugs in this code"
- Good prompt: "Given this Solidity smart contract, what are the critical program points where invariants should hold to prevent functional vulnerabilities?"

### Chain of Thought (CoT)
A prompting technique where you ask the AI to **show its reasoning step by step** instead of jumping to the answer.

**Example:**
- Without CoT: "What is 17 × 24?" → "408"
- With CoT: "What is 17 × 24? Think step by step." → "17 × 20 = 340, 17 × 4 = 68, 340 + 68 = 408"

### Tier of Thought (ToT) — SmartInv's Innovation ⭐
An **upgraded version of Chain of Thought** designed specifically for SmartInv. Instead of one chain of reasoning, it uses **multiple tiers** (levels) where each tier builds on the previous one:

```
Tier 1A: Understand the contract context
Tier 1B: Find critical program points
Tier 2A: Generate invariants for those points
Tier 2B: Identify which invariants are critical
Tier 3A: Rank the critical invariants
Tier 3B: Detect vulnerabilities
```

> [!NOTE]
> The key insight: ToT is more than just "think step by step." Each tier asks a **different type of question**, and the answer from one tier becomes the **input** for the next. This mimics how a **human expert auditor** thinks.

---

## 🔧 Verification Concepts

### Formal Verification
**Mathematically proving** that a program behaves correctly. Instead of just testing with examples, you prove it works for ALL possible inputs.

**Analogy:** Testing = driving a car 100 times and seeing if it crashes. Formal verification = mathematically proving the car's brakes will always work under any conditions.

### Bounded Model Checking
A type of formal verification that checks correctness **up to a certain number of steps** (not infinite). It's like saying: "I can prove this contract works correctly for any sequence of up to 10 transactions."

### VeriSol
The **verification tool** that SmartInv uses. Built by Microsoft Research, it converts Solidity contracts to a formal language (Boogie) and checks if invariants hold.

### Boogie
An **intermediate verification language** used by VeriSol. Solidity code is translated into Boogie, which is then checked by a prover.

### Corral
The **verification engine** that checks Boogie programs. When SmartInv's verifier finds a bug, it produces a **counterexample trace** — a step-by-step sequence showing exactly how the bug can be triggered.

---

## 🛡️ Security Concepts

### Zero-Day Vulnerability
A bug that is **previously unknown** — nobody has discovered or reported it before. "Zero days" since discovery. These are the most dangerous because there's no fix yet.

SmartInv found **119 zero-day vulnerabilities** in real-world contracts.

### Audit / Smart Contract Audit
A **manual security review** of a smart contract by human experts. Companies pay \$50,000–\$500,000+ for a professional audit. But even human auditors miss bugs — SmartInv aims to help automate parts of this process.

### Exploit
A technique or attack that **takes advantage of a bug** to steal money or cause harm.

---

## 🏁 Comparator Tools (What SmartInv is Compared Against)

| Tool | What It Does | Type |
|---|---|---|
| **Slither** | Static analysis — scans code for known bad patterns | Pattern matching |
| **Mythril** | Symbolic execution — explores all possible code paths | Formal methods |
| **Manticore** | Dynamic symbolic execution — simulates contract execution | Formal methods |
| **VeriSmart** | Checks arithmetic-related invariants automatically | Invariant checking |
| **SmarTest** | Generates tests to find exploits | Testing |
| **GPTScan** | Uses GPT to scan contracts (not fine-tuned) | AI-based |
| **SmartInv** | Multimodal invariant inference with ToT | AI + Formal methods |

---

## 🎯 Key Models Used in SmartInv

| Model | Description | Role in SmartInv |
|---|---|---|
| **LLaMA-7B** | Meta's open-source language model with 7 billion parameters | Base model that gets fine-tuned |
| **PEFT-LLaMA** | LLaMA fine-tuned using LoRA (parameter efficient) | Main model for heavy-mode SmartInv |
| **Alpaca-LLaMA** | Stanford's instruction-following LLaMA variant | Alternative fine-tuned model |
| **GPT-4** | OpenAI's commercial model | Used for light-mode SmartInv |
| **GPT-2** | Smaller OpenAI model | Compared in experiments |
| **T5** | Google's text-to-text model | Compared in experiments |
| **OPT-350M** | Meta's smaller open model | Compared in experiments |

---

> [!TIP]
> **For your presentation:** Don't try to define every term upfront. Instead, introduce them naturally as you explain the methodology. If your teacher asks "What is an invariant?", give the simple definition + the balance example. If they ask "What is PEFT?", use the turbocharger analogy.
