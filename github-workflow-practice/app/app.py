def deduplicate_items(items):
    """去除列表中的重复项"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    # 示例用法
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    result = deduplicate_items(sample_list)
    print(f"Original: {sample_list}")
    print(f"Deduplicated: {result}")
    #梁梓健和刘博源