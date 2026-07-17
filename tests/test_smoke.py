def test_import():
    from python_hot_reload import debug_reload_pymodules, reimport_dependencies
    assert callable(debug_reload_pymodules)
    assert callable(reimport_dependencies)
