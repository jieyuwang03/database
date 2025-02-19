import pymysql
from Config import config

semesters = ["春季学期", "夏季学期", "秋季学期"]
natures = ["本科生课程", "研究生课程"]

def query_class(id):
    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        if "'" in id or '"' in id or "--" in id:
            return "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID"

        # 查询教师信息
        select_sql = f"SELECT * FROM class WHERE 课程号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchall()
        if not result:
            reply1 = "课程号 not exists"
            reply2 = "课程号 not exists"
            reply3 = "课程号 not exists"
        else:
            reply1 = result[0][1]
            reply2 = result[0][2]
            reply3 = natures[result[0][3] - 1]

        select_sql = f"SELECT 教师工号, 年份, 学期, 承担学时 FROM tc WHERE 课程号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchall()
        reply4 = ""
        for item in result:
            reply4 += f"教师工号：{item[0]}， 年份：{item[1]}， 学期：{semesters[item[2]-1]}， 承担学时：{item[3]}\n"

        return reply1, reply2, reply3, reply4
    except Exception as e:
        return f"添加出错: {str(e)}"


def add_class(id, t_id1, t_id2, t_id3, t_id4, t_id5, t_y1, t_y2, t_y3, t_y4, t_y5, t_s1, t_s2, t_s3, t_s4, t_s5, t_h1, t_h2, t_h3, t_h4, t_h5, name, hour, nature):

    t_s1 = str(semesters.index(t_s1) + 1)
    t_s2 = str(semesters.index(t_s2) + 1)
    t_s3 = str(semesters.index(t_s3) + 1)
    t_s4 = str(semesters.index(t_s4) + 1)
    t_s5 = str(semesters.index(t_s5) + 1)
    nature = str(natures.index(nature) + 1)
    t_id = [t_id1, t_id2, t_id3, t_id4, t_id5]
    t_y = [t_y1, t_y2, t_y3, t_y4, t_y5]
    t_s = [t_s1, t_s2, t_s3, t_s4, t_s5]
    t_h = [t_h1, t_h2, t_h3, t_h4, t_h5]

    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID"

    for i in range(5):
        if t_id[i] and (t_y[i] == '' or t_y[i] == '' or t_s[i] == ''):
            return "信息填写不完整！"
    for i in range(5):
        for j in range(i+1, 5):
            if t_id[i] and t_id[j] and t_id[i] == t_id[j] and t_y[i] == t_y[j] and t_s[i] == t_s[j]:
                return "一名教师在同一年同一学期同一课程应只录入一次"
    for i in range(5):
        if t_id[i]:
            h = 0
            for j in range(5):
                if t_id[j] and t_y[j] == t_y[i] and t_s[j] == t_s[i]:
                    h += t_h[j]
            if h != hour:
                return "同一学年同一学期的课程学时总和应等于课程总学时"


    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 插入论文信息
        for i in range(5):
            if t_id[i]:
                select_sql = f"SELECT * FROM teacher WHERE 工号='{t_id[i]}'"
                cursor.execute(select_sql)
                result = cursor.fetchone()
                if not result:
                    return f"工号{t_id[i]}不存在！"

        select_sql = f"SELECT * FROM class WHERE 课程号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if result:
            reply = "课程号 already exists"
            return reply
        else:
            insert_sql = f"INSERT INTO class (课程号, 课程名称, 学时数, 课程性质) VALUES ('{id}', '{name}', '{hour}', '{nature}')"
            cursor.execute(insert_sql)
            connection.commit()

            for i in range(5):
                if t_id[i]:
                    insert_sql = f"INSERT INTO tc (教师工号, 课程号, 年份, 学期, 承担学时) VALUES ('{t_id[i]}', '{id}', '{t_y[i]}', '{t_s[i]}', '{t_h[i]}')"
                    cursor.execute(insert_sql)
                    connection.commit()
            reply = "Successfully added"
        # 关闭连接
        cursor.close()
        connection.close()
        return reply
    except Exception as e:
        return f"添加出错: {str(e)}"
    
def update_class(id, t_id1, t_id2, t_id3, t_id4, t_id5, t_y1, t_y2, t_y3, t_y4, t_y5, t_s1, t_s2, t_s3, t_s4, t_s5, t_h1, t_h2, t_h3, t_h4, t_h5, name, hour, nature):

    t_s1 = str(semesters.index(t_s1) + 1) if t_s1 else None
    t_s2 = str(semesters.index(t_s2) + 1) if t_s2 else None
    t_s3 = str(semesters.index(t_s3) + 1) if t_s3 else None
    t_s4 = str(semesters.index(t_s4) + 1) if t_s4 else None
    t_s5 = str(semesters.index(t_s5) + 1) if t_s5 else None
    nature = str(natures.index(nature) + 1) if nature else None
    t_id = [t_id1, t_id2, t_id3, t_id4, t_id5]
    t_y = [t_y1, t_y2, t_y3, t_y4, t_y5]
    t_s = [t_s1, t_s2, t_s3, t_s4, t_s5]
    t_h = [t_h1, t_h2, t_h3, t_h4, t_h5]

    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID"

    for i in range(5):
        if t_id[i] and (t_y[i] == '' or t_y[i] == '' or t_s[i] == ''):
            return "信息填写不完整！"
    for i in range(5):
        for j in range(i+1, 5):
            if t_id[i] and t_id[j] and t_id[i] == t_id[j] and t_y[i] == t_y[j] and t_s[i] == t_s[j]:
                return "一名教师在同一年同一学期同一课程应只录入一次"
    for i in range(5):
        if t_id[i]:
            h = 0
            for j in range(5):
                if t_id[j] and t_y[j] == t_y[i] and t_s[j] == t_s[i]:
                    h += t_h[j]
            if h != hour:
                return "同一学年同一学期的课程学时总和应等于课程总学时"

    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 更新教师信息
        for i in range(5):
            if t_id[i]:
                select_sql = f"SELECT * FROM teacher WHERE 工号='{t_id[i]}'"
                cursor.execute(select_sql)
                result = cursor.fetchone()
                if not result:
                    return f"工号{t_id[i]}不存在！"
        select_sql = f"SELECT * FROM class WHERE 课程号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if not result:
            reply = "课程号 not exists"
        else:
            if name:
                update_sql = f"UPDATE class SET 课程名称='{name}' WHERE 课程号='{id}'"
                cursor.execute(update_sql)
            if hour:
                update_sql = f"UPDATE class SET 学时数='{hour}' WHERE 课程号='{id}'"
                cursor.execute(update_sql)
            if nature:
                update_sql = f"UPDATE class SET 课程性质='{nature}' WHERE 课程号='{id}'"
                cursor.execute(update_sql)

            delete_sql = f"DELETE FROM tc WHERE 课程号='{id}'"
            cursor.execute(delete_sql)
            connection.commit()
            for i in range(5):
                if t_id[i]:
                    insert_sql = f"INSERT INTO tc (教师工号, 课程号, 年份, 学期, 承担学时) VALUES ('{t_id[i]}', '{id}', '{t_y[i]}', '{t_s[i]}', '{t_h[i]}')"
                    cursor.execute(insert_sql)
                    connection.commit()
            reply = "Successfully updated"
            # 关闭连接
        cursor.close()
        connection.close()
        return reply
    except Exception as e:
        return f"添加出错: {str(e)}"
    
def delete_class(id):
    
    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID"
    
    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 删除教师信息
        select_sql = f"SELECT * FROM class WHERE 课程号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if not result:
            reply =  "课程号 not exists"
        else:
            delete_sql = f"DELETE FROM class WHERE 课程号='{id}'"
            cursor.execute(delete_sql)
            connection.commit()
            reply = "Successfully deleted"
        # 关闭连接
        cursor.close()
        connection.close()
        return reply
    except Exception as e:
        return f"删除出错: {str(e)}"