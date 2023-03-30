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
        Layout(name="body", ratio=7),
        Layout(name="footer", ratio=5),
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

def make_status_table() -> Table:
    """Some example content."""
    global status_table
    status_table = Table(show_footer=False,show_lines=False,show_edge=False,show_header=False)
    
    status_table.add_column(style="green", justify="left")
    status_table.add_column(no_wrap=False,justify="left")
    status_table.add_row(
        "[white]Session Status",
        "[green]{Online}",
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
        "[white]51ms",
    )
    status_table.add_row(
        "[white]Web Interface",
        "[blue link=http://127.0.0.1:4040]http://127.0.0.1:4040",
    )
    status_table.add_row(
        "[white]Forwarding",
        "[blue]https://example.com.ingressify.io[/blue] -> [yellow]http://localhost:{local_port}[/yellow]",
    )
    status_table.add_row(
        "[white]Connections",
        """[cyan1]ttl\topn\trt1\trt5\tp50\tp90\n{ttl}\t{opn}\t{rt1}\t{rt5}\t{p50}\t{p90}[/cyan1]""",
    )
    return status_table

def make_body_panel() -> Panel:
    message = Table.grid()
    message.add_column()
    message.add_column(no_wrap=True)
    sponsor_message = make_body_table()
    status_table = make_status_table()
    message.add_row(sponsor_message)

    message_panel = Panel(
        Align.left(
            Group(Align.left(sponsor_message),"\n",Align.left(status_table)),
        ),
        box=box.ROUNDED,
        # padding=(1, 2),
        title="[b sky_blue]Ingreesify Status Table",
        border_style="bright_blue",
    )
    return message_panel

def make_http_table() -> Table:
    """Some example content."""
    global http_table
    http_table = Table(show_footer=False,show_lines=False,show_edge=False,show_header=False)
    
    http_table.add_column(style="green", justify="left")
    http_table.add_column(no_wrap=False,justify="left")
    http_table.add_row(
        "[green bold]/ GET",
        "[bold blue]304 Not Method",
    )
    http_table.add_row(
        "[green bold]/about GET",
        "[bold blue]200 OK",
    )
    http_table.add_row(
        "[green bold]/create POST",
        "[bold blue]502 Bad Request",
    )
    
   
    return http_table


def make_footer_panel() -> Panel:
    message = Table.grid()
    message.add_column()
    message.add_column(no_wrap=True)
    footer_table = make_footer_table()
    http_table = make_http_table()
    message.add_row(footer_table)

    message_panel = Panel(
        Align.left(
            Group(Align.left(footer_table),"\n",Align.left(http_table)),
        ),
        box=box.ROUNDED,
        # padding=(1, 2),
        title="[b green]HTTP Requests",
        border_style="bright_yellow",
    )
    return message_panel


layout = make_layout()
def update_layout(live):
    layout["header"].update(Header())
    layout["body"].update(make_body_panel())
    layout["footer"].update(make_footer_panel())
    # update_status_table(live,"Connecting",55,"edgeUrl","8000",[23,0.6,25,0.0,5,4])
    # update_http_table(live,reqs="[green bold]/ GET ",resp="[blue bold]OK OKS")
    # update_status_table(live,"Online",120,"edgeUrl","8000",[23,0.6,55,0.0,5,6])
    update_http_table(live,reqs="[green bold]/ POST ",resp="[blue bold]OK OKS")
    # update_status_table(live,"Connecting",80,"edgeUrl","8000",[23,0.6,25,0.0,5,4])
    # update_http_table(live,reqs="[green bold]/ PUT ",resp="[blue bold]OK OKS")
    # update_status_table(live,"Online",60,"edgeUrl","8000",[23,0.6,25,0.0,5,4])

def update_status_table(live,status,lentcy,edgeUrl,local_port,other):
    live.update(status_table.add_row(
        "[white]Session Status",
        f"[green]{status}",
    ))
    live.update(status_table.add_row(
        "[white]Account",
        "prafulpatekar23@gmail.com (Plan: Free)",
    ))
    live.update(status_table.add_row(
        "[yellow]Version",
        "[yellow]0.1.0",
    ))
    live.update(status_table.add_row(
        "[yellow]Region",
        "[yellow]India (in)",
    ))
    live.update(status_table.add_row(
        "[white]Latency",
        f"[white]{lentcy}ms",
    ))
    live.update(status_table.add_row(
        "[white]Web Interface",
        "[blue link=http://127.0.0.1:4040]http://127.0.0.1:4040",
    ))
    live.update(status_table.add_row(
        "[white]Forwarding",
        f"[blue]{edgeUrl}[/blue] -> [yellow]http://localhost:{local_port}[/yellow]",
    ))
    live.update(status_table.add_row(
        "[white]Connections",
        f"""[cyan1]ttl\topn\trt1\trt5\tp50\tp90\n{other[0]}\t{other[1]}\t{other[2]}\t{other[3]}\t{other[4]}\t{other[5]}[/cyan1]""",
    ))

def update_http_table( live,reqs, resp):
    
    live.update(http_table.add_row(reqs, resp))
    # http_table.update(http_table)


from time import sleep

from rich.live import Live

with Live(layout,  screen=True) as live:
    while True:
        update_layout(live)
        sleep(0.1)
        
        # for job in job_progress.tasks:
        #     if not job.finished:
        #         job_progress.advance(job.id)

        # completed = sum(task.completed for task in job_progress.tasks)
        # overall_progress.update(overall_task, completed=completed)



