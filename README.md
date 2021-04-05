# LIF - Large Integer Factorization library

This library will try to implement the [following algorithms](https://en.wikipedia.org/wiki/Integer_factorization#Factoring_algorithms)

### Update lif:
1. Upload your changes to github
2. Create a new [release]()
3. Rewrite `setup.py` (specifically the `download_url`)
4. Than run on your computer:
```bash
python setup.py sdist
twine upload dist/*
```
5. Upgrade using `pip install --upgrade lif`
