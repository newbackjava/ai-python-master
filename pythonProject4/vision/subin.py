# calc_ui.py
# Tkinter 예제: 쉬운 로직 + 예쁜 UI (단일 파일)
# 수업 포인트: 이벤트 핸들러 분리, 상태 관리, ttk 스타일, grid 레이아웃
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from decimal import Decimal, InvalidOperation

class Calculator:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("간단 계산기")
        self.master.geometry("320x460")  # 보기 좋은 비율
        self.master.resizable(False, False)

        # ===== 상태 변수 =====
        self.current = ""   # 화면에 입력/표시될 문자열
        self.stored = None  # 앞서 입력된 숫자
        self.op = None      # 선택된 연산자 (+, -, *, /)
        self.just_evaluated = False  # = 실행 직후인지 플래그

        # ===== 스타일 =====
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Display.TLabel", font=("Pretendard", 28), anchor="e", padding=12)
        style.configure("Sub.TLabel", font=("Pretendard", 11), foreground="#666", anchor="e", padding=(12, 0, 12, 8))
        style.configure("Num.TButton", font=("Pretendard", 16), padding=8)
        style.configure("Op.TButton", font=("Pretendard", 16), padding=8)
        style.configure("Wide.TButton", font=("Pretendard", 16), padding=8)

        # ===== 메인 프레임 =====
        root = ttk.Frame(self.master, padding=10)
        root.pack(fill="both", expand=True)

        # ===== 표시부 =====
        self.sub_label = ttk.Label(root, text="", style="Sub.TLabel")
        self.display = ttk.Label(root, text="0", style="Display.TLabel")
        self.sub_label.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.display.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # grid 가중치
        for r in range(2, 10):
            root.rowconfigure(r, weight=1)
        for c in range(4):
            root.columnconfigure(c, weight=1)

        # ===== 버튼 구성 (7-9, 4-6, 1-3, 0, ., C, ⌫, =, +, -, ×, ÷) =====
        # 2행부터 버튼
        btn = self._button  # 단축 참조

        # 제어 줄
        btn(root, "C", 2, 0, self.on_clear, style="Op.TButton")
        btn(root, "⌫", 2, 1, self.on_backspace, style="Op.TButton")
        btn(root, "±", 2, 2, self.on_negate, style="Op.TButton")
        btn(root, "÷", 2, 3, lambda: self.on_op("/"), style="Op.TButton")

        # 숫자 & 연산자
        btn(root, "7", 3, 0, lambda: self.on_digit("7"))
        btn(root, "8", 3, 1, lambda: self.on_digit("8"))
        btn(root, "9", 3, 2, lambda: self.on_digit("9"))
        btn(root, "×", 3, 3, lambda: self.on_op("*"), style="Op.TButton")

        btn(root, "4", 4, 0, lambda: self.on_digit("4"))
        btn(root, "5", 4, 1, lambda: self.on_digit("5"))
        btn(root, "6", 4, 2, lambda: self.on_digit("6"))
        btn(root, "−", 4, 3, lambda: self.on_op("-"), style="Op.TButton")

        btn(root, "1", 5, 0, lambda: self.on_digit("1"))
        btn(root, "2", 5, 1, lambda: self.on_digit("2"))
        btn(root, "3", 5, 2, lambda: self.on_digit("3"))
        btn(root, "+", 5, 3, lambda: self.on_op("+"), style="Op.TButton")

        btn(root, "0", 6, 0, lambda: self.on_digit("0"), colspan=2, style="Wide.TButton")
        btn(root, ".", 6, 2, lambda: self.on_dot())
        btn(root, "=", 6, 3, self.on_equal, style="Op.TButton")

        # ===== 키보드 바인딩 =====
        self.master.bind("<Key>", self.on_key)

        # 초기 표시
        self._render()

    # ---------- UI 헬퍼 ----------
    def _button(self, parent, text, row, col, cmd, colspan=1, style="Num.TButton"):
        b = ttk.Button(parent, text=text, command=cmd, style=style)
        b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=4, pady=4)
        return b

    def _render(self):
        # 보조 줄(저장된 값과 연산자)
        sub = ""
        if self.stored is not None:
            sub = f"{self._fmt(self.stored)} "
            if self.op:
                sub += self._op_symbol(self.op)
        self.sub_label.config(text=sub)

        # 메인 표시
        if self.current in ("", "-", "."):
            self.display.config(text=self.current if self.current else "0")
        else:
            # 1) Decimal로 안전히 변환 2) 정수면 소수점 제거
            try:
                val = Decimal(self.current)
                if val == val.to_integral():
                    self.display.config(text=str(val.quantize(Decimal("1"))))
                else:
                    # 불필요한 0 제거
                    self.display.config(text=str(val.normalize()))
            except InvalidOperation:
                self.display.config(text=self.current)

    @staticmethod
    def _fmt(x: Decimal | float | int):
        try:
            d = Decimal(str(x))
            if d == d.to_integral():
                return str(d.quantize(Decimal("1")))
            return str(d.normalize())
        except Exception:
            return str(x)

    @staticmethod
    def _op_symbol(op: str) -> str:
        return {"*": "×", "/": "÷", "+": "+", "-": "−"}.get(op, op)

    # ---------- 동작 ----------
    def on_digit(self, ch: str):
        if self.just_evaluated:
            # = 직후 숫자를 누르면 새 입력 시작
            self.current, self.stored, self.op = "", None, None
            self.just_evaluated = False

        # 0 앞자리 처리
        if self.current == "0":
            self.current = ch
        else:
            self.current += ch
        self._render()

    def on_dot(self):
        if self.just_evaluated:
            self.current, self.stored, self.op = "", None, None
            self.just_evaluated = False

        if "." not in self.current:
            self.current = self.current or "0"
            self.current += "."
            self._render()

    def on_op(self, op: str):
        # 현재 입력이 있으면 반영
        if self.current not in ("", "-", "."):
            try:
                val = Decimal(self.current)
            except InvalidOperation:
                val = Decimal(0)
            if self.stored is None:
                self.stored = val
            else:
                # 기존 연산을 먼저 평가
                self.stored = self._calc(self.stored, val, self.op)
            self.current = ""

        self.op = op
        self.just_evaluated = False
        self._render()

    def on_equal(self):
        if self.op and self.current not in ("", "-", "."):
            try:
                right = Decimal(self.current)
                self.stored = self._calc(Decimal(self.stored if self.stored is not None else 0), right, self.op)
                self.current = self._fmt(self.stored)
            except ZeroDivisionError:
                self.current = "오류(0으로 나눔)"
                self.stored = None
            except Exception:
                self.current = "오류"
                self.stored = None
            self.op = None
            self.just_evaluated = True
            self._render()

    def on_clear(self):
        self.current = ""
        self.stored = None
        self.op = None
        self.just_evaluated = False
        self._render()

    def on_backspace(self):
        if self.just_evaluated:
            # 결과 직후 백스페이스는 현재를 지우고 새 입력 준비
            self.current = ""
            self.just_evaluated = False
        else:
            self.current = self.current[:-1]
        self._render()

    def on_negate(self):
        if self.current.startswith("-"):
            self.current = self.current[1:]
        elif self.current and self.current != "0":
            self.current = "-" + self.current
        else:
            # 0 또는 빈 입력이면 -0 은 의미 없으니 무시
            pass
        self._render()

    def on_key(self, event: tk.Event):
        k = event.keysym
        ch = event.char

        if ch.isdigit():
            self.on_digit(ch)
        elif ch == ".":
            self.on_dot()
        elif ch in "+-*/":
            self.on_op(ch)
        elif k in ("Return", "KP_Enter"):
            self.on_equal()
        elif k == "BackSpace":
            self.on_backspace()
        elif k.upper() == "C":
            self.on_clear()
        # 그 외 키는 무시

    @staticmethod
    def _calc(left: Decimal, right: Decimal, op: str) -> Decimal:
        if op == "+":
            return left + right
        if op == "-":
            return left - right
        if op == "*":
            return left * right
        if op == "/":
            if right == 0:
                raise ZeroDivisionError
            return left / right
        return right

def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
