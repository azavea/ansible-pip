import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    """ Load default variables into dictionary.
    Args:
        Ansible - Requires the ansible connection backend.
    """
    return Ansible("include_vars", "./defaults/main.yml")["ansible_facts"]


def test_pip_exists(Command, AnsibleDefaults):
    """ Ensure the candidate version of pip is installed.

    Args:
        Command - Module to determine package install status and version
        GetAnsibleDefaults - Get default version of the package
    """
    pip_version_check = Command("pip --version")

    # We only care about the major.minor versions
    pip_version = AnsibleDefaults["pip_version"].split("*")[0]

    assert pip_version_check.rc == 0
    assert pip_version in pip_version_check.stdout
