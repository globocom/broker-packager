import os
import re
import click
from python.manager import PyManager
from r.manager import RManager
from broker import BrokerConnector


@click.group()
def bus():
    pass


@bus.command()
@click.option('--language', '-l', help='Language name', type=click.Choice(['python', 'r']), required=True)
@click.option('--name', '-n', help='Package Name', required=True)
@click.option('--version', '-v', help='Package Version', default="")
def install(language, name, version):
    click.echo(name+" python")

@bus.command()
@click.option('--endpoint', '-e', help='Bus Endpoint', default='localhost')
@click.option('--port', '-p', help='Bus Port', type=click.INT, default=61613)
@click.option('--destination', '-d', help='Bus Destination', required=True)
@click.option('--selector', '-s', help='Bus Header Selector')
@click.option('--python_json_path', '-p', help='Python packages json list path', default="")
@click.option('--r_json_path', '-r', help='R packages json list path', default="")
def monitor(endpoint, port, destination, selector, python_json_path, r_json_path):
    json_paths = {
        'python': python_json_path,
        'r': r_json_path
    }

    BrokerConnector(endpoint, port, destination, selector, json_paths)

installer = click.CommandCollection(sources=[bus])

if __name__ == '__main__':
    installer()
