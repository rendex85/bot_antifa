def cache_finder_photo(cache_dict: dict, url: str, type_name: str):
    try:
        current_type_dict = cache_dict[type_name]
        photo_vk_string = current_type_dict[url]
        return photo_vk_string
    except KeyError:
        return


def cache_append(cache_dict, url, value, type_name) -> None:
    try:
        current_type_dict = cache_dict[type_name]
    except KeyError:
        cache_dict[type_name] = {url: value}
        return
    current_type_dict[url] = value
