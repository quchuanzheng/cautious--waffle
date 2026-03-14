"""
简易个人收支记账小程序
功能：录入收支记录、查询记录、统计收支、删除记录
作者：AI Assistant
"""

from datetime import datetime

# ==================== 数据存储 ====================
# 使用列表存储所有收支记录，每条记录是一个字典
records = []


# ==================== 功能函数 ====================

def get_current_time():
    """
    获取系统当前时间
    返回格式：年-月-日 时:分
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def add_record():
    """
    录入收支记录
    包含类型、金额、备注、时间
    """
    print("\n" + "=" * 40)
    print("【录入收支记录】")
    print("=" * 40)
    
    # 输入收支类型并验证
    while True:
        record_type = input("请输入收支类型（收入/支出）：").strip()
        if record_type in ["收入", "支出"]:
            break
        print("⚠️  提示：类型只能是'收入'或'支出'，请重新输入！")
    
    # 输入金额并验证
    while True:
        amount_str = input("请输入金额（正数）：").strip()
        try:
            amount = float(amount_str)
            if amount > 0:
                break
            else:
                print("⚠️  提示：金额必须是正数，请重新输入！")
        except ValueError:
            print("⚠️  提示：金额必须是数字，请重新输入！")
    
    # 输入备注
    remark = input("请输入备注（可选，直接回车跳过）：").strip()
    if not remark:
        remark = "无"
    
    # 自动获取当前时间
    record_time = get_current_time()
    
    # 创建记录字典
    record = {
        "id": len(records) + 1,      # 记录编号
        "type": record_type,          # 收支类型
        "amount": amount,             # 金额
        "remark": remark,             # 备注
        "time": record_time           # 时间
    }
    
    # 添加到记录列表
    records.append(record)
    
    print("\n✅ 记录录入成功！")
    print(f"   类型：{record_type}")
    print(f"   金额：{amount:.2f} 元")
    print(f"   备注：{remark}")
    print(f"   时间：{record_time}")
    print("=" * 40)


def query_records():
    """
    查询所有收支记录
    以表格形式展示
    """
    print("\n" + "=" * 70)
    print("【查询所有记录】")
    print("=" * 70)
    
    # 检查是否有记录
    if not records:
        print("📭 暂无收支记录")
        print("=" * 70)
        return
    
    # 打印表头
    print(f"{'编号':<6}{'类型':<8}{'金额(元)':<12}{'时间':<20}{'备注':<20}")
    print("-" * 70)
    
    # 遍历并打印每条记录
    for record in records:
        print(f"{record['id']:<6}"
              f"{record['type']:<8}"
              f"{record['amount']:<12.2f}"
              f"{record['time']:<20}"
              f"{record['remark']:<20}")
    
    print("=" * 70)
    print(f"📊 共 {len(records)} 条记录")
    print("=" * 70)


def statistics():
    """
    统计当月收支情况
    计算总收入、总支出、结余
    """
    print("\n" + "=" * 40)
    print("【统计当月收支】")
    print("=" * 40)
    
    # 获取当前年月
    current_year_month = datetime.now().strftime("%Y-%m")
    
    # 初始化统计变量
    total_income = 0.0      # 总收入
    total_expense = 0.0     # 总支出
    
    # 遍历记录，统计当月数据
    for record in records:
        # 检查记录是否属于当前月份
        if record['time'].startswith(current_year_month):
            if record['type'] == "收入":
                total_income += record['amount']
            else:
                total_expense += record['amount']
    
    # 计算结余
    balance = total_income - total_expense
    
    # 打印统计结果
    print(f"📅 统计月份：{current_year_month}")
    print("-" * 40)
    print(f"💰 总收入：{total_income:>10.2f} 元")
    print(f"💸 总支出：{total_expense:>10.2f} 元")
    print(f"💵 结  余：{balance:>10.2f} 元")
    print("=" * 40)
    
    # 结余提示
    if balance > 0:
        print("🎉 本月有盈余，继续保持！")
    elif balance < 0:
        print("⚠️  本月超支，注意控制消费！")
    else:
        print("📝 本月收支平衡")


def delete_record():
    """
    删除指定编号的记录
    """
    print("\n" + "=" * 40)
    print("【删除记录】")
    print("=" * 40)
    
    # 检查是否有记录
    if not records:
        print("📭 暂无记录可删除")
        print("=" * 40)
        return
    
    # 显示现有记录
    print("现有记录：")
    for record in records:
        print(f"  编号 {record['id']}: {record['type']} {record['amount']:.2f}元 - {record['remark']}")
    
    print("-" * 40)
    
    # 输入要删除的记录编号
    while True:
        id_str = input("请输入要删除的记录编号（0取消）：").strip()
        try:
            record_id = int(id_str)
            if record_id == 0:
                print("❌ 已取消删除操作")
                return
            if record_id > 0:
                break
            else:
                print("⚠️  提示：编号必须是正整数，请重新输入！")
        except ValueError:
            print("⚠️  提示：编号必须是整数，请重新输入！")
    
    # 查找并删除记录
    for i, record in enumerate(records):
        if record['id'] == record_id:
            deleted_record = records.pop(i)
            
            # 重新编号
            for j, r in enumerate(records):
                r['id'] = j + 1
            
            print(f"\n✅ 已成功删除记录：")
            print(f"   类型：{deleted_record['type']}")
            print(f"   金额：{deleted_record['amount']:.2f} 元")
            print(f"   备注：{deleted_record['remark']}")
            print("=" * 40)
            return
    
    print(f"⚠️  未找到编号为 {record_id} 的记录")
    print("=" * 40)


def show_menu():
    """
    显示主菜单
    """
    print("\n" + "=" * 40)
    print("    📒 个人收支记账小程序")
    print("=" * 40)
    print("    1. 录入记录")
    print("    2. 查询记录")
    print("    3. 统计收支")
    print("    4. 删除记录")
    print("    0. 退出程序")
    print("=" * 40)


def main():
    """
    主函数
    程序入口，控制程序流程
    """
    print("\n" + "🎉" * 20)
    print("    欢迎使用个人收支记账小程序！")
    print("🎉" * 20)
    
    while True:
        # 显示菜单
        show_menu()
        
        # 获取用户选择
        choice = input("请输入选项（0-4）：").strip()
        
        # 根据选择执行对应功能
        if choice == "1":
            add_record()
        elif choice == "2":
            query_records()
        elif choice == "3":
            statistics()
        elif choice == "4":
            delete_record()
        elif choice == "0":
            print("\n" + "=" * 40)
            print("    感谢使用，再见！👋")
            print("=" * 40)
            break
        else:
            print("\n⚠️  无效选项，请输入 0-4 之间的数字！")


# ==================== 程序入口 ====================
if __name__ == "__main__":
    main()
