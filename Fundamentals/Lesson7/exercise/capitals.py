def capitolia():
    country = input().split(", ")
    capital = input().split(", ")
    dictio = dict(zip(country,capital))

    for key,value in dictio.items():
        print(f"{key} -> {value}")


capitolia()