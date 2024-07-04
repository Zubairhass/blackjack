class cardCounter(object):
    def __init__(self):
        
        while True:
            try:
                decks = int(input('How many decks are being used? '))
                if decks < 1 or decks > 8:
                    print("That's not a valid number of decks!")
                    continue
                break
            except ValueError:
                print("Please input valid number not string!")
                continue
        
        num_cards = decks * 52

        count = 0

        while True:
            card_value = input('What is card value? (Enter "done" to finish) ')
            
            if card_value.lower().strip() == 'done':
                break
            elif card_value.lower().strip() in ['k', 'q', 'j']:
                card_value = 10
            elif card_value.lower().strip() in ['a', '1']:
                card_value = 11

            try:
                card_value = int(card_value)
            except ValueError:
                print("That's not a valid card!")
                continue

            if card_value < 1 or card_value > 11:
                print("That's not a valid card!")
                continue

            if card_value in [10, 11]:
                count -= 1
            elif card_value in [2, 3, 4, 5, 6]:
                count += 1
            
            num_cards -= 1
            half_decks = round(num_cards/52 * 2)/2

            print('Running Count: ', count)
            print('True Count: ', round(count/max(half_decks, 0.5)))

card_counter = cardCounter()
print(card_counter)