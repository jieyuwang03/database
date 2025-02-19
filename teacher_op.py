import pymysql
from Config import config

sexes = ["男", "女"]
titles = ["博士后", "助教", "讲师", "副教授", "特任教授", "教授", "助理研究员", "特任副研究员", "副研究员", "特任研究员", "研究员"]

def query_teacher(id):
    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        if "'" in id or '"' in id or "--" in id:
            return "Invalid ID", "Invalid ID", "Invalid ID"

        # 查询教师信息
        select_sql = f"SELECT * FROM teacher WHERE 工号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchall()
        if not result:
            reply1 =  "ID not exists"
            reply2 = "ID not exists"
            reply3 = "ID not exists"
        else:
            reply1 = result[0][1]
            reply2 = sexes[result[0][2]-1]
            reply3 = titles[result[0][3]-1]
        return reply1, reply2, reply3
    except Exception as e:
        return f"添加出错: {str(e)}"


def add_teacher(id, name, sex, title):

    sex = str(sexes.index(sex) + 1)
    title = str(titles.index(title) + 1)

    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID"

    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 插入教师信息
        select_sql = f"SELECT * FROM teacher WHERE 工号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if result:
            reply =  "ID already exists"
        else:
            insert_sql = f"INSERT INTO teacher (工号, 姓名, 性别, 职称) VALUES ('{id}', '{name}', '{sex}', '{title}')"
            cursor.execute(insert_sql)
            connection.commit()
            reply = "Successfully added"
        # 关闭连接
        cursor.close()
        connection.close()
        return reply
    except Exception as e:
        return f"添加出错: {str(e)}"
    
def update_teacher(id, name, sex, title):

    sex = str(sexes.index(sex) + 1) if sex else None
    title = str(titles.index(title) + 1) if title else None

    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID"

    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 更新教师信息
        select_sql = f"SELECT * FROM teacher WHERE 工号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if not result:
            reply =  "ID not exists"
        else:
            if name:
                update_sql = f"UPDATE teacher SET 姓名='{name}' WHERE 工号='{id}'"
                cursor.execute(update_sql)
            if sex:
                update_sql = f"UPDATE teacher SET 性别='{sex}' WHERE 工号='{id}'"
                cursor.execute(update_sql)
            if title:
                update_sql = f"UPDATE teacher SET 职称='{title}' WHERE 工号='{id}'"
                cursor.execute(update_sql)
            connection.commit() 
            reply = "Successfully updated"
            # 关闭连接
        cursor.close()
        connection.close()
        return reply
    except Exception as e:
        return f"更新出错: {str(e)}"
    
def delete_teacher(id):

    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID"
    
    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 删除教师信息
        select_sql = f"SELECT * FROM teacher WHERE 工号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if not result:
            reply =  f"工号{id} not exists"
        else:
            delete_sql = f"DELETE FROM teacher WHERE 工号='{id}'"
            cursor.execute(delete_sql)
            connection.commit()
            reply = "Successfully deleted"
        # 关闭连接
        cursor.close()
        connection.close()
        return reply
    except Exception as e:
        return f"删除出错: {str(e)}"