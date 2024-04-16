from csv import DictReader
from typing import Dict
import csv

from src.models.dish import Recipe, Dish
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)
        self.path = inventory_file_path

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        with open("data/inventory_base_data.csv", encoding="utf-8") as file:
            inventory_data = csv.DictReader(file)
            inventory = {}

            for row in inventory_data:
                ingredient_name = row["ingredient"]
                initial_amount = int(row["initial_amount"])
                inventory[ingredient_name] = initial_amount

        return all(
            self.inventory.get(ingredient)
            and self.inventory.get(ingredient) >= int(recipe[ingredient])
            for ingredient in recipe
        )

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        if self.check_recipe_availability(recipe):
            for ingredient in recipe:
                self.inventory[ingredient] -= recipe[ingredient]

        else:
            raise ValueError


if __name__ == "__main__":

    teste = InventoryMapping()
    test_dish2 = Dish("Carbonara", 20)
    test_dish2.add_ingredient_dependency(Ingredient("ovo"), 10)
    test_dish2.add_ingredient_dependency(Ingredient("bacon"), 10)
    test_dish2.add_ingredient_dependency(Ingredient("limão"), 10)
    test_dish2.add_ingredient_dependency(Ingredient("fermento"), 10)

    teste.consume_recipe(test_dish2.recipe)
