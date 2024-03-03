#
class Rule:
    """게임 진행 룰 상태, 계산 함수 작성"""
    
    # 점수 딕셔너리를 상태로 저장
    # 점수딕셔너리(카드의 끗수에 맞는 점수를 미리 지정해 놓은 딕셔너리)
    def __init__(self):
        self.card_values = {
            'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
            'J': 10, 'Q': 10, 'K': 10
        }


    def cal_score(self, cards: list) -> int:
        """카드 리스트를 입력 받아서 카드의 점수를 합친 총 점수를 반환"""

        # DENO_NUM: 카드의 끗수를 지정하기 위한 상수
        DENO_NUM = -1
        # 
        total_score = 0

        # 카드의 끗수가 card_values의 키로 존재하지 않으면 -1 리턴(추후 에러메세지 추가)
        for card in cards:
            if not self.card_values.get(card[DENO_NUM]):
                return -1
            total_score += self.card_values.get(card[DENO_NUM])

        return total_score


    def check_bust(self, cards: list) -> bool:
        """카드 리스트를 입력 받아 버스트 유무를 bool값으로 반환"""

        # BUST_NUM: 버스트 기준을 지정하기 위한 상수
        BUST_NUM = 21

        return True if self.cal_score(cards) > BUST_NUM else False


    def check_stay(self, cards: list, stay_num: int) -> bool:
        """카드 리스트와 게임 참가자 각자의 stay 기준 정수를 입력 받아 스테이 유무를 bool값으로 반환"""

        return True if self.cal_score(cards) >= stay_num else False
