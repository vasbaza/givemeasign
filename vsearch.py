def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    # Возвращает множество букв из 'letters', найденных в указанной фразе
    return set(letters).intersection(set(phrase))
