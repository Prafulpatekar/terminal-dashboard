from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table

from random import choices


console = Console()




def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
    )
    layout["main"].split_row(
        Layout(name="body", ratio=8),
        Layout(name="footer", ratio=4),
    )
    return layout


class Header:
    """Display header with clock."""
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[i]Welcome to[/i] [b]Ingressify[/b] application",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
            
        )
        return Panel(grid, style="green on black")


def make_body_table() -> Table:
    """Some example content."""
    sponsor_message = Table.grid()
    sponsor_message.add_column(style="green", justify="left")
    sponsor_message.add_column(no_wrap=True,justify="left")
    sponsor_message.add_row(
        "Visit Website:",
        "[blue]https://api.ingressify.in",
    )
    return sponsor_message

def make_footer_table() -> Table:
    """Some example content."""
    sponsor_message = Table.grid()
    sponsor_message.add_column(style="green", justify="left")
    sponsor_message.add_column(no_wrap=True,justify="left")
    sponsor_message.add_row(
        "HTTP Requests:",
        "->",
    )
    return sponsor_message

status_table = Table(show_footer=False,show_lines=False,show_edge=False,show_header=False)
def make_status_table() -> Table:
    """Some example content."""
    status_table.add_column(style="green", justify="left")
    status_table.add_column(no_wrap=False,justify="left")
    return status_table

def make_body_panel() -> Panel:
    message = Table.grid()
    message.add_column()
    message.add_column(no_wrap=True)
    sponsor_message = make_body_table()
    # status_table = make_status_table()
    status_table_obj = status_table
    message.add_row(sponsor_message)
    message_panel = Panel(
        Align.left(
            Group(Align.left(sponsor_message),"\n",Align.left(status_table_obj)),
        ),
        box=box.ROUNDED,
        title="[b sky_blue]Ingreesify Status Table",
        border_style="bright_blue",
    )
    return message_panel

http_table = Table(show_footer=False,show_lines=False,show_edge=False,show_header=False)
http_table.add_column(style="green", justify="left")
http_table.add_column(no_wrap=False,justify="left")


def make_footer_panel() -> Panel:
    message = Table.grid()
    message.add_column()
    message.add_column(no_wrap=True)
    footer_table = make_footer_table()
    http_table_obj = http_table
    message.add_row(footer_table)

    message_panel = Panel(
        Align.left(
            Group(Align.left(footer_table),"\n",Align.left(http_table_obj)),
        ),
        box=box.ROUNDED,
        title="[b green]HTTP Requests",
        border_style="bright_yellow",
    )
    return message_panel


layout = make_layout()
layout["header"].update(Header())
layout["body"].update(make_body_panel())
layout["footer"].update(make_footer_panel())

def update_status_table(status,latency,edgeUrl,local_port,other):
    status_table.add_row(
        "[white]Session Status",
        f"[green]{status}",
    )
    status_table.add_row(
        "[white]Account",
        "prafulpatekar23@gmail.com (Plan: Free)",
    )
    status_table.add_row(
        "[yellow]Version",
        "[yellow]0.1.0",
    )
    status_table.add_row(
        "[yellow]Region",
        "[yellow]India (in)",
    )
    status_table.add_row(
        "[white]Latency",
        f"[white]{latency}ms",
    )
    status_table.add_row(
        "[white]Web Interface",
        "[blue link=http://127.0.0.1:4040]http://127.0.0.1:4040",
    )
    status_table.add_row(
        "[white]Forwarding",
        f"[blue]{edgeUrl}[/blue] -> [yellow]http://localhost:{local_port}[/yellow]",
    )
    status_table.add_row(
        "[white]Connections",
        f"""[cyan1]ttl: {other[0]}\nopn: {other[1]}\nrt1: {other[2]}\nrt5: {other[3]}\np50: {other[4]}\np90: {other[5]}\n[/cyan1]""",
    )
    return status_table

def update_http_table( reqs, resp):
    http_table.add_row(reqs, resp)
    return http_table


from time import sleep

from rich.live import Live

with Live(layout,refresh_per_second=4,  screen=True) as live:
    i = 1
    while True:
        sleep(1)
        update_status_table("Connecting",i+1,"edgeUrl","8000",[i,i+5,i,i,i+2,i+8])
        update_http_table(reqs="[green bold]/ GET ",resp=f"[blue bold]OK i")
        i+=1
        
        


