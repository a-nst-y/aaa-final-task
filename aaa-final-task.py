import click
import random
from pizza import Margherita, Pepperoni, Hawaiian


def log(text):
    def decorator(func):
        """Декоратор, выводящий время исполения указанного действия"""
        def wrapper(*args, **kwargs):
            random_time = random.randint(1, 10)
            print(text + str(random_time) + 'с!')
        return wrapper
    return decorator


@log('Приготовили за ')
def bake(pizza):
    """Готовит пиццу"""


@log('Доставили за ')
def delivered(pizza):
    """Доставляет пиццу"""


@click.group()
def cli():
    pass


@cli.command(name='order')
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', type=str)
@click.argument('size', type=str)
def order(pizza: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    print(f'Your order: pizza - {pizza}, size - {size}')
    bake(pizza)
    if delivery:
        delivered(pizza)


@cli.command(name='menu')
def menu():
    """Выводит меню"""
    print(margherita.open_in_menu())
    print(pepperoni.open_in_menu())
    print(hawaiian.open_in_menu())

if __name__ == '__main__':
    margherita = Margherita('pizza', ['ingredients'])
    pepperoni = Pepperoni('pizza', ['ingredients'])
    hawaiian = Hawaiian('pizza', ['ingredients'])
    cli()
