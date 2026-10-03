from radssh.core_plugins.star_tty import translate_terminal_input


def translate_one_byte_at_a_time(text):
    translated_text = b''
    pending_text = b''
    for offset in range(len(text)):
        translated, pending_text = translate_terminal_input(
            text[offset:offset + 1], pending_text)
        translated_text += translated
    return translated_text, pending_text


def test_translate_terminal_input_modern_key_sequences():
    assert translate_terminal_input(b'\033[127;5u') == (b'\x7f', b'')
    assert translate_terminal_input(b'\033[3;3~') == (b'\x17', b'')


def test_translate_terminal_input_keeps_unmapped_text():
    assert translate_terminal_input(
        b'abc\033[127;5uxyz\033[3;3~') == (b'abc\x7fxyz\x17', b'')


def test_translate_terminal_input_buffers_partial_sequence():
    translated, pending = translate_terminal_input(b'\033[127')
    assert translated == b''
    assert pending == b'\033[127'

    assert translate_terminal_input(b';5u', pending) == (b'\x7f', b'')


def test_translate_terminal_input_handles_variable_length_sequences():
    assert translate_one_byte_at_a_time(b'\033[127;5u') == (b'\x7f', b'')
    assert translate_one_byte_at_a_time(b'\033[3;3~') == (b'\x17', b'')


def test_translate_terminal_input_only_buffers_escape_prefixes():
    assert translate_terminal_input(b'x') == (b'x', b'')
    assert translate_terminal_input(b'\033') == (b'', b'\033')
    assert translate_terminal_input(b'[', b'\033') == (b'', b'\033[')


def test_translate_terminal_input_flushes_disconfirmed_prefix():
    assert translate_terminal_input(b'x', b'\033') == (b'\033x', b'')
    assert translate_terminal_input(b'x', b'\033[') == (b'\033[x', b'')
