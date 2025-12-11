# TODO Найдите количество книг, которое можно разместить на дискете
weight_of_1_boob_b = 4 * 25 * 50 * 100
Mb_to_b = 1.44 * 1024 ** 2
number_of_books = int(Mb_to_b // weight_of_1_boob_b)
print("Количество книг, помещающихся на дискету:", number_of_books)
