class FiveCardRanksInRowValidator():
    @property
    def _collections_of_five_straight_cards_in_a_row(self):
        index = 0 # starts at 0
        final_index = len(self.cards) - 1 #final index in a list is one less than the length -> ends at 6 (total of 7 cards)
        collections_of_five_straight_cards_in_a_row = []


        while index + 4 <= final_index:
            next_five_cards = self.cards[index: index + 5]
            next_five_indices = [card.rank_index for card in next_five_cards]
            

            if self._every_element_increasing_by_1(next_five_indices):
                collections_of_five_straight_cards_in_a_row.append(next_five_cards)

            index += 1
        return collections_of_five_straight_cards_in_a_row

    def _every_element_increasing_by_1(self, rank_indexes):
        # rank_indexes = [card.rank_index for card in self.cards]

        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]
        straight_consecutive_indexes = list(range(starting_rank_index, last_rank_index + 1))
        return rank_indexes == straight_consecutive_indexes