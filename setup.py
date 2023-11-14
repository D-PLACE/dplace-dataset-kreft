from setuptools import setup


setup(
    name='cldfbench_kreft',
    py_modules=['cldfbench_kreft'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-dataset-kreft=cldfbench_kreft:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
