import pymysql
from Config import config

types = ["full paper", "short paper", "poster paper", "demo paper"]
levels = ["CCF-A", "CCF-B", "CCF-C", "中文 CCF-A", "中文 CCF-B", "无级别"]

def query_paper(id):
    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()
        # 检测输入的ID中是否含有单双引号，以防止SQL注入
        if "'" in str(id) or '"' in str(id) or "--" in str(id):
            return "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID", "Invalid ID"

        # 查询教师信息
        select_sql = f"SELECT * FROM paper WHERE 序号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchall()
        if not result:
            return "论文序号 not exists", " ", " ", " ", " ", " "
        else:
            reply1 = result[0][1]
            reply2 = result[0][2]
            reply3 = result[0][3]
            reply4 = types[result[0][4] - 1]
            reply5 = levels[result[0][5] - 1]
            select_sql = f"SELECT 教师工号, 排名, 是否为通讯作者 FROM tpa WHERE 论文序号='{id}'"
            cursor.execute(select_sql)
            result = cursor.fetchall()
            reply6 = ""
            for item in result:
                reply6 += f"排名：{item[1]}， 教师工号：{item[0]}     {"通讯作者" if item[2] else ""}\n"

            return reply1, reply2, reply3, reply4, reply5, reply6
    except Exception as e:
        return f"添加出错: {str(e)}"


def add_paper(id, tid1, tid2, tid3, tid4, tid5, tid6, tid7, tid8, comm, name, source, year, type, level):

    type = str(types.index(type) + 1)
    level = str(levels.index(level) + 1)
    tid = [tid1, tid2, tid3, tid4, tid5, tid6, tid7, tid8]  
    if "'" in str(id) or '"' in str(id) or "--" in str(id):
            return "Invalid ID"
    if comm and tid[int(comm)-1] == '':
        return "通讯作者序号有误！"

    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 插入论文信息
        for i in range(8):
            if tid[i]:
                select_sql = f"SELECT * FROM teacher WHERE 工号='{tid[i]}'"
                cursor.execute(select_sql)
                result = cursor.fetchone()
                if not result:
                    return f"工号{tid[i]}不存在！"

        select_sql = f"SELECT * FROM paper WHERE 序号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if result:
            reply =  "ID already exists"
            return reply
        else:
            insert_sql = f"INSERT INTO paper (序号, 论文名称, 发表源, 发表年份, 类型, 级别) VALUES ('{id}', '{name}', '{source}', '{year}', '{type}', '{level}')"
            cursor.execute(insert_sql)
            connection.commit()

            for i in range(8):
                if tid[i]:
                    insert_sql = f"INSERT INTO tpa (教师工号, 论文序号, 排名, 是否为通讯作者) VALUES ('{tid[i]}', '{id}', '{i+1}', '{1 if i+1 == int(comm) else 0}')"
                    cursor.execute(insert_sql)
                    connection.commit()
            reply = "Successfully added"
        # 关闭连接
        cursor.close()
        connection.close()
        return reply
    except Exception as e:
        return f"添加出错: {str(e)}"
    
def update_paper(id, tid1, tid2, tid3, tid4, tid5, tid6, tid7, tid8, comm, name, source, year, type, level):

    type = str(types.index(type) + 1) if type else None
    level = str(levels.index(level) + 1) if level else None
    tid = [tid1, tid2, tid3, tid4, tid5, tid6, tid7, tid8]  
    if "'" in str(id) or '"' in str(id) or "--" in str(id):
        return "Invalid ID"
    if comm and tid[int(comm)-1] == '':
        return "通讯作者序号有误！"

    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 更新教师信息
        for i in range(8):
            if tid[i]:
                select_sql = f"SELECT * FROM teacher WHERE 工号='{tid[i]}'"
                cursor.execute(select_sql)
                result = cursor.fetchone()
                if not result:
                    return f"工号{tid[i]}不存在！"
        select_sql = f"SELECT * FROM paper WHERE 序号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if not result:
            reply =  f"序号{id} not exists"
        else:
            if name:
                update_sql = f"UPDATE paper SET 论文名称='{name}' WHERE 序号='{id}'"
                cursor.execute(update_sql)
            if source:
                update_sql = f"UPDATE paper SET 发表源='{source}' WHERE 序号='{id}'"
                cursor.execute(update_sql)
            if year:
                update_sql = f"UPDATE paper SET 发表年份='{year}' WHERE 序号='{id}'"
                cursor.execute(update_sql)
            if type:
                update_sql = f"UPDATE paper SET 类型='{type}' WHERE 序号='{id}'"
                cursor.execute(update_sql)
            if level:
                update_sql = f"UPDATE paper SET 级别='{level}' WHERE 序号='{id}'"
                cursor.execute(update_sql)
            
            delete_sql = f"DELETE FROM tpa WHERE 论文序号='{id}'"
            cursor.execute(delete_sql)
            connection.commit()
            for i in range(8):
                if tid[i]:
                    insert_sql = f"INSERT INTO tpa (教师工号, 论文序号, 排名, 是否为通讯作者) VALUES ('{tid[i]}', '{id}', '{i+1}', '{1 if i+1 == int(comm) else 0}')"
                    cursor.execute(insert_sql)
                    connection.commit()
            connection.commit() 
            reply = "Successfully updated"
            # 关闭连接
        cursor.close()
        connection.close()
        return reply
    except Exception as e:
        return f"更新出错: {str(e)}"
    
def delete_paper(id):
    if "'" in id or '"' in id or "--" in id:
            return "Invalid ID"
    try:
        # 建立数据库连接
        connection = pymysql.connect(**config)
        cursor = connection.cursor()

        # 删除教师信息
        select_sql = f"SELECT * FROM paper WHERE 序号='{id}'"
        cursor.execute(select_sql)
        result = cursor.fetchone()
        if not result:
            reply =  "ID not exists"
        else:
            delete_sql = f"DELETE FROM paper WHERE 序号='{id}'"
            cursor.execute(delete_sql)
            connection.commit()
            reply = "Successfully deleted"
        # 关闭连接
        cursor.close()
        connection.close()
        return reply
    except Exception as e:
        return f"删除出错: {str(e)}"
    
if __name__ == '__main__':
    print(query_paper("1"))