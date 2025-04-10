import random


def test_del_random_project(app):
    if len(app.project.get_list_soap()) == 0:
        app.project.check_on_create_page()
        app.project.create_new()
    old_list = app.project.get_list_soap()
    project_to_delete = random.choice(old_list)
    app.project.del_project_by_name(project_to_delete)
    old_list.remove(project_to_delete)
    new_list = app.project.get_list_soap()
    assert len(old_list) == len(new_list)
    assert sorted(old_list) == sorted(new_list)