import random

def run_gambler_simulation():
    stake = int(input("Enter starting Stake ($): "))
    goal = int(input("Enter Goal ($): "))
    trials = int(input("Enter Number of times to run the experiment: "))

    wins = 0
    total_bets = 0

    for i in range(trials):
        cash = stake
        
        while cash > 0 and cash < goal:
            total_bets += 1
            
            if random.random() < 0.5:
                cash += 1  
            else:
                cash -= 1  
       
        if cash == goal:
            wins += 1


    win_percentage = (wins / trials) * 100
    loss_percentage = 100 - win_percentage

    print(f"Total Trials: {trials}")
    print(f"Number of Wins: {wins}")
    print(f"Win Percentage: {win_percentage:.2f}%")
    print(f"Loss Percentage: {loss_percentage:.2f}%")
    print(f"Average bets per trial: {total_bets // trials}")


if __name__ == "__main__":
    run_gambler_simulation()