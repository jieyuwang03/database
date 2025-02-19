import gradio as gr
from teacher_op import query_teacher, add_teacher, update_teacher, delete_teacher
from paper_op import query_paper, add_paper, update_paper, delete_paper
from project_op import query_project, add_project, update_project, delete_project
from class_op import query_class, add_class, update_class, delete_class
from query import query_statistics
from todocx import ToDocx

with gr.Blocks() as demo:
    gr.Markdown("<center><h1>🏫教师信息管理系统🏫</h1></center>")
    with gr.Tab(label="👨‍🏫教师"):
        with gr.Tab(label="查询教师信息"):
            with gr.Column():
                t_id_query = gr.Textbox(label="教师工号查询：")
                btn_query = gr.Button(value="🔍查询")
                btn_query.click(fn=query_teacher, inputs=[t_id_query], 
                                outputs=[gr.Textbox(label="姓名查询"), 
                                         gr.Textbox(label="性别查询"), 
                                         gr.Textbox(label="职称查询")], 
                                         api_name="查询教师信息")

        with gr.Tab(label="添加教师信息"):
            with gr.Column():
                t_id_add = gr.Textbox(label="教师工号：")
                t_name_add = gr.Textbox(label="姓名：")
                t_sex_add = gr.Dropdown(["男", "女"], label="性别：")
                t_title_add = gr.Dropdown(["博士后", "助教", "讲师", "副教授", "特任教授", "教授", "助理研究员", "特任副研究员", "副研究员", "特任研究员", "研究员"], label="职称：")
                btn_add = gr.Button(value="➕添加")
                btn_add.click(fn=add_teacher, inputs=[t_id_add, t_name_add, t_sex_add, t_title_add], 
                              outputs=gr.Textbox(label="添加结果"), api_name="添加教师信息")


        with gr.Tab(label="删除教师信息"):
            t_id_del = gr.Textbox(label="教师工号：")
            btn_del = gr.Button(value="🗑删除")
            btn_del.click(fn=delete_teacher, inputs=[t_id_del], outputs=gr.Textbox(label="Output Box"), api_name="删除教师信息")
        
        with gr.Tab(label="更新教师信息"):
            t_id_update = gr.Textbox(label="教师工号：")
            t_name_update = gr.Textbox(label="更新姓名：")
            t_sex_update = gr.Dropdown(["男", "女"], label="更新性别：")
            t_title_update = gr.Dropdown(["博士后", "助教", "讲师", "副教授", "特任教授", "教授", "助理研究员", "特任副研究员", "副研究员", "特任研究员", "研究员"], label="更新职称：")
            btn_update = gr.Button(value="📬更新")
            test = gr.Textbox(label="更新结果")
            btn_update.click(fn=update_teacher, inputs=[t_id_update, t_name_update, t_sex_update, t_title_update], 
                             outputs=test, api_name="更新教师信息")

    
    with gr.Tab(label="📑论文"):
        with gr.Tab(label="查询论文"):
            with gr.Column():
                pa_id_query_paper = gr.Number(label="论文序号：")
                btn_query = gr.Button(value="🔍查询")
                btn_query.click(fn=query_paper, inputs=[pa_id_query_paper],
                                outputs=[gr.Textbox(label="论文名称"), 
                                         gr.Textbox(label="发表源"), 
                                         gr.Textbox(label="发表年份"), 
                                         gr.Textbox(label="类型"), 
                                         gr.Textbox(label="级别"),
                                         gr.Textbox(label="参与教师")], 
                                         api_name="查询论文")

        with gr.Tab(label="添加论文"):
            with gr.Column():
                id = gr.Number(label="论文序号：")
                with gr.Row():
                    with gr.Column(scale=9):
                        with gr.Row():
                            tid1 = gr.Textbox(label="NO1-教师工号：", scale=9)
                            tid2 = gr.Textbox(label="NO2-教师工号：", scale=9)
                            tid3 = gr.Textbox(label="NO3-教师工号：", scale=9)
                            tid4 = gr.Textbox(label="NO4-教师工号：", scale=9)
                        with gr.Row():
                            tid5 = gr.Textbox(label="NO5-教师工号：", scale=9)
                            tid6 = gr.Textbox(label="NO6-教师工号：", scale=9)
                            tid7 = gr.Textbox(label="NO7-教师工号：", scale=9)
                            tid8 = gr.Textbox(label="NO8-教师工号：", scale=9)
                    
                    comm = gr.Radio(["1", "2", "3", "4", "5", "6", "7", "8"], label="通讯作者排名：", scale=2)
                with gr.Row():
                    name = gr.Textbox(label="论文名称：", scale = 2)
                    sou = gr.Textbox(label="发表源：", scale = 1)
                with gr.Row():
                    year = gr.Number(label="发表年份：")
                    type = gr.Dropdown(["full paper", "short paper", "poster paper", "demo paper"], label="类型：")
                    level = gr.Dropdown(["CCF-A", "CCF-B", "CCF-C", "中文 CCF-A", "中文 CCF-B", "无级别"], label="级别：")
                btn = gr.Button(value="➕添加")
                btn.click(fn=add_paper, inputs=[id, tid1, tid2, tid3, tid4, tid5, tid6, tid7, tid8, comm, name, sou, year, type, level], 
                        outputs=gr.Textbox(label="添加结果"), api_name="添加论文")

        with gr.Tab(label="删除论文"):
            with gr.Column():
                id = gr.Textbox(label="论文序号：")
                btn = gr.Button(value="🗑删除")
                btn.click(fn=delete_paper, inputs=[id], outputs=gr.Textbox(label="删除结果"), api_name="删除论文")

        with gr.Tab(label="更新论文"):
            with gr.Column():
                id = gr.Number(label="论文序号：")
                with gr.Row():
                    with gr.Column(scale=9):
                        with gr.Row():
                            tid1 = gr.Textbox(label="NO1-教师工号：", scale=9)
                            tid2 = gr.Textbox(label="NO2-教师工号：", scale=9)
                            tid3 = gr.Textbox(label="NO3-教师工号：", scale=9)
                            tid4 = gr.Textbox(label="NO4-教师工号：", scale=9)
                        with gr.Row():
                            tid5 = gr.Textbox(label="NO5-教师工号：", scale=9)
                            tid6 = gr.Textbox(label="NO6-教师工号：", scale=9)
                            tid7 = gr.Textbox(label="NO7-教师工号：", scale=9)
                            tid8 = gr.Textbox(label="NO8-教师工号：", scale=9)
                    
                    comm = gr.Radio(["1", "2", "3", "4", "5", "6", "7", "8"], label="更新通讯作者排名：", scale=2)
                with gr.Row():
                    name = gr.Textbox(label="更新论文名称：")
                    sou = gr.Textbox(label="更新发表源：")
                with gr.Row():
                    year = gr.Number(label="更新发表年份：")
                    type = gr.Dropdown(["full paper", "short paper", "poster paper", "demo paper"], label="更新类型：")
                    level = gr.Dropdown(["CCF-A", "CCF-B", "CCF-C", "中文 CCF-A", "中文 CCF-B", "无级别"], label="更新级别：")
                btn = gr.Button(value="📬更新")
                btn.click(fn=update_paper, inputs=[id, tid1, tid2, tid3, tid4, tid5, tid6, tid7, tid8, comm, name, sou, year, type, level], 
                          outputs=gr.Textbox(label="更新结果"), api_name="更新论文")



    with gr.Tab(label="🎢项目"):
        with gr.Tab(label="查询项目"):
            with gr.Column():
                id = gr.Textbox(label="项目号：")
                btn_query = gr.Button(value="🔍查询")
                btn_query.click(fn=query_project, inputs=[id], 
                                outputs=[gr.Textbox(label="项目名称"), 
                                         gr.Textbox(label="项目来源"), 
                                         gr.Textbox(label="项目类型"), 
                                         gr.Textbox(label="总经费"), 
                                         gr.Number(label="起始年份"), 
                                         gr.Number(label="结束年份"),
                                         gr.Textbox(label="参与教师")])
                
        with gr.Tab(label="添加项目"):
            with gr.Column():
                id = gr.Textbox(label="项目号：")
                with gr.Column(scale=9):
                    with gr.Row():
                        pr_id1 = gr.Textbox(label="教师1工号：", scale=9)
                        pr_fu1 = gr.Number(label="承担经费", value=0)
                    with gr.Row():
                        pr_id2 = gr.Textbox(label="教师2工号：", scale=9)
                        pr_fu2 = gr.Number(label="承担经费", value=0)
                    with gr.Row():
                        pr_id3 = gr.Textbox(label="教师3工号：", scale=9)
                        pr_fu3 = gr.Number(label="承担经费", value=0)
                    with gr.Row():
                        pr_id4 = gr.Textbox(label="教师4工号：", scale=9)
                        pr_fu4 = gr.Number(label="承担经费", value=0)
                    with gr.Row():
                        pr_id5 = gr.Textbox(label="教师5工号：", scale=9)
                        pr_fu5 = gr.Number(label="承担经费", value=0)
                with gr.Row():
                    name = gr.Textbox(label="项目名称：")
                    source = gr.Textbox(label="项目来源：")
                with gr.Row():
                    type = gr.Dropdown(["国家级项目", "省部级项目", "市厅级项目", "企业合作项目", "其它类型项目"], label="项目类型：")
                    start = gr.Number(label="开始年份：")
                    end = gr.Number(label="结束年份：")
                
                btn = gr.Button(value="➕添加")
                btn.click(fn=add_project, inputs=[id, pr_id1, pr_id2, pr_id3, pr_id4, pr_id5, pr_fu1, pr_fu2, pr_fu3, pr_fu4, pr_fu5, name, source, type, start, end], 
                          outputs=[gr.Textbox(label="添加结果"), gr.Textbox(label="总经费")])

        with gr.Tab(label="删除项目"):
            id = gr.Textbox(label="项目号：")
            btn = gr.Button(value="🗑删除")
            btn.click(fn=delete_project, inputs=[id], outputs=gr.Textbox(label="删除结果"))

        with gr.Tab(label="更新项目"):
            with gr.Column():
                id = gr.Textbox(label="项目号：")
                with gr.Column(scale=9):
                    with gr.Row():
                        pr_id1 = gr.Textbox(label="教师1工号：", scale=9)
                        pr_fu1 = gr.Number(label="承担经费", value=0)
                    with gr.Row():
                        pr_id2 = gr.Textbox(label="教师2工号：", scale=9)
                        pr_fu2 = gr.Number(label="承担经费", value=0)
                    with gr.Row():
                        pr_id3 = gr.Textbox(label="教师3工号：", scale=9)
                        pr_fu3 = gr.Number(label="承担经费", value=0)
                    with gr.Row():
                        pr_id4 = gr.Textbox(label="教师4工号：", scale=9)
                        pr_fu4 = gr.Number(label="承担经费", value=0)
                    with gr.Row():
                        pr_id5 = gr.Textbox(label="教师5工号：", scale=9)
                        pr_fu5 = gr.Number(label="承担经费", value=0)
                name = gr.Textbox(label="更新项目名称：")
                source = gr.Textbox(label="更新项目来源：")
                type = gr.Dropdown(["国家级项目", "省部级项目", "市厅级项目", "企业合作项目", "其它类型项目"], label="更新项目类型：")
                with gr.Row():
                    start = gr.Number(label="更新开始年份：")
                    end = gr.Number(label="更新结束年份：")
                
                btn = gr.Button(value="📬更新")
                btn.click(fn=update_project, inputs=[id, pr_id1, pr_id2, pr_id3, pr_id4, pr_id5, pr_fu1, pr_fu2, pr_fu3, pr_fu4, pr_fu5, name, source, type, start, end], 
                          outputs=[gr.Textbox(label="更新结果"), gr.Textbox(label="总经费")])



    with gr.Tab(label="🏫课程"):
        with gr.Tab(label="查询课程"):
            with gr.Column():
                id = gr.Textbox(label="课程号：")
                btn = gr.Button(value="🔍查询")
                btn.click(fn=query_class, inputs=[id], 
                          outputs=[gr.Textbox(label="课程名称"), 
                                   gr.Textbox(label="学时数"), 
                                   gr.Textbox(label="课程性质"),
                                   gr.Textbox(label="参与教师")], api_name="查询课程")

        with gr.Tab(label="添加课程"):
            with gr.Column():
                id = gr.Textbox(label="课程号：")
                with gr.Column(scale=9):
                    with gr.Row():
                        t_id1 = gr.Textbox(label="教师1工号：", scale=9)
                        t_y1 = gr.Number(label="教学年份", value=0)
                        t_s1 = gr.Dropdown(["春季学期", "夏季学期", "秋季学期"], value="春季学期", label="学期")
                        t_h1 = gr.Number(label="承担学时", value=0)
                    with gr.Row():
                        t_id2 = gr.Textbox(label="教师2工号：", scale=9)
                        t_y2 = gr.Number(label="教学年份", value=0)
                        t_s2 = gr.Dropdown(["春季学期", "夏季学期", "秋季学期"], value="春季学期", label="学期")
                        t_h2 = gr.Number(label="承担学时", value=0)
                    with gr.Row():
                        t_id3 = gr.Textbox(label="教师3工号：", scale=9)
                        t_y3 = gr.Number(label="教学年份", value=0)
                        t_s3 = gr.Dropdown(["春季学期", "夏季学期", "秋季学期"], value="春季学期", label="学期")
                        t_h3 = gr.Number(label="承担学时", value=0)
                    with gr.Row():
                        t_id4 = gr.Textbox(label="教师4工号：", scale=9)
                        t_y4 = gr.Number(label="教学年份", value=0)
                        t_s4 = gr.Dropdown(["春季学期", "夏季学期", "秋季学期"], value="春季学期", label="学期")
                        t_h4 = gr.Number(label="承担学时", value=0)
                    with gr.Row():
                        t_id5 = gr.Textbox(label="教师5工号：", scale=9)
                        t_y5 = gr.Number(label="教学年份", value=0)
                        t_s5 = gr.Dropdown(["春季学期", "夏季学期", "秋季学期"], value="春季学期", label="学期")
                        t_h5 = gr.Number(label="承担学时", value=0)

                name = gr.Textbox(label="课程名称：")
                hour = gr.Number(label="学时数：")
                nature = gr.Dropdown(["本科生课程", "研究生课程"], label="课程性质：")
                btn = gr.Button(value="➕添加")
                btn.click(fn=add_class, inputs=[id, t_id1, t_id2, t_id3, t_id4, t_id5, t_y1, t_y2, t_y3, t_y4, t_y5, t_s1, t_s2, t_s3, t_s4, t_s5, t_h1, t_h2, t_h3, t_h4, t_h5, name, hour, nature], 
                          outputs=gr.Textbox(label="添加结果"), api_name="添加课程")

        with gr.Tab(label="删除课程"):
            id = gr.Textbox(label="课程号：")
            btn = gr.Button(value="🗑删除")
            btn.click(fn=delete_class, inputs=[id], 
                      outputs=gr.Textbox(label="删除结果"), api_name="删除课程")

        with gr.Tab(label="更新课程"):
            with gr.Column():
                id = gr.Textbox(label="课程号：")
                with gr.Column(scale=9):
                    with gr.Row():
                        t_id1 = gr.Textbox(label="教师1工号：", scale=9)
                        t_y1 = gr.Number(label="教学年份", value=0)
                        t_s1 = gr.Dropdown(["春季学期", "夏季学期", "秋季学期"], value="春季学期", label="学期")
                        t_h1 = gr.Number(label="承担学时", value=0)
                    with gr.Row():
                        t_id2 = gr.Textbox(label="教师2工号：", scale=9)
                        t_y2 = gr.Number(label="教学年份", value=0)
                        t_s2 = gr.Dropdown(["春季学期", "夏季学期", "秋季学期"], value="春季学期", label="学期")
                        t_h2 = gr.Number(label="承担学时", value=0)
                    with gr.Row():
                        t_id3 = gr.Textbox(label="教师3工号：", scale=9)
                        t_y3 = gr.Number(label="教学年份", value=0)
                        t_s3 = gr.Dropdown(["春季学期", "夏季学期", "秋季学期"], value="春季学期", label="学期")
                        t_h3 = gr.Number(label="承担学时", value=0)
                    with gr.Row():
                        t_id4 = gr.Textbox(label="教师4工号：", scale=9)
                        t_y4 = gr.Number(label="教学年份", value=0)
                        t_s4 = gr.Dropdown(["春季学期", "夏季学期", "秋季学期"], value="春季学期", label="学期")
                        t_h4 = gr.Number(label="承担学时", value=0)
                    with gr.Row():
                        t_id5 = gr.Textbox(label="教师5工号：", scale=9)
                        t_y5 = gr.Number(label="教学年份", value=0)
                        t_s5 = gr.Dropdown(["春季学期", "夏季学期", "秋季学期"], value="春季学期", label="学期")
                        t_h5 = gr.Number(label="承担学时", value=0)

                name = gr.Textbox(label="更新课程名称：")
                hour = gr.Number(label="更新学时数：")
                nature = gr.Dropdown(["本科生课程", "研究生课程"], label="更新课程性质：")
                btn = gr.Button(value="📬更新")
                btn.click(fn=update_class, inputs=[id, t_id1, t_id2, t_id3, t_id4, t_id5, t_y1, t_y2, t_y3, t_y4, t_y5, t_s1, t_s2, t_s3, t_s4, t_s5, t_h1, t_h2, t_h3, t_h4, t_h5, name, hour, nature], 
                          outputs=gr.Textbox(label="更新结果"), api_name="更新课程")

    
    with gr.Tab(label="查询统计"):
        with gr.Column():
            with gr.Row():
                id = gr.Textbox(label="教师工号：")
                start = gr.Number(label="起始年份：")
                end = gr.Number(label="结束年份：")
            with gr.Row():
                btn = gr.Button(value="🔍查询")
                btn2 = gr.Button(value="🌅导出")
            gr.Markdown("教师基本信息")
            with gr.Row():
                id_a = gr.Textbox(label="工号：")
                name_a = gr.Textbox(label="姓名：")
                sex_a = gr.Textbox(label="性别：")
                title_a = gr.Textbox(label="职称：")
            btn.click(fn=query_statistics, inputs=[id, start, end], 
                      outputs=[id_a, name_a, sex_a, title_a, gr.Textbox(label="教学情况"), gr.Textbox(label="发表论文情况"), gr.Textbox(label="项目承担情况")], api_name="查询统计")
            btn2.click(fn=ToDocx, inputs=[start, end], api_name="导出PDF")
    
demo.launch()


