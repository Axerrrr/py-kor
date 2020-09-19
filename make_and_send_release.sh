rm -rf ./py_kor.egg-info && rm -rf ./build && rm -rf ./dist
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*
python3 -m twine upload --repository pypi dist/*
