from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient_test1 = Ingredient("bacon")
    ingredient_test2 = Ingredient("ovo")
    ingredient_test3 = Ingredient("carne")
    ingredient_test4 = Ingredient("carne")

    assert ingredient_test1 != ingredient_test3
    assert ingredient_test3 == ingredient_test4
    assert ingredient_test2 != ingredient_test1

    assert ingredient_test1.name == "bacon"

    assert repr(ingredient_test1) == "Ingredient('bacon')"
    assert hash(ingredient_test1) != hash(ingredient_test4)
    assert hash(ingredient_test3) == hash(ingredient_test4)
    assert ingredient_test2.restrictions == {Restriction.ANIMAL_DERIVED}
