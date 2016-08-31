import pytest
import re


@pytest.fixture()
def GetCandidateVersion(Command):
    def CandidateVersion(pkg):
        """ Check the output of "apt-cache poicy <package-name>"
        to determine the candidate version for a package.

        Args:
            Command - module to run apt-cache policy
            pkg - name of the package you want to check candidates for

        Returns:
            Candidate version for pkg
        """
        policy = Command.check_output("apt-cache policy {}".format(pkg))
        candidates = re.search("Candidate: (.*)", policy)
        if candidates:
            return candidates.groups(0)[0]
        else:
            return ""
    return CandidateVersion


def test_pip_exists(Package, GetCandidateVersion):
    """ Ensure the candidate version of pip is installed.

    Args:
        Package - Module to determine package install status and version
        GetPolicy - Get version of candidate package
    """
    pip = Package("python-pip")
    pip_candidate_version = GetCandidateVersion("python-pip")
    assert pip.is_installed
    assert pip.version == pip_candidate_version
