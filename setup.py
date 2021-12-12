from setuptools import find_packages, setup

setup(
    name='pvu_netbox_plugin',
    version='0.1',
    description='A plugin of Projeto de Videomonitoramento Urbano for Netbox.',
    url='https://github.com/filipeandrade6/pvu-netbox-plugin',
    author='Filipe Andrade',
    author_email='filipe.engenharia42@gmail.com',
    license='MIT',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)