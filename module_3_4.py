def single_root_words(root_word, *other_words):
    """Функция для поиска однокоренных слов."""
    same_words = []

    # Приведение корневого слова к нижнему регистру для сравнения
    root_word_lower = root_word.lower()

    for word in other_words:
        # Приведение слова к нижнему регистру
        word_lower = word.lower()

        # Проверка на наличие корневого слова или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    return same_words


# Примеры вызовов функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)