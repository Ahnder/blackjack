# 상위 폴더 파일 import 위한 path 지정
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# import
from rule import Rule


#
def test_cal_score():
    rule = Rule()

    error_cards = ['clover_K', 'heart_U', 'diamond_8']
    test_cards = ['clover_K', 'heart_A', 'diamond_8']
    expected_score = 19
    
    # 에러 테스트 결과는 추후 에러 메세지 업데이트 후 변경 해야 함
    assert rule.cal_score(error_cards) == -1
    assert rule.cal_score(test_cards) == expected_score


#
def test_check_bust():
    rule = Rule()

    bust_cards = ['clover_K', 'heart_5', 'diamond_8']
    not_bust_cards = ['clover_K', 'heart_5', 'diamond_6']

    assert rule.check_bust(bust_cards) == True
    assert rule.check_bust(not_bust_cards) == False

#
def test_check_stay():
    rule = Rule()

    test_stay_num = 17
    stay_cards = ['clover_K', 'heart_5', 'diamond_2']
    not_stay_cards = ['clover_K', 'heart_5', 'diamond_A']

    assert rule.check_stay(stay_cards, test_stay_num) == True
    assert rule.check_stay(not_stay_cards, test_stay_num) == False
