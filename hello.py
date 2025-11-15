# def compare_data_structures():
#     """
#     比较Python中字典、元组和列表的区别
#     """
#     print("=" * 60)
#     print("          Python数据结构比较：字典 vs 元组 vs 列表")
#     print("=" * 60)
    
#     # 创建示例
#     sample_dict = {"name": "Alice", "age": 25, "city": "Beijing"}
#     sample_tuple = ("apple", "banana", "cherry")
#     sample_list = ["red", "green", "blue"]
    
#     print("\n1. 基本定义和语法：")
#     print(f"   字典: {sample_dict} - 使用花括号 {{key: value}}")
#     print(f"   元组: {sample_tuple} - 使用圆括号 (element,)")
#     print(f"   列表: {sample_list} - 使用方括号 [element]")
    
#     print("\n2. 可变性比较：")
#     # 测试可变性
#     try:
#         sample_list[0] = "yellow"
#         print(f"   ✅ 列表是可变的: 修改后 {sample_list}")
#     except Exception as e:
#         print(f"   ❌ 列表修改失败: {e}")
    
#     try:
#         sample_tuple[0] = "orange"
#         print(f"   ✅ 元组是可变的: 修改后 {sample_tuple}")
#     except Exception as e:
#         print(f"   ❌ 元组不可变: {e}")
    
#     try:
#         sample_dict["name"] = "Bob"
#         print(f"   ✅ 字典是可变的: 修改后 {sample_dict}")
#     except Exception as e:
#         print(f"   ❌ 字典修改失败: {e}")
    
#     print("\n3. 操作方法比较：")
    
#     # 列表操作
#     sample_list.append("purple")
#     print(f"   列表支持 append(): {sample_list}")
    
#     sample_list.insert(1, "orange")
#     print(f"   列表支持 insert(): {sample_list}")
    
#     # 字典操作
#     sample_dict["gender"] = "female"
#     print(f"   字典支持添加键值对: {sample_dict}")
    
#     del sample_dict["age"]
#     print(f"   字典支持删除键: {sample_dict}")
    
#     print("\n4. 性能和使用场景：")
#     print("   📊 列表: 有序集合，适合需要修改的动态数据")
#     print("   📊 元组: 有序但不可变，适合保护数据不被修改")
#     print("   📊 字典: 键值对映射，适合快速查找和关联数据")
    
#     print("\n5. 内存占用比较：")
#     import sys
#     print(f"   字典内存占用: {sys.getsizeof(sample_dict)} 字节")
#     print(f"   元组内存占用: {sys.getsizeof(sample_tuple)} 字节")
#     print(f"   列表内存占用: {sys.getsizeof(sample_list)} 字节")
    
#     print("\n6. 访问方式比较：")
#     print(f"   列表索引访问: sample_list[0] = {sample_list[0]}")
#     print(f"   元组索引访问: sample_tuple[1] = {sample_tuple[1]}")
#     print(f"   字典键访问: sample_dict['name'] = {sample_dict['name']}")
    
#     print("\n7. 迭代方式比较：")
#     print("   列表迭代 - 按顺序访问元素:")
#     for i, item in enumerate(sample_list):
#         print(f"      索引{i}: {item}")
    
#     print("   字典迭代 - 访问键值对:")
#     for key, value in sample_dict.items():
#         print(f"      {key}: {value}")

# def advanced_comparison():
#     """
#     高级特性比较
#     """
#     print("\n" + "=" * 60)
#     print("                   高级特性比较")
#     print("=" * 60)
    
#     # 嵌套结构
#     complex_list = [1, 2, ["a", "b"], {"key": "value"}]
#     complex_tuple = (1, 2, ["a", "b"], {"key": "value"})
#     complex_dict = {
#         "list_data": [1, 2, 3],
#         "tuple_data": (1, 2, 3),
#         "nested_dict": {"inner": "data"}
#     }
    
#     print("嵌套结构示例:")
#     print(f"   复杂列表: {complex_list}")
#     print(f"   复杂元组: {complex_tuple}")
#     print(f"   复杂字典: {complex_dict}")
    
#     # 修改嵌套结构中的可变元素
#     print("\n嵌套结构中的可变性:")
#     complex_tuple[2][0] = "modified"  # 修改元组中的列表
#     print(f"   修改元组中的列表元素: {complex_tuple}")
    
#     complex_dict["list_data"].append(4)  # 修改字典中的列表
#     print(f"   修改字典中的列表元素: {complex_dict}")

# def practical_examples():
#     """
#     实际应用场景示例
#     """
#     print("\n" + "=" * 60)
#     print("                   实际应用场景")
#     print("=" * 60)
    
#     # 列表应用 - 学生成绩管理
#     student_scores = [85, 92, 78, 96, 88]
#     print("📚 列表应用 - 学生成绩管理:")
#     print(f"   原始成绩: {student_scores}")
#     student_scores.sort()
#     print(f"   排序后: {student_scores}")
#     print(f"   最高分: {max(student_scores)}")
    
#     # 元组应用 - 坐标点
#     point1 = (10, 20)
#     point2 = (30, 40)
#     print("\n📍 元组应用 - 坐标点:")
#     print(f"   点1: {point1}, 点2: {point2}")
#     print(f"   点1的x坐标: {point1[0]}")
    
#     # 字典应用 - 学生信息
#     student_info = {
#         "id": "S001",
#         "name": "张三",
#         "courses": ["数学", "英语", "编程"],
#         "scores": {"数学": 90, "英语": 85, "编程": 95}
#     }
#     print("\n👨‍🎓 字典应用 - 学生信息:")
#     print(f"   学生姓名: {student_info['name']}")
#     print(f"   编程成绩: {student_info['scores']['编程']}")
#     print(f"   所有课程: {', '.join(student_info['courses'])}")

# def summary_table():
#     """
#     总结对比表格
#     """
#     print("\n" + "=" * 80)
#     print("                            总结对比表")
#     print("=" * 80)
    
#     comparison_data = [
#         ["特性", "列表(List)", "元组(Tuple)", "字典(Dict)"],
#         ["语法", "[]", "()", "{}"],
#         ["可变性", "可变", "不可变", "可变"],
#         ["有序性", "有序", "有序", "Python 3.7+ 有序"],
#         ["元素访问", "索引", "索引", "键"],
#         ["重复元素", "允许", "允许", "键不允许重复"],
#         ["内存占用", "较小", "最小", "较大"],
#         ["查找速度", "O(n)", "O(n)", "O(1)"],
#         ["使用场景", "动态数据集合", "固定数据集合", "键值对映射"]
#     ]
    
#     for row in comparison_data:
#         print(f"   {row[0]:<12} {row[1]:<20} {row[2]:<20} {row[3]:<20}")

# # 运行比较函数
# if __name__ == "__main__":
#     compare_data_structures()
#     advanced_comparison()
#     practical_examples()
#     summary_table()
    
#     print("\n🎯 关键要点总结:")
#     print("   • 列表：有序、可变，适合存储需要频繁修改的序列数据")
#     print("   • 元组：有序、不可变，适合存储不应被修改的数据")
#     print("   • 字典：键值对映射，适合通过键快速查找值的场景")

'''
2025年11月
PC端重新尝试配置github，一是通过修改host提升github访问成功率，要注意，修改后要刷新dns缓存，通过cmd运行ipconfig /flushdns 命令即可。测试有效

111

'''