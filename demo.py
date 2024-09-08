from manim import *

class P23200010200___(Scene):
       def construct(self):
              question_text = Text("我们只需要寻找一个组合,使得刚刚翻译的三个命题均为真", font_size=36).move_to(UP*1.7)
              self.play(Write(question_text), run_time=6)
              # 清屏并逐渐淡出
              self.wait(2)
              
              formula1 = MathTex(
              r"\bigcap_{i=1}^{9}\bigcap_{n=1}^{9}\bigcup_{j=1}^{9} P(i,j,n)"
              ).scale(0.8).move_to(ORIGIN + UP*0.2)
              self.play(Write(formula1))

              formula2 = MathTex(
              r"\bigcap_{j=1}^{9}\bigcap_{n=1}^{9}\bigcup_{i=1}^{9} P(i,j,n)"
              ).scale(0.8).move_to(ORIGIN + DOWN * 1.2)
              self.play(Write(formula2))

              formula3 = MathTex(
              r"\bigcap_{r=0}^{2}\bigcap_{s=0}^{2}\bigcap_{n=1}^{9}\bigcup_{i=1}^{3}\bigcup_{j=1}^{3} P(3r+i,3s+j,n)"
              ).scale(0.8).move_to(ORIGIN + DOWN*2.56)
              self.play(Write(formula3))
              
              self.wait(10)
              self.play(FadeOut(formula1,formula2,formula3))
              
              self.play(FadeOut(question_text), run_time=2)
              self.wait(2)
