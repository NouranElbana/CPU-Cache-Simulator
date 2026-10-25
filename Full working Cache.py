import matplotlib.pyplot as plt
#CPU has 5 main jobs:
    #Define Cache size and memory requests
    #Perform FIFO & LRU
    #Calculate performance (Hits, misses, hit rate & AMAT)
    #Compare results across different cache capacities
    #Generate graph

#Step 1: Define the FIFO function
#FIFO removes the oldest entry which is in the position 0 when the cache is full
#It adds the new entry at the end of the cache
def fifo(cache_size, requested_memory):

    cache = []
    hits = 0
    misses = 0

    if cache_size <= 0:
        raise ValueError("Cache size must be greater than zero")

    for number in requested_memory:
        if number in cache:
            hits += 1
        else:
            misses += 1

            if cache_size == len(cache):
                cache.pop(0)

            cache.append(number)

    return cache, hits, misses

    #total, hit_rate = cache_calculations(hits, misses)
    #return cache, hits, misses, total, hit_rate  # Return the values back after calculations

#Step 2: Define the LRU function
#LRU removes the least recently used entry when the cache is full
#LRU removes the actual number if I do remove(0) it will find the value 0 and remove not position 0 like pop
#Then it will add it to the end of the cache
def lru(cache_size, requested_memory):

    cache = []
    hits = 0
    misses = 0

    if cache_size <= 0:
        raise ValueError("Cache size must be greater than zero")

    for number in requested_memory:
        if number in cache:
            hits += 1
            cache.remove(number)
            cache.append(number)
        else:
            misses += 1

            if cache_size == len(cache):
                cache.pop(0)

            cache.append(number)

    return cache, hits, misses

#Step 3: Calculate cache hit rate
def hit_rate_calculation(hits, misses):

    total = hits + misses

    if total == 0:
        return 0, 0

    hit_rate = (hits / total) * 100

    return total, hit_rate

#Step 4: Calculate AMAT (Average Memory Access Time)
#Estimates how long CPU takes to access memory accounting for both cache hits and misses
def calculate_amat(hit_rate, hit_time, miss_penalty):

    miss_rate= (100- hit_rate)/100
    amat = hit_time + (miss_rate * miss_penalty)

    return amat

#Step 5: The main function
def main():

    cache_sizes = [2, 3, 4, 5]
    requested_memory = [10, 20, 30, 10, 40, 10]
    hit_time = 2  # Assumed cache hit time in ns
    miss_penalty = 40  # Assumed additional miss delay in ns
    fifo_hit_rates = []
    lru_hit_rates = []

    for size in cache_sizes:
        cache, hits, misses = fifo(size, requested_memory)
        total, hit_rate = hit_rate_calculation(hits, misses)
        amat = calculate_amat(hit_rate, hit_time, miss_penalty)
        fifo_hit_rates.append(hit_rate)

        print("Cache Size:", size)
        print("FIFO Hits:", hits)
        print("FIFO Misses:", misses)
        print("FIFO Hit Rate:", round(hit_rate, 2), "%")
        print("FIFO AMAT:", round(amat, 2), "ns")
        print()

        cache, hits, misses = lru(size, requested_memory)
        total, hit_rate = hit_rate_calculation(hits, misses)
        amat = calculate_amat(hit_rate, hit_time, miss_penalty)
        lru_hit_rates.append(hit_rate)

        print("LRU Hits:", hits)
        print("LRU Misses:", misses)
        print("LRU Hit Rate:", round(hit_rate, 2), "%")
        print("LRU AMAT:", round(amat, 2), "ns")
        print()

#Step 6: To plot graphs

    plt.plot(cache_sizes, fifo_hit_rates, label="FIFO")
    plt.plot(cache_sizes, lru_hit_rates, label="LRU")

    plt.title("FIFO vs LRU Cache Performance")
    plt.xlabel("Cache Size (blocks)")
    plt.ylabel("Cache Hit Rate (%)")
    plt.ylim(0, 100)
    plt.xticks(cache_sizes)
    plt.grid(True)

    plt.legend()
    plt.savefig("cache_performance.png", dpi=300)
    plt.show()

main()