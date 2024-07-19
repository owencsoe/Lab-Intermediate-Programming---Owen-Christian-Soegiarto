class Fraction:
    def _init_(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("The numerator and denominator must be integers.")
        
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            sign = -1 if (numerator < 0) ^ (denominator < 0) else 1
            a = abs(numerator)
            b = abs(denominator)
            gcd = self._gcd(a, b)
            self._numerator = sign * (a // gcd)
            self._denominator = b // gcd
    
    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def _add_(self, other):
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only add Fraction with Fraction.")
    
    def _sub_(self, other):
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._denominator - other._numerator * self._denominator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only subtract Fraction with Fraction.")

    def _mul_(self, other):
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._numerator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only multiply Fraction with Fraction.")

    def _truediv_(self, other):
        if isinstance(other, Fraction):
            new_numerator = self._numerator * other._denominator
            new_denominator = self._denominator * other._numerator
            if new_denominator == 0:
                raise ZeroDivisionError("Resulting denominator cannot be zero.")
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Can only divide Fraction by Fraction.")
    
    def _neg_(self):
        return Fraction(-self._numerator, self._denominator)

    def _eq_(self, other):
        return self._numerator == other._numerator and self._denominator == other._denominator

    def _str_(self):
        return f"{self._numerator}/{self._denominator}"
    
    def _repr_(self):
        return f"Fraction({self._numerator}, {self._denominator})"
    
    def _float_(self):
        return self._numerator / self._denominator
    
    def _int_(self):
        return self._numerator // self._denominator
    

## Bank Class
class BankAccount:
    _next_account_number = 1  
    def _init_(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def _str_(self):
        return f"Account({self.account_number}): {self.owner}, Balance: ${self.balance:.2f}"

    def _repr_(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance}, account_number={self.account_number})"



## Family
class Family:
    def _init_(self, parents, *children):
        if len(parents) != 2:
            raise ValueError("Family must have exactly two parents.")
        
        self.parents = parents
        self.children = list(children)
    
    def add_child(self, child):
        self.children.append(child)
    
    def _iter_(self):
        return iter(self.children)
    
    def _str_(self):
        parents_str = f"Parents: {self.parents[0]} and {self.parents[1]}"
        children_str = ", ".join(self.children) if self.children else "No children"
        return f"{parents_str}\nChildren: {children_str}"
    
    def _repr_(self):
        return f"Family(parents={self.parents}, children={self.children})"