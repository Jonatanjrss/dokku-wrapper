def test_set_global_domain(mocker, dokku):
    mocker.patch(
        "dokku_wrapper.services.domains.run_command",
        return_value="-----> Set localhost")
    result = dokku.domains.set_global("localhost")
    assert result is True