import gradio as gr
from teacher_op import add_teacher, update_teacher

titles = ["博士后", "助教", "讲师", "副教授", "特任教授", "教授", "助理研究员", "特任副研究员", "副研究员", "特任研究员", "研究员"]

with gr.Blocks() as demo:
    gr.Markdown("<center><h1>教师信息管理系统</h1></center>")
    t_title = gr.Dropdown(titles, label="职称：")
    bt = gr.Button(value="查询")
    bt.click(fn=None, inputs=None, outputs=t_title, api_name="greet")

demo.launch()