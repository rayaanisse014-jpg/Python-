cost_per_track = int(input('Cost in cents to download one track: '))
available_budget = int(input('Available budget (dollars): '))
downloaded_track = int(input('Number of tracks already downloaded: '))

## Calculate amount spent 
amount_spent = cost_per_track * downloaded_track

## Convert budget to cent 
budget_cent = available_budget * 100

## Calculate remaining_balance 
remaining_balance = budget_cent - amount_spent 

## Calulate additional tracks that can be purchased 
additional_track = remaining_balance // cost_per_track

## Display result 
print(f"You have enough money left for {additional_track} tracks.")

