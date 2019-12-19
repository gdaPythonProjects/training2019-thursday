import click
import json
import sys
import os

from managers.requester import Requester
from managers.interpreter import Interpreter
from analyzers.weather import WeatherAnalyzer
from analyzers.ploter import Ploter


@click.group()
def cli():
    """ Simple weather app in python """
    pass


@cli.command()
@click.option("--city", required=True, type=str, help="City name")
def get(city):
    """ This command prints weather in given city """
    requester = Requester()
    weather = requester.get_weather(city)
    print(weather)


@cli.command()
@click.option("--city", required=True, type=str, help="City name")
def save(city):
    """ Save command saves weather to .wea file"""
    requester = Requester()
    weather = requester.get_weather(city)
    with open("{}.wea".format(city), "w") as f:
        json.dump(weather.__dict__, f, indent=4)


def get_cities_from_files(directory):
    cities = []
    for i in os.listdir(directory):
        if i.endswith("wea"):
            with open(os.path.join(directory, i)) as f:
                cities.append(Interpreter.from_file(json.load(f)))
    return cities


@cli.command()
@click.option("--coldest", is_flag=True, help="Returns info about coldest city")
@click.option("--verbose", is_flag=True, help="Also print every city")
@click.option("--directory", type=str, required=True, default=sys.path[0])
def analyze(coldest, directory, verbose):
    cities = get_cities_from_files(directory)
    analyzer = WeatherAnalyzer(cities)
    if verbose:
        analyzer.print_all_weathers()
    if coldest:
        analyzer.coldest()


@cli.command()
@click.option("--directory", type=str, required=True, default=sys.path[0])
def plot(directory):
    cities = get_cities_from_files(directory)
    analyzer = Ploter(cities)
    analyzer.temperature_plot()


if __name__ == "__main__":
    cli()
