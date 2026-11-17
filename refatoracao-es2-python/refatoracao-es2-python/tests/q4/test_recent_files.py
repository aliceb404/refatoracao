from refatoracao.q4.recent_files import RecentFiles


def test_add_file_should_keep_most_recent_first_and_respect_limit():
    rf = RecentFiles(3)

    rf.add_file("/a")
    rf.add_file("/b")
    rf.add_file("/c")
    rf.add_file("/d")

    assert len(rf) == 3
    assert rf[0] == "/d"
    assert rf[1] == "/c"
    assert rf[2] == "/b"


def test_refactor_goal_replace_inheritance_with_delegation():
    # TODO: após refatorar, RecentFiles NÃO deve herdar de list (verificar em code review).
    pass
