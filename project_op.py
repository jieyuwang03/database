import pymysql
from Config import config

types = ["国家级项目", "省部级项目", "市厅级项目", "企业合作项目", "其它类型项目"]

def query_project(id):
    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        if "'" in id or '"' in id or "--" in id:
            return "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID"

        # 查询教师信息
        select_sql = f"SELECT * FROM project WHERE 项目号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchall()
        if not result:
            reply1 = "项目号 not exists"
            reply2 = "项目号 not exists"
            reply3 = "项目号 not exists"
            reply4 = "项目号 not exists"
            reply5 = "项目号 not exists"
            reply6 = "项目号 not exists"
        else:
            reply1 = result[0][1]
            reply2 = result[0][2]
            reply3 = types[result[0][3] - 1]
            reply4 = result[0][4]
            reply5 = result[0][5]
            reply6 = result[0][6]
        select_sql = f"SELECT 教师工号, 排名, 承担经费 FROM tpr WHERE 项目号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchall()
        reply7 = ""
        for item in result:
            reply7 += f"排名：{item[1]}， 教师工号：{item[0]}， 承担经费：{item[2]}\n"

        return reply1, reply2, reply3, reply4, reply5, reply6, reply7
    except Exception as e:
        return f"添加出错: {str(e)}"


def add_project(id, pr_id1, pr_id2, pr_id3, pr_id4, pr_id5, pr_fu1, pr_fu2, pr_fu3, pr_fu4, pr_fu5, name, source, type, start, end):

    total_funding = pr_fu1 + pr_fu2 + pr_fu3 + pr_fu4 + pr_fu5
    type = str(types.index(type) + 1)
    pr_id = [pr_id1, pr_id2, pr_id3, pr_id4, pr_id5]  
    pr_fu = [pr_fu1, pr_fu2, pr_fu3, pr_fu4, pr_fu5]
    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID", "ERROR"
    if start > end:
        return "开始年份大于结束年份！", "ERROR"

    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 插入论文信息
        for i in range(5):
            if pr_id[i]:
                select_sql = f"SELECT * FROM teacher WHERE 工号='{pr_id[i]}'"
                cursor.execute(select_sql)
                result = cursor.fetchone()
                if not result:
                    return f"工号{pr_id[i]}不存在！"

        select_sql = f"SELECT * FROM project WHERE 项目号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if result:
            reply1 =  "项目号 already exists"
            reply2 = "项目号 already exists"
            return reply1, reply2
        else:
            insert_sql = f"INSERT INTO project (项目号, 项目名称, 项目来源, 项目类型, 总经费,  开始年份, 结束年份) VALUES ('{id}', '{name}', '{source}', '{type}', '{total_funding}', '{start}', '{end}')"
            cursor.execute(insert_sql)
            connection.commit()

            for i in range(5):
                if pr_id[i]:
                    insert_sql = f"INSERT INTO tpr (教师工号, 项目号, 排名, 承担经费) VALUES ('{pr_id[i]}', '{id}', '{i+1}', '{pr_fu[i]}')"
                    cursor.execute(insert_sql)
                    connection.commit()
            reply1 = "Successfully added"
            reply2 = str(total_funding)
        # 关闭连接
        cursor.close()
        connection.close()
        return reply1, reply2
    except Exception as e:
        return f"添加出错: {str(e)}"
    
def update_project(id, pr_id1, pr_id2, pr_id3, pr_id4, pr_id5, pr_fu1, pr_fu2, pr_fu3, pr_fu4, pr_fu5, name, source, type, start, end):

    total_funding = pr_fu1 + pr_fu2 + pr_fu3 + pr_fu4 + pr_fu5
    type = str(types.index(type) + 1) if type else None
    pr_id = [pr_id1, pr_id2, pr_id3, pr_id4, pr_id5]  
    pr_fu = [pr_fu1, pr_fu2, pr_fu3, pr_fu4, pr_fu5]
    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID"
    if start > end:
        return "开始年份大于结束年份！", "ERROR"

    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 更新教师信息
        for i in range(5):
            if pr_id[i]:
                select_sql = f"SELECT * FROM teacher WHERE 工号='{pr_id[i]}'"
                cursor.execute(select_sql)
                result = cursor.fetchone()
                if not result:
                    return f"工号{pr_id[i]}不存在！", "ERROR"
        select_sql = f"SELECT * FROM project WHERE 项目号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if not result:
            reply1 = "项目号 not exists"
            reply2 = "项目号 not exists"
        else:
            if name:
                update_sql = f"UPDATE project SET 项目名称='{name}' WHERE 项目号='{id}'"
                cursor.execute(update_sql)
            if source:
                update_sql = f"UPDATE project SET 项目来源='{source}' WHERE 项目号='{id}'"
                cursor.execute(update_sql)
            if type:
                update_sql = f"UPDATE project SET 项目类型='{type}' WHERE 项目号='{id}'"
                cursor.execute(update_sql)
            update_sql = f"UPDATE project SET 总经费='{total_funding}' WHERE 项目号='{id}'"
            cursor.execute(update_sql)
            if start:
                update_sql = f"UPDATE project SET 开始年份='{type}' WHERE 项目号='{id}'"
                cursor.execute(update_sql)
            if end:
                update_sql = f"UPDATE project SET 结束年份='{type}' WHERE 项目号='{id}'"
                cursor.execute(update_sql)
            
            delete_sql = f"DELETE FROM tpr WHERE 项目号='{id}'"
            cursor.execute(delete_sql)
            connection.commit()
            for i in range(5):
                if pr_id[i]:
                    insert_sql = f"INSERT INTO tpr (教师工号, 项目号, 排名, 承担经费) VALUES ('{pr_id[i]}', '{id}', '{i+1}', '{pr_fu[i]}')"
                    cursor.execute(insert_sql)
                    connection.commit()
            connection.commit() 
            reply1 = "Successfully updated"
            reply2 = str(total_funding)
            # 关闭连接
        cursor.close()
        connection.close()
        return reply1, reply2
    except Exception as e:
        return f"更新出错: {str(e)}"
    
def delete_project(id):

    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID"
    
    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 删除教师信息
        select_sql = f"SELECT * FROM project WHERE 项目号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if not result:
            reply =  "项目号 not exists"
        else:
            delete_sql = f"DELETE FROM project WHERE 项目号='{id}'"
            cursor.execute(delete_sql)
            connection.commit()
            reply = "Successfully deleted"
        # 关闭连接
        cursor.close()
        connection.close()
        return reply
    except Exception as e:
        return f"删除出错: {str(e)}"