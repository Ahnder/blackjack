# 상위 폴더 파일 import 위한 path 지정
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# import
from carddeck import Card, CardDeck


def test_make_card():
    card = Card()

    test_suit = 'clover'
    test_deno = 'K'
    expected = 'clover_K'

    assert card.make_card(test_suit, test_deno) != 'clover K'
    assert card.make_card(test_suit, test_deno) == expected


def test_make_new_deck():
    deck = CardDeck()

    deck.make_new_deck()

    assert len(deck.deck) != 0
    assert len(deck.deck) == 52


def test_shuffle_deck():
    deck = CardDeck()
    
    # 덱이 비어있을 시 확인(임시로 -1이 출력됨, 덱이 비어있을 시 기능 추가 후 다시 작성해야 함)
    assert deck.shuffle_deck() == -1
    # 덱 생성 후 확인
    deck.make_new_deck()
    temp_deck = deck.deck[:]
    deck.shuffle_deck()

    assert deck.deck != temp_deck


def test_draw_card():
    deck = CardDeck()
    
    # 덱이 비어있을 시 확인(임시로 -1이 출력됨, 덱이 비어있을 시 기능 추가 후 다시 작성해야 함)
    assert deck.shuffle_deck() == -1
    # 덱 생성 후 확인
    deck.make_new_deck()
    # 카드 드로우 메서드로 리스트의 pop을 사용하므로 리스트의 마지막 요소로 테스트
    expected_card = deck.deck[-1]
    test_card = deck.draw_card()

    assert type(test_card) == str
    assert test_card == expected_card
 