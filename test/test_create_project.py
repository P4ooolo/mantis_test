def test_add_new_project(app):
    old_list = app.project.get_list_soap()
    app.project.check_on_create_page()
    old_list.append(app.project.create_new())
    new_list = app.project.get_list_soap()
    assert len(old_list) == len(new_list)
    assert sorted(old_list) == sorted(new_list)