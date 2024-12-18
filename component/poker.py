import threading
from enum import Enum





class PokerSuit(Enum):
    """
    黑桃spade,红桃heart,方片diamond,梅花club
    """


    NONE = 0
    SPADE = 1
    HEART = 2
    DIAMOND = 3
    CLUB = 4

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

ALL_SUITS = [PokerSuit.SPADE, PokerSuit.HEART, PokerSuit.DIAMOND, PokerSuit.CLUB]
SUIT_TO_STR = {
        PokerSuit.CLUB: '♣',
        PokerSuit.HEART: '♥',
        PokerSuit.DIAMOND: '♦',
        PokerSuit.SPADE: '♠',
    }

class PokerRank(Enum):
    """
    BLOCK_JOCKER = small jocker
    COLORED_JOCKER = big jocker
    """
    TWO =2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    BLACK_JOCKER = 15
    COLORED_JOCKER = 16

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value


    def __lt__(self, other):
        return self.value < other.value

ALL_RANKS = [PokerRank.TWO, PokerRank.THREE, PokerRank.FOUR, PokerRank.FIVE,
            PokerRank.SIX, PokerRank.SEVEN, PokerRank.EIGHT, PokerRank.NINE,
            PokerRank.TEN, PokerRank.JACK, PokerRank.QUEEN, PokerRank.KING,
            PokerRank.ACE, PokerRank.BLACK_JOCKER, PokerRank.COLORED_JOCKER]

RANKS_WITHOUT_JOCKER =  [PokerRank.TWO, PokerRank.THREE, PokerRank.FOUR, PokerRank.FIVE,
            PokerRank.SIX, PokerRank.SEVEN, PokerRank.EIGHT, PokerRank.NINE,
            PokerRank.TEN, PokerRank.JACK, PokerRank.QUEEN, PokerRank.KING,
            PokerRank.ACE]

asd = {
    PokerRank.TWO: 1,
}

RANK_TO_STR = {
    PokerRank.TWO: "2", PokerRank.THREE: "3", PokerRank.FOUR: "4", PokerRank.FIVE: "5",
    PokerRank.SIX: "6", PokerRank.SEVEN: "7", PokerRank.EIGHT: "8", PokerRank.NINE: "9",
    PokerRank.TEN: "10",PokerRank.JACK:"J", PokerRank.QUEEN: "Q", PokerRank.KING: "K",
    PokerRank.ACE: "A",PokerRank.BLACK_JOCKER: "S Jocker", PokerRank.COLORED_JOCKER: "B Jocker"
    }

class PokerCard:

    """
    pocker entity, unchangeable type
    any instantiation will be cached(lazy initialization)
    ensure thread safety
    """

    __slots__ = ('__suit', '__rank')



    __singletons = {}

    __lock = threading.Lock()

    @classmethod
    def build(cls, rank: PokerRank, suit: PokerSuit = None):
        """
        static factory function
        """
        # basic concurrent safety
        with cls.__lock:
            if (suit, rank) not in cls.__singletons:
                # lazy init
                instance = super().__new__(cls)
                cls.__singletons[suit, rank] = instance
                instance.__init(rank=rank, suit=suit)

        return cls.__singletons[suit, rank]

    def __init__(self):
        raise RuntimeError("unsupported, use factory builder")

    def __init(self, rank: PokerRank, suit: PokerSuit = None):
        """
               :param suit: 花色
               :param rank: 点数
               """

        assert suit in PokerSuit
        assert rank in PokerRank

        if rank in (PokerRank.COLORED_JOCKER, PokerRank.BLACK_JOCKER):
            self.__suit = PokerSuit.NONE
        else:
            assert suit != PokerSuit.NONE

        self.__suit: PokerSuit = suit
        self.__rank: PokerRank = rank

    def __str__(self):
        if self.suit == PokerRank.COLORED_JOCKER:
            return "Colored Joker"
        elif self.suit == PokerRank.BLACK_JOCKER:
            return "Black Joker"
        else:
            return f"{SUIT_TO_STR[self.__suit]} {RANK_TO_STR[self.__rank]}"




    def __repr__(self):
        return self.__str__()




    @property
    def suit(self):
        return self.__suit



    @property
    def rank(self):
        return self.__rank



    @property
    def pocker(self) -> tuple[PokerSuit, PokerRank]:
        return self.suit, self.rank

    def __hash__(self):
        return hash((self.suit, self.rank))

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank


    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank



class GameHand:
    """
    dealt card, could be one or more cards
    """

    __slots__ = '__hand'


    def __init__(self, cards: list[PokerCard], sort: bool = False):
        """
        :param cards: hand cards
        :param sort: whether sorting is required
        """
        self.__hand: list[PokerCard] = cards[:]
        if sort:
            self.__hand.sort()

    def __str__(self):
        return f"{self.__hand}"

    def __repr__(self):
        return f"{self.__hand}"


    @property
    def cards(self) -> tuple[PokerCard, ...]:
        """
        notice: result is readonly
        :return: hand cards but tuple
        """
        return tuple(self.__hand)


    @property
    def cards_amount(self) -> int:
        return len(self.__hand)



    def remove_card(self, card: PokerCard):
        self.__hand.remove(card)



    def add_card(self, card: PokerCard):
        self.__hand.append(card)


