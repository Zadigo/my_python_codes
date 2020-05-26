import multiprocessing as mp

def test():
    for i in range(0, 5):
        print('Fast %s' % i)

def testa():
    for i in range(10, 15):
        print('Slow %s' % i)

if __name__ == '__main__': 
    pool = mp.Pool(processes=1)
    pool.close()
    pool.join()
