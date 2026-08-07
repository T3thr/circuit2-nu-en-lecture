# Master Prompt: สั่งการ Claude Opus / GPT-5 (สำหรับโจทย์ข้อที่ 3)

> **วิธีใช้งาน:** คัดลอกข้อความในกรอบด้านล่างทั้งหมด ไปวางในช่องแชตของ Claude Opus หรือ Claude 3.7 Sonnet เพื่อประมวลผลและสร้างเอกสารเฉลยละเอียดสำหรับ **โจทย์ข้อที่ 3** ตามมาตรฐาน **Skill `circuit2-oral-exam-generator`**

---

```markdown
Role & Master Mission:
คุณคือ "อาจารย์มนุษย์ผู้คลั่งไคล้การสอนวิศวกรรมไฟฟ้า" (Master Human EE Educator)
โปรดปฏิบัติตามมาตรฐานการสอนใน Skill `circuit2-oral-exam-generator` (ในไฟล์ .agents/skills/circuit2-oral-exam-generator/SKILL.md) อย่างเคร่งครัด!

ภารกิจของคุณคือ: "สร้างชุดเฉลยและสื่อการสอนใน problems/problem-3/solution3/ สำหรับโจทย์วงข่ายความนำไฟฟ้าและสมการชุดตัด (Cut-set Equations) สอนนิสิตไร้พื้นฐานให้เข้าใจลึกซึ้ง ไร้จุดสะดุด เรียงลำดับความคิดอย่างร้อยเรียงสมบูรณ์แบบ จนสามารถตอบคำถามกรรมการสอบปากเปล่าได้คะแนนเต็ม 100/100!"

---

🎯 สิ่งที่ต้องสร้างใน CLAUDE_SOLUTION.md ( Seamless Deepening ):

1. Zero Mathematical Gaps (พิสูจน์คณิตศาสตร์แบบไม่ละบรรทัด):
   - ห้ามใช้คำว่า "ในทำนองเดียวกัน" หรือข้ามขั้นตอนย้ายข้างสมการเด็ดขาด!
   - พิสูจน์หาแรงดันปม $V_a = E_1$, $V_d = -E_2$, Supernode $(b,c)$ $V_c - V_b = E_3$
   - พิสูจน์ KCL ที่ Supernode $(b,c)$:
     $G_1(V_b - E_1) + G_3 V_b + G_2(V_b + E_3 - (-E_2)) = 0$
     แสดงการดึงตัวร่วมและย้ายข้างสมการอย่างละเอียดจนได้:
     $V_b = \frac{G_1 E_1 - G_2 E_2 - G_2 E_3}{G_1 + G_2 + G_3}$
     $V_c = \frac{G_1 E_1 - G_2 E_2 + (G_1 + G_3) E_3}{G_1 + G_2 + G_3}$
   - พิสูจน์ทฤษฎีกราฟและการสร้าง Fundamental Cut-set Matrix $[Q_f]$ ขนาด $4 \times 7$ และเขียนสมการเมทริกซ์เวกเตอร์ $[Q_f][Y_b][Q_f]^T [V_n] = [J_{eq}]$ อย่างสมบูรณ์แบบ

2. Physical & Topological Bridge (เชื่อมโยงฟิสิกส์และทฤษฎีกราฟ):
   - อธิบายมโนทัศน์ความนำไฟฟ้า $G$ (Conductance) เปรียบเทียบกับความกว้างท่อน้ำ
   - อธิบายแนวคิด Cut-set (ชุดตัด) ด้วยภาพการตัดกิ่งวงจรเพื่อแยกกราฟออกเป็น 2 ส่วน

3. Ultimate Oral Defense Masterclass (ขยายบทซ้อมตอบเป็น 15 ข้อ):
   - เก็งคำถามสอบปากเปล่า 15 ข้อ พร้อมบทพูดซ้อมจริง 2 ระดับ:
     [1] Defensive Script: บทตอบรอดชีวิต ไม่ตกกับดักเรื่องขั้วของ $E_2$ ที่ติดลบ
     [2] Proactive Distinction Script: บทตอบเกียรตินิยม แสดงความเข้าใจทฤษฎีกราฟระดับสูง

---

💻 สิ่งที่ต้องสร้างใน interactive_dashboard.html ( Masterpiece Enhancement ):

1. UI & Interaction Standard:
   - ติดตั้งปุ่มถอยหลังกลับหน้าหลักมุมบนซ้าย (`top: 14px; left: 14px;`) ลิงก์ `../../../index.html`
   - ติดตั้งปุ่มเปิดรูปภาพโจทย์มุมซ้ายล่าง (`bottom: 24px; left: 24px;`) แสดงผลทุกแท็บ
   - ปุ่มเลื่อนแท็บ `◀` / `▶` สลับแท็บทันที ซ่อนเมื่อสุดขอบ

2. Interactive Matrix & Voltage Studio (ในแท็บ Simulation Lab):
   - Slider ปรับค่า $E_1, E_2, E_3, G_1, G_2, G_3, G_4$ แบบ Real-time
   - คำนวณค่า $V_a, V_b, V_c, V_d$ และแสดงเมทริกซ์ $[Q_f]$ เปลี่ยนแปลงสดบนหน้าจอ!

---

จงดำเนินการสร้าง/ปรับปรุงไฟล์ทั้งหมดใน problems/problem-3/solution3/ (ทั้ง CLAUDE_SOLUTION.md, interactive_dashboard.html, README.md, solve_circuit.py) ให้เป็นเวอร์ชันสมบูรณ์แบบที่สุดตามมาตรฐาน Skill `circuit2-oral-exam-generator`!
```
