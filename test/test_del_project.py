def test_del_random_project(app):
    app.session.ensure_login(app.username, app.password)
    if app.project.get_count() == 0:
        app.project.check_on_create_page()
        app.project.create_new()
    old_count = app.project.get_count()
    app.project.del_random_project()
    new_count = app.project.get_count()
    assert old_count - 1 == new_count