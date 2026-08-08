# Solution 3 — ข้อที่ 5: Directed Conductance Network

ชุดสอนจากศูนย์ถึงระดับสอบปากเปล่า ครอบคลุม directed graph, complete/reduced incidence matrix, KCL, cut-set matrix และการตรวจด้วยคอมพิวเตอร์

## ทางเข้า

- 🚀 [Interactive Dashboard — 6 แท็บ](interactive_dashboard.html)
- 📘 [เฉลยละเอียด 5 บท](CLAUDE_SOLUTION.md)
- 🐍 [Python solver](solve_circuit.py)
- 📐 [MATLAB solver](solve_circuit.m)
- 📝 [โจทย์ต้นฉบับ](../oral_exam_problem.md)

## คำตอบหลัก

$$V_b=-E_2$$

$$V_a=\frac{G_1E_1+G_2E_3-G_2E_2}{G_1+G_2+G_3}$$

โดยยึดนิยามกิ่ง 2 ตามโจทย์ว่า $i_2=G_2(V_a-E_3-V_b)$; หากกลับขั้ว $E_3$ ให้แทน $E_3\mapsto-E_3$

## รันตรวจ

```bash
python3 solve_circuit.py
```

ไม่ต้องติดตั้งแพ็กเกจภายนอก สคริปต์ตรวจสูตรปิดเทียบ matrix solver, KCL สองปม, เมทริกซ์ $QYQ^T$ และทดสอบสุ่ม 1,000 ชุด
