import random
from abc import ABC, abstractmethod

from component.poker import GameHand, PokerRank, PokerCard, ALL_SUITS, RANKS_WITHOUT_JOCKER


class InsufficientCardsError(Exception):
    pass

class PokerSender(ABC):

    __slots__ = ('_pokers',)

    def __init__(self):
        self._pokers = []

    @abstractmethod
    def get_pocker(self, n: int) -> list[GameHand]:
        """
        send pokers
        :param n: sets of card
        :return: n sets of cards
        """
        pass

    def left_card_amount(self):
        return len(self._pokers)

    def __build_pokers(self, jocker=False):
        for suit in ALL_SUITS:
            for rank in RANKS_WITHOUT_JOCKER:
                poker = PokerCard.build(suit=suit, rank=rank)
                self._pokers.append(poker)

        if jocker:
            self._pokers.append(PokerCard.build(PokerRank.BLACK_JOCKER))
            self._pokers.append(PokerCard.build(PokerRank.COLORED_JOCKER))

    def _init_pokers(self, jocker=False, card_set=1):
        self._pokers = []
        for _ in range(card_set):
            self.__build_pokers(jocker=jocker)









class ZhaJinHuaPokerSender(PokerSender):

    """
    炸金花 没有英文名字
    unable to ensure threading safety
    """

    def __init(self, random_generator):

        super()._init_pokers(jocker=False, card_set=self.__card_set)
        random_generator.shuffle(self._pokers)


    def __init__(self, card_set=1, random_generator=random.Random()):
        super().__init__()

        assert card_set > 0

        self.__card_set = card_set
        self.__random_generator = random_generator

        self.__init(random_generator=random_generator)


    def get_pocker(self, n: int) -> list[GameHand]:
        pokers = super()._pokers

        if 3 * n > len(pokers):
            raise InsufficientCardsError()

        # 0 -4:-1; 1 -7:-4; 2 -10:-7
        hand_cards = [GameHand(pokers[-3 * i - 1:-3 * i - 4:-1], True) for i in range(n)]
        del pokers[-3 * (n - 1) - 3:]

        return hand_cards

    def reload(self):
        self.__init(self.__random_generator)

if __name__ == '__main__':
    sender = ZhaJinHuaPokerSender(card_set=3)

    count = {}
    for _ in range(52):
        pocker_ = sender.get_pocker(1)[0]
        for card in pocker_.cards:
            count[card] = count.get(card, 0) + 1
    for e in count:
        print(e, ":", count[e])

