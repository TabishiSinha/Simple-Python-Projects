from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
max=0
to_continue=True
bidding_chart={}
while(to_continue):
  name=input("Enter your name: ")
  bid=int(input("Enter your bid: $ "))
  clear()
  bidding_chart[name]=bid
  result=input("Are there more bidders? Type yes or no: ").lower()
  if result=='no':
    to_continue=False
key_list=list(bidding_chart.keys())
val_list=list(bidding_chart.values())
for m in bidding_chart.values():
  if m>max:
    max=m

position=val_list.index(max)
name=key_list[position]
print(bidding_chart)
print(f"The maximum bid is ${max} by {name}.")
