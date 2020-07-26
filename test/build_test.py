import platform
import pytest
import testinfra

ROOT = 'root'


def test_python():
    assert platform.python_version() == '3.8.5'


def test_pip_packages(host):
    pip_packages = host.pip_package.get_packages

    assert pip_packages()['pip']['version'] == '20.1.1'
    assert pip_packages()['pytest']['version'] == '5.4.3'
    assert pip_packages()['testinfra']['version'] == '5.2.2'


def test_current_user(host):
    user = host.user()

    assert user.name == ROOT
    assert user.group == ROOT
