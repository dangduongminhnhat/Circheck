from enum import Enum
import colorama
from AST import FileLocation

colorama.init(autoreset=True)


class ReportType(Enum):
    ERROR = "Error"
    WARNING = "Warning"


class Report:
    def __init__(self, type_: ReportType, location: FileLocation, message: str, has_location: bool = True):
        self.type = type_
        self.location = location
        self.message = message
        self.has_location = has_location

    def show(self):
        if self.type == ReportType.ERROR:
            color = colorama.Fore.RED
            icon = "❌"
        else:
            color = colorama.Fore.YELLOW
            icon = "⚠️"

        path = self.location.path
        print(f"{icon} [{self.type.value}] in {path}")
        if self.has_location:
            start_line = self.location.start.line
            start_col = self.location.start.column
            print(f"     {start_line}:{start_col} - {self.message}")
        else:
            print(f"     {self.message}")
