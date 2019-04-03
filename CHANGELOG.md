## 2.0.0

- Add `pip_executable` variable to support Python 2 and 3 installations.
- Removed deprecated tests-as-filters in `when` directives.
- Updated minimum supported Ansible version to 2.5.x.

## 1.1.0

- Add `pip_get_pip_version` to support older `get-pip.py` releases. See version history at https://bootstrap.pypa.io.

## 1.0.1

- Prevent `get-pip.py` download when it is already present.

## 1.0.0

- Install pip using `get-pip.py` instead of `apt`. See Install pip, setuptools, and wheel in the [pip documentation](https://packaging.python.org/installing/#install-pip-setuptools-and-wheel) for more information.

## 0.2.0

- Replace existing Vagrant testing setup with Molecule.
- Add Molecule testing support for Ubuntu 16.04.

## 0.1.1

- Make use of a version glob to install the `pip` package.

## 0.1.0

- Initial release.
