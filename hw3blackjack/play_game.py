# play_game.py

from DeckOfCards import *

def score_hand(cards):
    """
    Returns the best Blackjack score for a list of Card objects
    by counting aces as 1 or 11 appropriately.
    """
    total = 0
    ace_count = 0
    
    # First pass: add up all values, count how many Aces
    for card in cards:
        total += card.val
        if card.face == "Ace":
            ace_count += 1
    
    # If we are over 21 but have an Ace, reduce total by 10 for each Ace if possible
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
        
    return total

def main():
    print("Welcome to Black Jack!\n")
    
    # Create the deck of cards (52 cards)
    deck = DeckOfCards()
    
    # Loop to allow multiple games
    while True:
        # Print deck before shuffle
        print("deck before shuffled:\n")
        deck.print_deck()
        
        # Shuffle the deck
        deck.shuffle_deck()
        
        # Print deck after shuffle
        print("\ndeck after shuffled:\n")
        deck.print_deck()
        print()
        
        # Deal two cards to the user
        user_cards = []
        for i in range(2):
            c = deck.get_card()
            user_cards.append(c)
            print(f"Card number {i+1} is: {c.face} of {c.suit}")
        
        # Calculate and display user's total
        user_score = score_hand(user_cards)
        print(f"\nYour total score is: {user_score}")
        
        # User hits
        card_count = 2
        while user_score <= 21:
            ans = input("Would you like a hit?(y/n) ")
            if ans.lower() == 'y':
                card_count += 1
                new_card = deck.get_card()
                user_cards.append(new_card)
                print(f"\nCard number {card_count} is: {new_card.face} of {new_card.suit}")
                
                # Recompute score
                user_score = score_hand(user_cards)
                
                # If this card is an Ace, show the special message
                if new_card.face == "Ace":
                    print(f"You got an Ace. Your total score is: {user_score}")
                else:
                    print(f"Your total score is: {user_score}")
                
                # Check if busted
                if user_score > 21:
                    break
            else:
                break
        
        # If user busts
        if user_score > 21:
            print("\nYou busted, you lose!")
        else:
            # Deal two cards to the dealer
            dealer_cards = []
            dealer_cards.append(deck.get_card())
            dealer_cards.append(deck.get_card())
            
            print(f"\nDealer card number 1 is: {dealer_cards[0].face} of {dealer_cards[0].suit}")
            print(f"Dealer card number 2 is: {dealer_cards[1].face} of {dealer_cards[1].suit}")
            
            # Dealer keeps hitting while under 17
            dealer_score = score_hand(dealer_cards)
            dealer_card_count = 2
            while dealer_score < 17:
                dealer_card_count += 1
                hit_card = deck.get_card()
                dealer_cards.append(hit_card)
                print(f"\nDealer hits, card number {dealer_card_count} is: {hit_card.face} of {hit_card.suit}")
                dealer_score = score_hand(dealer_cards)
            
            print(f"\nDealer score is: {dealer_score}")
            
            # Determine win or lose
            if dealer_score > 21:
                print("Dealer Busted, you win!!!")
            else:
                # Compare scores
                if user_score > dealer_score:
                    print("Your score is higher, you win!!!")
                elif user_score == dealer_score:
                    # Tie means dealer is "equal or higher"
                    print("Dealer score is equal or higher, you lose!")
                else:
                    # dealer_score > user_score
                    print("Dealer score is higher, you lose!")
        
        # Ask for another game
        play_again = input("\nanother game?(y/n): ")
        if play_again.lower() != 'y':
            print("\nProcess exited with code: 0")
            break

# Run the main function when this file is executed drectly
if __name__ == "__main__":
    main()
