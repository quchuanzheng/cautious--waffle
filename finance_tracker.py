import datetime

records = []

def get_current_time():
    """获取当前系统时间，格式：年-月-日 时:分"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def show_menu():
    """显示主菜单"""
    print("\n" + "="*40)
    print("          个人收支记账小程序")
    print("="*40)
    print("1. 录入收支记录")
    print("2. 查询所有记录")
    print("3. 统计当月收支")
    print("4. 删除记录")
    print("0. 退出程序")
    print("="*40)

def input_record():
    """录入收支记录"""
    print("\n--- 录入收支记录 ---")
    
    while True:
        record_type = input("请选择类型（收入/支出）：").strip()
        if record_type in ["收入", "支出"]:
            break
        print("错误：类型只能是「收入」或「支出」，请重新输入！")
    
    while True:
        try:
            amount = float(input("请输入金额："))
            if amount > 0:
                break
            print("错误：金额必须是正数，请重新输入！")
        except ValueError:
            print("错误：请输入有效的数字！")
    
    note = input("请输入备注（可选）：").strip()
    if not note:
        note = "无"
    
    new_record = {
        "type": record_type,
        "amount": round(amount, 2),
        "note": note,
        "time": get_current_time()
    }
    
    records.append(new_record)
    print(f"\n✅ 记录录入成功！")
    print(f"类型：{new_record['type']} | 金额：¥{new_record['amount']:.2f} | 备注：{new_record['note']} | 时间：{new_record['time']}")

def show_all_records():
    """查询所有收支记录"""
    print("\n--- 所有收支记录 ---")
    if not records:
        print("暂无记录")
        return
    
    for i, record in enumerate(records, 1):
        print(f"[{i}] {record['time']} | {record['type']:4} | ¥{record['amount']:>8.2f} | 备注：{record['note']}")

def calculate_monthly():
    """统计当月收支情况"""
    print("\n--- 当月收支统计 ---")
    current_month = datetime.datetime.now().strftime("%Y-%m")
    
    monthly_income = 0.0
    monthly_expense = 0.0
    
    for record in records:
        if record["time"].startswith(current_month):
            if record["type"] == "收入":
                monthly_income += record["amount"]
            else:
                monthly_expense += record["amount"]
    
    balance = monthly_income - monthly_expense
    
    print(f"统计月份：{current_month}")
    print(f"总收入：¥{monthly_income:.2f}")
    print(f"总支出：¥{monthly_expense:.2f}")
    print(f"结  余：¥{balance:.2f}")
    
    if balance > 0:
        print(f"💰 本月结余：¥{balance:.2f}")
    elif balance < 0:
        print(f"⚠️  本月超支：¥{abs(balance):.2f}")
    else:
        print("ℹ️  本月收支平衡")

def delete_record():
    """删除指定记录"""
    print("\n--- 删除记录 ---")
    if not records:
        print("暂无记录可删除")
        return
    
    show_all_records()
    
    while True:
        try:
            index = int(input("\n请输入要删除的记录序号（输入0取消）："))
            if index == 0:
                print("已取消删除操作")
                return
            if 1 <= index <= len(records):
                break
            print(f"错误：请输入1到{len(records)}之间的数字！")
        except ValueError:
            print("错误：请输入有效的数字！")
    
    deleted = records.pop(index - 1)
    print(f"\n✅ 已删除记录：")
    print(f"{deleted['time']} | {deleted['type']} | ¥{deleted['amount']:.2f} | 备注：{deleted['note']}")

def main():
    """主函数"""
    print("欢迎使用个人收支记账小程序！")
    
    while True:
        show_menu()
        
        try:
            choice = input("请选择功能（输入数字）：").strip()
            
            if choice == "1":
                input_record()
            elif choice == "2":
                show_all_records()
            elif choice == "3":
                calculate_monthly()
            elif choice == "4":
                delete_record()
            elif choice == "0":
                print("\n感谢使用个人收支记账小程序，再见！")
                break
            else:
                print("\n❌ 错误：请输入0-4之间的有效数字！")
        except Exception as e:
            print(f"\n❌ 发生错误：{str(e)}，请重试！")

if __name__ == "__main__":
    main()
