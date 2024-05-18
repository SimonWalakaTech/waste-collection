class User:
  def __init__(self, name, card_id):
    self.name = name
    self.card_id = card_id
    self.points = 0

  def add_points(self, points):
    self.points += points

class Bin:
  def __init__(self, type):
    self.type = type  # Recycling, Compost, etc.

  def scan_card(self, user):
    if self.type == "Recycling":
      user.add_points(2)
    elif self.type == "Compost":
      user.add_points(1)

# Example Usage
user1 = User("Alice", 12345)
recycling_bin = Bin("Recycling")

recycling_bin.scan_card(user1)
print(f"{user1.name} earned {user1.points} points for recycling!")
