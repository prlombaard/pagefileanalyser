def bytes_from_file(filename, chunksize=8192):
    print(f"bytes_from_file({filename},{chunksize})")
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                yield chunk
                #for b in chunk:
                #    yield b
            else:
                break

def do_stuff_with(b):
    #print("help")
    count_non_zero=0
    count_zero_consecutive=0
    was_zero=False
    for c in b:
        if c!=0:
            count_non_zero+=1
            was_zero = False
        #else:
        #    was_zero = True
    
        #if (was_zero and c==0):
        #    count_zero_consecutive+=1
        
    return count_non_zero,count_zero_consecutive

def main():
    import time
    print("Pagefile Analyser")
    filename = "pagefile.sys"
    print(f"Analysing {filename}")

    count_bytes = 0
    count_kilo_bytes = count_bytes/1024
    count_mega_bytes = count_kilo_bytes/1024
    count_giga_bytes = count_mega_bytes/1024
    t = time.time()

    count_non_zero = 0
    count_zero_consecutive = 0
    
    for b in bytes_from_file(filename, 32768):
        #print(type(b))
        count_bytes+=len(b)
        count_kilo_bytes = count_bytes/1024
        count_mega_bytes = count_kilo_bytes/1024
        count_giga_bytes = count_mega_bytes/1024

        if (count_mega_bytes%100==0):
            e = time.time()
            d = e - t
            rate_bytes_per_second = (count_bytes)/d

            print(f"{time.time()}:{len(b)},{rate_bytes_per_second/1024/1024}{count_bytes},{count_kilo_bytes},{count_mega_bytes},{count_giga_bytes}")
            #print(f"Processed {count_giga_bytes} GB in {d} seconds, {rate_bytes_per_second/1024/1024}")
            #break

        x,y = do_stuff_with(b)
        count_non_zero += x
        count_zero_consecutive += y
       

    print(f"non zero values:{count_non_zero}")
    print(f"consecutive zeros: {count_zero_consecutive}")


    print(f"Total read:")
    print(f"{count_bytes} B")
    print(f"{count_kilo_bytes} kB")
    print(f"{count_mega_bytes} MB")
    print(f"{count_giga_bytes} GB")

    print(f"Time taken ({time.time() - t}) seconds")

if __name__ == "__main__":
    main()