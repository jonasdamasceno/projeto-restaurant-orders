from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    test_dish1 = Dish("Petit gateau", 30)
    test_dish2 = Dish("Carbonara", 20)
    test_dish3 = Dish("Petit gateau", 30)

    test_dish2.add_ingredient_dependency(Ingredient("ovo"), 1)
    test_dish2.add_ingredient_dependency(Ingredient("bacon"), 10)

    assert test_dish2.get_ingredients() == {
        Ingredient("ovo"),
        Ingredient("bacon"),
    }

    assert test_dish2.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert test_dish1.name == "Petit gateau"
    assert hash(test_dish1) != hash(test_dish2)
    assert hash(test_dish3) == hash(test_dish1)
    assert test_dish1 != test_dish2
    assert test_dish1 == test_dish3

    assert repr(test_dish1) == "Dish('Petit gateau', R$30.00)"

    with pytest.raises(TypeError):
        Dish("Parmegiana", "Teste")

    with pytest.raises(ValueError):
        Dish("Parmegiana", -3)
