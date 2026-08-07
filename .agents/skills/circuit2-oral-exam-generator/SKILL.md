---
name: circuit2-oral-exam-generator
description: Generates, analyzes, and builds professional Electrical Engineering (Circuit Analysis II) oral exam solutions, interactive HTML dashboards, Master Prompts, and automatically updates the root index.html master portal hub.
---

# Circuit 2 Oral Exam Solution & Interactive Portal Generator Skill

Skill สำหรับวิเคราะห์ สร้างเอกสารเฉลยวิชาการวิศวกรรมไฟฟ้า (Circuit Analysis II) สร้างสื่อการสอนแบบโต้ตอบ (Interactive HTML Dashboard) และอัปเดตหน้าหลัก `index.html` แบบอัตโนมัติ 

---

## 🎯 ปรัชญาและเป้าหมายสูงสุด (Core Philosophy)

1. **Zero-to-Hero Pedagogical Scaffolding:** 
   ปูพื้นฐานจาก 0 ด้วยมโนทัศน์ทางกายภาพ (Feynman Technique เช่น ท่อน้ำ ถังน้ำ พลังงาน) ก่อนแตะสมการคณิตศาสตร์ เพื่อให้นิสิตที่ไม่มีพื้นฐานอ่านแล้วบรรลุแจ้งเห็นจริงจนกลายเป็นปรมาจารย์
2. **Zero Mathematical Gaps:**
   การพิสูจน์วงจร (KCL, KVL, Differential Equations, Laplace Transform, Asymptotic Fitting) ต้องแสดงการย้ายข้าง แทนค่าทศนิยม และอินทิเกรตบรรทัดต่อบรรทัด โดยไม่มีการข้ามขั้นตอนหรือละไว้ในฐานที่เข้าใจ
3. **Master Distinction Oral Defense (100/100):**
   เก็งคำถามสอบปากเปล่าเจาะลึก 10-15 ข้อ พร้อมบทพูดซ้อมจริงของนิสิต ชี้จุดกับดักที่คนมักโดนหลอกจนได้ 0 คะแนน และแสดงแนวทางตอบสไตล์เกียรตินิยม
4. **Interactive Dashboard Standard:**
   แดชบอร์ด HTML ปุ่มเดียวจบ Responsive 100% สไตล์ Dark Mode + Glassmorphism UI พร้อมระบบควบคุมแบบ Mobile-first (ปุ่มย้อนกลับมุมบนซ้าย `←`, ปุ่มเปิดโจทย์มุมซ้ายล่าง `📐`, ปุ่มเลื่อนแท็บ `◀` / `▶` ที่สลับแท็บและซ่อนอัตโนมัติ)
5. **Automatic Master Portal Synchronization:**
   อัปเดตการ์ดโจทย์ในหน้าหลัก `index.html` และ `README.md` ให้เป็นระเบียบ เรียบง่าย และมีปุ่มกดหลักเพียงปุ่มเดียวต่อข้อ

---

## 📂 โครงสร้างมาตรฐานระดับโปรเจกต์ (Standard Directory Layout)

เมื่อสร้างหรือเพิ่มโจทย์ข้อใหม่ (เช่น `problem-N`) ต้องจัดวางโครงสร้างตามมาตรฐานดังนี้:

```text
oral-exam/
├── index.html                                <-- Master Portal แดชบอร์ดรวมโจทย์ทุกข้อ (Auto Sync)
├── .nojekyll                                 <-- ป้องกัน GitHub Pages 404
├── .gitignore
└── problems/
    └── problem-N/                            <-- โฟลเดอร์โจทย์ข้อที่ N
        ├── oral_exam_problem.md              <-- ถอดข้อความโจทย์และตารางอุปกรณ์ (Component Matrix)
        ├── image.png                         <-- รูปภาพโจทย์ต้นฉบับ
        ├── circuit_fig1.png                  <-- รูปภาพแผนภาพวงจรไฟฟ้า
        ├── data303212qz02.md                 <-- ชุดข้อมูลตัวเลขวัดจริง (ถ้ามี)
        ├── OFFICIAL_SOLUTION_ANALYSIS.md     <-- บทวิเคราะห์เฉลยลายมืออาจารย์
        ├── PROBLEM_EVALUATION_AND_KNOWLEDGE_MAP.md <-- แผนผังความรู้และสโคปวิชา
        ├── PROMPT_FOR_CLAUDE_OPUS.md         <-- Master Prompt สำหรับส่งให้ AI คำนวณขยายผล
        ├── reference/                        <-- ลายมือเฉลยอาจารย์ (PDF) และเอกสารอ้างอิง
        └── solution3/                        <-- ชุดเฉลยและสื่อการสอนฉบับสมบูรณ์
            ├── CLAUDE_SOLUTION.md            <-- บทเรียนและเฉลยละเอียดละออ 5 บท
            ├── README.md                     <-- สารบัญประจำข้อ
            ├── solve_circuit.py              <-- สคริปต์คำนวณและฟิตพารามิเตอร์ (Python)
            ├── solve_circuit.m               <-- สคริปต์คำนวณ (MATLAB)
            └── interactive_dashboard.html   <-- สื่อการสอนแบบโต้ตอบ HTML (Master Dashboard)
```

---

## 📋 ขั้นตอนการทำงานมาตรฐาน (Standard Workflow Step-by-Step)

### ขั้นตอนที่ 1: วิเคราะห์โจทย์และสร้างแผนผังความรู้ (Domain Analysis)
1. อ่านและถอดข้อความโจทย์ลงใน `problems/problem-N/oral_exam_problem.md`
2. สร้างตาราง **Component Matrix** จำแนกอุปกรณ์ อักขระ สัญลักษณ์ ทิศทางกระแส และขั้วแรงดัน
3. สร้าง `PROBLEM_EVALUATION_AND_KNOWLEDGE_MAP.md` จำแนกหัวข้อ Circuit 2 (เช่น KCL/KVL, Dependent Sources, Transient, AC, Laplace, Parameter Identification)
4. สร้าง `OFFICIAL_SOLUTION_ANALYSIS.md` หากมีเฉลยลายมืออาจารย์ผู้สอน

### ขั้นตอนที่ 2: ร่างบทเรียนและเฉลยละเอียด (CLAUDE_SOLUTION.md)
ต้องประกอบด้วย 5 บทหลักเสมอ:
- **บทที่ 1: เห็นภาพกายภาพก่อนสูตร (Physical Intuition)** — อุปมาอุปไมยท่อน้ำ แรงดัน ประจุ
- **บทที่ 2: แกะโจทย์และพิสูจน์วงจรทีละบรรทัด (Circuit Proofs)** — KCL/KVL อินทิเกรต ไม่ข้ามรอยต่อ
- **บทที่ 3: วิธีคิดคำนวณด้วยมือ (Hand Derivation)** — ช่วงเชิงเส้น $y=mx+c$ ตัวเลขทศนิยมจริง
- **บทที่ 4: วิธีคิดด้วยคอมพิวเตอร์ (Optimization & Identifiability)** — เปรียบเทียบ Hand vs Computer และวิเคราะห์ Structural Non-identifiability
- **บทที่ 5: คัมภีร์ซ้อมตอบสอบปากเปล่า (Oral Defense Masterclass)** — เก็ง 10-15 ข้อพร้อมบทพูดซ้อมจริง (Defensive vs Distinction Script)

### ขั้นตอนที่ 3: สร้างสื่อการสอนแบบโต้ตอบ (interactive_dashboard.html)
สร้างไฟล์ Single-file HTML/CSS/JS (Modern Dark Mode + Glassmorphism UI) โดยมีองค์ประกอบบังคับ:
1. **ปุ่มถอยหลังกลับหน้าหลัก (Fixed Top-Left Back Button):**
   ```html
   <a href="../../../index.html" class="top-back-btn" title="กลับหน้าหลัก (Main Portal Hub)" aria-label="กลับหน้าหลัก">←</a>
   ```
   ```css
   .top-back-btn { position: fixed; top: 14px; left: 14px; z-index: 9999; width: 38px; height: 38px; border-radius: 50%; background: var(--panel-solid); border: 1.5px solid var(--line-strong); color: var(--ink); display: inline-flex; align-items: center; justify-content: center; text-decoration: none; font-size: 1.2rem; font-weight: 800; box-shadow: 0 6px 20px rgba(0,0,0,0.35); backdrop-filter: blur(14px); }
   ```
2. **ปุ่มลอยเปิดรูปโจทย์ (Fixed Bottom-Left Floating Icon):**
   ```html
   <button id="stickyProblemBtn" aria-label="เปิดดูรูปภาพโจทย์" title="เปิดดูรูปภาพโจทย์ (image.png)"><span class="arrow-icon">📐</span></button>
   ```
   ```css
   #stickyProblemBtn { position: fixed; bottom: 24px; left: 24px; z-index: 9999; display: inline-flex; width: 38px; height: 38px; border-radius: 50%; background: var(--panel-solid); border: 1.5px solid var(--accent); color: var(--accent); align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 6px 20px rgba(0,0,0,0.35); backdrop-filter: blur(14px); }
   ```
3. **ระบบเลื่อนแท็บสำหรับ Mobile User (Direct Tab-Switching Arrows):**
   - ปุ่มลูกศร `◀` (ซ้าย) และ `▶` (ขวา) ตรง `.tabbar`
   - เมื่อกดลูกศร จะทำการ **สลับไปยังแท็บถัดไป/ก่อนหน้าทันที** และเลื่อนแท็บให้อยู่ตรงกลาง
   - **ซ่อนปุ่มซ้ายสุดเมื่ออยู่แท็บแรก (idx = 0)** และ **ซ่อนปุ่มขวาสุดเมื่ออยู่แท็บสุดท้าย**
4. **โครงสร้างแท็บเนื้อหา 6 แท็บ:**
   - แท็บ 1: โจทย์จริง & วงจร
   - แท็บ 2: ปูพื้นฐานจาก 0
   - แท็บ 3: พิสูจน์ KCL & KVL
   - แท็บ 4: ลายมืออาจารย์ vs คอมพิวเตอร์
   - แท็บ 5: คัมภีร์สอบปากเปล่า
   - แท็บ 6: Simulation Lab & Parameter Studio

### ขั้นตอนที่ 4: อัปเดตหน้าหลักและสารบัญ (Master Portal Auto Sync)
1. อัปเดตไฟล์ `index.html` ที่ Root Directory ให้การ์ดโจทย์ข้อที่ N ปักป้าย `✅ พร้อมใช้งาน`
2. ใส่ปุ่มกดหลักเพียงปุ่มเดียว:
   ```html
   <a href="problems/problem-N/solution3/interactive_dashboard.html" class="btn btn-primary">
     🚀 เข้าสู่เฉลย &amp; สื่อโต้ตอบ (ข้อที่ N)
   </a>
   ```
3. อัปเดต `README.md` และ Git Commit/Push ขึ้น GitHub Repository
