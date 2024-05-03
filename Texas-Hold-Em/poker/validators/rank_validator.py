class RankValidator():
    def _ranks_with_count(self, count):
        return {
            key: value 
            for key, value in self._card_rank_counts.items() 
            if value == count
        }
    
    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts