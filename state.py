from abc import ABC, abstractmethod
from PIL import Image
from image_operation import compare
import operator
from time import sleep


class State(ABC):
    def __init__(self, rects, points=None):
        self.im = Image.open('state_images/{}.png'.format(type(self).__name__))
        self.rects = rects
        self.points = points
        self.boxes = [(x, y, x + w, y + h) for (x, y, w, h) in rects]

    def name(self):
        return type(self).__name__

    @abstractmethod
    def do_automation(self, device, capture):
        pass


class PlayAttackState(State):
    def do_automation(self, device, capture):
        print('tap attack speed / damage')
        device.tap_point(self.points['attack_speed'])
        device.tap_point(self.points['damage'])


class PlayDefenseState(State):
    def do_automation(self, device, capture):
        pass


class PlayUtilityState(State):
    def do_automation(self, device, capture):
        pass


class GameOverState(State):
    def do_automation(self, device, capture):
        print('tap retry')
        device.tap_point(self.points['retry'])


#(x1, y1, x2, y2) 10, 140, 40, 780
states = {
    PlayAttackState(rects=[(10, 780, 140, 40), ], points={'damage': (300, 900), 'attack_speed': (600, 900)}),
    PlayDefenseState(rects=[(10, 780, 140, 40), ]),
    PlayUtilityState(rects=[(10, 780, 140, 40), ]),
    GameOverState(rects=[(180, 1000, 100, 30), ], points={'retry': (230, 1020)})
}

def find_state(capture) -> State:
    scores = {}
    #print(capture)
    #capture.crop((10, 780, 150, 820)).show()
    for idx, s in enumerate(states):
        score = 0
        print(s)
        for box in s.boxes:
            #print(box)
            #cropped_image = s.im.crop(box)
            #cropped_image.show()
            sleep(5)
            score += compare(s.im, capture, box)
        scores[s] = score / len(s.boxes)

    state, score = sorted(scores.items(), key=operator.itemgetter(1))[0]

    if score < 0.01:
        return state
