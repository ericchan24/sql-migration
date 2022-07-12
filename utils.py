# all_tables
def load_converted_all_tables() -> str:
    converted_query = '''SELECT *
FROM _v_table'''

    return converted_query

def load_example_all_tables() -> str:
    example_query = '''SELECT *
FROM all_tables'''
    
    return example_query

# all_tab_columns
def load_converted_all_tab_columns() -> str:
    converted_query = '''SELECT *
FROM _v_sys_columns'''

    return converted_query

def load_example_all_tab_columns() -> str:
    example_query = '''SELECT *
FROM all_tab_columns'''
    
    return example_query
    
# dual
def load_converted_dual() -> str:
    converted_query = '''SELECT 1
FROM _v_dual'''

    return converted_query

def load_example_dual() -> str:
    example_query = '''SELECT 1
FROM dual'''

    return example_query

# list_agg
def load_converted_list_agg() -> str:
    converted_query = '''-- create data to simulate LIST_AGG
WITH major_unpivot AS (
SELECT 1 AS student_id
    , 'English' AS major
FROM dual

UNION ALL

SELECT 1 AS student_id
    , 'Economics' AS major
FROM dual

UNION ALL

SELECT 1 AS student_id
    , 'Chemistry' AS major
FROM dual

UNION ALL

SELECT 2 AS student_id
    , 'Spanish' AS major
FROM dual

UNION ALL

SELECT 2 AS student_id
    , 'Biology' AS major
FROM dual
)

SELECT student_id
    , LISTAGG(major, ', ') WITHIN GROUP(ORDER BY major) AS major_list
FROM major_unpivot
GROUP BY student_id'''

    return converted_query

def load_example_list_agg() -> str:
    example_query = '''-- create data to simulate LIST_AGG
WITH major_unpivot AS (
SELECT 1 AS student_id
    , 'English' AS major
FROM _v_dual

UNION ALL

SELECT 1 AS student_id
    , 'Economics' AS major
FROM _v_dual

UNION ALL

SELECT 1 AS student_id
    , 'Chemistry' AS major
FROM _v_dual

UNION ALL

SELECT 2 AS student_id
    , 'Spanish' AS major
FROM _v_dual

UNION ALL

SELECT 2 AS student_id
    , 'Biology' AS major
FROM _v_dual
)

-- order the major so that the list will be in alphabetical order
, major_unpivot_ordered AS (
SELECT student_id, major
FROM major_unpivot
ORDER BY student_id, major)

SELECT student_id
    , REGEXP_REPLACE(GROUP_CONCAT(major), ',', ', ') AS major_list -- use regexp_replace to get the desired formatting
FROM major_unpivot_ordered
GROUP BY student_id
ORDER BY student_id'''

    return example_query

# pivot
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

# sysdate
def load_converted_sysdate() -> str:
    converted_query = '''SELECT CURRENT_DATE
FROM _v_dual'''
    
    return converted_query
    
def load_example_sysdate() -> str:
    example_query = '''SELECT SYSDATE
FROM dual'''

    return example_query

# trunc
def load_converted_trunc() -> str:
    converted_query = '''SELECT DATE_TRUNC('DAY', CURRENT_TIMESTAMP)
FROM _v_dual'''
    
    return converted_query
    
def load_example_trunc() -> str:
    example_query = '''SELECT TRUNC(SYSDATE)
FROM dual'''

    return example_query

# to_number
def load_converted_to_number() -> str:
    converted_query = '''SELECT CAST('1' AS INT)
FROM _v_dual'''
    
    return converted_query

def load_example_to_number() -> str:
    example_query = '''SELECT TO_NUMBER('1')
FROM dual'''

    return example_query

# unpivot
def load_converted_unpivot() -> str:
    converted_query = '''-- create data to simulate an unpivot
WITH survey_table AS (
SELECT 1 AS participant_id
    , 'Y' AS q1_answer
    , 'N' AS q2_answer
    , 'Y' AS q3_answer
FROM _v_dual

UNION ALL

SELECT 2 AS participant_id
    , NULL AS q1_answer
    , 'Y' AS q2_answer
    , 'Y' AS q3_answer
FROM _v_dual
)

-- netezza friendly way to unpivot
SELECT participant_id
    , 'Q1' AS question_num
    , q1_answer AS question_answer
FROM survey_table
WHERE q1_answer IS NOT NULL

UNION ALL 

SELECT participant_id
    , 'Q2' AS question_num
    , q2_answer AS question_answer
FROM survey_table
WHERE q2_answer IS NOT NULL

UNION ALL 

SELECT participant_id
    , 'Q3' AS question_num
    , q3_answer AS question_answer
FROM survey_table
WHERE q3_answer IS NOT NULL'''
    
    return converted_query

def load_example_unpivot() -> str:
    example_query = '''-- create data to simulate an unpivot
WITH survey_table AS (
SELECT 1 AS participant_id
    , 'Y' AS q1_answer
    , 'N' AS q2_answer
    , 'Y' AS q3_answer
FROM dual

UNION ALL

SELECT 2 AS participant_id
    , NULL AS q1_answer
    , 'Y' AS q2_answer
    , 'Y' AS q3_answer
FROM dual
)

SELECT *
FROM survey_table
UNPIVOT EXCLUDE NULLS (
    question_answer  
    FOR question_num IN ( 
        q1_answer AS 'Q1'
        , q2_answer AS 'Q2'
        , q3_answer AS 'Q3'
    )
)'''
    
    return example_query