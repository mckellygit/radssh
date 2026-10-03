from radssh.shell import readline_key_bindings


def test_gnu_readline_key_bindings_include_terminal_sequences():
    assert readline_key_bindings() == [
        '"\\e[127;5u": backward-delete-char',
        '"\\e[3;3~": unix-word-rubout',
    ]


def test_libedit_key_bindings_include_terminal_sequences():
    assert readline_key_bindings(using_libedit=True) == [
        'bind "^[[127;5u" ed-delete-prev-char',
        'bind "^[[3;3~" ed-delete-prev-word',
    ]
