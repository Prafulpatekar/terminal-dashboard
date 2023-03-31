commands = [
    {
        'level_one':'configs',
        'level_two':'add-authtoken',
        'command_type': 'parameterized',
        'argument':'auth-token-string', 
        'flags': []
    },
    {
        'level_one':'configs',
        'level_two':'check',
        'command_type': 'flagged',
        'argument':'', 
        'flags': [
            {
                'flag_name':'--config',
                'argument':'C:/Users/Praful Patekar/AppData/Local/ingressify/ingressify.yml'
            },
            {
                'flag_name':'--log',
                'argument':'C:/Users/Praful Patekar/AppData/Local/ingressify/ingressify.log'
            },
            {
                'flag_name':'--log-level',
                'argument':'info'
            },
            {
                'flag_name':'--log-format',
                'argument':'json'
            },
        ]
    },
    {
        'level_one':'service',
        'level_two':'start',
        'command_type': 'basic(service)',
        'argument':'', 
        'flags': []
    },
    {
        'level_one':'proxy',
        'level_two':'http',
        'command_type': 'hybrid',
        'argument':'80', 
        'flags': [
            {
                'flag_name':'--log',
                'argument':'C:/Users/Praful Patekar/AppData/Local/ingressify/ingressify.log' 
            }
        ]
    },
    {
        'level_one':'credits',
        'level_two':'',
        'command_type': 'hybrid/special',
        'argument':'', 
        'flags': [
            {
                'flag_name':'--config',
                'argument':'C:/Users/Praful Patekar/AppData/Local/ingressify/ingressify.yml' 
            }
        ]
    },
]

skelton = [
            {
                'level_one':'level one command name',# required
                'level_two':'level two command name',# optional
                'command_type': 'basic(service)/parameterized/flagged/hybrid(parameterized-flagged)', # required
                'argument':'value of command', # if command_type is parameterized then it is required
                'flags': [ # if command_type is flagged then atleast one flag is required
                    {
                        'flag_name':'flag name (example: --log)',# required
                        'argument':'flag value' # required
                    },
                    {
                        'flag_name':'flag name (example: --log)',# required
                        'argument':'flag value' # required
                    }
                    
                ]
            },
            

        ]


# Third Party Library
# Standard Library
import random
import time

# Project Library
from rich import print
from rich.console import Console
from rich.live import Live
from rich.padding import Padding
from rich.progress import track
from rich.table import Table

reqs_dict = {
    0: {"url": "GET /", "response": "304 Not Modified"},
    1: {"url": "POST /create", "response": "200 Ok"},
    2: {"url": "GET /create", "response": "404 Not Found"},
    3: {"url": "GET /about", "response": "200 ok"},
    4: {"url": "GET /about-us", "response": "502 bad gateway"},
}

console = Console()
request_table = Table.grid()
table_status = Table.grid()


def get_requests_table():
    request_table.title = "[green]HTTP Requests"
    request_table.title_justify = "left"
    request_table.style = "bold"
    request_table.add_column("             ")
    request_table.add_column("             ")
    request_table.add_column("             ")
    request_table.add_column("             ")
    return request_table


def update_requests_table(live, reqs, resp):
    request_table.add_row(reqs, "             ", "             ", resp)
    live.update(request_table)


def get_status_table():
    table_status.title = "[green]Session Status Table"
    table_status.title_justify = "left"
    table_status.style = "bold"
    return table_status


def update_status_table(live, status, ttl, opn, rt1, rt5, p50, p90):
    table_status.add_column("            ")
    table_status.add_column("                          ")
    table_status.add_column("            ")
    table_status.add_row("[white]Session Status", "                          ", f"[green]{status}")
    table_status.add_row("[white]Account", "                          ", "prafulpatekar23@gmail.com (Plan: Free)")
    table_status.add_row("[yellow]Version", "                          ", "[yellow]0.1.0")
    table_status.add_row("[yellow]Region", "                          ", "[yellow]India (in)")
    table_status.add_row("[white]Latency", "                          ", "51ms")
    table_status.add_row("[white]Web Interface", "                          ", "http://127.0.0.1:4040")
    table_status.add_row(
        "[white]Forwarding",
        "                          ",
        "https://example.com.io -> http://localhost:{local_port}",
    )
    table_status.add_row(
        "[white]Connections",
        "                          ",
        f"""[cyan1]ttl\t[cyan1]opn\t[cyan1]rt1\t[cyan1]rt5\t[cyan1]p50\t[cyan1]p90\n{ttl}\t{opn}\t{rt1}\t{rt5}\t{p50}\t{p90}""",
    )
    live.update(table_status)


def get_console():
    while True:
        with Live(console=console, auto_refresh=True, screen=True, refresh_per_second=1) as live:
            console.print(Padding("[green bold]info", (1, 0), expand=True))
            console.print(
                "[white italic]Visit Website: The info by click on " + "[blue bold]https://api.info.in"
            )
            console.print(get_status_table(), justify="left")
            console.print(get_requests_table(), justify="left")

            for i in range(5):
                update_status_table(
                    live,
                    random.choice(["Online", "Offline", "Connecting"]),
                    str(i + 1),
                    str(i + 2),
                    str(i + 2 - 1),
                    str(i + 6),
                    str(i + 8),
                    str(i + 9),
                )
                time.sleep(1)
                i += 1

            for i in range(5):
                update_requests_table(live, reqs_dict[i]["url"], reqs_dict[i]["response"])
                time.sleep(1)
                i += 1
