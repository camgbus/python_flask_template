from pt.dir.class_file import ClassObj

def test_class_file():
    obj = ClassObj(5)
    assert obj.get_attr() == 5