import random
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

class Prize:
    def __init__(self, name, quantity, cost):
        self.name = name
        self.quantity = quantity
        self.cost = cost

'''
prizes = [
    Prize("SP獎 Switch OLED", 1, 9980),
    Prize("A獎 Switch Lite", 2, 5150),
    Prize("B獎 AirPods 2", 4, 3945),
    Prize("C獎 Switch遊戲卡收納包", 6, 135),
    Prize("D獎 Switch收納包 伊布", 6, 160),
    Prize("E獎 Switch收納包 皮卡丘", 6, 140),
    Prize("F獎 衛生棉收納包", 20, 15),
    Prize("G獎 功德按鍵", 35, 10),
    Prize("H獎 手機支架 厚椅款", 40, 6)
]
'''
prizes = [
    Prize("SP獎 iphone 15 pro", 1, 29900),
    Prize("A獎 Air HomePod", 1, 9300),
    Prize("B獎 AirPods 2", 1, 3945),
    Prize("C獎 HomePod mini", 1, 2799),
    Prize("D獎 Air Tags", 4, 785),
    Prize("E獎 官方一番賞任選三抽", 4, 0),
    Prize("F獎 全店自製一番賞$700以下一抽", 36, 0),
    Prize("G獎 全店自製一番賞$500以下一抽", 36, 0),
    Prize("H獎 全店自製一番賞$400以下一抽", 36, 0)
]
'''
prizes = [
    Prize("SP獎 Switch OLED", 1, 9980),
    Prize("A獎 Switch Lite", 1, 5150),
    Prize("B獎 AirPods 2", 1, 3945),
    Prize("C獎 Switch遊戲卡收納包", 7, 135),
    Prize("D獎 Switch收納包 伊布", 7, 160),
    Prize("E獎 Switch收納包 皮卡丘", 7, 140),
    Prize("F獎 衛生棉收納包", 26, 15),
    Prize("G獎 功德按鍵", 40, 10),
    Prize("H獎 手機支架 厚椅款", 40, 6)
]
'''
draw_cost = 1800

def calculate_total_cost(prizes):
    return sum(prize.quantity * prize.cost for prize in prizes)

def simulate_draw(prizes):
    boss_cost = 0
    customer_spending = 0
    round_count = 0
    
    while any(prize.quantity > 0 for prize in prizes[:3]):
        round_count += 1
        chosen_prize = random.choices(prizes, weights=[prize.quantity for prize in prizes])[0]
        chosen_prize.quantity -= 1
        boss_cost += chosen_prize.cost
        customer_spending += draw_cost
        
    return boss_cost, customer_spending, round_count

def simulate_multiple_draws(prizes, simulations):
    boss_costs = []
    customer_costs = []
    customer_wins = 0
    round_counts = []
    boss_profits = []
    
    for _ in range(simulations):
        prizes_copy = [Prize(prize.name, prize.quantity, prize.cost) for prize in prizes]
        boss_cost, customer_spending, round_count = simulate_draw(prizes_copy)
        boss_costs.append(boss_cost)
        customer_costs.append(customer_spending)
        round_counts.append(round_count)
        boss_profits.append(customer_spending - boss_cost)  # 老闆的收益是客戶花費減去老闆成本
        
        if customer_spending < boss_cost:
            customer_wins += 1
            
    return boss_costs, customer_costs, customer_wins, round_counts, boss_profits

total_cost = calculate_total_cost(prizes)
simulations = 10000
boss_costs, customer_costs, customer_wins, round_counts, boss_profits = simulate_multiple_draws(prizes, simulations)

# 設置中文字體
font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")

# 繪製抽獎成本折線圖
plt.plot(range(1, simulations + 1), customer_costs, label='客戶費用')
plt.plot(range(1, simulations + 1), boss_costs, label='老闆成本')
plt.xlabel('抽獎次數', fontproperties=font)
plt.ylabel('成本', fontproperties=font)
plt.title('抽獎成本', fontproperties=font)
plt.legend(prop=font)
plt.grid(True)
plt.show()

print(f"在 {simulations} 次模擬中，客戶獲勝了 {customer_wins} 次。")

# 老闆平均收益
average_boss_profit = sum(boss_profits) / simulations
print(f"老闆平均{simulations}次每次可以賺 {average_boss_profit:.2f} 元。")

# 計算平均抽幾次遊戲會結束
average_rounds = sum(round_counts) / simulations
print(f"平均抽 {average_rounds:.2f} 次遊戲會結束。")
