# """
# Gas Conversion Test Script

# This script tests the gas_conversion.py module to verify that:
# 1. The price is correctly read from the file
# 2. Calculations convert correctly between amount and kg
# """

# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from gas_project.src.api.models.gas_conversion import get_current_price, calculate_gas_conversion

# def test_current_price():
#     """Test that we can read the current price"""
#     price = get_current_price()
#     print(f"Current price: ₦{price} per kg")
#     assert isinstance(price, float), "Price should be a float"
#     assert price > 0, "Price should be positive"
#     return price

# def test_amount_to_kg(price):
#     """Test converting amount to kg"""
#     # Test with multiple amounts
#     test_amounts = [100, 500, 1000, 5000]
    
#     print("\nTesting Amount to KG conversion:")
#     print("-" * 40)
#     print(f"{'Amount (₦)':^15}{'KG':^15}")
#     print("-" * 40)
    
#     for amount in test_amounts:
#         amount, kg = calculate_gas_conversion('amount', amount)
#         print(f"{amount:^15.2f}{kg:^15.2f}")
        
#         # Verify calculation
#         expected_kg = amount / price
#         assert abs(kg - expected_kg) < 0.02, f"KG calculation incorrect: expected ~{expected_kg:.2f}, got {kg}"

# def test_kg_to_amount(price):
#     """Test converting kg to amount"""
#     # Test with multiple kg values
#     test_kgs = [0.5, 1, 3, 5, 12.5]
    
#     print("\nTesting KG to Amount conversion:")
#     print("-" * 40)
#     print(f"{'KG':^15}{'Amount (₦)':^15}")
#     print("-" * 40)
    
#     for kg_value in test_kgs:
#         amount, kg = calculate_gas_conversion('kilogram', kg_value)
#         print(f"{kg:^15.2f}{amount:^15.2f}")
        
#         # Verify calculation
#         expected_amount = kg * price
#         assert abs(amount - expected_amount) < 0.02, f"Amount calculation incorrect: expected ~{expected_amount:.2f}, got {amount}"

# def main():
#     """Run all tests"""
#     print("=" * 50)
#     print("GAS CONVERSION TESTS")
#     print("=" * 50)
    
#     try:
#         price = test_current_price()
#         test_amount_to_kg(price)
#         test_kg_to_amount(price)
        
#         print("\n" + "=" * 50)
#         print("✓ All tests passed!")
#         print("=" * 50)
#         return 0
#     except AssertionError as e:
#         print(f"\n❌ Test failed: {e}")
#         return 1

# if __name__ == "__main__":
#     sys.exit(main())
