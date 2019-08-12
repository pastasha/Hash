# Hash
Требуется построить хеш-таблицу, для поиска в которой используется метод открытой адресации (размещение и поиск элементов 
– обязательно, удаление – желательно). 
Длина таблицы q – простое число в диапазоне 10-20 тысяч. 
Таблица строится для набора случайных символьных строк длиной 1-20 символов и хранит номера или адреса этих строк. 
Хеш-функция для строки S длины L:
f(S) = ((…(S[1] * 31 + S[2]) * 31 + …+S[L-1]) * 31 +S[L]) mod q.
Необходимо вычислить среднюю трудоемкость поиска при различной заполненности таблицы (например, 25, 50, 75, 90 и 99%). 
Для этого нужно сначала разместить в таблице нужное число строк, а потом для каждой строки подсчитать число шагов, 
выполняемых при ее поиске. 
Все вычисления провести для трех вариантов: линейные пробы, квадратичные пробы и двойное хеширование.
