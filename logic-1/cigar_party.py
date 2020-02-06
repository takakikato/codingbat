def cigar_party(cigars, is_weekend):
    """
    When squirrels get together for a party, they like to have cigars. A
    squirrel party is successful when the number of cigars is between 40 and
    60, inclusive. Unless it is the weekend, in which case there is no upper
    bound on the number of cigars. Return True if the party with the given
    values is successful, or False otherwise.
    """
    return is_weekend or (not is_weekend and 40 <= cigars <= 60)

print(cigar_party(30, False))
print(cigar_party(40, False))
print(cigar_party(50, False))
print(cigar_party(70, True))


# # my code
# def cigar_party(cigars, is_weekend):
#     """
#     When squirrels get together for a party, they like to have cigars. 
#     A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
#     Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
#     Return True if the party with the given values is successful, or False otherwise.
#     """
#     if is_weekend and cigars >= 40:
#         return True
#     else:
#         if 40 <= cigar <= 60:
#             return True
#         else:
#             return False


# def main():
#     is_weekend = bool(input('Is it a weekend: '))
#     cigars = int(input('How many cigars: '))
#     print(cigar_party(cigars, is_weekend))


# if __name__ == "__main__":
#     main()