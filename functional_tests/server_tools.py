from fabric.api import run
from fabric.context_managers import settings, shell_env
import os
#import password of aws password login

def _get_manage_dot_py(host):
    return f'~/sites/{host}/virtualenv/bin/python3.7 ~/sites/{host}/manage.py'


def reset_database(host):
    PW=os.environ.get("PW")#
    print("printing PW from reset_database",PW)#
    manage_dot_py = _get_manage_dot_py(host)

    with settings(host_string=f'ubuntu@{host}',user='ubuntu',password=PW):#
        run(f'{manage_dot_py} flush --noinput')


def _get_server_env_vars(host):
    env_lines = run(f'cat ~/sites/{host}/.env').splitlines()
    return dict(l.split("=") for l in env_lines if l)


def create_session_on_server(host, email):  
    PW=os.environ.get("PW")#
    print("printing PW from create_session_on_server",PW)#
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'ubuntu@{host}',user='ubuntu',password=PW):#
        env_vars = _get_server_env_vars(host)
        with shell_env(**env_vars):
            session_key = run(f'{manage_dot_py} create_session {email}')
            return session_key.strip()
