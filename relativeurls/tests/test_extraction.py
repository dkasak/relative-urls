from relativeurls.relativeurls import extract_endpoints


def qq(s: bytes) -> bytes:
    """Double-quote bytes input."""
    return b'"%b"' % s


def q(s: bytes) -> bytes:
    """Single-quote bytes input."""
    return b"'%b'" % s


def test_no_slash():
    assert extract_endpoints(qq(b"foo/bar/baz")) == set()


def test_plain():
    assert extract_endpoints(qq(b"/foo/bar/baz")) \
        == set(["/foo/bar/baz"])


def test_plain_single_quoted():
    assert extract_endpoints(q(b"/foo/bar/baz")) \
        == set(["/foo/bar/baz"])


def test_terminating_semicolon_is_stripped():
    assert extract_endpoints(q(b"/foo/bar/baz") + b";") \
        == set(["/foo/bar/baz"])


def test_embedded_semicolon_is_preserved():
    assert extract_endpoints(q(b"/foo/bar/quux;baz") + b";") \
        == set(["/foo/bar/quux;baz"])


def test_query_string_is_preserved():
    assert extract_endpoints(q(b"/foo/bar/baz?a=1&b=2")) \
        == set(["/foo/bar/baz?a=1&b=2"])


def test_endpoints_are_extracted_from_absolute_urls():
    # TODO: Add an option to disable/enable this behaviour.
    assert extract_endpoints(q(b"http://foo/bar/baz")) \
        == set(["/bar/baz"])

    assert extract_endpoints(q(b"https://foo/bar/baz")) \
        == set(["/bar/baz"])


def test_fragment_is_preserved():
    # TODO: Add an option to disable/enable this behaviour.
    assert extract_endpoints(q(b"/foo/bar/quux#foobar")) \
        == set(["/foo/bar/quux#foobar"])


def test_endpoints_with_template_args_are_caught():
    # TODO: Add an option to disable/enable this behaviour.
    assert extract_endpoints(q(b"/user/{id}/info")) \
        == set(["/user/{id}/info"])

    # TODO: Add an option to disable/enable this behaviour.
    assert extract_endpoints(q(b"/${postid}/")) \
        == set(["/${postid}/"])
