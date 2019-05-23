def get_from_db(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT result as user_action, feedback, device FROM t_feedback_models ORDER BY id DESC LIMIT 1;')
    record = cursor.fetchone()
    cursor.close()

    row = {}
    row["user_action"] = str(record[0])
    row["feedback"] = record[1]
    row["device"] = record[2]

    return row

def assert_from_db(conn, user_action, feedback):
    result = get_from_db(conn)
    flag = False

    if result["user_action"] != user_action:
        flag = True

    if result["feedback"] != feedback:
        if len(set([result["feedback"], feedback]) - set(['', None])) != 0:
            flag = True

    if flag:
        raise AssertionError(f"params from request - 'user_action': " \
                f"'{user_action}', 'feedback': '{feedback}'\nparams from DB " \
                f"- 'user_action': '{result['user_action']}', 'feedback': "\
                f"'{result['feedback']}'")
