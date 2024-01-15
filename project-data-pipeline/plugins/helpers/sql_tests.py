class SQLTests:
    # sql test cases and expected results
    sql_tests = [
        {
            'test_query': 'SELECT COUNT(*) FROM artists WHERE artistid IS NULL',
            'expected_result': 0
        },
        {
            'test_query': 'SELECT COUNT(*) FROM songplays WHERE playid IS NULL',
            'expected_result': 0
        },
        {
            'test_query': 'SELECT COUNT(*) FROM songplays WHERE start_time IS NULL',
            'expected_result': 0
        },
        {
            'test_query': 'SELECT COUNT(*) FROM songplays WHERE userid IS NULL',
            'expected_result': 0
        },
        {
            'test_query': 'SELECT COUNT(*) FROM songs WHERE songid IS NULL',
            'expected_result': 0
        },
        {
            'test_query': 'SELECT COUNT(*) FROM time WHERE start_time IS NULL',
            'expected_result': 0
        },
        {
            'test_query': 'SELECT COUNT(*) FROM users WHERE userid IS NULL',
            'expected_result': 0
        }
    ]