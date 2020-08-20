import random

class Node:

    def __init__(self, colour, number, next = None):

        self.colour = colour
        self.number = number
        self.next = next

    def get_colour(self):
        return self.colour

    def get_number(self):
        return self.number

    def get_next(self):
        return self.next

    def set_colour(self, colour):
        self.colour = colour

    def set_number(self, number):
        self.number = number

    def set_next(self, next):
        self.next = next

class Stack:

    def __init__(self, limit):
        self.top = None
        self.limit = limit
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.limit

    def peek(self):
        return self.top

    def pop(self):
        if self.is_empty():
            print("Stack is Empty!")
        else:
            card_to_remove = self.top
            self.top = card_to_remove.get_next()
            self.length -= 1
            return f"{card_to_remove.get_colour()}-{card_to_remove.get_number()}"

    def push(self, colour, number):
        if self.is_full():
            print("Stack is Full!")

        else:
            new_card = Node(colour, number)
            new_card.set_next(self.top)
            self.top = new_card
            self.length += 1


game = Stack(20)

card_colours = ["red", "blue", "green", "yellow"]
card_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
card_in_deck = []

while not game.is_full():
    card_colour = random.choice(card_colours)
    card_num = random.choice(card_numbers)

    if not [card_colour, card_num] in card_in_deck:
        game.push(card_colour, card_num)
        card_in_deck.append([card_colour, card_num])



print("-"*15)
print("Player 1: ")
print("-"*15)
print(f"1- {game.pop()}\n2- {game.pop()}\n3- {game.pop()}\n4- {game.pop()}\n5- {game.pop()}")
print("-"*15)
print("Player 2: ")
print("-"*15)
print(f"1- {game.pop()}\n2- {game.pop()}\n3- {game.pop()}\n4- {game.pop()}\n5- {game.pop()}\n\n")

print("-"*15)
print(f"First card in deck: {game.peek().get_colour()}-{game.peek().get_number()}")
print("-"*15)
