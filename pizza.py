class Pizza:
    """Класс для создания рецептов пиццы по имени и ингридиентам"""
    def __init__(self, name: str, ingredients: list):
        self.name = name
        self.ingredients = ingredients

    def show_ingredients(self):
        """Возвращает рецепт пиццы в виде словаря"""
        pizza_recipe = {self.name: self.ingredients}
        return pizza_recipe


class Margherita(Pizza):
    """класс для пиццы маргарита"""
    def __init__(self,  name: str, ingredients: list):
        super().__init__(name='Margherita🧀',
                         ingredients=['tomato sauce',
                                      'mozzarella',
                                      'tomatoes'])

    def open_in_menu(self):
        for key, value in Pizza.show_ingredients(self).items():
            return key + ': ' + ', '.join(value)


class Pepperoni(Pizza):
    """Класс для пиццы пепперони"""
    def __init__(self,  name: str, ingredients: list):
        super().__init__(name='Pepperoni🍕',
                         ingredients=['tomato sauce',
                                      'mozzarella',
                                      'pepperoni'])

    def open_in_menu(self):
        for key, value in Pizza.show_ingredients(self).items():
            return key + ': ' + ', '.join(value)


class Hawaiian(Pizza):
    """класс для гавайской пиццы"""
    def __init__(self,  name: str, ingredients):
        super().__init__(name='Hawaiian🍍',
                         ingredients=['tomato sauce',
                                      'mozzarella',
                                      'chicken',
                                      'pineapple'])

    def open_in_menu(self):
        """"""
        for key, value in Pizza.show_ingredients(self).items():
            return key + ': ' + ', '.join(value)


if __name__ == '__main__':
    Margherita(Pizza)
    Pepperoni(Pizza)
    Hawaiian(Pizza)
