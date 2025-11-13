# Releasing the ea


```shell
cldfbench makecldf cldfbench_kreft.py --with-zenodo --with-cldfreadme --glottolog-version v5.2
pytest
```

```shell
cldfbench readme cldfbench_kreft.py
cldfbench zenodo --communities dplace cldfbench_kreft.py
dplace check cldfbench_kreft.py
```

```shell
git status
git tag
```

Adapt CHANGELOG.md.
Add, commit and push all changes.

```shell
dplace release cldfbench_kreft.py vX.Y
```