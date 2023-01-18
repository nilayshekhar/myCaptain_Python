def calculate_grade(website):
    # Assign a grade based on the number of features the website has
    if website.has_product_search and website.has_shopping_cart and website.has_payment_system and website.has_customer_reviews:
        grade = "A"
    elif website.has_product_search and website.has_shopping_cart and website.has_payment_system:
        grade = "B"
    elif website.has_product_search and website.has_shopping_cart:
        grade = "C"
    else:
        grade = "D"

    return grade

# Example usage:
website = {"has_product_search": True, "has_shopping_cart": True, "has_payment_system": True, "has_customer_reviews": True}
grade = calculate_grade(website)
print(grade) # Output: A
