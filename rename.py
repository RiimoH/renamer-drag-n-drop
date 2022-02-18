from pathlib import Path

def append(old_path: Path, appendix: str, separator: str = '_') -> Path:
    parent = old_path.parent
    stem = old_path.stem
    suf = old_path.suffix

    new = parent / (stem + separator + appendix + suf)
    return new

def replace (old_path: Path, match: str, replacer: str) -> Path:
    new_path = str(old_path).replace(match, replacer)
    return Path(new_path)

def insert(old_path: Path, prefix: str, separator: str = '_') -> Path:
    parent = old_path.parent
    name = old_path.name
    suf = old_path.suffix

    new = parent / (prefix + separator + name)
    return new

def switch(old_path: Path, *new_order: str, separator: str = '_') -> Path:
    parent = old_path.parent
    stem = old_path.stem.split(separator)
    suf = old_path.suffix
    order = map(int, new_order)
    
    new = parent / ('_'.join([stem[x-1] for x in order]) + suf)
    return new

def execute(old: Path, new: Path):
    try:
        old.rename(new)
    except Exception as e:
        print(e)
