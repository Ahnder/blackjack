# 상위 폴더 파일 import 위한 path 지정
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# import
from gamer import Player


#
def test_receive_card():
    player = Player()
    test_card = 'diamond_9'

    player.receive_card(test_card)
    
    assert len(player.cards) != 0
    assert player.cards[0] == test_card


def test_declare_bust():
    player = Player()

    assert player.bust != True
    
    player.declare_bust()
    assert player.bust == True


def test_declare_stay():
    player = Player()

    assert player.stay != True
    
    player.declare_stay()
    assert player.stay == True
