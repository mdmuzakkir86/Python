
# importing user define module
import zTest_module
import sys
city = zTest_module.cities_list[1]
print(city)

cities = zTest_module.cities_list
print(cities)

print(sys.path, '\n\n')

for area in zTest_module.cities_list:
    print(area)
