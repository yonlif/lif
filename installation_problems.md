In MacOS one might receive the following error while pip installing:

```
clang: warning: libstdc++ is deprecated; move to libc++ with a minimum deployment target of OS X 10.9 [-Wdeprecated]
ld: library not found for -lstdc++
clang: error: linker command failed with exit code 1 (use -v to see invocation)
error: command 'g++' failed with exit status 1
```

The proper fix to that is simply run before pip installing the following command:

```bash
export CFLAGS="-std=c++11 -stdlib=libc++"
```

Than reinstall lif.

---

Got another problem you could not solve? Please leave an [issue on github](https://github.com/yonlif/lif/issues).  
Solved a problem? **Awesome** - please send a PR to this document :)
