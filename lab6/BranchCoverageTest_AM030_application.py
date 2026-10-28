# Lab 6 - Branch coverage tests for vending_machine.py
# Aman Priyansh | PES1UG24AM030
#
# Every decision (if / while / for) is tested on BOTH sides:
# the True branch and the False branch.

import pytest
from vending_machine import select_item, make_change, purchase


# ---------- select_item ----------

# Decision 1: item not in PRICES -> True
def test_select_invalid_item():
    assert select_item("water", {"cola": 5}, 200) == "invalid"


# Decision 1 False + Decision 2 True: item exists but is missing from stock dict
def test_select_item_missing_from_stock():
    assert select_item("candy", {}, 200) == "sold_out"


# Decision 2 True: item in stock dict with count 0
def test_select_sold_out():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"


# Decision 3 True (boundary): one less than the price
def test_select_insufficient_by_one():
    assert select_item("cola", {"cola": 5}, 149) == "insufficient"


# Decision 3 False (boundary): exactly the price is enough
def test_select_exact_credit_ok():
    assert select_item("cola", {"cola": 5}, 150) == "ok"


# ---------- make_change ----------

# Decision 4 True: negative amount raises an error
def test_change_negative_raises_error():
    with pytest.raises(ValueError):
        make_change(-1)


# Decision 4 False + while never True + Decision 7 False: zero change
def test_change_zero():
    assert make_change(0) == []


# while True for every coin once
def test_change_uses_every_coin():
    assert make_change(190) == [100, 50, 25, 10, 5]


# while True repeatedly for the same coin
def test_change_same_coin_twice():
    assert make_change(200) == [100, 100]


# Decision 7 True: leftover that no coin can pay
def test_change_impossible():
    assert make_change(3) is None


# ---------- purchase ----------

# Decision 8 True: select_item failed (sold out)
def test_purchase_sold_out():
    assert purchase("cola", {"cola": 0}, 200) == ("sold_out", [])


# Decision 8 True: select_item failed (invalid item)
def test_purchase_invalid_item():
    assert purchase("water", {"cola": 5}, 200) == ("invalid", [])


# Decision 8 False + Decision 9 True: no exact change, stock must not change
def test_purchase_no_exact_change():
    stock = {"cola": 5}
    assert purchase("cola", stock, 153) == ("no_exact_change", [])
    assert stock["cola"] == 5


# Decision 9 False: exact money, change is an empty list (not None)
def test_purchase_exact_money():
    stock = {"cola": 5}
    assert purchase("cola", stock, 150) == ("dispensed", [])
    assert stock["cola"] == 4


# Decision 9 False: normal purchase with change
def test_purchase_with_change():
    stock = {"chips": 2}
    assert purchase("chips", stock, 175) == ("dispensed", [50, 25])
    assert stock["chips"] == 1
