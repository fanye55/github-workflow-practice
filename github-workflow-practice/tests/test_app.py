import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.app import deduplicate_items

def test_deduplicate_basic():
    """测试基本去重功能"""
    input_list = [1, 2, 2, 3, 4, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert deduplicate_items(input_list) == expected

def test_deduplicate_empty():
    """测试空列表"""
    assert deduplicate_items([]) == []

def test_deduplicate_strings():
    """测试字符串去重"""
    input_list = ["a", "b", "b", "c"]
    expected = ["a", "b", "c"]
    assert deduplicate_items(input_list) == expected