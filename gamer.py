#
class Gamer:
    def __init__(self):
        self.cards = []
        self.stay = False
        self.bust = False


    def receive_card(self, card: str):
        """카드 한장을 받아서 cards에 추가"""

        self.cards.append(card)


    def declare_bust(self):
        """bust를 True로 변경"""

        self.bust = True


    def declare_stay(self):
        """stay를 True로 변경"""

        self.stay = True


#
class Dealer(Gamer):
    # 딜러는 자신의 카드들의 총 스코어가 17이 넘으면 stay를 선언하고 드로우를 멈춘다
    def __init__(self):
        super().__init__()
        self.stay_number = 17


#
class Player(Gamer):
    """플레이어 클래스, 플레이어만의 기능을 추가하기 전 까지는 pass로 클래스만 설정"""
    pass
