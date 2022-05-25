import re

# def convert_dual(query: str) -> str:
#     '''
#     SYSDATE
#     converts oracle sql syntax into netezza sql syntax
#     replaces dual with _v_dual
#     Parameters
#     ----------
#     query: str
#         query to convert
    
#     Returns
#     -------
#     converted_query: str
#     '''
#     # word boundary, TRUNC, whitespace, (, <col_name> , )
#     # dual
#     converted_query = re.sub(r"\bdual\b", r"_v_dual"
#         , query
#         , count = 0
#         , flags = re.IGNORECASE)

#     return converted_query


def load_converted_dual() -> str:
    converted_query = '''SELECT 1
FROM _v_dual'''

    return converted_query

def load_example_dual() -> str:
    example_query = '''SELECT 1
FROM dual'''

    return example_query

def load_converted_pivot() -> str:
    converted_query = '''-- create data to simulate a pivot
WITH survey_table AS (
SELECT 1 AS participant_id
    , 'Q1' AS question_num
    , 'Y' AS question_answer
FROM _v_dual

UNION ALL

SELECT 1 AS participant_id
    , 'Q2' AS question_num
    , 'N' AS question_answer
FROM _v_dual

UNION ALL

SELECT 1 AS participant_id
    , 'Q3' AS question_num
    , 'Y' AS question_answer
FROM _v_dual

UNION ALL

SELECT 2 AS participant_id
    , 'Q2' AS question_num
    , 'Y' AS question_answer
FROM _v_dual

UNION ALL 

SELECT 2 AS participant_id
    , 'Q3' AS question_num
    , 'Y' AS question_answer
FROM _v_dual
)

-- netezza friendly way to pivot
SELECT participant_id
    , MAX(CASE WHEN question_num = 'Q1' THEN question_answer ELSE NULL END) AS q1_answer
    , MAX(CASE WHEN question_num = 'Q2' THEN question_answer ELSE NULL END) AS q2_answer
    , MAX(CASE WHEN question_num = 'Q3' THEN question_answer ELSE NULL END) AS q3_answer
FROM survey_table
GROUP BY participant_id'''
    
    return converted_query

def load_example_pivot() -> str:
    example_query = '''-- create data to simulate a pivot
WITH survey_table AS (
SELECT 1 AS participant_id
    , 'Q1' AS question_num
    , 'Y' AS question_answer
FROM dual

UNION ALL

SELECT 1 AS participant_id
    , 'Q2' AS question_num
    , 'N' AS question_answer
FROM dual

UNION ALL

SELECT 1 AS participant_id
    , 'Q3' AS question_num
    , 'Y' AS question_answer
FROM dual

UNION ALL

SELECT 2 AS participant_id
    , 'Q2' AS question_num
    , 'Y' AS question_answer
FROM dual

UNION ALL 

SELECT 2 AS participant_id
    , 'Q3' AS question_num
    , 'Y' AS question_answer
FROM dual
)

SELECT *
FROM survey_table
PIVOT (
    MAX(question_answer)
    FOR question_num IN (
        'Q1' AS q1_answer
        , 'Q2' AS q2_answer
        , 'Q3' AS q3_answer
    )
)'''
    
    return example_query

# def convert_sysdate(query: str) -> str:
#     '''
#     SYSDATE
#     converts oracle sql syntax into netezza sql syntax
#     replaces SYSDATE with CURRENT_DATE
#     Parameters
#     ----------
#     query: str
#         query to convert
    
#     Returns
#     -------
#     converted_query: str
#     '''
#     # word boundary, TRUNC, whitespace, (, <col_name> , )
#     # DATE_TRUNC('DAY', <col_name>)
#     converted_query = re.sub(r"\bsysdate\b", r"CURRENT_DATE"
#         , query
#         , count = 0
#         , flags = re.IGNORECASE)

#     converted_query = convert_dual(converted_query)

#     return converted_query

def load_converted_sysdate() -> str:
    converted_query = '''SELECT CURRENT_DATE
FROM _v_dual'''
    
    return converted_query
    
def load_example_sysdate() -> str:
    example_query = '''SELECT SYSDATE
FROM dual'''

    return example_query

# def convert_trunc(query: str, fmt: str = None) -> str:
#     '''
#     TRUNC
#     converts oracle sql syntax into netezza sql syntax
#     replaces TRUNC(<col_name>) with DATE_TRUNC('DAY', <col_name>)
#     Parameters
#     ----------
#     query: str
#         query to convert
    
#     Returns
#     -------
#     converted_query: str
#     '''
#     # word boundary, TRUNC, whitespace, (, <col_name> , )
#     # DATE_TRUNC('DAY', <col_name>)
#     converted_query = re.sub(r"\btrunc\s*\((.+)\)", r"DATE_TRUNC('DAY', \1)"
#         , query
#         , count = 0
#         , flags = re.IGNORECASE)

#     return converted_query

def load_converted_trunc() -> str:
    converted_query = '''SELECT DATE_TRUNC('DAY', CURRENT_TIMESTAMP)
FROM _v_dual'''
    
    return converted_query
    
def load_example_trunc() -> str:
    example_query = '''SELECT TRUNC(SYSDATE)
FROM dual'''

    return example_query

# def convert_to_number(query: str, fmt: str = None) -> str:
#     '''
#     https://www.ibm.com/docs/en/psfa/7.2.1?topic=constants-data-types-aliases
#     TO_NUMBER
#     converts oracle sql syntax into netezza sql syntax
#     replaces TO_NUMBER(<col_name>) --> CAST(<col_name> AS <DATATYPE>)

#     Parameters
#     ----------
#     query: str
#         query to convert
    
#     Returns
#     -------
#     converted_query: str
#     '''
#     # word boundary, to_number, whitespace, (, <col_name>, )
#     converted_query = re.sub(r"\bto_number\s*\((.+)\)", r"CAST(\1 AS <DATATYPE>)"
#         , query
#         , count = 0
#         , flags = re.IGNORECASE)
    
#     return converted_query

def load_converted_to_number() -> str:
    converted_query = '''SELECT CAST('1' AS INT)
FROM _v_dual'''
    
    return converted_query

def load_example_to_number() -> str:
    example_query = '''SELECT TO_NUMBER('1')
FROM dual'''

    return example_query

# def run_all(query: str) -> str:
#     '''
#     This function runs all the conversion functions

#     Parameters
#     ----------
#     query: str
#         query to convert
    
#     Returns
#     -------
#     converted_query: str   
#     '''
#     converted_query = convert_dual(query)
#     converted_query = convert_sysdate(converted_query)
#     converted_query = convert_to_number(converted_query)
#     converted_query = convert_trunc(converted_query)

#     return converted_query
