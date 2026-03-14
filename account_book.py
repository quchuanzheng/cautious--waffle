"""
简易个人收支记账小程序
功能：录入收支记录、查询记录、统计收支、删除记录
作者：Python入门示例
"""

from datetime import datetime

# 存储所有收支记录的列表
records = []

def show_menu():
    """显示主菜单"""
    print("\n" + "="*40)
    print("       个人收支记账小程序")
    print("="*40)
    print("  1. 录入记录")
    print("  2. 查询记录")
    print("  3. 统计收支")
    print("  4. 删除记录")
    print("  0. 退出程序")
    print("="*40)

def add_record():
    """录入收支记录"""
    print("\n--- 录入收支记录 ---")
    
    # 选择收支类型
    while True:
        record_type = input("请选择类型（1-收入 / 2-支出）：").strip()
        if record_type == "1":
            record_type = "收入"
            break
        elif record_type == "2":
            record_type = "支出"
            break
        else:
            print("❌ 输入错误，请输入 1 或 2")
    
    # 输入金额
    while True:
        amount_input = input("请输入金额（正数）：").strip()
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("❌ 金额必须为正数，请重新输入")
                continue
            break
        except ValueError:
            print("❌ 输入格式错误，请输入数字")
    
    # 输入备注
    note = input("请输入备注（可选，直接回车跳过）：").strip()
    if not note:
        note = "无"
    
    # 自动获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 创建记录字典
    record = {
        "type": record_type,
        "amount": amount,
        "note": note,
        "time": current_time
    }
    
    # 添加到记录列表
    records.append(record)
    print(f"\n✅ 录入成功！【{record_type}】金额：{amount:.2f}元，时间：{current_time}")

def query_records():
    """查询所有收支记录"""
    print("\n--- 查询收支记录 ---")
    
    if not records:
        print("📭 暂无记录")
        return
    
    print(f"\n共有 {len(records)} 条记录：")
    print("-" * 60)
    print(f"{'序号':<6}{'类型':<8}{'金额':<12}{'备注':<15}{'时间':<20}")
    print("-" * 60)
    
    for index, record in enumerate(records, start=1):
        print(f"{index:<6}{record['type']:<8}{record['amount']:<12.2f}{record['note']:<15}{record['time']:<20}")
    
    print("-" * 60)

def calculate_statistics():
    """统计当月收支情况"""
    print("\n--- 统计当月收支 ---")
    
    if not records:
        print("📭 暂无记录，无法统计")
        return
    
    # 获取当前年月
    current_year_month = datetime.now().strftime("%Y-%m")
    
    # 初始化统计变量
    total_income = 0.0
    total_expense = 0.0
    
    # 遍历当月记录进行统计
    for record in records:
        if record["time"].startswith(current_year_month):
            if record["type"] == "收入":
                total_income += record["amount"]
            else:
                total_expense += record["amount"]
    
    # 计算结余
    balance = total_income - total_expense
    
    # 打印统计结果
    print(f"\n📊 {current_year_month} 月度收支统计：")
    print("=" * 40)
    print(f"  总收入：{total_income:>12.2f} 元")
    print(f"  总支出：{total_expense:>12.2f} 元")
    print("-" * 40)
    print(f"  结  余：{balance:>12.2f} 元")
    print("=" * 40)

def delete_record():
    """删除收支记录"""
    print("\n--- 删除收支记录 ---")
    
    if not records:
        print("📭 暂无记录，无法删除")
        return
    
    # 先显示所有记录
    query_records()
    
    # 选择要删除的记录
    while True:
        choice = input("\n请输入要删除的记录序号（输入 0 取消）：").strip()
        
        if choice == "0":
            print("已取消删除操作")
            return
        
        try:
            index = int(choice)
            if 1 <= index <= len(records):
                # 删除指定记录
                deleted_record = records.pop(index - 1)
                print(f"\n✅ 删除成功！已删除：【{deleted_record['type']}】{deleted_record['amount']:.2f}元")
                return
            else:
                print(f"❌ 序号超出范围，请输入 1-{len(records)} 之间的数字")
        except ValueError:
            print("❌ 输入格式错误，请输入数字")

def main():
    """主程序入口"""
    print("\n欢迎使用个人收支记账小程序！")
    
    while True:
        show_menu()
        choice = input("\n请选择功能（输入数字）：").strip()
        
        if choice == "1":
            add_record()
        elif choice == "2":
            query_records()
        elif choice == "3":
            calculate_statistics()
        elif choice == "4":
            delete_record()
        elif choice == "0":
            print("\n感谢使用，再见！👋")
            break
        else:
            print("❌ 输入错误，请输入 0-4 之间的数字")

# 程序入口
if __name__ == "__main__":
    main()
