from setuptools import setup, find_packages

setup(
    name="tljh-repo2docker",
    version="0.0.1",
    entry_points={"tljh": ["tljh_repo2docker = tljh_repo2docker"]},
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "dockerspawner @ git+https://github.com/jupyterhub/dockerspawner",
        "jupyterhub-nativeauthenticator~=1.0",
        "jupyter_client~=7.3",
        "aiodocker~=0.21",
    ],
)
