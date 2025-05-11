import json
class TowerBuilder:
    def __init__(self):
        self.__products = json.dumps({
            'common': dict(image="images/tower/common_foundation.png", damage=2, cost=3, radius=1, improve_cost_array=(4, 6), armor_piercing=False, poison=0, additional_money=2,
                            additional_image="images/tower/common_gun.png"),
            'sniper': dict(image="images/tower/common_foundation.png", damage=4, cost=5, radius=2, improve_cost_array=(6, 8), armor_piercing=False, poison=0, additional_money=0,
                            additional_image="images/tower/sniper_gun.png"),
            'anty_shield': dict(image="images/tower/anty_shield.png", damage=3, cost=4, radius=1.5, improve_cost_array=(5, 7), armor_piercing=True, poison=0, additional_money=0),
            'venom': dict(image="images/tower/venom_foundation.png", damage=2, cost=5, radius=1, improve_cost_array=(4, 6), armor_piercing=False, poison=2, additional_money=0,
                           additional_image="images/tower/venom_gun.png")})