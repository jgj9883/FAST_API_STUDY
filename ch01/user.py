import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from sqlite import sql_select


def user_info(user_id, user_password):
    user_pw = sql_select(user_id)
    if user_pw == user_password:
        print("로그인 성공")
        return True
    else:
        print("로그인 실패")
        return False




