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
    converted_query = re.sub(r"\btrunc\s*\((.+)\)", r"DATE_TRUNC('DAY', \1)"
        , query
        , count = 0
        , flags = re.IGNORECASE)

    return converted_query
    
def load_trunc_example() -> str:
    example_query = '''SELECT TRUNC(<my_col>)
FROM my_table''')

    return example_query

def convert_to_number(query: str, fmt: str = None) -> str:
    '''
    https://www.ibm.com/docs/en/psfa/7.2.1?topic=extensions-conversion-functions
    https://www.ibm.com/docs/en/psfa/7.2.1?topic=functions-template-patterns-datetime-conversions
    https://www.databasestar.com/oracle-to_number/
    https://www.youtube.com/watch?v=-qHg-uGhggE
    TO_NUMBER
    converts oracle sql syntax into netezza sql syntax
    replaces TO_NUMBER(<col_name>) --> TO_NUMBER(<col_name>, <fmt>)

    Parameters
    ----------
    query: str
        query to convert
    
    Returns
    -------
    converted_query: str
    '''
    # word boundary, to_number, whitespace, (, <col_name>, )
    converted_query = re.sub(r"\bto_number\s*\((.+)\)", r"TO_NUMBER(\1, <fmt>)"
        , query
        , count = 0
        , flags = re.IGNORECASE)
    
    return converted_query

def load_to_number_example() -> str:
    example_query = (
    '''SELECT TO_NUMBER(<my_col>)
FROM my_table''')

    return example_query

def run_all(query: str) -> str:
    '''
    This function runs all the conversion functions

    Parameters
    ----------
    query: str
        query to convert
    
    Returns
    -------
    converted_query: str   
    '''
    converted_query = convert_to_number(converted_query)
    converted_query = convert_trunc(query)

    return converted_query
