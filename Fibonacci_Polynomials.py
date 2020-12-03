class FibonacciNumber():

    def matrix_square(self, A, mod):
        return self.mat_mult(A, A, mod)

    def mat_mult(self, A, B, mod):
        if mod is not None:
            return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
                    [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]

    def matrix_pow(self, M, power, mod):
        # Special definition for power=0:
        if power <= 0:
            return M

        powers = list(reversed([True if i == "1" else False for i in bin(power)[2:]]))  # Order is 1,2,4,8,16,...

        matrices = [None for _ in powers]
        matrices[0] = M

        for i in range(1, len(powers)):
            matrices[i] = self.matrix_square(matrices[i - 1], mod)
        result = None

        for matrix, power in zip(matrices, powers):
            if power:
                if result is None:
                    result = matrix
                else:
                    result = self.mat_mult(result, matrix, mod)


        return result[0][1]


fib_matrix = [[1, 1],
              [1, 0]]


class Equation_Solution():

    def __init__(self):
        self.fibonacci_number = FibonacciNumber()

    def mpow(self, x, p, new_mod):
        if p == 1:
            return x
        if p % 2:
            return x * self.mpow(x, p - 1, new_mod) % new_mod
            # print("mpow p%2 ye girdi")
        r = self.mpow(x, p // 2, new_mod)
        # print("mpow a girdi",r)

        return r * r % new_mod

    def Equation(self, n, x, mod):
        denominator = (x * x + x - 1)  # Denkelemin paydası
        new_mod = denominator * mod  # Denklemin modunun alınacağı yer

        f_nn = self.fibonacci_number.matrix_pow(fib_matrix, n + 1, new_mod)
        f_n = self.fibonacci_number.matrix_pow(fib_matrix, n, new_mod)

        numerator = (f_n * self.mpow(x, n + 2, new_mod) + f_nn * self.mpow(x, n + 1, new_mod) - x) % (new_mod)

        return numerator / denominator

    def calculater(self):
        n = pow(10, 15)
        mod = 1307674368000
        Result = 0
        # 100
        for x in range(1, 101):
            # print("F ye gidiyor")
            Result += self.Equation(n, x, mod)
            Result %= mod
        # print("her bir x_rance için girid")
        print("İşlemin sounucu =", Result)
        return Result


if __name__ == "__main__":
    Equation = Equation_Solution()
    Equation.calculater()
