def test_add_new_project(app):
    app.session.ensure_login(app.username, app.password)
    old_count = app.project.get_count()
    app.project.check_on_create_page()
    app.project.create_new()
    new_count = app.project.get_count()
    assert old_count + 1 == new_count