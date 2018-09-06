@dataclass
class SourceStr:
    s : str
    line : int
    column : int


def phase1(input: str):
    # conversion to "source character set" done before
    # no trigraphs
    # attach line/column information
