def get_last_elements(items, n):
    """
    Bu fonksiyon bir listenin son n elemanını döndürmelidir.
    Ancak slice indekslemesinde bir hata barındırır.
    """
    if not isinstance(items, list):
        return "Hata: Liste gerekli"
    
    # BUG: Off-by-one error (Gereksiz +1 var)
    # Doğrusu: items[len(items) - n:]
    return items[len(items) - n + 1:]

my_data = [10, 20, 30, 40, 50]
result = get_last_elements(my_data, 3)
print(f"Sonuç: {result}")
