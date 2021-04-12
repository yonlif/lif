# LIF - Large Integer Factorization

lif factorizes large integers fast by implementing multiple algorithms using C++, 
lif also provides convenient python interface.

Usage:

```python
import lif
lif.trial_division(12)
>>> [2, 2, 3]
```

Or using the command line interface (CLI):

```bash
lif 12 --algo=trial_division
> 2, 2, 3
```

### TODO

This library will try to implement the [following algorithms](https://en.wikipedia.org/wiki/Integer_factorization#Factoring_algorithms)

- [X] Trial division
- [ ] Wheel factorization
- [ ] Pollard's rho algorithm - WIP
- [ ] Algebraic-group factorisation algorithms
- [ ] Fermat's factorization method
- [ ] Euler's factorization method
- [ ] Special number field sieve

### Build and contribute
1. Download from github
2. Build using `python setup.py build_ext --inplace`
3. Submit a PR

#### Update lif:
1. Upload your changes to github
2. Create a new [release]()
3. Rewrite `setup.py` (specifically the `download_url`)
4. Than run on your computer:
```bash
python setup.py sdist
twine upload dist/*
```
5. Upgrade using `pip install --upgrade lif`
