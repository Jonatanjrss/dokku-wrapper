import pytest


def test_create_app(mocker, dokku):
    mocker.patch("dokku_wrapper.services.apps.run_command", return_value="""-----> Creating myapp...
-----> Creating new app virtual host file...""")
    result = dokku.apps.create("myapp")
    assert "myapp" == result["name"]


def test_create_app_already_exists(mocker, dokku):
    mocker.patch(
        "dokku_wrapper.services.apps.run_command",
        side_effect=Exception(" !     Name is already taken")
    )
    with pytest.raises(Exception):
        dokku.apps.create("myapp")


def test_list_apps(mocker, dokku):
    mocker.patch("dokku_wrapper.services.apps.run_command", return_value="=====> My Apps\nmyapp")
    result = dokku.apps.list()
    assert result == ["myapp"]


def test_destroy_app(mocker, dokku):
    mocker.patch(
        "dokku_wrapper.services.apps.run_command",
        return_value="""-----> Destroying myapp (including all add-ons)
-----> Cleaning up...
-----> Retiring old containers and images""")
    result = dokku.apps.destroy("myapp")
    assert result is True