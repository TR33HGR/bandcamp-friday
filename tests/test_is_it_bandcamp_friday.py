from hamcrest import assert_that, is_
from bandcamp_friday.is_it_bandcamp_friday import is_true


def test():
    assert_that(is_true(), is_(True))
