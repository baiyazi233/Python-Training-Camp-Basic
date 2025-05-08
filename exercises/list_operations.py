"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    if operation == "add":  
        students.append(args[0]) 
    elif operation == "remove":  
        if args[0] in students:  
            students.remove(args[0])  
        else:
            print("学生不存在，无法删除")  
    elif operation == "update": 
        if args[0] in students:  
            index = students.index(args[0]) 
            students[index] = args[1] 
        else:
            print("学生不存在，无法更新")  
    else:
        print("无效的操作类型")  
    return students 