# python-hot-reload

Dev-time helpers to reload changed modules (`importlib.reload`), reimport dependents, and rebind live instances' `__class__`.

Primary entrypoint: `debug_reload_pymodules()` (formerly in PyKotor `utility/tricks.py`).

## Install

```bash
pip install -e .
pip install git+https://github.com/oldrepublicwizard/python-hot-reload.git
```

Optional peer: [`LoggerPlus`](https://github.com/oldrepublicwizard/LoggerPlus).

## Origin

Extracted from [PyKotor](https://github.com/OpenKotOR/PyKotor) `utility/tricks.py`.

## License

LGPL-3.0-or-later
