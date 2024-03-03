# import
import random

#
class Card:
    """블랙잭 게임에 쓰일 카드의 무늬와 끗수 관리 및 생성 되는 카드의 형태 관리"""
    def __init__(self):
        # suits = 카드의 무늬 리스트
        # denos = 카드의 끗수 리스트
        self.suits = ['spade', 'heart', 'diamond', 'clover']
        self.denos = list('A23456789TJQK')


    def make_card(self, suit: str, deno: str) -> str:
        """무늬와 끗수를 조합하여 하나의 카드(str)로 출력"""

        return suit + '_' + deno


#
class CardDeck(Card):
    """카드덱을 저장하고, 랜덤하게 순서를 섞고, 카드를 드로우한다"""
    def __init__(self) -> None:
        super().__init__()
        self.deck = []


    def make_new_deck(self) -> list:
        """총 52장으 카드로 구성 된 덱(list)을 생성"""

        self.deck = [
            self.make_card(suit, deno)
            for suit in self.suits
            for deno in self.denos
        ]


    def shuffle_deck(self):
        """덱을 랜덤하게 섞는다"""

        # 덱이 비어있는 경우의 오류를 대비하기 위한 임시 코드
        if not self.deck:
            return -1

        random.shuffle(self.deck)


    def draw_card(self):
        """덱의 맨 윗장 카드를 드로우"""

        # 덱이 비어있는 경우의 오류를 대비하기 위한 임시 코드
        if not self.deck:
            return -1

        return self.deck.pop()
