import re

def convert_trunc(query: str, fmt: str = None) -> str:
    '''
    TRUNC
    converts oracle sql syntax into netezza sql syntax
    replaces TRUNC(<col_name>) with DAY_TRUNC('DAY', <col_name>)
    
    Parameters
    ----------
    query: str
        query to convert
    
    Returns
    -------
    converted_query: str
    '''
    # word boundary, TRUNC, whitespace, (, <col_name> , )
    # DATE_TRUNC('DAY', <col_name>)
    converted_query = re.sub(r"\btrunc\s*\(([\S\s]+)\)", r"DATE_TRUNC('DAY', \1)"
        , query
        , count = 0
        , flags = re.IGNORECASE)

    converted_query = re.sub(r"\btrunc\((.+)\)", r"DATE_TRUNC('DAY', \1)"
        , query
        , count = 0
        , flags = re.IGNORECASE)

    return converted_query
    
def load_trunc_example() -> str:
    example_query = (
    '''SELECT TRUNC(<my_col>)
    FROM my_table''')

    return example_query