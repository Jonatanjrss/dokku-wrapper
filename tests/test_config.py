def test_set_config(mocker, dokku):
    mocker.patch("dokku_wrapper.services.config.run_command", return_value="""-----> Setting config vars
A:  1""")
    result = dokku.config.set("myapp", key="A", value=1)
    assert result is True


def test_list_config(mocker, dokku):
    mocker.patch("dokku_wrapper.services.config.run_command", return_value="""-----> Setting config vars
A:  1""")
    result = dokku.config.list("myapp")
    assert result == [{"A": "1"}]

    mocker.patch("dokku_wrapper.services.config.run_command", return_value="""=====> test env vars
A:  1
B:  2""")
    result = dokku.config.list("myapp")
    assert result == [{"A": "1"}, {"B": "2"}]
