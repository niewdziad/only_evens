# only_evens
#
Ta funkcja używa listowego składania, aby stworzyć listę zawierającą tylko liczby parzyste, które są zarówno parzyste pod względem wartości, jak i indeksu. Wyrażenie [num for idx, num in enumerate(list_) if idx % 2 == 0 and num % 2 == 0] iteruje przez elementy listy list_ za pomocą funkcji enumerate, która zwraca indeks i wartość dla każdego elementu. Następnie sprawdzane jest, czy indeks i wartość są oba parzyste, a jeśli tak, to dodawane są do wynikowej listy.

Testy asercji sprawdzają, czy funkcja działa zgodnie z oczekiwaniami, zwracając poprawne wyniki dla różnych zestawów danych wejściowych.