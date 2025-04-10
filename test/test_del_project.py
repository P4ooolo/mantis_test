def test_del_random_project(app):
    if app.project.get_count() == 0:
        app.project.check_on_create_page()
        app.project.create_new()
    old_list = app.project.get_list()
    del_project = app.project.del_random_project()
    old_list.remove(del_project)
    new_list = app.project.get_list()
    assert len(old_list) == len(new_list)
    assert sorted(old_list) == sorted(new_list)