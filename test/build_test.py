import platform
import pytest
import testinfra

ROOT = 'root'


def test_python():
    assert platform.python_version() == '3.8.5'


@pytest.mark.parametrize('name,version', [
    ('testinfra', '5.2.2'),
])
def test_pip_packages(host, name, version):
    pip_packages = host.pip_package.get_packages

    assert pip_packages()[name]['version'] == version


def test_current_user(host):
    user = host.user()

    assert user.name == ROOT
    assert user.group == ROOT
