import pytest

from coupon_validator import coupon_discount, best_discount, is_expired


# ----------------------------- coupon_discount -----------------------------

def test_welcome_coupon_new_user():
    assert coupon_discount("WELCOME10", 200, True, "mon") == 20


def test_welcome_coupon_existing_user():
    assert coupon_discount("WELCOME10", 200, False, "mon") == 0


def test_weekend_coupon_saturday_large_cart():
    assert coupon_discount("WEEKEND20", 500, False, "sat") == 100


def test_weekend_coupon_sunday_large_cart():
    assert coupon_discount("WEEKEND20", 600, True, "sun") == 120


def test_weekend_coupon_small_cart_returns_flat_50():
    assert coupon_discount("WEEKEND20", 499, False, "sat") == 50


def test_weekend_coupon_weekday_is_zero():
    assert coupon_discount("WEEKEND20", 500, False, "mon") == 0


def test_flat100_above_threshold():
    assert coupon_discount("FLAT100", 301, False, "mon") == 100


def test_flat100_at_threshold_is_zero():
    assert coupon_discount("FLAT100", 300, False, "mon") == 0


def test_unknown_coupon_is_zero():
    assert coupon_discount("UNKNOWN", 500, False, "sun") == 0


@pytest.mark.parametrize("total", [0, -1, -100])
def test_non_positive_cart_raises(total):
    with pytest.raises(ValueError, match="empty cart"):
        coupon_discount("WELCOME10", total, True, "mon")


# ------------------------------- best_discount -----------------------------

def test_best_discount_selects_largest_coupon():
    assert best_discount(["WELCOME10", "WEEKEND20", "FLAT100"], 1000, True, "sat") == 200


def test_best_discount_keeps_zero_when_no_coupon_applies():
    assert best_discount(["WELCOME10", "UNKNOWN"], 200, False, "mon") == 0


def test_best_discount_applies_forty_percent_cap():
    # WEEKEND20 returns 50 on a 100 cart; the 40% cap is 40.
    assert best_discount(["WEEKEND20"], 100, False, "sat") == 40


def test_best_discount_equal_to_cap_is_not_changed():
    assert best_discount(["WEEKEND20"], 500, False, "sat") == 100


def test_best_discount_empty_coupon_list():
    assert best_discount([], 250, True, "mon") == 0


# -------------------------------- is_expired --------------------------------

def test_zero_validity_expired():
    assert is_expired(10, 5, 0) is True


def test_negative_validity_expired():
    assert is_expired(10, 5, -1) is True


def test_expiry_after_validity_window():
    assert is_expired(16, 5, 10) is True


def test_not_expired_before_validity_window_ends():
    assert is_expired(14, 5, 10) is False


def test_not_expired_on_last_valid_day():
    assert is_expired(15, 5, 10) is False


def test_expired_one_day_after_last_valid_day():
    assert is_expired(16, 5, 10) is True
