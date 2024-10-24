"""Alchemy."""
from collections import Counter
from copy import copy
from typing import Any


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """

    def __init__(self, name: str) -> None:
        """Do."""
        self.name = name

    def __repr__(self) -> str:
        """Do."""
        return f'<AE: {self.name}>'


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.storage: list[AlchemicalElement] = list()

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in TypeError exception.

        :param element: Input object to add to storage.
        """
        if not isinstance(element, AlchemicalElement):
            raise TypeError

        self.storage.append(element)

    def pop(self, element_name: str) -> AlchemicalElement or None:
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        last_inserted = None

        # iterate elements starting from the end
        for element in self.storage[::-1]:
            # if element matches the searched name
            if element.name == element_name:
                last_inserted = element
                break

        if last_inserted is not None:
            self.storage.remove(last_inserted)
        return last_inserted

    def extract(self) -> list[AlchemicalElement]:
        """
        Return a list of all of the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            storage.extract() # -> [<AE: Water>, <AE: Fire>]
            storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted
         everything.

        :return: A list of all of the elements that were previously in the storage.
        """
        to_return = copy(self.storage)
        self.storage.clear()
        return to_return

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            print(storage.get_content())

        Output in console:
            Content:
             * Fire x 1
             * Water x 1

        The elements must be sorted alphabetically by name.

        :return: Content as a string.
        """
        output = 'Content:\n'

        sorted_storage = sorted(self.storage, key=lambda element: element.name)
        element_counter = Counter(element.name for element in sorted_storage)

        if len(element_counter) == 0:
            output += ' Empty.'
            return output

        for name, count in element_counter.items():
            output += f' * {name} x {count}\n'

        return output.rstrip("\n")


def _contains_duplicates(element_list: list[Any]) -> bool:
    unique_elements = set()
    for element in element_list:
        if element in unique_elements:
            return True
        else:
            unique_elements.add(element)
    return False


class AlchemicalRecipes:
    """AlchemicalRecipes class."""

    def __init__(self):
        """
        Initialize the AlchemicalRecipes class.

        Add whatever you need to make this class function.
        """
        self.recipes: dict[tuple[str, str], str] = dict()

    def add_recipe(self, first_component_name: str, second_component_name: str, product_name: str):
        """
        Determine if recipe is valid and then add it to recipes.

        A recipe consists of three strings, two components and their product.
        If any of the parameters are the same, raise the 'DuplicateRecipeNamesException' exception.
        If there already exists a recipe for the given pair of components, raise the 'RecipeOverlapException' exception.

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :param product_name: The name of the product element.
        """
        if _contains_duplicates([first_component_name, second_component_name, product_name]):
            raise DuplicateRecipeNamesException

        product_ingredients: tuple[str, str] = (first_component_name, second_component_name)
        if product_ingredients in self.recipes or product_ingredients[::-1] in self.recipes:
            raise RecipeOverlapException

        self.recipes[product_ingredients] = product_name

    def get_product_name(self, first_component_name: str, second_component_name: str) -> str | None:
        """
        Return the name of the product for the two components.

        The order of the first_component_name and second_component_name is interchangeable, so search for combinations
        of (first_component_name, second_component_name) and (second_component_name, first_component_name).

        If there are no combinations for the two components, return None

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            recipes.get_product_name('Water', 'Wind')  # ->  'Ice'
            recipes.get_product_name('Wind', 'Water')  # ->  'Ice'
            recipes.get_product_name('Fire', 'Water')  # ->  None
            recipes.add_recipe('Water', 'Fire', 'Steam')
            recipes.get_product_name('Fire', 'Water')  # ->  'Steam'

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :return: The name of the product element or None.
        """
        if (normal_order := (first_component_name, second_component_name)) in self.recipes:
            return self.recipes[normal_order]
        if (reversed_order := (second_component_name, first_component_name)) in self.recipes:
            return self.recipes[reversed_order]
        return None


class DuplicateRecipeNamesException(Exception):
    """Raised when attempting to add a recipe that has same names for components and product."""


class RecipeOverlapException(Exception):
    """Raised when attempting to add a pair of components that is already used for another existing recipe."""


class Cauldron(AlchemicalStorage):
    """
    Cauldron class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Cauldron class."""
        super().__init__()
        self.recipes = recipes

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can combine with anything already inside.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            cauldron = Cauldron(recipes)
            cauldron.add(AlchemicalElement('Water'))
            cauldron.add(AlchemicalElement('Wind'))
            cauldron.extract() # -> [<AE: Ice>]

        :param element: Input object to add to storage.
        """
        super().add(element)


if __name__ == '__main__':
    element_one = AlchemicalElement('Fire')
    element_two = AlchemicalElement('Water')
    element_three = AlchemicalElement('Water')
    storage = AlchemicalStorage()

    print(element_one)  # <AE: Fire>
    print(element_two)  # <AE: Water>

    storage.add(element_one)
    storage.add(element_two)

    print(storage.get_content())
    # Content:
    #  * Fire x 1
    #  * Water x 1

    print(storage.extract())  # [<AE: Fire>, <AE: Water>]
    print(storage.get_content())
    # Content:
    #  Empty

    storage.add(element_one)
    storage.add(element_two)
    storage.add(element_three)

    print(storage.pop('Water') == element_three)  # True
    print(storage.pop('Water') == element_two)  # True

    recipes = AlchemicalRecipes()
    recipes.add_recipe('Fire', 'Water', 'Steam')
    recipes.add_recipe('Fire', 'Earth', 'Iron')
    recipes.add_recipe('Water', 'Iron', 'Rust')

    print(recipes.get_product_name('Water', 'Fire'))  # -> 'Steam'

    try:
        recipes.add_recipe('Fire', 'Something else', 'Fire')
        print('Did not raise, not working as intended.')

    except DuplicateRecipeNamesException:
        print('Raised DuplicateRecipeNamesException, working as intended!')

    try:
        recipes.add_recipe('Fire', 'Earth', 'Gold')
        print('Did not raise, not working as intended.')

    except RecipeOverlapException:
        print('Raised RecipeOverlapException, working as intended!')

    cauldron = Cauldron(recipes)
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Water'))
    cauldron.add(AlchemicalElement('Fire'))

    print(cauldron.extract())  # -> [<AE: Earth>, <AE: Steam>]

    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('Water'))

    print(cauldron.extract())  # -> [<AE: Earth>, <AE: Iron>, <AE: Rust>]
