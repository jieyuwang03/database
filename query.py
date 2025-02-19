import pymysql
from Config import config

sexes = ["男", "女"]
titles = ["博士后", "助教", "讲师", "副教授", "特任教授", "教授", "助理研究员", "特任副研究员", "副研究员", "特任研究员", "研究员"]
semesters = ["春季学期", "夏季学期", "秋季学期"]
types = ["国家级项目", "省部级项目", "市厅级项目", "企业合作项目", "其它类型项目"]
levels = ["CCF-A", "CCF-B", "CCF-C", "中文 CCF-A", "中文 CCF-B", "无级别"]

def query_statistics(id, start, end):
    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID"
    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        select_sql = f"SELECT * FROM teacher WHERE 工号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchall()
        if not result:
            tid =  f"该教师不存在！"
            tname =  f"该教师不存在！"
            tsex =  f"该教师不存在！"
            ttitle =  f"该教师不存在！"
            classes_md =  f"该教师不存在！"
            papers_md =  f"该教师不存在！"
            projects_md =  f"该教师不存在！"

            reply = f"{tid}\n{tname}\n{tsex}\n{ttitle}\n{classes_md}\n{papers_md}\n{projects_md}"
            
            with open('query_result.txt', 'w', encoding = 'utf-8') as f:
                f.write(reply)

            return tid, tname, tsex, ttitle, classes_md, papers_md, projects_md
        else:
            tid = result[0][0]
            tname = result[0][1]
            tsex = sexes[result[0][2]-1]
            ttitle = titles[result[0][3]-1]
            imform = f"{tid} {tname} {tsex} {ttitle}\n"

        # 查询语句，可以根据需要调整，这里以教师名称中包含keyword为例
        query_sql = f"SELECT class.课程号, class.课程名称, tc.承担学时, tc.年份, tc.学期 FROM teacher, tc, class WHERE class.课程号=tc.课程号 AND teacher.工号=tc.教师工号 AND teacher.工号='{id}' AND tc.年份>={start} AND tc.年份<={end}"
        cursor.execute(query_sql)
        classes = cursor.fetchall()
        print(classes)
        classes_md = "课程信息\n"
        for class_info in classes:
            classes_md += f"{class_info[0]} {class_info[1]} {class_info[2]} {class_info[3]} {semesters[class_info[4]-1]}\n"
        print(classes_md)
        
        query_sql = f"SELECT paper.序号, paper.论文名称, paper.发表源, paper.发表年份, paper.级别, tpa.排名, tpa.是否为通讯作者 FROM teacher, tpa, paper WHERE paper.序号=tpa.论文序号 AND teacher.工号=tpa.教师工号 AND teacher.工号='{id}' AND paper.发表年份>={start} AND paper.发表年份<={end}"
        cursor.execute(query_sql)
        papers = cursor.fetchall()
        papers_md = "论文信息\n"
        i = 1
        for paper_info in papers:
            papers_md += f"{i}.{paper_info[0]}: {paper_info[1]}, {paper_info[2]}, {paper_info[3]}, {levels[paper_info[4]-1]}, 排名第{paper_info[5]} {', 通讯作者' if paper_info[6] else ''}\n"
            i += 1
        print(papers_md)

        query_sql = f"SELECT project.项目名称, project.项目来源, project.项目类型, project.开始年份, project.结束年份, project.总经费, tpr.承担经费 FROM teacher, tpr, project WHERE project.项目号=tpr.项目号 AND teacher.工号=tpr.教师工号 AND teacher.工号='{id}' AND project.开始年份>={start} AND project.结束年份<={end}"
        cursor.execute(query_sql)
        projects = cursor.fetchall()
        projects_md = "项目信息\n"
        i = 1
        for project_info in projects:
            projects_md += f"{i}.{project_info[0]}, {project_info[1]}, {types[project_info[2]-1]}, {project_info[3]}-{project_info[4]}, 总经费：{project_info[5]}, 承担经费：{project_info[6]}\n"
            i += 1
        print(projects_md)
        # 关闭连接
        cursor.close()
        connection.close()
        
        # 返回查询结果，这里简单地转换为字符串展示
        reply = f"""{imform}{classes_md}{papers_md} {projects_md}"""

        # 将reply转换成.md文件
        with open('query_result.txt', 'w', encoding = 'utf-8') as f:
            f.write(imform)
            f.write(classes_md)
            f.write(papers_md)
            f.write(projects_md)

        return tid, tname, tsex, ttitle, classes_md, papers_md, projects_md
    except Exception as e:
        return f"查询出错: {str(e)}"
    
if __name__ == '__main__':
    query_statistics("1", "1", "3")
