import pygame
from ProductClass import Product

class ConfigShop:

    def __init__(self, scale_products):
        self.towers_object_array = []
        self.button_update_array = []
        self.scale_products = scale_products
        self.tower_characteristic_image = (pygame.transform.scale(pygame.image.load('images/UI/up/damageUpUp.png'), (100, 100)),
                                      pygame.transform.scale(pygame.image.load('images/UI/up/radiusUpUp.png'), (100, 100)))
        self.imageShop = pygame.transform.scale(pygame.image.load('images/UI/shopBackground.png'), (1000 * 0.4, 1000))
        self.products = [Product("images/tower/commonFoundation.png", 3, scale_products, (20, 150), 2, 170, (4, 6), False, 0, "images/tower/commonGun.png"),  # coordinate = (20, 150 + i * 120)
                    Product("images/tower/sniperFoundation.png", 5, scale_products, (20, 270), 4, 230, (6, 8), False, 0, "images/tower/sniperGun.png"),
                    Product("images/tower/antyShield.png", 4, scale_products, (20, 390), 3, 200, (5, 7), True, 0),
                    Product("images/tower/venomFoundation.png", 5, scale_products, (20, 510), 2, 170, (6, 8), False, 2, "images/tower/venomGun.png")]

    def get_towers_object_array(self):
        return self.towers_object_array

    def get_button_update_array(self):
        return self.button_update_array

    def new_value_towers_object_array(self, new_value):
        self.towers_object_array = new_value

    def new_value_update_array(self, new_value):
        self.button_update_array = new_value

    def get_scale_products(self):
        return self.scale_products

    def get_tower_characteristic_image(self):
        return self.tower_characteristic_image

    def get_imageShop(self):
        return self.imageShop

    def get_products(self):
        return self.products