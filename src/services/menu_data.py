import csv
from models.dish import Dish, Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self.read_file_csv(source_path)

    def read_file_csv(self, source_path: str):
        all_dishes_dict = {}

        with open(source_path, encoding="utf-8") as file:
            reader_file = csv.DictReader(file)

            for row in reader_file:
                dish = row["dish"]
                price = float(row["price"])
                ingredient = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                if dish not in all_dishes_dict:
                    all_dishes_dict[dish] = Dish(dish, price)

                all_dishes_dict[dish].add_ingredient_dependency(
                    Ingredient(ingredient), recipe_amount
                )

        return set(all_dishes_dict.values())
