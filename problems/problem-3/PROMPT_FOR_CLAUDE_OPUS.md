# Master Prompt: สั่งการ Claude Opus / GPT-5 สำหรับโจทย์ข้อที่ 3

> **วิธีใช้งาน:** คัดลอกข้อความในกรอบด้านล่างทั้งหมด ไปวางในช่องแชตของ Claude Opus หรือ Claude 3.7 Sonnet เพื่อให้ AI สร้างและคำนวณชุดเฉลย `problems/problem-3/solution3/` ตามมาตรฐาน **Skill `circuit2-oral-exam-generator`** ได้ผลลัพธ์ละเอียด ลึกซึ้ง ไร้รอยต่อ 100%

---

```markdown
Role & Master Mission:
คุณคือ "อาจารย์มนุษย์ผู้คลั่งไคล้การสอนวิศวกรรมไฟฟ้า" (Master Human EE Educator)
โปรดปฏิบัติตามมาตรฐานการสอนใน Skill `circuit2-oral-exam-generator` (ในไฟล์ .agents/skills/circuit2-oral-exam-generator/SKILL.md) อย่างเคร่งครัด!

ภารกิจของคุณคือ: "ศึกษาข้อล้มเหลวของการเฉลยที่ตื้นเกินไปในอดีตซึ่งทำให้นิสิตสอบปากเปล่าได้ 0 คะแนน แล้วสร้างชุดเฉลยและสื่อการสอนใหม่ใน problems/problem-3/solution3/ ที่สอนนิสิตไร้พื้นฐานให้เข้าใจลึกซึ้ง ไร้จุดสะดุด เรียงลำดับความคิดอย่างร้อยเรียงสมบูรณ์แบบ จนสามารถตอบคำถามกรรมการสอบปากเปล่าเรื่อง 'วงข่ายความนำไฟฟ้าและสมการชุดตัด (Conductance Network & Fundamental Cut-Set Matrix)' ได้คะแนนเต็ม 100/100!"

---

Input Context & Reference Files (ไฟล์อ้างอิงของข้อที่ 3):
1. ไฟล์โจทย์ต้นฉบับ: ../oral_exam_problem.md, ../image.png และ ../circuit_fig3.png
2. องค์ประกอบวงจร:
   - ความนำไฟฟ้า: $G_1, G_2, G_3, G_4 [\mho]$
   - แหล่งกำเนิดแรงดันอิสระ: $E_1, E_2, E_3 [\text{V}]$
   - ปมไฟฟ้า: ปม $a, b, c, d$ และปมอ้างอิง $e$ ($V_e = 0\text{ V}$)

---

Detailed Deliverables Required (สิ่งที่ต้องสร้างใน problems/problem-3/solution3/):

1. CLAUDE_SOLUTION.md (เอกสารเฉลยและบทเรียนฉบับสอนจนบรรลุ)
ต้องเรียงลำดับหัวข้อการสอนอย่างมีจังหวะและภาษาธรรมชาติมนุษย์ 5 บทหลัก:

 บทที่ 1: เห็นภาพกายภาพก่อนสูตร (Physical Intuition & Zero-to-Hero Analogies)
   - ปูเรื่องความนำไฟฟ้า (Conductance $G = 1/R$ หน่วย Siemens/Mho $\mho$) เปรียบเทียบกับ "ความกว้างของท่อน้ำ" (ท่อใหญ่ = น้ำไหลสะดวก = Conductance สูง)
   - อธิบายมโนทัศน์ของปม (Node), ปมอ้างอิง (Reference Ground $e$), แรงดันดึงดูด/ผลักของแหล่งกำเนิดแรงดัน $E_1, E_2, E_3$
   - ปูมโนทัศน์ของ "ชุดตัด (Cut-Set)" และ "Supernode" เปรียบเทียบกับการขีดเส้นล้อมรอบพื้นที่ทางกายภาพ แล้วนับกระแสเข้าเท่ากับกระแสออก

 บทที่ 2: แกะโจทย์และพิสูจน์วงจรทีละบรรทัด (Step-by-Step Circuit Proof & Cut-Set Matrix)
   - Zero Mathematical Gaps: แสดงการตั้งสมการ KCL และ KVL ละเอียดยิบทุกบรรทัด ห้ามข้ามขั้นตอน!
   - พิสูจน์แรงดันปมตรงกำหนด: $V_a = E_1$ และ $V_d = -E_2$ (แสดงขั้ว $+$ / $-$ ชัดเจน)
   - พิสูจน์สมการ Supernode ระหว่างปม $b$ และ $c$ ผ่านแหล่งกำเนิด $E_3$: $V_c - V_b = E_3 \implies V_c = V_b + E_3$
   - สร้างสมการชุดตัดหลัก (Fundamental Cut-Set KCL Equation) สำหรับ Supernode $(b, c)$:
     $$G_1(V_b - V_a) + G_3 V_b + G_2(V_c - V_d) = 0$$
   - ย้ายข้างสมการอย่างเป็นระบบ แสดงการแทนค่า $V_a = E_1, V_d = -E_2, V_c = V_b + E_3$ บรรทัดต่อบรรทัด จนได้คำตอบแรงดันปม $V_b, V_c$ ในรูปตัวแปร $G_1, G_2, G_3, G_4, E_1, E_2, E_3$

 บทที่ 3: การตั้งและแก้ไขสมการในรูปแบบเมทริกซ์เวกเตอร์ (Matrix-Vector Formulation)
   - แสดงการจัดรูปสมการลงในเมทริกซ์ความนำไฟฟ้า (Conductance Matrix Vector Form):
     $$\mathbf{G} \cdot \mathbf{V} = \mathbf{I}$$
   - พิสูจน์การหาเมทริกซ์ผกผัน (Inverse Matrix) และ Determinant แบบเขียนแสดงทีละขั้นตอน
   - สุ่มแทนตัวเลขจริง (เช่น $G_1=2, G_2=1, G_3=3, G_4=4\ \mho, E_1=10, E_2=5, E_3=12\ \text{V}$) และคำนวณตัวเลขเป๊ะๆ ทุกทศนิยมให้เห็นกับตา

 บทที่ 4: การคำนวณด้วยคอมพิวเตอร์และการวิเคราะห์เชิงโครงสร้าง (Computer Optimization & Sensitivity)
   - สคริปต์ Python (`solve_circuit.py`) คำนวณหาค่า $V_a, V_b, V_c, V_d$ ด้วย SymPy และ NumPy
   - อธิบายการวิเคราะห์ความไว (Sensitivity Analysis): ผลกระทบเมื่อค่า $G_1$ หรือ $E_3$ เปลี่ยนแปลงไปต่อแรงดันที่ปมต่างๆ

 บทที่ 5: คัมภีร์ซ้อมตอบสอบปากเปล่าคะแนนเต็ม 100/100 (Master Oral Defense Guide - 15 ข้อ)
   - เก็งคำถามสอบปากเปล่าเด็ดอาจารย์ 15 ข้อ พร้อมบทพูดซ้อมจริงของนิสิต
   - แต่ละข้อแบ่งการตอบเป็น 2 ระดับ:
     [1] บทตอบรอดชีวิต (Defensive Script): ตอบตรงประเด็น ไม่ตกกับดัก (ได้คะแนนผ่าน)
     [2] บทตอบเกียรตินิยม (Proactive Distinction Script): ตอบขยายความทฤษฎี Graph Theory, Incidence Matrix, และ Cut-Set Matrix เพื่อเอา 100/100

---

2. interactivedashboard.html (สื่อการสอนแบบโต้ตอบระดับ Masterpiece)
   - Responsive Single-file HTML/CSS/JS (Modern Dark Mode + Glassmorphism UI)
   - ปุ่มย้อนกลับมุมบนซ้าย (`top: 14px; left: 14px;`) ลิงก์ `../../../index.html`
   - ปุ่มลอยเปิดรูปโจทย์มุมซ้ายล่าง (`bottom: 24px; left: 24px;`) แสดงผลทุกแท็บ
   - ปุ่มเลื่อนแท็บ `◀` / `▶` สลับแท็บทันที ซ่อนเมื่อสุดขอบ
   - 6 แท็บบทเรียน:
     1. โจทย์จริง & วงจร
     2. ปูพื้นฐานจาก 0 (ภาพท่อน้ำ & Conductance)
     3. พิสูจน์ KCL, KVL & Supernode
     4. สมการเมทริกซ์ชุดตัด (Matrix Solver)
     5. คัมภีร์ซ้อมตอบสอบปากเปล่า (15 ข้อ 100/100)
     6. Simulation Lab & Interactive Node Calculator

---

3. solve_circuit.py, solve_circuit.m และ README.md
   - สร้างสคริปต์คำนวณและอัปเดตสารบัญใน problems/problem-3/solution3/

---

จงใช้ทักษะของอาจารย์มหาวิทยาลัยที่เป็นมนุษย์ ถ่ายทอดด้วยภาษาไทยที่สละสลวย อุ่นนุ่ม ลึกซึ้ง และเป็นระบบขั้นสุด ตามมาตรฐาน Skill `circuit2-oral-exam-generator` เพื่อให้เฉลยข้อที่ 3 สมบูรณ์แบบและได้ 100/100!
```
