# Lab 6 - Code (line) coverage tests for vending_machine.py
# Aman Priyansh | PES1UG24AM030

import pytest
from vending_machine import select_item, make_change, purchase


# ---------- select_item ----------

def test_select_invalid_item():
    assert select_item("water", {"cola": 5}, 200) == "invalid"


def test_select_sold_out():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"


def test_select_insufficient_credit():
    assert select_item("cola", {"cola": 5}, 100) == "insufficient"


def test_select_ok():
    assert select_item("cola", {"cola": 5}, 150) == "ok"


# ---------- make_change ----------

def test_change_negative_amount_raises_error():
    with pytest.raises(ValueError):
        make_change(-10)


def test_change_normal():
    assert make_change(65) == [50, 10, 5]


def test_change_impossible():
    assert make_change(3) is None


# ---------- purchase ----------

def test_purchase_fails_when_select_fails():
    assert purchase("cola", {"cola": 0}, 200) == ("sold_out", [])


def test_purchase_no_exact_change():
    stock = {"cola": 5}
    assert purchase("cola", stock, 153) == ("no_exact_change", [])
    assert stock["cola"] == 5   # stock must NOT go down


def test_purchase_dispensed():
    stock = {"cola": 5}
    assert purchase("cola", stock, 200) == ("dispensed", [50])
    assert stock["cola"] == 4   # stock goes down by 1
