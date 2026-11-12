import pytest

from coupon_validator import coupon_discount, best_discount, is_expired


# Explicitly exercise true and false outcomes of every decision in the module.

@pytest.mark.parametrize(
    "code,total,new_user,day,expected",
    [
        ("WELCOME10", 200, True, "mon", 20),       # WELCOME10 + new user
        ("WELCOME10", 200, False, "mon", 0),       # WELCOME10 + existing user
        ("WEEKEND20", 500, False, "sat", 100),     # weekend + threshold met
        ("WEEKEND20", 500, False, "sun", 100),     # Sunday weekend branch
        ("WEEKEND20", 499, False, "sat", 50),      # weekend + threshold not met
        ("WEEKEND20", 500, False, "mon", 0),       # weekday branch
        ("FLAT100", 301, False, "mon", 100),       # amount above threshold
        ("FLAT100", 300, False, "mon", 0),         # amount at threshold
        ("OTHER", 500, False, "mon", 0),           # unknown coupon
    ],
)
def test_coupon_discount_decision_branches(code, total, new_user, day, expected):
    assert coupon_discount(code, total, new_user, day) == expected


@pytest.mark.parametrize("total", [0, -1])
def test_coupon_discount_rejects_non_positive_cart(total):
    with pytest.raises(ValueError, match="empty cart"):
        coupon_discount("OTHER", total, False, "mon")


def test_best_discount_loop_takes_update_branch():
    # First coupon establishes a best value; next coupon is larger and replaces it.
    assert best_discount(["WELCOME10", "WEEKEND20"], 1000, True, "sat") == 200


def test_best_discount_loop_skips_update_branch():
    # No coupon produces a value greater than the initial best of zero.
    assert best_discount(["UNKNOWN", "WELCOME10"], 200, False, "mon") == 0


def test_best_discount_cap_true_branch():
    assert best_discount(["WEEKEND20"], 100, False, "sat") == 40


def test_best_discount_cap_false_branch():
    assert best_discount(["WELCOME10"], 200, True, "mon") == 20


def test_best_discount_equal_cap_boundary():
    assert best_discount(["WEEKEND20"], 500, False, "sat") == 100


@pytest.mark.parametrize("days_valid", [0, -1])
def test_is_expired_non_positive_validity_branch(days_valid):
    assert is_expired(10, 5, days_valid) is True


def test_is_expired_elapsed_days_greater_than_validity_branch():
    assert is_expired(16, 5, 10) is True


def test_is_expired_elapsed_days_equal_to_validity_branch():
    assert is_expired(15, 5, 10) is False


def test_is_expired_elapsed_days_less_than_validity_branch():
    assert is_expired(14, 5, 10) is False
