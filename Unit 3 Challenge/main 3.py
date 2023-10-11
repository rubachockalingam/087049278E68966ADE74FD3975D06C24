def linearSearchProduct(productList,targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


#Example Usage:
product = ["shoes", "boot", "leafer", "shoes", "sandals", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(product,target)
print(result)