ch = "y"
bid = {}


def bidder():
    name = input("Enter Your name: ")
    bid_amt = int(input("Enter Your Bid: "))
    bid[name] = bid_amt
    ch = input("Do you want to continue y/n")

    if ch == "y":
        bidder()
    else:
      bidder_price =0
      for x , y in bid.items():
        if bidder_price < y:
          bidder_name = x
          bidder_price = y
        else:
          print(f"Higgest bidder is {bidder_name} with Rs {bidder_price}")


bidder()